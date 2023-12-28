line01 = "********************"  # header / footer
line02 = "*                  *"  # re-use
line03 = "*     WELCOME!     *"
line04 = "*******"

# line01, =, * are all expressions. Its any word, group of words, or symbols that is a value. Expression = value.
# each value is unique. So a statement is a group of expressions designed to carry out a task or action. Statements can also contain statements within them
# in this case line04 = "*******" is a statement

# https://forum.freecodecamp.org/t/python-formatting/641059/3
# Hi, Ive just had the same issue. Im not sure how its successfully removing the spaces
# before line04 in Daves example, when I try it does nothing. It also prompts to use either Black or autopep8
# as the formatter. I ended up installing Black and setting that as the default.
# Opening the Output window for Black I could see it complaining “Skipping non python code”.
# Basically the formatter is working but it’s not seeing the spaces before
# line04 in Daves example as python code so its doing nothing.
# If you were to put a bunch of spaces between ‘line04 =’ and “*****” it will reformat ok.
# So I verified this post and it worked!

# starts with a blank line
print("")  # this prints an empty string
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
# shift, option, command and down arrow allow copy and instant paste right below. comments extend to the end of the line
