# by Kami Bigdely 
# Replace magic numbers with named constanst
force_value = 8.9875517923 * 1e9
even = 2

# First Section
# Given two point charges, calcualte the electric force exerted on them.

q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance be10tween two charges: "))

def force(q1, q2, distance):
    return force_value * q1 * q2 / (distance**2)

print ("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
def even_num(number):
    return number % even == 0

num = int(input('Enter an integer number: '))
if even_num(num):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")