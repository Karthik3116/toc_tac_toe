# class abc():
#     class_var = 0
#     class_var += 1
#     def __init__(self,var):

        
#         self.var = var
#         print("class object value ", abc.class_var)
#         print("object value is ", self.var)


#         pass

# abc(10)
# abc(20)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

# Creating objects/instances of the class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing object attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# Calling object methods
person1.say_hello()  # Output: Hello, my name is Alice.
person2.say_hello()  # Output: Hello, my name is Bob.
