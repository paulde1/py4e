# tuples are not mutables just like strings

x = (3,5,4)
x.sort() # leads to a traceback no .functions because sets it apart from list. 

list = list()
dir(list) # see all the dot functions available 

tuple = tuple()
dir(tuple) # only count and index available