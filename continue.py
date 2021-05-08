li = [2, 3, 4, 5, 6]
l2 = [4,5,6,7,8]

for i, p in zip(li, l2):
    print(i,p)


zipped = list(zip(li, l2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

for l1, l in zip(li, l2):
    print(l1)

items = ['Apple', 'Bannana', 'Orange']
counts = [3, 6, 4]
prices = [0.25, 0.34, 0.45]

sentences = []
for (item, count, price) in zip(items, counts, prices):
    sentence = 'i bought ' + str(count) + ' ' + str(item) + 's at ' + str(price) + ' cents each.'
    sentences.append(sentence)
    print('I bougt {} {}  s at {} cents each. \n.format(str(count), str(item), str(price)))

print(sentences)