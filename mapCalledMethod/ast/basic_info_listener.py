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
        startline_number = str(ctx.start.line)
        endline_number = str(ctx.stop.line)

        # print(c2)
        for calledMethod in self.call_methods:
            self.calledMethodToMethod[calledMethod] = c2
        


    def enterMethodCall(self, ctx:JavaParser.MethodCallContext):
        cmName = ctx.parentCtx.getText()
        # print(cmName)
        if 'assert' in ctx.parentCtx.getText():
            pass
        else:
            calledMethod = cmName[cmName.rfind('.')+1:][:cmName[cmName.rfind('.')+1:].find('(')]
            print(calledMethod)
            self.call_methods.append(calledMethod)
            print(self.call_methods)

    # Enter a parse tree produced by JavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):        # self.mapClassToMethod = defaultdict(list)
        className = ctx.getChild(1).getText()  # ---> class name
        # print('class name : ' + className)

      