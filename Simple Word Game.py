#Made By Seth Howard - 11/7/2020
#PythonChallenge6.py - Simple Word Game

import pyttsx3
engine = pyttsx3.init()

print("Enter an adjective:")
adjective1 = input()
print("Enter a name:")
personName = input()
print("Enter a present-tense verb:")
verb1 = input()
print("Enter a past-tense verb")
verb2 = input()
print("Enter a past-tense verb")
verb3 = input()
print("Enter a past-tense verb")
verb4 = input()
print("Enter a place:")
placeName = input()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

line1 = f"It was a {adjective1} summer day and {personName} was very"
line2 = f"hot. {personName} decided to {verb1} to the swimming pool. At"
line3 = f"the pool, the people {verb2}, {verb3}, and {verb4} in the"
line4 = f"water. At the end of the day, everyone left and went to the {placeName}."

fullStory = f"{line1} {line2} {line3} {line4}"

print(fullStory)
engine.say(fullStory)

engine.runAndWait()



