t1 = (10,20)
print(t1)
# t1.append(7)   Error
# print(t1)

tuplelist  = list(t1)
tuplelist.append(6)
t1 = tuple(tuplelist)
print(t1)

tuplelist  = list(t1)
tuplelist.remove(6)
t1 = tuple(tuplelist)
print(t1)

tuplelist  = list(t1)
tuplelist.clear()
t1 = tuple(tuplelist)
print(t1)

del t1
