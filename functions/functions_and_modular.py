#FUNCTIONS

#creating a function
def my_super_awesome_cool_function():
    print("HELLOOOOOO" * 2)

#calling the function
my_super_awesome_cool_function()

#define a function with params
def param_funciton(bob):
    print(bob)

#calling the funcion using a param
param_funciton("WHATEVER I PUT HERE GETS USED")

#creating the function that returns something
def humble_return_funciton_of_doom(name):
    return f"{name} IS DOOMED FOREVER"

#calling the function and setting the value that is returned into a variable
bobs_fate = humble_return_funciton_of_doom("BOB")
#printing his fate after the function has returned
print(bobs_fate)


#importing my own personal module
import own_module

#calling the function from inside the own_module.py file
own_module.module_function_of_despair_and_agony()

