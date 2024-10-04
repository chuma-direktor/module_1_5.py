immutable_var = 1,2,'a','b','c'
immutable_var1 = (1,2,'a','b','c')
immutable_var2 = ([1,2,'a','b','c'])
print(immutable_var)
print(immutable_var1)
print(immutable_var2)

mutable_list = ([1,2],'a','b','c')
print(mutable_list)
mutable_list[0][0] = 2
print(mutable_list)
