import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_choice=input("choose voice - maile(1) or female (2):")
if voice_choice=="1":
    engine.setProperty('voice',voices[0].id)
elif voice_choice=="2":
    engine.setProperty('voice', voices[1].id)
else:
    print("invalid choice! using defaulf voice only..")
    engine.setProperty('voice',voices[1].id)
text=input("enter the text that you want to convert inlo voice:")
engine.say(text)
engine.runAndWait()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate -500000)