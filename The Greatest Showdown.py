#Identify the Greatest

num_1= int(input("Enter the first number"))

num_2= int(input("Enter the second number"))

num_3= int(input("Enter the third number"))

if num_1 > num_2:
    if num_1 > num_3:
        print( num_1)

elif num_2> num_3:
    print(num_2)

else:
    print(num_3)

#Identify the Smallest
    
num_1= int(input("Enter the first number"))

num_2= int(input("Enter the second number"))

num_3= int(input("Enter the third number"))

if num_1 < num_2:
    if num_1 < num_3:
        print( num_1)

elif num_2< num_3:
    print(num_2)

else:
    print(num_3)


#Task3: Equality check
num_1= int(input("Enter the first number"))

num_2= int(input("Enter the second number"))

num_3= int(input("Enter the third number"))

if num_1 == num_2 or num_1==num_3:
    my_max=max(num_1,num_2,num_3)
    print( "There are two numbers that equal each other")

elif num_2== num_3:
    print("There are two numbers that equal each other")

else:
    print(num_3)