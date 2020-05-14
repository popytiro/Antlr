import logging.config
from ast.ast_processor import AstProcessor
from ast.basic_info_listener import BasicInfoListener
from pathlib import Path
# import csv


if __name__ == '__main__':
    c = 0
    # メソッド抽出するファイルへのパス指定
    java_files = Path("C:/Users/acmil/Desktop/Antlr/Research/dataset/test/cassandra").glob("**/*.java") # cassandraのjavaファイルのみとりあえずやってみる
    for file in java_files:
        # java_filesの数の確認
        print(c)
        c+=1
        # fileの確認
        print(file)
        target_file_path = file

        ast_info = AstProcessor(BasicInfoListener()).execute(target_file_path)