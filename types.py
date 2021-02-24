a = 'Hello'
b = 'world'

c = '{} {}'.format(a, b)
print(c)

#Using .format()
user = 'Misha'
d = 'Hello {name}!'.format(name = user)
print(d)

#Using f'' Strings
r = f'Hello, {user}!'
print(r)

print(len(r)) #length of a string

q = 'Hello'.upper() #all CAPS
print(q)

v = 'Hello'.lower() #all lowercase
print(v)

h = 'python'.capitalize() #first letter in uppercase
print(h)

l = "   Hello   "
print(l.strip()) #cuts unuseful  spaces

k =  'Прив3т т3б3'.replace('3', 'e') #replacing some symbols in the string
print(k)

j = "learn.python.ru"
print(j.split('.')) #splitting string into a list
print(len(j.split())) #calculating the words in a sentence


#inputs

name = input('Write your name: ')
print(f'Hello, {name}')

print(bool(1))
