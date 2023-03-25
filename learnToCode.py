print("Nigel Mdletshe")
#Stack Overflow is your friend

sentence= "I want to be a Quant"
print(sentence)

#Booleans - True or False

# Number in Python
# 2 types : 1 - Integer == Whole numbers 4,5,6
#         : 2 - Float  == Not a whole number 4.5,5.5,0.125

#print(type(3))
#print(type(1.255))

# turn float into int
num1 = 1.02577
num2 = int(num1)

#print(type(num2))

#Counting in python
#0,1,2,3,4,5
#importing things in Python
import math
#Math in Python
math_box = 34.45 ** 43
#print(math_box)

#Strings
sentence = 'Hey this is my sentence'
#print(sentence)

#Lists
myList = [num1,num2,sentence]
print(myList)

#Dictionary - key & value

my_dictionary = {'name':'moon','age':'30','fav_food':"pizza",'location':'The Motherland: South Africa'}
print(my_dictionary)
print(my_dictionary['location'])

#if, elif, else
sentence_1 = 'Hey whats up?'
sentence_2 = "Whaat's good?"
number1 = 45
number2 = 65.5

if number1 == number2: # True
    print(sentence_1)
elif number1 >= number2:
    print(sentence_2)   
else: # do this if all else is false
    print('this is the fail safe')

#indexing
myList = [num1,num2,sentence]
#print(myList[-1])

# Counting forward is 0 1 2 3 ...
# Counting backwards -1 -2 -3 ....

# Loops
# While Loops and for loops
# while loops : Loop until false

hours = 2
while hours < 5:
    print('Do your fucking Job')
    hours =(hours + 0.1)

# For loops - loop until a condition is fulfilled
x = [1, 2,3,4,5,6,7,8,9,10]

for y in x:
    print(y)

for x in range(10):
    print('Keep going cousin')

#functions
def storage_unit():
    shoes = 'jordans'
    game = 'zelda'
    age = 27
    gpa = 2.56

    my_List = [shoes,game,age,'hey there']
    print(my_List)
    return shoes, my_List
# returning allows use in other parts of the code.
storage_unit()    

shoes = storage_unit()[0]
print(shoes)

# Pass information into a function - read up on this
def passing(car):

    car = 'Benz'
    money= 15000000

    print(car)

#google sheets , excel == Pandas
#package/ library 
import pandas as pd
#use pandas by typing pd

#How to use Pandas
df = pd.read_csv('C:/Users/Student\Documents/Python Tutorials/BTC-USD.csv')
print(df)

# time series data - data over the course of time that changes every day
first_50 = df.head(50)
print(first_50)

last_50 = df.tail(50)
print(last_50)
#slicing
print(df[0:100])

#just date column
print(df['Date'])

#just close price column
print(df['Close'])

close_df = df['Close']

# How to access a value out of one column
# build a new dataframe based off a condition
df_40k = df.loc[df['Close'] > 40000]
print(df_40k)

# how to get a specific value out of a data
date_of_40797 = df.loc[df['Close']==40797.609375,'Date'].values[0] 
print(date_of_40797)

#Book - learn python the hard way
#Book - Automate boring stuff with python
#Pandas documentation

