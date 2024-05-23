import texttospeech as tts
import speechtotext as stt
import random as r


# Given the two numbers and the operation, say the question
def sayQuestion(num1, num2, curOps):
    q = ""
    if curOps == "+":
        q = str(num1) + " plus " + str(num2)
    elif curOps == "-":
        q =  str(num1) + " minus " + str(num2)
    elif curOps == "*":
        q = str(num1) + " times " + str(num2)
    else:
        q = str(num1) + " divded by " + str(num2)
    tts.saySomething(q)

# Check whether the user wants to ignore certain question types for this operation
# e.g. multiples of 10, multiples of 5, divisible by 1, etc.
def askForRules(op):
    pass




#
preset = input("Hello. Do you to load a preset? (Y/N)")

# If preset with setting exists
if(preset == "Y"):
    pass

# Else, continue with manual setup
else:
    ops = input("Please specify which operations to include: +-*/")
    ops = ops.split("")

    for op in ops:
        if op == "+":
            lower = input("Select a lower-bound for the range")
            higher = input("Select a higher-bound for the range")

            addRules = askForRules(op)





