import csv
import pprint

with open('C:/Users/acmil\Desktop\Antlr\Research\src/calleMethod_methodName.csv', 'rt', newline='') as csvfile:  # まず、ファイルをオープンする
    reader = csv.reader(csvfile) # csvモジュールのreader関数でreaderという変数名のreaderオブジェクトを作成する
    profile = [row for row in reader] # リスト内包表記によりreaderの中身をリストに追加していく。for文でも可
    
   