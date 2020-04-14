import csv 
import pprint

def extract_methods(text):
    res = []
    k = text.split('(')
    for e in k:
        # print('e：' + e)
        index = e.find('.')
        if index > 0:
            res.append(e[index+1:])
        elif index == -1:
            res.append(e)
    for e in res:
        if ')' in e:
            res.remove(e)
    return res

with open('C:/Users/acmil/Desktop/Antlr/extractMethodName/src/cassandra.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print('メソッド抽出前：' + row[0])
        a = str(row[0])
        b = extract_methods(a)
        print('メソッド抽出後：' + str(b))


# s1 = 'searchIterator(ColumnFilter.selection(columns()),false).next(clustering)'
# s2 = 'current.staticRow.filter(columns,partitionDeletion,setActiveDeletionToRow,metadata)'
# test = 'buffer.remaining()'



# print(extract_methods(s1))1
# print(extract_methods(s2))
# print(extract_methods(test))