
# s = 'searchIterator(ColumnFilter.selection(columns()),false).next(clustering)'
s =  'current.staticRow.filter(columns,partitionDeletion,setActiveDeletionToRow,metadata)'

def extract_methods(text):
    strs = text.split('(')
    res = []
    for e in strs:
        if ')' in e:
            strs.remove(e)
        index = e.find('.')
        if index > 0:
            res.append(e[index+1:])
        elif index == -1:
            res.append(e)
    return res



print(extract_methods(s))
