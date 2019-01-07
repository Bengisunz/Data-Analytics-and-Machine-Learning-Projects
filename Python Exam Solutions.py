#QUESTIONS & ANSWERS

print("PART A- Task 1")

#Python is a powerful language that has a growing ecosystem.
#Productivity and readability of python makes it easy to use again.
#It is not so sophistication. Python has open source scientific packages for data visualization,
#machine learning, complex data analysis.
#You can read others' code in python easily. It is easier that learn python than other programming languages.
#Python is dynamically type interpreted language. Therefore, it requires no compilation.
#It has visualization libraries. Debugging is easier on Python

#**********************************************************************************************
print("PART A- Task 2")

#Python 3 was introduced in 2008. There are main differences between Python 2 and Python 3. For example;
# *print function: "print" is treated as a statement In Python 2.
# *integer division: Python 2 treats numbers that you type without any digits after the decimal point as integers that is not good for data analysis
# *raising exceptions: Python 3 needs different syntax for raising exceptions.
#It is said that "Python 3 is the future". There are the new features in Python 3. Python 3 becomes more popular for data analysis.
#Therefore it has is growing community.

#**********************************************************************************************

print("PART A- Task 3")
#Task-3: Please provide a very brief history of Python as a programming language (150-250 words).


#"Python version 1.0 was released in January 1994. The major new features included in this release were the functional programming tools lambda, map, # filter and reduce, which Guido Van Rossum never liked.
#Six and a half years later in October 2000, Python 2.0 was introduced. This release included list comprehensions, a full garbage collector and it was supporting unicode.
#Python flourished for another 8 years in the versions 2.x before the next major release as Python 3.0 (also known as "Python 3000" and "Py3K") was released.
# Python 3 is not backwards compatible with
# Python 2.x. The emphasis in Python 3 had been on the removal of duplicate programming constructs and modules, thus fulfilling or coming close to
# fulfilling the 13th law of the Zen of Python: "There should be one -- and preferably only one -- obvious way to do it."" Python Course, retrieved from https://www.python-course.eu/python3_history_and_philosophy.php


#----------------------------------------------------------------------------------------------------------------------------------

print("PART B")
print("TASK 1")


oddnumlist=[]
for i in range(101,909):    #finding the odd numbers in the range
    if (i%2!=0):
        oddnumlist.append(i)
        i += 1
    print(oddnumlist)

def intcontrol(n):
    assert str.isdigit(n), 'Please enter an integer!'  #checking if the number is interger or not
    return n

number1=input("Enter a number: ")
intcontrol(number1)
number2=input("Enter a number: ")
intcontrol(number2)
number3=input("Enter a number: ")
intcontrol(number3)

def listvalues(start,interval,stop):
    mylist = []
    cursor=start
    while (cursor<=stop):
        mylist.append(cursor)
        cursor = cursor+interval
    print(mylist)
    return mylist

print(listvalues(number1,number2,number3))


#*****************************************************************************************************
print("PART B")
print("TASK 2")

#Multipling first 5 numbers that are even
mynums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
num_mul = 1
count = 0
n=5
for x in mynums:
    if (x%2!=0):
        continue   #passing next iteration
    num_mul = num_mul * x
    count = count + 1
    if count == n+1:
        break        #exiting from the loop
print("Multiplication of even ones of first", n,"elements is: ", num_mul)

#*****************************************************************************************************

print("TASK 3")

import numpy as np
randomarray=np.random.randint(10,high=99, size=21)
print(randomarray)

secondarray=np.random.randint(1,high=55, size=(100, 6))
print(secondarray)
for i in range(secondarray.shape[1]):
    v=secondarray[i]
    print(v)
    v2=np.sort(v)
    print(v2) #sorted row

#------------------------------------------------------------------------------------------------------------
print("PART 3")
print("TASK 1")

import sys    #modifing default recursion method of python because python does not let recursion greater than 1000 by default
sys.setrecursionlimit(1000000)

def factorial_iter(num):
    toplam=1
    while num>0:
        toplam=num*toplam
        num=num-1
    return toplam

def factorial_rec(num2):
    if num2==0:
        return (1)
    else:
        return num2*factorial_rec(num2-1)

