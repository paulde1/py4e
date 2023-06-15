# tuples are not mutables just like strings

x = (3,5,4)
x.sort() # leads to a traceback no .functions because sets it apart from list. 

list = list()
dir(list) # see all the dot functions available 

tuple = tuple()
dir(tuple) # only count and index available

#another way to aassign a tuple
(x,y) = (4, "paul")
print(y) # paul

#sort a dict by key 
d = {
    "a":10,
    "b":15,
    "c":22
}
d.items()
#dict_items([("a", 10), ("c",22),("b",1)])
sorted(d.items())
#[("a",10),("b",1),("c",22)]

#another way to sort tuple by key using loop

tuple = sorted(d.items())
tuple

for k,y in sorted(d.items()):
    print(k,y)

#sort by swappiing k with y

templist = list()
for k,y in d.items() :
    templist.append((y,k)) # swapping order of key value pair
print(templist, "temp before sort")
templist =sorted(templist, reverse = True)
print(templist, "temp after sort")
