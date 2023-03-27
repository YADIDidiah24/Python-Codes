import random

letters = '0123456789ABCDEF';
color = '#';
for  i in range(6):
    color += random.choice(letters);
    print(color)