import datetime
def RunFactorial(number, impl):
    val = 0
    begintime = datetime.datetime.now()
    if (impl == "rec"):
        val = factorial_rec(number)
    else:
        val = factorial_iter(number)
    endtime=datetime.datetime.now()
    difftime = (endtime - begintime).microseconds / 1000  # to understand microsecond >1 microsecond =1.0 × 10-6 seconds
    print("factorial: " + str(val))
    print(str(impl) + " took " + difftime.__str__() + " miliseconds.")

RunFactorial(10,"iter")
RunFactorial(10,"rec")
#The time of Iter method for 10 is 0 miliseconds.
#The time of Iter method for 10 is 0 miliseconds.

RunFactorial(100,"iter")
RunFactorial(100,"rec")
#The time of Iter method for 1000 is 0 miliseconds.
#The time of Iter method for 1000 is 0 miliseconds.

RunFactorial(1000,"iter")
RunFactorial(1000,"rec")
#The time of Iter method for 10000 is 0 miliseconds.
#The time of Iter method for 10000 is 0 miliseconds.


RunFactorial(10000,"iter")
RunFactorial(10000,"rec")
#The time of Iter method for 10000 is 46.852 miliseconds.
#Recursion method for 10000 takes time.

RunFactorial(100000,"iter")
RunFactorial(100000,"rec")
#The time of Iter a for 100000 is 147.898 miliseconds.
#Recursion method for 100000 takes time.

#As a conclusion, iteration method is faster than recursion method.

#*********************************************************************************************************


print("TASK 2")

import random

def intcontrol(n):              #checking if the number is interger or not
    assert str.isdigit(n), 'Please enter an integer!'
    return n

maxturns=3
turn=1
while(turn <= maxturns):
    rdnums = random.randint(0, 100)
    #print(rdnums)
    guessnum = input("Please guess a number between 0 and 100")
    intcontrol(guessnum)
    guessnum=int(guessnum)
    if guessnum==rdnums:
        print("You guess is right")
    elif guessnum>rdnums:
        print("Your guess is higher than mine")
    else:
        print("Your guess is lower than mine")
    turn = turn+1


#**********************************************************************************************
print("TASK 3")

player1 = input("Please your choose:")
if not (player1=="rock" or player1=="paper" or player1=="scissors"):
    print("Enter correct input from ‘rock, paper and scissors’")
player2 = input("Please your choose:")
if not (player2=="rock" or player2=="paper" or player2=="scissors"):
    print("Enter correct input from ‘rock, paper and scissors’")

if player1==player2:
    print("No winner")
else:
    if player1=="rock" or player2=="rock":
        if player1=="paper" or player2=="paper":
            print("paper wins")
        else:
            print("rock wins")
    else:
        print("scissors wins")   #There is no alternative choose other than scissors-paper scenario



#--------------------------------------------------------------------------------------------------------------
print("PART D")
#Task-1: Please inspect through the following code in Python. Try to understand and explain the algorithm.
#Hint: You might execute this script on your computer to see the outputs for given inputs. Please note that these lines might not
#directly work on your computer due to indentation problem. You need to do the proper indentation before any usage.

print("TASK 1")

# Program to: COMMENT HERE PLEASE
lower = int(input("Enter lower range: ")) # TAKING AN INPUT AS INTEGER FROM USER
upper = int(input("Enter upper range: ")) # TAKING AN ANOTHER INPUT AS INTEGER FROM USER
# PRINTING THE INPUTS WITH THEIR NAMES
print("Numbers in the interval " + str(lower) + " - " + str(upper))

for num in range(lower, upper + 1):
    order = len(str(num)) # GETTING NUMBER OF DIGITS
    sum = 0 #CREATING A VARIABLE
    temp = num #
    while temp > 0: # LOOP WHILE temp IS GREATER THAN ZERO
        digit = temp % 10 # ASSIGNING A VARIBLE WHICH REPRESENTS REMAINDER FROM DIVISION OPERATION
        sum += digit ** order # INCREASING SUM WITH POWER OF digit ^ order
        temp //= 10 #TAKING THE FIRST DIGIT OF THE DIVISION
        if num == sum: # IF num IS EQUAL TO sum
            print(num) # PRINTING THE NUM


