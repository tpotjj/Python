init_tuple = ()
print (init_tuple.__len__())


init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
 
print(init_tuple_a == init_tuple_b)


init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
print(result)