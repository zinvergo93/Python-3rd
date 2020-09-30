# pretty_price(3.20, 99) > 3.99
# pretty_price(3.20, 0.99) > 3.99

def pretty_price(base_price, extension):
    if extension > 0.99:
        extension = (extension * 0.01)
    return int(base_price) + extension
    
print(pretty_price(3.20, 0.99))
print(pretty_price(3.20, 99))
print(pretty_price(3.20, 10))



# Jordan's solution
# isinstance is boiler plate code

# def pretty_price(gross_price, extension):
#     if isinstance(extension, int):
#         extension = extension * 0.01
    
#     return int(gross_price) + extension

# print(pretty_price(3.20, 0.99))
# print(pretty_price(3.20, 99))
