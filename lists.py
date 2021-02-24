phones = ["iPhone Xs", "Samsung Galaxy S10", "Xiaomi Mi8"] #creating a list

phones.append("iPhone Xs") #adding to the end of a list

phones.count("iPhone Xs") #counting a quantity in the list

phones[1] #accessing to a specific element

print(phones[1:3]) #printing from 1st till 2nd, 3rd is not accounted

print(phones[:2]) #printing from 0 and 1st elements

print(phones[-1]) #the end of the list

phones.index("iPhone Xs") #giving an index

phones.sort() #sorting in a special order

#removing objects

del phones[1]
phones.remove("iPhone Xs")


#EXERCISES
numbers = [3, 5, 7, 9, 10.5]

print(numbers)
numbers.append("Python")
print(len(numbers))

print(numbers[0])
print(numbers[-1])
print(numbers[2:5])

numbers.remove("Python")