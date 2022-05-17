# def factorial(n):
#     if n==1:
#         return 1
#     if n==0:
#         return 1
#     recurse = n * factorial(n-1)
#     print(recurse)
#     return recurse 

# factorial(5)
 
# print ("x")
# if 4 > 5:
#     print(7)

# else:
#     print(8)
# print(4)
# 
# 
#     
# chained and nested conditions 
# score =int(input("Enter your exam score:\n:>"))

# if score <= 100:
#    if score >= 90:
#       print('A')
#    elif score >= 80:
#       print('B')
#    elif score >= 70:
#       print('C')
#    elif score >= 60:
#       print('D') 
#    elif score >= 50:
#       print('E')
#    elif score >= 40:
#       print('F')
#    else:
#         print("Comrade go learn work.")
# else:
#       print('Even me no do reach that one!')      


# Lambda
# my_str = "this is a lovely string"
# a = list(map(lambda f:f.upper(), my_str))
# print(a)
# print("".join(a))

# from array import array
# import random

# print("Guess the computer's choice to win  the prize.")
# a= [1,2,3,4,5,6,7]
# random.shuffle(a)
# com_choice= random.choice(a)
# user =int(input("Your choice\n:>"))
# if user == com_choice:
#     print("You win")
# else:
#     if user > com_choice:
#         print("Too high")
#     else:
#         print("Too low")
#     print("You lose")            
 
# options  = ["r", "p", "s"]
# print("""Select R for Rock, P for Paper,S for scissors""")
# com_choice= random. choice(options)
# player_choice = input(">").lower()
# if player_choice in options:
#     if player_choice == options[0] and
#     com_choice == options[2]:
#         print("You win")
#         print("Computer choose", com_choice)
#     elif    

# a = 0
# for i in range (90,120):
#     if i%2==1:
#        a+=1
#        print(i)
# print(" ")
# print(a)
# print(" ")
  



# b = [1,2,3,4,15,22,21,33,50,55,72,66,95]
# c = 0
# for i in b:
#     if i%3==0 or i%5==0:
#         print(i)
#         c+=1
# print(' ')
# print(c)

def prime(num):
# num = int(input("Enter a number: "))
# prime number are greater than 1
    if num > 1:
    # check for the factor
        for i in range(2, num):
            if num % i == 0:
                return False
                break
        else:
            return True
# if num <= 1 it is not a prime number  
    else:
        return False

primeNum = [a for a in range(98,176) if prime(a)]
print(primeNum)


   
#   Data Structure

# b = [6,7,8,9,10]
# b[3] =82
# print(b)



# Tranverse a list
# a = [1,2,3,4,5,6,7]
# a [2:5]


# print(a)


# List comprehension
# a= [x**2 for x in range (10)]
# print(a)


# m= 0.728
# p = [1,2,3,4,7,8,9,10]

# c = [(i-m)**2 for i in p]
# print (c)

# sum(c)
# print(sum(c))





