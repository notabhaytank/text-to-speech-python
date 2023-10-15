import pyttsx3

print("BASIC TEXT-TO-SPEECH SYNTHESIZER, using pyttx3 library")
while True:
    text_speech = pyttsx3.init()
    answer = input("Input the text: ")
    if answer == "quit":
        break
    text_speech.say(answer)
    text_speech.runAndWait()
