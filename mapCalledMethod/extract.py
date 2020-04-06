import re
s1 = 'searchIterator(ColumnFilter.selection(columns()),false).next(clustering)'
s2 = 'searchIterator(columns())'
s3 = 'seachtIterator()'
s4 = 'searchIterator(columns(abc(aaa)))'
s5 = 'searchIterator(columns(abc(aaa(dfe))))'

def extract_methods(text):
    res = []
    k = text.split('(')
    for e in k:
        index = e.find('.')
        if index > 0:
            res.append(e[index+1:])
        elif index == -1:
            res.append(e)
    for e in res:
        if ')' in e:
            res.remove(e)
    return res

def regx_m(txt):
    return re.findall(r'\b[A-Za-z_]\w*(?=\()', txt)
    
print(regx_m(s1))
print(regx_m(s2))
print(regx_m(s3))
print(regx_m(s4))
print(regx_m(s5))
print(extract_methods(s1))
print(extract_methods(s2))
print(extract_methods(s3))
print(extract_methods(s4))
print(extract_methods(s5))