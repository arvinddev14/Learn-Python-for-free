print("Today is good day to learn python")
print('python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " world")
greeting = "Hello"
name = "Arvind"
print(greeting + name )

#if we want space we can add that too
print(greeting + ' ' + name)


age = 24
print(age)
#To determine the type python thinks we have declared.
print(type(greeting))
print(type(age))
#string value in double quotes will overwrite integer value even if the variable is same
age_in_words = "2 years"
print(name + f" is {age} years old") #when add two values with same varaiable then we will get an type error.it can only concatenate string .
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")