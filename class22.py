'''Tuple Operations
Outline:
Write a program to perform the following operations: 1. Create a tuple with different datatypes
2. Create another tuple of integers
3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple
5. Perform slicing on the tuple'''
new = (100, 3.14, "Hi", True)
new2 = (1,2,3,4,5,5,5,5)
new3 = new2 + (9,)
print(new3)
print(new2.count(5))
new4 = new2[1:4]
print(new4)
new5 = (25,"book",7.5,"pencil","paper","pen",36,2.5)
new6 = new5[2:]
print(new6)
'''
Flip Flop
Outline:
Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not.
If it's a palindrome, then it is the same after being reversed.
'''
palindrome = (1,2,2,3)
def pal(num):
    return num == num[::-1]
if pal(palindrome):
    print("the given tuple is a palindrome")
else:
    print("the given tuple is not a palindrome")

'''Weather Prediction
Outline:
Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element
is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1.
On the basis of the value of rainy and sunny, predict the weather.'''
weather = (1, 0, 0, 0, 1, 1, 0, 1, 1)
sunny = 0
rainy = 0
for i in weather:
    if i == 1:
        rainy += 1
    else:
        sunny += 1
if sunny > rainy:
    print("Its probably summmer")
elif sunny < rainy:
    print("Its probably monsoon")
else:
    print("Its probably a neutral weather")
