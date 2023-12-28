meaning = 42
print("")
# The print() function prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before written to the screen.


if meaning > 10:
    print("Right on!")
else:
    print("Not today")
# The if-else statement is used to execute both the true part and the false part of a given condition.
# If the condition is true, the if block code is executed and if the condition is false, the else block code is executed.
# Command + / (Mac) to toggle commenting. The selected lines will be commented out with a hash symbol (#) at the beginning of each line. Press the same shortcut again to uncomment the lines.
# testing
# testing
# testing


# In my case I get output Right on! in the terminal because 42 > 10. If it was < 10 the terminal outputs Not today
# then in the Python terminal when i type in python3 meaning.py it will run this script and output Right on!
# this works because im already in the directory folder, file. if i were to run this in zsh i would have to navigate first
# Ternary Operator is a shortcut to the if else, check website in notes for explanation
# replace line 6 to 9 with: print("Right on!") if meaning > 10 else print("Not today")
# i can also go to the terminal and type this in after i set meaning = to any value
