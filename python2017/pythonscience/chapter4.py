# Chapter 4: Conditionals
# 07.31.17

def new_line():
    print

print "4.1 The Modulus Operator"
print "quotient = 7/3"
print "print quotient"
quotient = 7/3
print quotient
print "remainder = 7%3"
print "print remainder"
remainder = 7%3
print remainder
# 7/3 = 2 with 1 leftover
new_line()

print "4.2 Boolean values and expressions"
print "type(true)"
print type(true)
# includes other comparison operators
# - == equals
# - != not equal
# - > greater than
# - < less than
# - >= greater than or equal
# - <=  less than or equal
new_line()

print "4.4 Conditional Execution"
print "if x > 0: "
print "    print \"x is positive.\""
print "    print \"x =\","
print "    print x "
x = 3
if x > 0:
    print "x is positive. "
    print "x = ",x
new_line()

print "4.5 Alternative Execution"
if x%2 == 0:
    print x, "is even"
else:
    print x, "is odd"

print "4.6 Chained Conditionals"
print "y = 5"
y = 5
if x<y:
    print x,"is less than", y
elif x>y:
    print x,"is greather than", y
else:
    print x,"is equal to", y
new_line()

print "4.7 Nested Conditionals"
if x==y:
    print x, "and", y, "are equal"
else:
    if x < y:
        print x, "is less than", y
    else:
        print x, "is greater than", y

if 0 < x and x < 10:
    print x, "is less than 10 but greater than 0."
new_line()

print "4.9 Keyboard Input"
my_input = raw_input("What is your name?")
print my_input
prompt = "What is your name?"
my_input = raw_input(prompt)
# use raw_input to get all input and then convert based on prompt. 

print "4.10 Type Conversion"
# int for integer conversion int(2.3) = 2
# float for float coversion float(2) = 2.0
# str for string conversion str(32) = '32'
# bool for boolean conversion
#   Python assigns boolean values to values of other types. For numerical types like integers and floating-
#   points, zero values are false and non-zero values are true. For strings, empty strings are false and non-
#   empty strings are true.
