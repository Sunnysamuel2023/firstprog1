import random

#random is a built in module which generates psuedo numbers

a = random.randint(1,10) #returns integer number between the range provided both included
b = random.randrange(1, 10)#returns integer number between the range provided includes a but less than range
c = random.random()#returns float number between 0.0 to 0.99999999
d = random.uniform(1,3) #returns floating point number between range
l = [23,43,54,325,23234]
random.choice(l)
print(a,b,c,d)


