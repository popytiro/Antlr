from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ast.JavaLexer import JavaLexer
from ast.JavaParser import JavaParser
from pprint import pformat
import csv 



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
        # print(self.listener.called_methods)
        # print(self.listener.methods)
        # print(self.listener.calsses)
        print(self.listener.calledMethodToMethod)
        for key in self.listener.calledMethodToMethod:
            print(key)
        
        for value in self.listener.calledMethodToMethod.values():
            print(value)

        save_row = {}

        with open("a.csv",'w') as f:
            fieldnames = ['called method', 'method']
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",",quotechar='"')
            writer.writeheader()

            for calledMethod in self.listener.calledMethodToMethod.keys():
                writer.writerow({'called method': calledMethod, 'method': self.listener.calledMethodToMethod[calledMethod] })
                print(calledMethod)
                print(self.listener.calledMethodToMethod[calledMethod])
            


