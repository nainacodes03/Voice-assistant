import os
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser

# Initialize pyttsx3 engine once
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception:
            return "Sorry! I cannot understand"

# Greet user
say("Hello! I am your Voice Assistant. How can I help you?")

while True:
    text = takeCommand().lower()

    # Website shortcuts
    sites = {
        'open google': 'https://www.google.com',
        'open facebook': 'https://www.facebook.com',
        'open youtube': 'https://www.youtube.com'
    }

    for command, link in sites.items():
        if command in text:
            say(f"Opening {command.replace('open ', '')}")
            webbrowser.open(link)

    # Play music
    if "open music" in text:
        if os.path.exists("output.mp3"):
            os.startfile("output.mp3")
        else:
            say("Music file not found.")

    # Tell time
    elif "tell time" in text:
        strftime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Sir, the time is {strftime}")

    # Wikipedia search
    elif "wikipedia" in text:
        say("Searching Wikipedia...")
        try:
            query = text.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            say(result)
        except:
            say("Sorry, I couldn't fetch results from Wikipedia.")

    # Open file
    elif "open id" in text:
        if os.path.exists("D:\\hello.txt"):
            os.startfile("D:\\hello.txt")
        else:
            say("File not found.")

    # Stop command
    elif "stop" in text or "exit" in text or "quit" in text:
        say("Goodbye! Have a nice day.")
        break

    # Repeat what user said
    else:
        say(text)
