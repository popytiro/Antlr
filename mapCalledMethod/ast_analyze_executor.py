import logging.config
from ast.ast_processor import AstProcessor
from ast.basic_info_listener import BasicInfoListener


if __name__ == '__main__':
    target_file_path = '/Users/ryosuke/Desktop/cassandra/AbstractAllocator.java'
    target_file_path = '/Users/ryosuke/Desktop/cassandra/AbstractBTreePartition.java'

    # ★ポイント１
    ast_info = AstProcessor(None, BasicInfoListener()).execute(target_file_path)