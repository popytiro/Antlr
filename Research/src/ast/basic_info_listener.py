from ast.JavaParserListener import JavaParserListener
from ast.JavaParser import JavaParser

import pprint
import csv


# ★ポイント３
# JavaParserListenerを拡張（継承）して独自のListenerであるBasicInfoListenerを定義します。
class BasicInfoListener(JavaParserListener):


    # ★ポイント４
    # 解析結果を保持するast_infoを定義します。プロパティの名称および内容は解析したい目的に応じて各自で適宜修正してください。
    def __init__(self):
        self.call_methods = []
        self.ast_info = {
            'packageName': '',
            'className': '',
            'implements': [],
            'extends': '',
            'imports': [],
            'fields': [],
            'methods': []
        }

    # ★ポイント５
    # JavaParserListenerで定義されているフックポイントの関数をオーバライドして独自の解析処理を実装します。
    # 例えばenterPackageDeclarationは名前が示す通り、Javaのソースコードのパッケージ定義が開始された箇所で呼び出されます。
    # 引数のctxは型が異なりますが、親クラスが存在するため、構文解析で必要となる基本情報にはどのコンテキストクラスでもアクセスすることができます。
    # Enter a parse tree produced by JavaParser#packageDeclaration.

    def enterPackageDeclaration(self, ctx: JavaParser.PackageDeclarationContext):
        self.ast_info['packageName'] = ctx.qualifiedName().getText()

    # Enter a parse tree produced by JavaParser#importDeclaration.
    def enterImportDeclaration(self, ctx: JavaParser.ImportDeclarationContext):
        import_class = ctx.qualifiedName().getText()
        self.ast_info['imports'].append(import_class)

    # Enter a parse tree produced by JavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):

        # print("{0} {1} {2}".format(ctx.start.line, ctx.start.column, ctx.getText()))
        # print("")
        # print("{}".format(ctx.getText()))
        self.call_methods = []

    # Exit a parse tree produced by JavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):

        # ★ポイント６
        # AST（抽象構文木）の名前が示す通りctxは木構造になっています。getChild関数でそのコンテキストの子ノードにアクセスすることができます。子ノードの内容はコンテキストによって異なります。
        c1 = ctx.getChild(0).getText()  # ---> return type
        c2 = ctx.getChild(1).getText()  # ---> method name
        # c3 = ctx.getChild(2).getText()  # ---> params
        params = self.parse_method_params_block(ctx.getChild(2))

        method_info = {
            'returnType': c1,
            'methodName': c2,
            'params': params,
            'callMethods': self.call_methods
        }
        self.ast_info['methods'].append(method_info)
        # print(self.ast_info['methods'])
        # ターゲットメソッド名の表示
        # pprint.pprint(method_info['methodName'])
        # 呼び出しメソッド名の表示
        # pprint.pprint(method_info['callMethods'])

        # ターゲットメソッド名を配列に格納
        methodName_list = []
        methodName_list.append(method_info['methodName'])
        # print(methodName_list)

        # 呼び出しメソッド名を配列に格納
        callMethods_list = []
        callMethods_list.append(method_info['callMethods'])
        pprint.pprint(callMethods_list)

        # ターゲットメソッドと呼び出しメソッドを辞書で紐づける
        # link_methodName_callMethods = dict(zip(callMethods_list,methodName_list))
        link_methodName_callMethods = dict(
            zip(methodName_list, callMethods_list))
        # pprint.pprint(link_methodName_callMethods)

        # csvに出力
        for key in link_methodName_callMethods:
            # print(key)
            # print(link_methodName_callMethods[key])
            for val in link_methodName_callMethods[key]:
                # print(key)
                # print(val)
                # print("called method:" + val + "target method:" + key)

                # with open("a.csv",'a', newline="") as f:
                #     fieldnames = ['called method', 'method']
                #     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",",quotechar='"')
                #     writer.writeheader()
                #     for calledMethod in link_methodName_callMethods.keys():
                #         print(key)
                #         writer.writerow({'called method': val, 'method': key })
                # pprint.pprint(calledMethod)
                # pprint.pprint(link_methodName_callMethods[calledMethod])

                #csvファイルにメソッド名を抽出する
                with open("calleMethod_methodName_cassandra.csv", 'a', newline="", encoding="utf-8") as f:
                    fieldnames = ['called method', 'method']
                    writer = csv.DictWriter(
                        f, fieldnames=fieldnames, delimiter=",", quotechar='"')
                    # writer.writeheader()
                    for calledMethod in link_methodName_callMethods.keys():
                        writer.writerow({'called method': val, 'method': key})

    # Enter a parse tree produced by JavaParser#methodCall.
    def enterMethodCall(self, ctx: JavaParser.MethodCallContext):
        # ★ポイント７
        # 通常、AST（抽象構文木）では具象情報である行番号や文字位置を保持しませんが、ANTLRではこれらの情報をコンテキストで保持しています。やはりソースコードを解析する際にこれらの情報は役立つので、必要に応じて利用してください。

        # ctx.start.line　：　当該コンテキストのソースコード上の行番号
        # ctx.start.column　：　当該コンテキストのソースコード上の文字位置
        line_number = str(ctx.start.line)
        column_number = str(ctx.start.column)
        # self.call_methods.append(line_number + ' ' + column_number + ' ' + ctx.parentCtx.getText())
        # メソッドの行数と何文字目かを消した
        self.call_methods.append(ctx.parentCtx.getText())

    # Enter a parse tree produced by JavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        child_count = int(ctx.getChildCount())
        if child_count == 7:
            # class Foo extends Bar implements Hoge
            # c1 = ctx.getChild(0)  # ---> class
            c2 = ctx.getChild(1).getText()  # ---> class name
            # c3 = ctx.getChild(2)  # ---> extends
            c4 = ctx.getChild(3).getChild(
                0).getText()  # ---> extends class name
            # c5 = ctx.getChild(4)  # ---> implements
            # c7 = ctx.getChild(6)  # ---> method body
            self.ast_info['className'] = c2
            self.ast_info['implements'] = self.parse_implements_block(
                ctx.getChild(5))
            self.ast_info['extends'] = c4
        elif child_count == 5:
            # class Foo extends Bar
            # or
            # class Foo implements Hoge
            # c1 = ctx.getChild(0)  # ---> class
            c2 = ctx.getChild(1).getText()  # ---> class name
            c3 = ctx.getChild(2).getText()  # ---> extends or implements

            # c5 = ctx.getChild(4)  # ---> method body
            self.ast_info['className'] = c2
            if c3 == 'implements':
                self.ast_info['implements'] = self.parse_implements_block(
                    ctx.getChild(3))
            elif c3 == 'extends':
                # ---> extends class name or implements class name
                c4 = ctx.getChild(3).getChild(0).getText()
                self.ast_info['extends'] = c4
        elif child_count == 3:
            # class Foo
            # c1 = ctx.getChild(0)  # ---> class
            c2 = ctx.getChild(1).getText()  # ---> class name
            # c3 = ctx.getChild(2)  # ---> method body
            self.ast_info['className'] = c2

    # Enter a parse tree produced by JavaParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx: JavaParser.FieldDeclarationContext):
        field = {
            'fieldType': ctx.getChild(0).getText(),
            'fieldDefinition': ctx.getChild(1).getText()
        }
        self.ast_info['fields'].append(field)

    def parse_implements_block(self, ctx):
        implements_child_count = int(ctx.getChildCount())
        result = []
        if implements_child_count == 1:
            impl_class = ctx.getChild(0).getText()
            result.append(impl_class)
        elif implements_child_count > 1:
            for i in range(implements_child_count):
                if i % 2 == 0:
                    impl_class = ctx.getChild(i).getText()
                    result.append(impl_class)
        return result

    def parse_method_params_block(self, ctx):
        params_exist_check = int(ctx.getChildCount())
        result = []
        # () ---> 2
        # (Foo foo) ---> 3
        # (Foo foo, Bar bar) ---> 3
        # (Foo foo, Bar bar, int count) ---> 3
        if params_exist_check == 3:
            params_child_count = int(ctx.getChild(1).getChildCount())
            if params_child_count == 1:
                param_type = ctx.getChild(1).getChild(0).getChild(0).getText()
                param_name = ctx.getChild(1).getChild(0).getChild(1).getText()
                param_info = {
                    'paramType': param_type,
                    'paramName': param_name
                }
                result.append(param_info)
            elif params_child_count > 1:
                for i in range(params_child_count):
                    if i % 2 == 0:
                        param_type = ctx.getChild(1).getChild(
                            i).getChild(0).getText()
                        param_name = ctx.getChild(1).getChild(
                            i).getChild(1).getText()
                        param_info = {
                            'paramType': param_type,
                            'paramName': param_name
                        }
                        result.append(param_info)
        return result
