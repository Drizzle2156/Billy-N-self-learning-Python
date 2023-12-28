# while loop review
# requires variables to be ready
value = "y"
count = 0

while value:  # the condition
    count += 1
    print(count)  # print count and keep incrementing by 1
    if (count == 5):  # if statements are mathematical conditions
        break  # stops the loop even if while condition is true
    else:  # run block of code once when the condition is no longer true
        value = 0
        continue  # stop/skip the curent iterationa, continue with next