#PART D- TASK 2
#Task-2: There are two different algorithms given in this task. Please explain and compare them in terms of their algorithm.

#SORTS THE LIST IN ASCENDING ORDER BY LOOPING THROUGH EVERY ITEM SEQUENCIALLY

def algorithm_1 (alist):
    length = len(alist) # CREATING AN VARIABLE BASED ON THE LENGTH OF THE LIST
    for i in range(0,length): # TAKING EVERY ITEM IN THE RANGE
        for j in range(i,length): # TAKING EVERY ITEM IN THE RANGE
            if alist[j] < alist[i]: # IF THE J IS HIGHER THAN I
                tmp = alist[i] # THIS BLOG SWAPS VALUE OF TWO LIST ITEMS
                alist[i] = alist[j] #
                alist[j] = tmp # THEN ASSIGNING alist WHICH HAS i TO tmp

#SORTS THE LIST IN DESCENDING ORDER BY LOOPING THROUGH EVERY ITEM SEQUENCIALLY

def algorithm_2 (alist):
        length = len(alist) # CREATING AN VARIABLE BASED ON LENGTH OF THE LIST
        for i in range(length-1, 0, -1): # TAKING EVERY ITEM IN THE RANGE
        pos = 0 # CREATING AN pos OBJECT
            for j in range(1, i+1): # TAKING EVERY ITEM IN THE RANGE
                if alist[j] > alist[pos]: # COMPARING THE ITEMS OF THE LISTS
                    pos = j # ASSIGNING pos TO j
        tmp = alist[i] # # THIS BLOG SWAPS VALUE OF TWO LIST ITEMS
        alist[i] = alist[pos] # ASSIGNING TWO LISTS
        alist[pos] = tmp # COMMENT HERE PLEASE
    return alist # COMMENT HERE PLEASE



#PART D- TASK 3
#Task-3: Please provide sufficient explanation for the given code below. How does it work? What does it do?

import random as rd
board = [1,2,3,4,5,6,7,8,9] # CREATING A board
def show_board(): # DEFINING showboard THAT CREATES A TABLE
    print (str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
    print ('----------')
    print (str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
    print ('----------')
    print (str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
def winConditions(char, s1, s2, s3): # CHECKING IF ALL POINTS ARE THE SAME AS GIVEN THREE chars
    if board[s1] == char and board[s2] == char and board[s3] == char:
        return True
def wins(char): # ALL POSSIBLE WINNING CONDITIONS
    if winConditions(char, 0, 1, 2):
        return True
    if winConditions(char, 3, 4, 5):
        return True
    if winConditions(char, 6, 7, 8):
        return True
    if winConditions(char, 2, 4, 6):
        return True
    if winConditions(char, 0, 3, 6):
        return True
    if winConditions(char, 1, 4, 7):
        return True
    if winConditions(char, 2, 5, 8):
        return True
    if winConditions(char, 0, 4, 8):
        return True
print("Welcome to tic-tac-toe. You will be playing as X \n")

def control():
    count = 0
    while True: # LOOP UNTIL THERE IS A WINNER OR TIE
        tile = input("Select an available tile between (1-9): ")
        move_1 = int(tile) # CONVERTING TILE TO A INTEGER THEN ASSIGNING IT TO move_1 FOR PLAYER 1
        if board[move_1 - 1] != 'x' and board[move_1 - 1] != 'o':
            board[move_1 - 1] = 'x'
            count = count + 1
            #print(count)
            if wins('x'):
                print("X Wins!")
                break
            elif count == 9:
                print("Tie")
                break
        while True: # SECOND PLAYER'S TURN
            move_2 = rd.randint(1,9)
            if board[move_2 - 1] != 'x' and board[move_2 - 1] != 'o':
                board[move_2 - 1] = 'o'
                count = count + 1
                #print(count)
                show_board()
                if wins('o'):
                    print("O Wins!")
                    break
                break
        else:
            print("Spot Taken... Try again.")
        control()

#THIS PROGRAM CREATES A BOARD AND LOOP UNTIL THERE IS A WINNING CONDITION OR A TIE.
#IT MANAGES USERS TURNS AND CHECKS WINNING CONDITIONS ON  EVERY MOVE.