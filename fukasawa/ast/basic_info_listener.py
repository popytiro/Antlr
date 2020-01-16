from ast.JavaParserListener import JavaParserListener
from ast.JavaParser import JavaParser
from collections import defaultdict

# ★ポイント３
class BasicInfoListener(JavaParserListener):

    # ★ポイント４
    def __init__(self):
        self.call_methods = []
        self.ast_info = {
            'methods': []
        }
        self.called_methods =defaultdict(list)
        self.methods = []

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
        startline_number = str(ctx.start.line)
        endline_number = str(ctx.stop.line)

        method_info = {
            # 'returnType': c1,
            'methodName': c2,
            # 'params': params,
            'callMethods': self.call_methods
        }
        self.ast_info['methods'].append(method_info)
        self.called_methods[c2].append(self.call_methods)
        self.methods.append(startline_number + ' ' +  endline_number + ' ' + c2)

    def enterMethodCall(self, ctx:JavaParser.MethodCallContext):
        cmName = ctx.parentCtx.getText()
        if 'assert' in ctx.parentCtx.getText():
            pass
        else:
            s = cmName.rfind('.')
            editcmName = cmName[s+1:]

            b = editcmName.find('(')
            fincmName = editcmName[:b]
            # print(fincmName)
            self.call_methods.append(fincmName)


