product = {
    "name": "iPhone Xs",
    "stock": 24,
    "price": 65432.1
}
len(product)

product["memory"] = 64 #adding a new pair
product["name"] = "iPhone Xs Plus" #adding new value to the existing key
print(product)

#Safe call to a key - 
# if it is not clear 
# whether a key-value pair is in the dictionary, not to call an error

print(product.get("name"))
#If not exist, it will show None instead of error

#With get() we can set a value, 
# which we will get if there is no such key in the dict
print(product.get("discount", 0)) # will print 0 so there is no "discount" in the dict
print(product.get("stock", 100)) # will print right value of 100 instead of incorrect

#We can sum up dicts and lists together in one another

phones = ["Samsung Galaxy S10", "iPhone Xs"]

product["recommended"] = phones

print(product)

product["recommended"].append("Xiaomi Mi10")

#A list of dictionaries
stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 
     'recommended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
]

#Accessing the data
print(stock[2])
print(stock[2]["price"] - 30000.5)
print(stock[0]["recommended"][1])


#EXERCISES

cities = {
    "city": "Moscow", 
    "temperature": "20"
    }

print(cities["city"])
cities["temperature"] = int(cities["temperature"]) - 5
print(cities)

print(cities.get("country"))
print(cities.get("country", "Russia"))

cities["date"] = "27.05.2019"

print(len(cities))