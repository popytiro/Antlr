from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ast.JavaLexer import JavaLexer
from ast.JavaParser import JavaParser
from pprint import pformat



class AstProcessor:

    def __init__(self, listener):
        # self.logging = logging
        # self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    # ★ポイント２
    # 解析対象のファイルからJavaLexerのインスタンスを生成し、それを利用してJavaParserのインスタンスを生成します。
    # 解析はParseTreeWalkerのインスタンスのwalkメソッドを呼び出すことで実行されます。
    # Listenerの処理が異なってもこの流れは同じです。
    def execute(self, input_source):
        print("hello")
        parser = JavaParser(CommonTokenStream(JavaLexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        # self.logger.debug('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        # print(self.listener.call_methods)
        # print(self.listener.ast_info['methods'])
        print('hello')
        return self.listener.ast_info