# Variables, Expressions, and Statements
# 07.19.17

# 2.1 Values and Data Types
print("")
print ("2.1 Values and Data Types")
print 4
# print works on both integers and strings.
# type(input) can tell you what type a value has
print("Hello World is a :"), # use a comma to concatenate print statements
print(type("Hello, World!")) # <type 'str'>
print("17 is a:"),
print(type(17)) # <type 'int'>
print("3.2 is a:"),
print(type(3.2)) # <type 'float'>
print("\"3,2\" is a:"),
print(type("3.2")) # <type 'string'>
print("You expect 1,000,000 to come out 1,000,000?"),
print 1,000,000
print("It's because 1,000,000 is not a legal int in Python. It's a list of three items to be printed.")
print("")

# 2.2 Variables
# Assignment is the ability to manipulate variables.
print("2.2 Variables")
message = "What's up, Doc?"
n = 17
pi = 3.14159
c = 'c'
print("We have 3 variables, message, n, pi, and c")
print("Lets find out what they got.")
print("message ="),
print(message),
print(type(message))
print("n ="),
print(n),
print(type(n))
print("pi ="),
print(pi),
print(type(pi))
print('c ='),
print(c),
print(type(c))
print("")

# 2.3 Variable Names and Keywords
print("2.3 Variable names and Keywords")
print("Variable names can be arbitrarily long.")
print("They can contain both letters and numbers.")
print("But they must begin with a number.")
print("Remember: Case matters. Bruce and bruce are different variables.")
print
print("Python has 31 keywords:")
print("and       as       assert       break       class       continue")
print("________________________________________________________________")
print("def       del      elif         else        except      except")
print("________________________________________________________________")
print("finally   for      from         global      if          import")
print("________________________________________________________________")
print("in        is       lambda       not         or          pass")
print("________________________________________________________________")
print("print     raise    return       try         while       with")
print("________________________________________________________________")
print("yield")
print

# 2.4 Statements
x = 2
print("2.4 Statements")
print "print 1"
print 1
print "x = 2"
print x
print

# 2.5 Evaluating Expressions
print "2.5 Evaluating Expressions"
print "1 + 1 =",
print 1+1
print

# 2.6 Operations and Operands
print "2.6 Operations and Operands"
print "20 + 32 = ",
print 20 + 32
minute = 59
print "minute = 59"
print "minute/60 = ",
print minute/60
print "minute/60 = 0.9833 (due to truncation)"
print "minute*10/60 = ",
print minute*10/60
print

# 2.7 Order of Operations
print "2.7 Order of Operations"
print "Python follows the rules of precendence. PEMDAS"
print
print "P Parenthesis"
print
print "E Exponents",
print "2**1 + 1 = (2^1) + 1 = ",
print 2**1+1
print
print "M Multiplication"
print
print "D Divison"
print
print "A Addition"
print
print "S Subtraction"
print
print "Operators with the same precedence are read from left to right."
print "60*100/60 is interpreted as 60 * 100, then 6000/60."
print

# 2.8 Operations on Strings
print "2.8 Operations on Strings"
print "Assuming that message is a string, these operations are illegal: "
print "- message-1"
print "- \"Hello\"/123"
print "- message*hello"
print "\"15\"+2"
print
fruit = "banana"
print "fruit = \"banana\""
baked_good = " nut bread"
print "baked_good = \"nut bread\""
print "print fruit + baked_good"
print fruit + baked_good
print

# 2.9 Input
print "2.9 Input"
# print "n = raw_input(\"Please enter your name:\")"
# print "print n"
n = raw_input("Please enter your name: ")
print n
# print "n = input(\"Enter a numerical expression: \")"
# print "print n"
n = input("Enter an numerical expression: ")
print n
print

# 2.10 Composition
print "2.10 Composition"
print "Usage of concatenation with print statements"
print "print \"32 + 3 =\", print 32 + 3 "
print "32 + 3 = 35"
print

# 2.11 Comments
print "2.11 Comments"
print "Comments are made with # in your programming."
print "Comments are useful for marking up your programming and explaing what something does."
print

# 2.13 Exercises

print "1 Record what happens when you print an assignment statement:"
print "print n = 7"
# print n = 7
print "invalid syntax"
print "print 7 + 5"
print 7 + 5
print "print 5.2, \"this\", 4-2, \"that\", 5/2.0"
print 5.2,
print "this",
print 4-2,
print "that",
print 5/2.0
print

print "2 Take the sentence: All work and no play makes Jack a dull boy.",
print "Store each word in a separate variable then print out the sentence on one line using print."
print "word = \"All \""
print "word1 = \"work \""
print "word3 = \"and \""
print "word4 = \"no \""
print "word5 = \"play \""
print "word6 = \"makes \""
print "word7 = \"Jack \""
print "word8 = \"a \""
print "word9 = \"dull \""
print "word10 = \"boy.\""
word = "All "
word1 = "work "
word3 = "and "
word4 = "no "
word5 = "play "
word6 = "makes "
word7 = "Jack "
word8 = "a "
word9 = "dull "
word10 = "boy."
print "print word + word1 + word2 + word3 + word4 + word5 + word6 + word7 + word8 + word9 + word10 "
print word + word1 + word3 + word4 + word5 + word6 + word7 + word8 + word9 + word10
print

print "3 Add parenthesis to the expression 6 * 1 - 2 to change it's value from 4 to -6"
print "print 6 * ( 1 - 2 )"
print 6 * (1 - 2)
print

print "5 The difference between input and raw_input is that input evaluates the input string and raw_input does not."
print"x = input()"
print"type in 3.14"
x = input()
print type(x)
# <type 'int'>
print
print "x = input()"
print"type in 'The knights who say \"ni!\"'"
x = input()
print type(x)
# <type 'str'>
print
# print "x = input()"
# print "type in The knights who say \"ni!\""
# x = input()
# print type(x)
# ERROR
print
print "x = raw_input()"
print "type in 'The knights who say \"ni!\"'"
x = raw_input()
print type(x)
# <type 'str'>
print
