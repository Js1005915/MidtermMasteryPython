#creating a class
class my_super_awesome_amazing_class:
    #global var
    awesome_global_var = "what are you looking at"

    #init function
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #personal function for the class
    def scream(self):
        print(self.name, "is screaming!")

#creates an object based off of the class
class_object = my_super_awesome_amazing_class("BOB", 200)

#accessing an attribute
print("Age:", class_object.age)

#updating an attribute
class_object.name = "OUR BRAND NEW NAME"
print(class_object.name)

class_object.scream()