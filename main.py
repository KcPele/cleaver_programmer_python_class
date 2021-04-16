name = ['name', 'title', 'agents']

l = []
for item in name:
    l.append(item)
print(l)

import turtle
kc_tutrtle = turtle.Turtle(shape='classic')
kc_tutrtle.color('green', 'blue')
for i in range(0,4):
    kc_tutrtle.forward(100)
    kc_tutrtle.right(90)
    kc_tutrtle.forward(100)
    kc_tutrtle.right(90)
    kc_tutrtle.forward(100)
    kc_tutrtle.right(90)
    kc_tutrtle.forward(100)
    kc_tutrtle.forward(100)
    kc_tutrtle.circle(60)
   
   
print([person for person in name])

num = [1, 2, 3, 4]

print([2 * num1 for num1 in num])

movies_and_rating = {
    'Intersteller':6.59,
    'Dark Night': 6,
    'Avangers':9.5,
    'justiclegue':6.8,
    'Spiderman': 8.5
}
l = []


print( [movie for movie in movies_and_rating if movies_and_rating[movie] > 6] )

