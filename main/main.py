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
        q = str(num1) + " divided by " + str(num2)
    tts.saySomething(q)

# Specify the range of numbers that can be asked
def selectRange(op):
    lower = input("Select a lower-bound for the range for " + op + " ")
    higher = input("Select a higher-bound for the range for " + op + " ")
    return (lower, higher)

# Specify the rules 
def basicRules(rules, op):

    if(input("Allow multiples of 10? (Y/N) ") == "N"):
        rules.append((1, "candidate % 10 != 0"))
    if(input("Allow multiples of 5? (Y/N) ") == "N"):
        rules.append((1, "candidate % 5 != 0"))
    if(input("Allow even numbers? (Y/N) ") == "N"):
        rules.append((1, "candidate % 2 != 0"))
    if(input("Allow odd numbers? (Y/N) ") == "N"):
        rules.append((1, "candidate % 2 != 1"))
    if(input("Allow single digit numbers? (Y/N) ") == "N"):
        rules.append((1, "candidate < 10 && candidate > -10"))
    if(input("Allow the number zero? (Y/N) ") == "N"):
        rules.append((1, "candidate != 0"))
    if(input("Allow positive " + op + " positive numbers? (Y/N) ") == "N"):
        rules.append((2, "candidate1 > 0 and candidate2 > 0"))
    if(input("Allow positive " + op + " negative numbers? (Y/N) ") == "N"):
        rules.append((2, "(candidate1 > 0 and candidate2 < 0) or (candidate1 < 0 and candidate2 > 0)"))
    if(input("Allow negative " + op + " negative numbers? (Y/N) ") == "N"):
        rules.append((2, "candidate1 < 0 and candidate2 < 0"))

    while(True):
        if(input("Would you like to add another custom rule? (Y/N) ") == "Y"):
            rules.append(input("Enter your custom rule: "))
        else:
            break

# Check whether the user wants to ignore certain question types for this operation
# e.g. multiples of 10, multiples of 5, divisible by 1, etc.
def createRules(op):
    
    rules = []
    
    # For addition, subtraction, multiplication, rules are straightforward
    if op in ["+","-","*"]:
        basicRules(rules, op)
    # For division
    else:
        if(input("Allow multiples of 10? (Y/N) ") == "N"):
            rules.append((1, "candidate % 10 != 0"))
        if(input("Allow multiples of 5? (Y/N) ") == "N"):
            rules.append((1, "candidate % 5 != 0"))
        if(input("Allow even numbers? (Y/N) ") == "N"):
            rules.append((1, "candidate % 2 != 0"))
        if(input("Allow odd numbers? (Y/N) ") == "N"):
            rules.append((1, "candidate % 2 != 1"))
        if(input("Allow single digit numbers? (Y/N) ") == "N"):
            rules.append((1, "candidate < 10 && candidate > -10"))
        
        if(input("Allow decimals? (Y/N) ") == "N"):
            rules.append((2, "candidate1 % candidate2 == 0"))
        
        while(True):
            if(input("Would you like to add another custom rule? (Y/N) ") == "Y"):
                rules.append(input("Enter your custom rule: "))
            else:
                break
    
    return rules

def setRange(rulesForThisOp):
    lowerBound = rulesForThisOp[0][0]
    upperBound = rulesForThisOp[0][1]

    # Populate entire range
    numbers = []
    for i in range(lowerBound, upperBound):
        numbers[i - lowerBound] = i
    
    # Eliminate invalid numbers
    for rule in rulesForThisOp:
        if rule[0] == 1:
            for i in range(len(numbers)):
                candidate = numbers[i]
                if not(eval(rule[1])):
                    numbers[i] == "Remove"
    
    # Remove all numbers failing to meet the rules
    trueNumbers = [num for num in numbers if num != "Remove"]
    return trueNumbers


# "Main method"
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
    preset = input("Hello. Do you want to load a preset? (Y/N) ")

    # If preset with setting exists
    if(preset == "Y"):
        try:
            fileName = input("What is the name of the file? Omit .txt ")
            file = open(fileName + ".txt", "r")
        except OSError:
            print("Error accessing file. Verify name of the file")
            return
        
        data = file.readline()
        # TODO

    # Else, continue with manual setup
    else:
        ops = input("Please specify which operations to include: +-*/ ")
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
            opRules = createRules(op)
            # Populate the rules for that operation
            for rule in opRules:
                rules[op].append(rule)

        # Populate ranges and eliminate numbers that breach the rules
        numbers = {
            "+": [],
            "-": [],
            "*": [],
            "/": []
        }
        for op in ops:
            # A list of valid numbers for this particular operation
            numbers[op] = setRange(rules[op])
        
        # Ask whether to save these inputs
        if(input("Save as a preset? (Y/N) ")):
            
            while(True):
                fileName = input("Name your preset: ")
        






if __name__ == "__main__":
    clientInteraction()





