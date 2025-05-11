import random
import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices =  engine.getProperty('voices')
engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as  source:
            print("Say Something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("Tulip thinks you said " + content)
        except Exception as e:
            print("Please try again...")

    return content

def main_process():
    while True:    
        request = command().lower()
        if"hello" in request:
            speak("Welcome, How can I help you?")
        elif "play music" in request:
            speak("playing music")
            song = random.randint(1,5)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=3Cp2QTBZAFQ")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=B2cNnvbu3Vc")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=0RDI9CMilhk")
            elif song == 4:
                webbrowser.open("https://www.youtube.com/watch?v=HTeP7ja9UFY")
            elif song == 5:
                webbrowser.open("https://www.youtube.com/watch?v=PZtFYkMYyJA")
        elif "what is the time now" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
        elif "what is the date today" in request:
            now_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak("Today's date is " + str(now_date))
    
main_process()