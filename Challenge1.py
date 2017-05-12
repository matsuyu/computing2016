
# coding: utf-8

# ## Make a copy of this notebook and upload the completed notebook (in .ipynb format) to your GitHub.

# In[1]:

# Write a program that will work out the distance travelled if the user enters 
# the speed and the time.
speed = 5 
time = 8 
print("Distance travelled:",speed*time)


# In[8]:

# Write a program to tell you the speed you would have to travel at in order 
# to go a distance within a certain time entered.
distance = 40
time =8
print("Minimum speed:",distance/time)


# In[4]:

# Write a program to work out how many days you have lived for.
import datetime 
birth = datetime.date(1998,7,29)
today = datetime.date.today()
print("Days lived:",(today-birth).days)


# In[5]:

# Write a program to work out how many seconds you have lived for.
import datetime 
birth = datetime.date(1998,7,29)
today = datetime.date.today()
print("Days lived:",(today-birth).total_seconds())


# In[11]:

# Write a program that will accept a date of birth and determine whether one 
# is considered an adult (i.e. 21 years old).
import datetime 
birth = datetime.date(1998,7,29)
today = datetime.date.today()
year = today.year-birth.year
if today.month<birth.year:
    year-=1
elif today.month == birth.year:
    if today.day<birth.day:
        year-=1
if year>=21:
    print("An adult")
else:
    print("Not an adult")


# In[16]:

# Write a program that will generate a random playing card e.g. '9 Hearts',
# 'Queen Spades' when the return key is pressed.
# Note: Rather than generate a random number from 1 to 52. Create two random 
# numbers – one for the suit and one for the card.
import random
suits=["Spades","Hearts","Clubs","Diamonds"]
cards=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
print(cards[random.randrange(0,13)]+" "+suits[random.randrange(0,4)])


# In[ ]:

# Make a game of rock, paper, scissors against the computer.
# Algorithm
# Tell user to enter either rock,paper or scissors
# Get the response
# Generate a random number from 1 to 3 (1=rock,2=paper,3=scissors)
# Compare user selection and computer selection
# Display who wins.
import random
print("Enter rock,paper or scissors:")
a=input()
game = random.randrange(1,4)
if a == "rock":
    if game == 1:
        print("Draw")
    elif game == 2:
        print("You lose")
    else:
        print("You win")
if a == "paper":
    if game == 2:
        print("Draw")
    elif game == 3:
        print("You lose")
    else:
        print("You win")
if a == "scissors":
    if game == 3:
        print("Draw")
    elif game == 1:
        print("You lose")
    else:
        print("You win")


# In[21]:

# For the rock, paper, scissors game above, ensure that the user enters a valid 
# entry. Add a loop structure to play several times and keep a running score.
import random
print("Enter rock,paper or scissors:")
a=input()
score=0
game = random.randrange(1,4)
while a!="end":
    if a == "rock":
        if game == 1:
            print("Draw")
        elif game == 2:
            print("You lose")
            score-=1
        else:
            print("You win")
            score+=1
    elif a == "paper":
        if game == 2:
            print("Draw")
        elif game == 3:
            print("You lose")
            score-=1
        else:
            print("You win")
            score+=1
    elif a == "scissors":
        if game == 3:
            print("Draw")
        elif game == 1:
            print("You lose")
            score-=1
        else:
            print("You win")
            score+=1
    else:
        print("invalid input")
    print("Your score:",score)
    print("Enter rock,paper or scissors or end to stop:")
    a=input()


# In[2]:

# Write a program that will give the answer to logic gate questions e.g.
# Enter logic gate : OR
# Enter first input : 1
# Enter second input :0
# Result = 1
# It should work for the logic gates OR, XOR, NAND and NOR gates.
print("Enter logic gate:")
logic = input()
print("Enter first input :")
a=int(input())
print("Enter second input :")
b=int(input())
if logic == "OR":
    c=a|b
elif logic =="XOR":
    c=a^b
elif logic =="NAND":
    c=not(a and b)
else:
    c = (a==0) and (b==0)
print('Result = ',c)


# In[9]:

# Write a program that will display all the factors of an input number that
# are bigger than 1.
# (e.g. the factors of the number 12 are 6,4,3 and 2 because they divide
# into 12 exactly).
# Hint: To find out whether a number X is a factor of Y use:
# If Y mod X == 0 (there is nothing remaining when Y is divided by X)

num = int(input())
for i in range (2,round(num**0.5+1)):
    if (num%i==0):
        print(i)
        print(num//i)


# In[ ]:




# In[ ]:



