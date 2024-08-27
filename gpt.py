import random
import operator
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition
recognizer = sr.Recognizer()

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            response = recognizer.recognize_google(audio)
            print(f"You said: {response}")
            return response
        except sr.UnknownValueError:
            speak_text("Sorry, I didn't catch that. Please try again.")
            return recognize_speech()
        except sr.RequestError:
            speak_text("Speech recognition service is unavailable. Please try again later.")
            return None

# Function to generate a random math problem
def generate_problem():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv  # Ensure integer division
    }
    
    operation = random.choice(list(operations.keys()))
    
    if operation == '/':
        # Ensure division problems result in integer answers
        b = random.randint(5, 100)
        a = b * random.randint(5, 100)
    elif operation == "*":
        # Smaller range for multiplication
        a = random.randint(5, 25)
        b = random.randint(5, 25)
    else:
        a = random.randint(5, 100)
        b = random.randint(5, 100)
    
    return a, b, operation, operations[operation]

# Function to run the math quiz
def math_quiz():
    correct_answers = 0
    total_problems = 50
    
    for _ in range(total_problems):
        a, b, operation, func = generate_problem()
        
        speakable = {
            "+" : "plus",
            "-" : "minus",
            "*" : "times",
            "/" : "divided by"
        }

        problem_text = f"What is {a} {speakable[operation]} {b}?"
        print(problem_text)  # Optionally print the problem
        speak_text(problem_text)
        
        user_response = recognize_speech()
        
        if user_response is not None:
            try:
                try:
                    user_answer = int(user_response)
                except ValueError:
                    user_answer = int(word_to_number(user_response))

                correct_answer = func(a, b)
                
                if user_answer == correct_answer:
                    speak_text("Correct!")
                    print("Correct!")
                    correct_answers += 1
                else:
                    speak_text(f"Wrong! The correct answer is {correct_answer}.")
                    print(f"Wrong! The correct answer is {correct_answer}.")
            except ValueError:
                speak_text("That doesn't seem to be a valid number. Let's try another problem.")
        else:
            break  # If speech recognition fails, stop the quiz
    
    final_score = f"You got {correct_answers} out of {total_problems} correct!"
    speak_text(final_score)
    print(final_score)

def word_to_number(word):
    # Dictionary mapping written numbers to their integer values
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90
    }

    try:
        # Split the input string into words
        words = word.lower().replace('-', ' ').split()

        # Start with a total value of 0
        total = 0
        current = 0

        for word in words:
            if word in numbers:
                current += numbers[word]
            elif word == "hundred":
                current *= 100
            elif word == "thousand":
                current *= 1000
                total += current
                current = 0
            elif word == "million":
                current *= 1000000
                total += current
                current = 0
            else:
                raise ValueError(f"Invalid word found: {word}")

        total += current
        return total
    
    except ValueError as e:
        raise e

# Start the quiz
if __name__ == "__main__":
    math_quiz()