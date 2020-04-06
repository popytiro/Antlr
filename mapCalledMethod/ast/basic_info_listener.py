from ast.JavaParserListener import JavaParserListener
from ast.JavaParser import JavaParser
from collections import defaultdict

# ★ポイント３
class BasicInfoListener(JavaParserListener):

    # ★ポイント４
    def __init__(self):
        self.called_methods = defaultdict(list)
        self.methods = []
        self.classes = []
        self.calledMethodToMethod = defaultdict(list)

    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):

        # print("{0} {1} {2}".format(ctx.start.line, ctx.start.column, ctx.getText()))
        self.call_methods = []

    # Exit a parse tree produced by JavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):

        # ★ポイント６
        # c1 = ctx.getChild(0).getText()  # ---> return type
        c2 = ctx.getChild(1).getText()  # ---> method name
        # c3 = ctx.getChild(2).getText()  # ---> params
        # params = self.parse_method_params_block(ctx.getChild(2))
        target_method_line_number = str(ctx.start.line)

        # print(c2)
        for calledMethod in self.call_methods:
            self.calledMethodToMethod[calledMethod] = target_method_line_number + '_' +c2

    def enterMethodCall(self, ctx:JavaParser.MethodCallContext):
        called_method_line_number = str(ctx.start.line) # メソッド呼び出しが存在する行番号
        called_method_name = ctx.parentCtx.getText() # ---> method name

        if called_method_name.count('.') > 1: # 1文に複数のメソッド呼び出しが行われている場合
            multiple_called_method_name = called_method_name.split('.') # 複数のメソッド呼び出しが行われている文を分割して配列に格納
            multiple_called_method_name.pop(0) # 配列の先頭はメソッド呼び出しでないので削除
            print(multiple_called_method_name) # 配列を表示
            for divided_called_method_name in multiple_called_method_name: # 配列要素を処理
                print(divided_called_method_name[:divided_called_method_name.rfind('(')])
                calledMethod = divided_called_method_name[:divided_called_method_name.rfind('(')]
                self.call_methods.append(called_method_line_number + '_' + calledMethod)

        else:
            if 'assert' in ctx.parentCtx.getText():
                pass
            else:
                calledMethod = called_method_name[called_method_name.rfind('.')+1:][:called_method_name[called_method_name.rfind('.')+1:].find('(')]
                self.call_methods.append(called_method_line_number + '_' + calledMethod)
        
    # Enter a parse tree produced by JavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):        # self.mapClassToMethod = defaultdict(list)
        className = ctx.getChild(1).getText()  # ---> class name
        # print('class name : ' + className)

      