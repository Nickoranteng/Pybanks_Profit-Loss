  # 1. "oooo needs some work" will print out because 
  #  2*5  is NOT greater than 10 thus the else statement will print out
x = 5
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")


  # 2. Question 2 works! Will print out since the lenght of "dog" is 3 which is 
  #less than 5
x = 5
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")

  # 3. GOT QUESTION 3! will print because 2 exponent 3 is equal to 8 and 8 is
  # greater than y(5)
  # and 5 exponent 2 is 25. 25 is less than 26 thus both conditions are met in 
  #the IF statement 
  # thus the IF statement will print out
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")
else:
    print("Oh good you can count")

 # 4. Dan is in group three will print since the 
 # variable "Dan" appears only in group three
 
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")

 # 5. Can ride bumper cars
 # since the height is 66 and adult permission is true, the elif statement with 
 # the OR condition will meet the condition the the print statement "can ride bumper cars will
 # print out 
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
#