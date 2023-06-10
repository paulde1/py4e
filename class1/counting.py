counts = dict()
print('enter a line of text')
line = input('')

words = line.split()

# print('Words:', words)

print('Counting ...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

ppp = {
    "tommy": 1, 
    "Angel" : 2, 
    "chaya" : 3,
    "Cidney" : 4, 
    "ben" : 5
}

print(list(ppp))
print(ppp.values())
print(ppp.keys())
