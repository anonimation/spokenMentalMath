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


def selectRange(op):
    lower = input("Select a lower-bound for the range for " + op)
    higher = input("Select a higher-bound for the range for " + op)
    return (lower, higher)


# Check whether the user wants to ignore certain question types for this operation
# e.g. multiples of 10, multiples of 5, divisible by 1, etc.
def createRules(op):
    
    rules = []
    
    if op == "+":
        if(input("Allow multiples of 10? (Y/N)") == "N"):
            rules.append((1, "candidate % 10 != 0"))
        if(input("Allow multiples of 5? (Y/N)") == "N"):
            rules.append((1, "candidate % 5 != 0"))
        if(input("Allow even numbers? (Y/N)") == "N"):
            rules.append((1, "candidate % 2 != 0"))
        if(input("Allow odd numbers? (Y/N)") == "N"):
            rules.append((1, "candidate % 2 != 1"))
        if(input("Allow single digit numbers? (Y/N)") == "N"):
            rules.append((1, "candidate < 10 && candidate > -10"))
        if(input("Allow the number zero? (Y/N)") == "N"):
            rules.append((1, "candidate != 0"))
        if(input("Allow positive plus positive numbers? (Y/N)") == "N"):
            rules.append((2, "candidate1(candidate1 * candidate2 < 0)"))
        #if(input("Allow positive "))

        while(True):
            if(input("Would you like to add another custom rule? (Y/N)") == "Y"):
                rules.append("Enter your custom rule:")
            else:
                break

        return rules

    elif op == "-":
        pass
    elif op == "*":
        pass
    else:
        pass 





def clientInteraction():

    # Key is the operation
    # Value is a list
        # First item in list is a tuple, (lowerbound, upperbound), inclusive
        # Remaining items are rules
            # For elimination rules, form (1, rule)
            # For pairing rules, form (2, rule)
    # An empty value means don't include that operation
    rules = {
        "+": [],
        "-": [],
        "*": [],
        "/": []
    }

    # Begin client interaction
    preset = input("Hello. Do you want to load a preset? (Y/N)")

    # If preset with setting exists
    if(preset == "Y"):
        pass

    # Else, continue with manual setup
    else:
        ops = input("Please specify which operations to include: +-*/")
        ops = ops.split("")

        # Exit if invalid
        if len(ops) == 0:
            print("No operations selected. Goodbye!")
            return

        # For each of the selected operations
        for op in ops:

            # Ask the user for the range of numbers that are valid
            rules[op].append(selectRange(op))

            # Ask the user for any rules (e.g. no even numbers, no multiples of 10, etc.)
            rules = createRules(op)
            # Populate the rules for that operation
            for rule in rules:
                rules[op].append(rule)






if __name__ == "__main__":
    clientInteraction()





