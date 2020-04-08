s1 = 'searchIterator(ColumnFilter.selection(columns()),false).next(clustering)'
# s2 = 'current.staticRow.filter(columns,partitionDeletion,setActiveDeletionToRow,metadata)'
test = 'buffer.remaining()'

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

# print(extract_methods(s1))
# print(extract_methods(s2))
print(extract_methods(test))
