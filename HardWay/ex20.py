#from the module sys, import the function or paramater argv
from sys import argv
#The two arguments in argv so it has the script (ex20.py) and
#input_file (test.txt or whatever file you input).
script, input_file = argv
#The function that will print the whole txt file after it reads it
def print_all(f):
   print(f.read())
#The f.seek(0) brings the readline line back to the beginning in the test
#file so that it doesnt coninture from the end of the file.
def rewind(f):
   f.seek(0)
#The function uses the text file (f) and reads a line, then prints the
#current line of the line count
def print_a_line(line_count, f):
   print(line_count, f.readline())
#Openss the input_file when the variable current_file is used
current_file = open(input_file)
#prints string out and skips a line at the end
print("First let's print the whole file:\n")
#Runs print_all function which opens input_file and then prints the
#whole txt file
print_all(current_file)
#prints the string
print("Now let's rewind, kind of like a tape.")
#Runs the function rewind using the current_file variable and the brings
#the line back to the beginning with the seek(0) function
rewind(current_file)
#prints the string
print("Let's print three lines:")
#prints the first line while also showing the number the line is on
current_line = 1
print_a_line(current_line, current_file)
#prints the second line while showing the number the line is on which is 2
current_line += 1
print_a_line(current_line, current_file)
#prints the third line of the text file since it is + 1 line of the
#current line which is 2 (it would be 1 if it had seek(0) in it instead)
current_line += 1
print_a_line(current_line, current_file)
