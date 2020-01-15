from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ast.JavaLexer import JavaLexer
from ast.JavaParser import JavaParser
from pprint import pformat


class AstProcessor:

    def __init__(self, logging, listener):
        # self.logging = logging
        # self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    # ★ポイント２
    def execute(self, input_source):
        parser = JavaParser(CommonTokenStream(JavaLexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        # self.logger.debug('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        # print(self.listener.ast_info)
        # print(self.listener.call_methods)
        print(self.listener.called_methods)
        print(self.listener.called_methods['setUp'])
        # print(self.listener.methods['testLocationTrackerShouldBeExcludedFromInterpolation'])
        # print(len(self.listener.methods['testLocationTrackerShouldBeExcludedFromInterpolation']))
        print(sum(len(v) for v in self.listener.called_methods['testLocationTrackerShouldBeExcludedFromInterpolation']))
        print(self.listener.methods)
        for method in self.listener.methods:
            num = sum(len(v) for v in self.listener.called_methods[method])
            for i in range(num):
                print(method)
                # print(num)

        # return self.listener.ast_info