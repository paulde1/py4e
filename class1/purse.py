purse = dict()
purse['money']= 12
purse['candy'] = 3
purse['tissues'] = 75
# print(purse, "purse1")
purse['candy'] = purse['candy'] + 2
# print(purse, "purse2")

 
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in names :
        counts[name] = 1
    else :
        counts[name]= counts[name] + 1
print(counts)
