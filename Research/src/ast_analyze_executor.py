import logging.config
from ast.ast_processor import AstProcessor
from ast.basic_info_listener import BasicInfoListener
from pathlib import Path
import csv
# import pprint

# def code_search_net(dic, ast_process, post_process, frm=0, to=10000):
#     java_files = Path("C:/Users/yuki-fu/Desktop/先行研究の再現/dataset/").glob("**/*.java")
#     for file in java_files:


if __name__ == '__main__':
    # logging_setting_path = '../resources/logging/utiltools_log.conf'
    # logging.config.fileConfig(logging_setting_path)
    # logger = logging.getLogger(__file__)
    c = 0
    # メソッド抽出するファイルへのパス指定
    java_files = Path("C:/Users/acmil/Desktop/Antlr/Research/dataset/test/cassandra").glob("**/*.java")
    for file in java_files:
        print(c) #javafilrの数の確認
        # if c == 2:
        #    exit()
        c+=1
        # print(c)
        print(file)

        #target_file_path = 'C:/temp/解析対象のファイル.java'
        target_file_path = file

        # ★ポイント１
        # 独自に実装したListenerのインスタンスを生成した後、後述するAstProcessorのインスタンスを生成します。
        # 解析対象のファイルのファイルパスを引数としてAstProcessorのexecuteメソッドを実行し、ソースコードの解析を実行します。
        # executeメソッドの戻り値は解析結果です。
        ast_info = AstProcessor(BasicInfoListener()).execute(target_file_path)
        

        # print(ast_info)