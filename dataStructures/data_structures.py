#LISTS - changeable, ordered, and allow duplicates

#creating a list to store items
mylist = ["bob", "Joe"]

#accessing an item in a list
print(mylist[0])

#update an item in the list
mylist[0] = "MEOW"
print(mylist[0])

#DICTIONARIES - ordered, changeable, and doesnt allow duplicates

#creating a dictionary, withh key value pairs
mydict = {
    "name": "bob",
    "age": 123,
    "mother": ""
}

#accessing a value of a dict using a key
print(mydict["age"])

#updating the value of an existing key
mydict["mother"] = "BOBS MOTHER"
print(mydict["mother"])

#SETS - unordered, unindexed, doesnt allow duplicates

#creats a set, but with a duplicate of "two fish"
myset = {"one fish", "two fish", "gold fish", "two fish"}
print(myset)

#TUPLES - ordered and unchangeable

#creating a tuple
myincredibletuple = ("apple", "orange", "pineapple", "watermelon", "machine gun")

#accessing the value in the tuple
print(myincredibletuple[4])

