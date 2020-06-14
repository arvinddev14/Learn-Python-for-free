#                    1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
print(backwards)

#create a slice that produces the characters qpo
backwardss = letters[16:13:-1]
print(backwardss)

#slice the string to produce edcba
backwardss2 = letters[4::-1]
print(backwardss2)

#slice the string to produce the last 8 characters , in reverse order
backwardss3 = letters[:-9:-1]
print(backwardss3)

print(letters[-4:]) #wxyz
print(letters[-1:]) #z
print(letters[:1]) #a
print(letters[0]) #a