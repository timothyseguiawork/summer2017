# Chapter 3 Functions
# 07.20.17

print "Functions"
print

print "3.1 Definitons and Use"
# In the context of programming, a function is a named sequence of statements that
#   performs a desired operation. This operation is specified in a function definition
#   In Python, the syntax for a function definition is:
#   def Name( LIST OF PARAMETERS ):
#       statements
#   All functions have the same pattern
#   1. A header, which begins with a keyword and ends with a colon
#   2. A body consisting of one or more Python statemnets, each indented the same
#      amount - 4 spaces is the Python standard - from the header.
print "This is a function that creates a new line."
#   The function is named new_line()
print "def new_line():"
print " print # a print statement with no arguments prints a new line"
def new_line():
    """ A print statement with no arguments prints a new line """
    print

new_line()
print "First Line."
new_line()
print "Second Line."
new_line()

def three_lines():
    """ A print statement that prints 3 new lines """
    print
    new_line()
    print

new_line()
print "3.2 Follow the Flow of Execution (The order of which statements are executed)"
new_line()

print "3.3 Parameters, Arguments, and the import statement"

def print_twice(parameter):
    print parameter,
    print parameter

print_twice("memes")
new_line()
print_twice("memes" * 4)
new_line()

print "3.4 Python Functions can be Composed"
print "This means that you can use the result of one function as the input to another."
print_twice(abs(-5))
print_twice("help")
new_line()

print "3.5 Variables and Parameters are LOCAL (stuff that's created within a function, stays in a function)"
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
# When cat_twice terminates, the variable "cat" is destroyed.
cat_twice("memes", "help")
new_line()

print "3.6 Stack Diagrams (look it up at the website)"
new_line()

# 1 Create a function named nine_lines that uses three_lines to print 9 blank lines.
#   also create a function named clear_screen that creates 25 blank lines.
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print "CREATING NINE LINES OF SPACE..."
nine_lines()
print "CLEARING SPACE..."
clear_screen()
