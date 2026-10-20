#FOR LOOP
mylist = ['meow', 'bark', 'whistle']

#goes through each item in the list, passing in the value as sound in this case
for sound in mylist:
    print(sound)


#WHILE LOOP
hungry = True
foods_ate = 0

#while hungry is true, could also be written as hungry == True
while(hungry):
    if (foods_ate > 5):
        hungry = False
    else:
        print(f"still hungry, Foods ate: {foods_ate}")
        foods_ate += 1
