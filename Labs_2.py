# 1. Write a python program to handle a ZeroDivisionError exception when divising by zero

print("Line 1")
print("Line 2")
print("Line 3")
print("Line 4")
print("Line 5")
print("Line 6")

try:
    print(7997/0)

except ZeroDivisionError as a:
    print(a)
print("Line 7")
print("Line 8")
print("Line 9")
print("Line 10")



#2.WAP in python that prompts the user to input an integer and raises a value error exception if input is not a valid integer

try:
    user_input = int(input("Enter a number: "))
    print(f"You entered value is: {user_input}")
except ValueError as e:
    print(f"Error reported: {e}")   
    
    
# FileNotFoundError Exception

try:
    open("poiuhukijuhyg.txt") 
except FileNotFoundError as e:    
    print(f"Error reported: {e}")
    
    
    
#3. WAP in python in python to count  uppercase character in the text file "ABC txt"

def count_uppercase_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    uppercase_count = sum(1 for char in text if char.isupper())
    print(f"Number of uppercase characters: {uppercase_count}")

# Specify the path to your text file
file_path = 'ABC.txt'
count_uppercase_in_file(file_path)


#Write a function_words() in python to read lines from the text file "story.txt", and display those , which are less than 4 characters
def function_words(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) < 4:
                    print(word)

# Specify the path to your text file
file_path = 'story.txt'
function_words(file_path)
