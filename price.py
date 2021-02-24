first_price = input("Write down the price: ")

def format_price(price):
    price = int(float(price))
    return f'Price is: {price} rubles'

print(format_price(first_price))