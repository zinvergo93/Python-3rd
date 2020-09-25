# class Invoice:

#     def greeting(self):
#         return 'Hi there'

# # Instantiation

# inv_one = Invoice()
# print(inv_one.greeting())

# inv_two = Invoice()
# print(inv_two.greeting())

# *******************************

# class Dog:
    
#     def speak(self):
#         return 'The intricacies and amazing nature of that which is String Theory.... I mean *Bark*'

# bark_one = Dog()
# print(bark_one.speak())


# # ********************
# class Invoice:
#     def __init__(self, client, total):
#         self.client = client
#         self.total = total
    
#     def formatter(self):
#         return f'{self.client} owes: ${self.total}'

# google = Invoice('Google', 100000)
# snapchat = Invoice('Snapchat', 20000)

# print(google.formatter())
# print(snapchat.formatter())

class Cat:
    def __init__(self, name, noise):
        self.name = name
        self.noise = noise

    def get_name(self):
        return self.name
    def speak(self):
        return f'"{self.noise}" said {self.name}, then he knocked a vase on the table and stared at his misfortunate owner.\n'


jerome = Cat('Jerome Snuggins', 'If you don\'t feed me at 3am, I will smother you in your sleep. Meow')
terrence = Cat('Terrence', 'I just pooped on your pillow') 

print(jerome.speak())
print(jerome.get_name())
print('\n')
print(terrence.speak())
print(terrence.get_name())

