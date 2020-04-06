detected_called_method = "cloned.put(buffer.duplicate().append('a'));"

n1 = detected_called_method.find('.')+1
print('n1: ' + str(n1))
m1 = detected_called_method[n1:]
k1 = m1.find('(')+1
print('m1: ' + str(m1))
print('k1: ' + str(m1[:k1-1]))

n2 = m1.find('.')+1
print('n2: ' + str(n2))
m2 = m1[n2:]
print('m2: ' + str(m2))
k2 = m2.find('(')+1
print('k1: ' + str(m2[:k2-1]))

n3 = m2.find('.')+1
print('n3: ' + str(n3))
m3 = m2[n3:]
print('m3: ' + str(m3))
k3 = m3.find('(')+1
print('k1: ' + str(m3[:k3-1]))

detected_called_method2 = "cloned.put(buffer.duplicate().append('a'));"

l = detected_called_method2.split('.')
print(l)
print(detected_called_method2.count('.'))

    
