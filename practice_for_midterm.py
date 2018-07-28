#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:56:00 2018

@author: tuheenahmmed
"""


'''
even odd
'''

x= int(input('Enter an integer: '))

if x%2 ==0:
    print ('')
    print ('Even')
    
else:
    print ('')
    print ('Odd')
    
print ('Done with conditional')



'''
divisible by 2 & 3
'''
x= int(input('Enter an integer: '))

if x%2 == 0:
    if x%3 == 0:
        
        print ('Divisible by 2 and 3')
        
    else:
        
        print ('Divisible by 2 and not by 3')
        
elif x%3 ==0:
    print ('Divisible by 3 and not by 2')
    
    

'''
compound booleans
'''
x=10
y=10
z=10

if x==y and y==z:
    print ('fuck helen all the night in her pudanda and pigu')

else:
    
    if x < y and x < z:
    
        print ('x is least')

    elif y < z:
    
        print ('y is least')
    
    else:
        print ('z is least')
    
    

'''
INDENTATION
'''

x = float (input("Enter a number for x: "))
y = float (input("Enter a number for y: "))


if x == y:
    
    print ("x and y are equal")
        
if y != 0:
    print ("therefore, x/y is", x/y)
        
elif x < y:
    
    print ("x is smaller")
    
else:
    print ("y is smaller")
    
print ("Thanks")
    


#chapter 3

#find a cube root of a perfect cube

x = int(input('Enter an integer: '))

ans=0

while ans**3 < abs(x):
    
    ans = ans+1
    
if ans**3 != abs(x):
    print (x, 'is not a perfect cube')
    
else:
    if x < 0:
         
        ans = -ans
        
    print ('Cube root of' , x, 'is', ans)



#cube root using for loop

x = int (input('Enter an integer: '))

for ans in range (0, abs(x)+1):
    
    if ans**3 > abs(x):
        break
    
if ans**3 != abs(x):
    print (x, 'is not a perfect cube')
    
else:
    if x < 0:
         
        ans = -ans
        
    print ('Cube root of' , x, 'is', ans)
    


# Implementation of Newton-Raphson method
    
#Newton=Raphson for square root
    
#Find x such that x**2 - 24 is within epsilon of 0
    
epsilon = 0.01

k = 24.0

guess = k/2.0

while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2*guess))
    
print ('Square root of' , k, 'is about', guess)


#######

temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable") 
else:
   print("Cold")
   
   
   
##########

s = 'azcbobobegghakl'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1


print('Number of vowels: ' + str(numVowels))



############

mysum = 0

for i in range (5, 11, 2):
    
    mysum += i
    
    if mysum == 5:
        
        break

print (mysum)


#############

x=3

ans = 0

itersLeft = x

while (itersLeft != 0):
    
    ans = ans + x
    itersLeft = itersLeft -1
    
print (str(x) + '*' + str(x)+ ' = ' + str (ans))


#############

cube = 8
#x = int(input('Enter an integer: '))

cube =int (input("cube root of Helens Pudanda is : " ))

for guess in range (cube+1):
    
    if guess**3 == cube:
        
        print ('Cube root of ' , cube, 'is', guess)



############
###CUBE ROOT OF A NUMBER
###########        
        
cube =int (input("cube root of Helens Pudanda is : " ))

for guess in range (abs(cube)+1):
    
    if guess**3 >= abs(cube):
        
        break
    
if guess**3 != abs(cube):
    
    print (cube, 'is not a perfect cube')
    
else:
    
    if cube <0:
        
        guess = - guess
        
    print ('Cube root of ' + str(cube)+ 'is ' + str(guess))
    


#############
    
s = 'abcdefgi'

for index in range (len(s)):
    
    if s[index] == 'i' or s[index] == 'u':
        
        print ("There is an i or u")
        


s = 'abcdefgi'

for char in s:
    
    if char == 'i' or char == 'u':
        
        print ('There is an i or u')
        


###########
        
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    


#############
    
#cube root using Newton-Raphson method
    
'''

x(n+1) = xn - f(xn)/first derivitive (f(xn))

'''

#############
    
epsilon = 0.01
y = 27.0
guess = y/3.0
numGuesses = 0

print (abs(guess**3-y))
while (abs(guess**3-y)) >= epsilon:
    print (abs(guess**3-y))
    numGuesses += 1
    a=abs(guess**3-y)
    print (a)
    guess = guess - (a/(3*(guess**2)))      ### solve for x**3 -a =0
    print (guess)
    guess = round(guess,2)
    
#print (str(guess))

print('numGuesses = ' + str(numGuesses))
print('Cube root of ' + str(y) + ' is about ' + str(guess))


############
#function
############

def pudanda (x,y):
    
    if x > y:
        print ('cherrys pudanda')
        
    else:
        print ('helens pudanda')
        
pudanda (5,6)

############
#recursion


def factrR (n):
    
    if n==1:
        return n
    
    else:
        return n*factrR(n-1)
    
print (factrR (3))


###########
#function


def factI(n):
    
    result = 1
    while n >1 :
        result = result * n
        n-=1
    
    return result

print (factI(3))


#############

#Fibonacci Numbers
##########

def fibN (n):
    
    if n==0 or n==1:
        return 1
    
    else:
        
        return fibN(n-1)+fibN(n-2)

print (fibN(5))
    
def testFib(n):
    for i in range (n+1):
        print ('fib of', i, '=', fibN(i))
        


###############
#even by function
##############

def is_even(i):
    
    print ("hi")
    
    return i%2 == 0

is_even (3)

print (is_even(3))



###############

def mult_iter (a,b):
    
    result = 0
    
    while b > 0:
        
        result += a
        
        b -= 1
        
    return result

print (mult_iter (5,10))



####################

def isPalindrome (s):
    
    def toChars (s):
        s = s.lower()
        ans = ''
        
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans +c
                
        return ans
    

    def isPal (s):
        if len(s) <= 1:
            return True
        
        else:
            return s[0] == s[-1] and isPal (s[1:-1])
        
    return isPal (toChars(s))

print (isPalindrome('ablewasiereisawleba'))



#####################
def fib_efficient (n,d):
    
    if n in d:
        return d[n]
    
    else:
       
        ans = fib_efficient (n-1,d) + fib_efficient (n-2, d)
        print (ans, n-1, d, n-2, d)
        d[n] = ans
        return ans
    
d = {1:1 , 2:2}

print (fib_efficient (6, d))



#function exercise

 
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

a(False, 2, 3)




#########
midterm exam
##############
[1]

x = "pi" 
y = "pie"

x, y = y, x 

print (x)
print (y)

will swap the values of x and y, resulting in x = "pie" and y = "pi".


[2]



def f(x):
    while x > 3:
        f(x+1)
        
f(4)



[4]

i=5
j=5


while i >= 0:
    while j >= 0:
        print(i, j)
        
 
 Review
Problem 1-7
0.0/1.0 point (graded)
Assume f() is defined. In the statement a = f(), a is always a function.



def f():
    
        print ('helens pudanda')

    
a= f()        
        

listA = [0.234,'apple',(1,2),77]  
tupB = (listA,'MIT',[4,5])  
        
len (listA)     


L = {'1':1, '2':2, '3':3}


len(L)

        
        
        
        
    @@@@@@@
    
def mult_iter (a,b):
    
    result = 0
    
    while b > 0:
        
        result += a
        
        b -= 1
        break
        
    return result

print (mult_iter (5,10))


        
        
        
        
s[1024] = 3 
type(s)
        



  stuff  = 'iQ'
  for thing in stuff:
        if thing == 'iQ':
           print("Found it")
           
         
            
           
           
           
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x          
           
print(Square(-5))         
           




####

L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3

print(d['b'])
           
           
           
 
################
#problem 3
################     

Write a simple procedure, myLog(x, b), that computes the logarithm of a number x relative to a base b. 
For example, if x = 16 and b = 2, then the result is 4 - because . 
If x = 15 and b = 3, then the result is 2 - because  is the largest power of 3 less than 15.

In other words, myLog should return the largest power of b such that b to that power is still less than or equal to x.

x and b are both positive integers; b is an integer greater than or equal to 2. Your function should return an integer answer.     
           


                  
           
 **********
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    i =0
    if b>=2:
       
       while (b**i < x):
       
           i=i+1
           
       print (i)  
myLog(16,2)


*******************          
           
           
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    i =0
    if x>=b:
       
       while (b**i < x):
       
           i=i+1
           
       return i 
   
    
    else:
        return 0
    
print (myLog(16,2))





#########

           
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    i =0
    
       
    while (b**i < x):
       
           i=i+1
           
    return i
   
myLog(16,2)

##########

final one

###############

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    i =0
    ans =0
    if x>b:
       
       while (ans <= x):
       
           i=i+1
           ans = b**i
           print (ans)
           print (i)
           
       return i-1
   
    
    else:
        return 0
    
print (myLog(16,2))

@@@@@@@@@@@@@@
graded
@@@@@@@@@@@@@@

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    i =0
    ans =0
    if x>b:
       
       while (ans <= x):
       
           i=i+1
           ans = b**i
       
       return i-1
   
    
    else:
        return 0
    
print (myLog(77,6))



##########
problem 4
##########

L = [[1, 2], [3, 4], [5, 6, 7]]

range(L)

L[0]

L.reverse()


print(L)



[[7, 6, 5], [4, 3], [2, 1]]




def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    
    L.reverse()
    
    for i in range (len(L)):
        
        L[i]= L[i].reverse()
        #print(L(i))

    return L

L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L) 
print(L)


###############

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    
    L.reverse()
    
    x=L[0]
    x.reverse()
    print('funky',x)
    L=x
    print(L)
    

    #return L

L = [[1, 2], [3, 4], [5, 6, 7]]
range(len(L))
deep_reverse(L) 
print(L)



#####################


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    
    Z= L.reverse()
    
    for i in range(len(Z)):
    
            Z[i]= Z[i].reverse()
            
            Z+=Z[i]
            print (Z)
    #Q=Z[i]
    #x=L[0]
    #x.reverse()
    #print('funky',x)
    #L=x
    #print(L)
    

    #return L

L = [[1, 2], [3, 4], [5, 6, 7]]
range(len(L))
deep_reverse(L) 
print(L)





#########final one############


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    Z=[]
    #L.reverse()
    #print(L.reverse())
    
    for i in range(len(L)):
    
            L[i].reverse()
            
            Z+=L[i]
            print (Z)
    
    L.reverse()        
    

#L = [[1, 2], [3, 4], [5, 6, 7]]

#deep_reverse(L) 
#print(L)

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)




###########graded one##########

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    Z=[]

    
    for i in range(len(L)):
    
            L[i].reverse()
            
            Z+=L[i]
  
    
    L.reverse()        
    


L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)







########problem 5#################

0.0/20.0 points (graded)
Write a function called dict_invert that takes in a dictionary with immutable values 
and returns the inverse of the dictionary. 
The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. 
The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.

Here are some examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}




###########

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    
    if d=={}:
        
        return d
    
    else:
        
    
        x= d.keys()
    
    #print (x)
        y = d.values()
        newdict=[y,x]
    
    return newdict
    
 
#d = {1:10, 2:20, 3:30}
    
d=({})

#len(d)
#d ={10: [1], 20: [2], 30: [3]}
dict_invert(d)
print(d)
    
    
############



###########

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    
    newd={}
    
    if d=={}:
        
        return d
    
    else:
        
        for i in d:
            
            d.keys[i]=d.values[i]
            
         
        return d.keys[i]
    
       # x= d.keys()
    
    #print (x)
       # y = d.values()
       # newdict={y,x}
    
    return newdict
    
 
d = {1:10, 2:20, 3:30}
    
#d=({})

#len(d)
#d ={10: [1], 20: [2], 30: [3]}
dict_invert(d)
print(d)


###########


def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    
    
    
    if d=={}:
        
        return d
    
    else:
        

        newdict = {}
        for k, v in d.iteritems():
            keys = inv.setdefault(v, [])
            keys.append(k)
    return newdict
    
 
d = {1:10, 2:20, 3:30}
    
#d=({})

#len(d)
#d ={10: [1], 20: [2], 30: [3]}
dict_invert(d)
print(d)







################

0.0/20.0 points (graded)
Write a function called gcd that calculates the greatest common divisor of two positive integers. 
The gcd of two or more integers, when at least one of them is not zero, 
is the largest positive integer that divides the numbers without a remainder.

One way is recursively, 
where the greatest common denominator of a and b can be calculated as gcd(a, b) = gcd(b, a mod b). 
Hint: remember the mod symbol is % in Python. Do not import anything.

For example, the greatest common divisor (gcd) between a = 20 and b = 12 is:
gcd(20,12) is the same as gcd(12, 20 mod 12)	= gcd(12,8)
gcd(12,8) is the same as gcd(8, 12 mod 8)	= gcd(8,4)
gcd(8,4)	is the same as gcd(4, 8 mod 4) = gcd(4,0)
The gcd is found (and the gcd is equal to a) when we reach 0 for b.

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    #YOUR CODE HERE
    
    if b==0:
        return a
        
    else:
        return gcd(b,a%b)


print (gcd(4,0))





###############
        
problem 7
###############

def applyF_filterG(L, f, g):
    
    def f(i):
        return i + 2
    def g(i):
        return i > 5
    
    for i in len(L):
        
        if g(f(i))==true:
            
            return g(f(i))
        
        else:
            if L=L():
                
                return -1
        
    

L = [0, -10, 5, 6, -4]
#len(L)
print(applyF_filterG(L, f, g))
print(L)




def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    
    X=[]
    
    def f(i):
        return i + 2
        print(i)
    def g(i):
        return i > 5
        print(g)
        
    if len(L)==0:
        return -1
    
    else:
        
        for i in range(len(L)):
        
            if g(f(i)) == True:
            
                X+=L[i]
                print (X)
        

        return X

        
    

L = [0, -10, 5, 6, -4]
#len(L)
print(applyF_filterG(L, 3, 1))
print(L)  
    
L=[]
len(L)


    






           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           






































































































































































    