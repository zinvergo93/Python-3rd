# class User:
#     def __init__(self, email, first_name, last_name):
#         self.email = email
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def greeting(self):
#         return f'Hi {self.first_name} {self.last_name}'


# class AdminUser(User): 
#     def active_users(self):
#         return '500'

# tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')
# kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

# print(tiffany.active_users())
# print(tiffany.greeting())


# ******************************************************


# *************Pet Class example************************

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         return 'I don\'t speak'

# class Dog(Pet):

#     def speak(self):
#         return 'Woof'
    
#     def get_name(self):
#         return self.name
   
#     def get_age(self):
#         return self.age



# class Cat(Pet):

#     def speak(self):
#         return 'Meow'

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

# class Fish(Pet):
#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

# cat_one = Cat('Sprinkles', '8')
# dog_one = Dog('Diesel', '4')
# fish_one = Fish('Bubbles', '6 months')

# print(dog_one.speak())
# print(dog_one.get_name())
# print(dog_one.get_age())
# print('\n')
# print(cat_one.speak())
# print(cat_one.get_name())
# print(cat_one.get_age())
# print('\n')
# print(fish_one.speak())
# print(fish_one.get_name())
# print(fish_one.get_age())



# **************************************************

# *****************Class solution*******************
class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_name(self):
    return self.name
  
  def speak(self):
    return "I don't speak"
class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color
  def speak(self):
    return 'Meow'
class Dog(Pet):
  def speak(self):
    return "Woof"
class Fish(Pet):
  pass

cat_one = Cat('Sprinkles', '8', 'orange')
# dog = Dog('Boris', '11', 'bark', 'his', 'rubber bone')

dog_one = Dog('Diesel', '4')
fish_one = Fish('Bubbles', '6 months')

print(dog_one.speak())
print(dog_one.get_name())
print('\n')
print(cat_one.speak())
print(cat_one.get_name())
print('\n')
print(fish_one.speak())
print(fish_one.get_name())