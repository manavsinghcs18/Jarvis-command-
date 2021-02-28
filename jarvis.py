import datetime     #pip install datetime
import pyttsx3  #pip install pyttsx3
import speech_recognition as sr     #pip install speechRecognition
import wikipedia    #pip install wikipedia
import webbrowser   #pip install webbrouser
import os           #pip install os
import smtplib      #pip install smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    # It will give the voice command to user
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    # It will wish Good morning , afternoon and evening to the user
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I'm Jarvis. Please tell me How can i help you?")


def takeCommand():
    # It takes Microphone input to the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.energy_threshold = 300  # minimum audio energy to consider for recording
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.15
        r.dynamic_energy_ratio = 1.5
        r.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

        r.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        r.non_speaking_duration = 0.5  # seconds of non-speaking audio to keep on both sides of the recording

        # if we Take 1 second gap to tell the command to jarvis then jarvis will return the output
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# for sending Email
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('manav.singh_cs18@gla.ac.in','9456476587')
    server.sendmail('manav.singh_cs18@gla.ac.in',to,content)
    server.close()

#for Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def square(a):
    return a**2
def cube(a):
    return a**3


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

    # logic for executing task based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        while True:
            try:
                print("Any think else you want to search on wikipedia")
                speak("Any think else you want to search on wikipedia")
                topic=takeCommand()

                if 'yes' in topic:
                    speak("Sir, What you want to search?")
                    print("Sir, What you want to search?")
                    topic=takeCommand()
                    if 'wikipedia' in query:
                        print("Searching wikipedia...")
                        speak('Searching Wikipedia...')
                        topic = topic.replace("wikipedia", "")
                        results = wikipedia.summary(topic, sentences=1)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    else:
                        continue
                elif 'no' in topic:
                        print("Thankyou for using wikipedia! have a nice day sir")
                        speak("Thankyou for using wikipedia! have a nice day sir")
                        exit()
            except Exception as e:
                # print(e)
                print("have a nice day sir ;D")
                speak("have a nice day sir")    
    
    elif 'youtube' in query:
        print("What you want to search on youtube?")
        speak("What you want to search on youtube?")
        topic=takeCommand()
        webbrowser.open(f"youtube.com {topic}")
    
    elif 'google' in query:
        print("What you want to search on google?")
        speak("What you want to search on google?")
        topic=takeCommand()
        webbrowser.open(f"google.com {topic}")
        while True:
            try:
                print("Any think else you want to search on google")
                speak("Any think else you want to search on google")
                topic=takeCommand()

                if 'yes' in topic:
                    speak("Sir, What you want to search?")
                    print("Sir, What you want to search?")
                    topic=takeCommand()
                    webbrowser.open(f"google.com {topic}")
                elif 'no' in topic:
                        print("Thankyou for using google! have a nice day sir")
                        speak("Thankyou for using google! have a nice day sir")
                        exit()
            except Exception as e:
                # print(e)
                print("have a nice day sir ;D")
                speak("have a nice day sir")

    elif 'chrome' in query:
        print("What you want to search on chrome?")
        speak("What you want to search on chrome?")
        topic = takeCommand()
        webbrowser.open(f"chrome.com {topic}")
        while 1:
            try:
                print("Any think else you want to search on chrome")
                speak("Any think else you want to search on chrome")
                topic=takeCommand()

                if 'yes' in topic:
                    speak("Sir, What you want to search?")
                    print("Sir, What you want to search?")
                    topic=takeCommand()
                    webbrowser.open(f"chrome.com {topic}")
                elif 'no' in topic:
                        print("Thankyou for using chrome! have a nice day sir")
                        speak("Thankyou for using chrome! have a nice day sir")
                        exit()
            except Exception as e:
                # print(e)
                print("have a nice day sir ;D")
                speak("have a nice day sir")


    elif 'gdb compiler' in query:
        print("Which language you want to use on gdb compiler?")
        speak("Which language you want to use on gdb compiler?")
        topic = takeCommand()
        webbrowser.open(f"gdbcompiler.com {topic}")
    
    elif 'whatsapp' in query:
        print("Opening whatsapp...")
        speak("Opening whatsapp...")
        webbrowser.open("whatsappweb.com")

    elif 'play store' in query:
        print("What you want to install from microsoft store?")
        speak("What you want to install from microsoft store?")
        topic =takeCommand()
        webbrowser.open(f"microsoftstoregames.com {topic}")
    
    
    elif 'stack overflow' in query:
        webbrowser.open("stackoverflow.com")
    
    elif 'play music' in query:
        print("what kind of music you want to listen? online or offline")
        speak("what kind of music you want to listen? online or offline")
        topic=takeCommand()
        if 'online' in topic:
            print("Which song you want to listen?")
            speak("Which song you want to listen?")
            topic =takeCommand()
            webbrowser.open(f"gaana.com {topic}")    #for online purpose

        #for offline purpose
        # elif 'offline' in topic:
        #     music_dir = ‪"F:\\music_dir\\Songs"
        #     songs=os.listdir(music_dir)
        #     # print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))
    
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")

    elif 'open vs code' in query:
        codePath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif 'mail to manav' in query:
        try:
            speak ("What should i say?")
            content= takeCommand()
            to = "manavsingh2908@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent :D")
        except Exception as e :
            print(e)
            speak("Sorry my friend Manav, I'm not able to sent the email at the moment")
            speak("Sorry my friend Manav, I'm not able to sent the email at the moment")
    
    elif 'calculator' in query:
        speak("Sir, What you want to perform?")
        print("Sir, What you want to perform?")
        while True:

            topic =takeCommand()
            if 'add' in topic:
                speak("what is the first number you want to perform in addition?")
                a=int(input("what is the first number you want to perform in addition?"))
                speak("what is the second number you want to perform in addition?")
                b=int(input("what is the second number you want to perform in addition?"))
                speak(add(a,b))
                print(add(a,b))
            elif 'sub' in topic:
                speak("what is the first number you want to perform in subtraction?")
                a=int(input("what is the first number you want to perform in subtraction?"))
                speak("what is the second number you want to perform in subtraction?")
                b=int(input("what is the second number you want to perform in subtraction?"))
                speak(sub(a,b))
                print(sub(a,b))
            elif 'mul' in topic:
                speak("what is the first number you want to perform in multiplication?")
                a=int(input("what is the first number you want to perform in multiplication?"))
                speak("what is the second number you want to perform in multiplication?")
                b=int(input("what is the second number you want to perform in multiplication?"))
                speak(mul(a,b))
                print(mul(a,b))
            elif 'div' in topic:
                speak("what is the first number you want to perform in division?")
                a=int(input("what is the first number you want to perform in division?"))
                speak("what is the second number you want to perform in division?")
                b=int(input("what is the second number you want to perform in division?"))
                speak(div(a,b))
                print(div(a,b))
            elif 'mod' in topic:
                speak("what is the first number you want to perform in modulus?")
                a=int(input("what is the first number you want to perform in modulus?"))
                speak("what is the second number you want to perform in modulus?")
                b=int(input("what is the second number you want to perform in modulus?"))
                speak(mod(a,b))
                print(mod(a,b))
            elif 'square' in topic:
                speak("what is the number you want to perform square?")
                a=int(input("what is the number you want to perform square?"))
                speak(square(a))
                print(square(a))
            elif 'cube' in topic:
                speak("what is the number you want to perform cube?")
                a=int(input("what is the number you want to perform cube?"))
                speak(cube(a))
                print(cube(a))

            try:
                print("any think else you want to perform with calculator")
                speak("any think else you want to perform with calculator")
                topic=takeCommand()

                if 'yes' in topic:
                    speak("Sir, What you want to perform?")
                    print("Sir, What you want to perform?")
                    topic=takeCommand()
                    if 'add' in topic:
                        speak("what is the first number you want to perform in addition?")
                        a=int(input("what is the first number you want to perform in addition?"))
                        speak("what is the second number you want to perform in addition?")
                        b=int(input("what is the second number you want to perform in addition?"))
                        speak(add(a,b))
                        print(add(a,b))
                    elif 'sub' in topic:
                        speak("what is the first number you want to perform in subtraction?")
                        a=int(input("what is the first number you want to perform in subtraction?"))
                        speak("what is the second number you want to perform in subtraction?")
                        b=int(input("what is the second number you want to perform in subtraction?"))
                        speak(sub(a,b))
                        print(sub(a,b))
                    elif 'mul' in topic:
                        speak("what is the first number you want to perform in multiplication?")
                        a=int(input("what is the first number you want to perform in multiplication?"))
                        speak("what is the second number you want to perform in multiplication?")
                        b=int(input("what is the second number you want to perform in multiplication?"))
                        speak(mul(a,b))
                        print(mul(a,b))
                    elif 'div' in topic:
                        speak("what is the first number you want to perform in division?")
                        a=int(input("what is the first number you want to perform in division?"))
                        speak("what is the second number you want to perform in division?")
                        b=int(input("what is the second number you want to perform in division?"))
                        speak(div(a,b))
                        print(div(a,b))
                    elif 'mod' in topic:
                        speak("what is the first number you want to perform in modulus?")
                        a=int(input("what is the first number you want to perform in modulus?"))
                        speak("what is the second number you want to perform in modulus?")
                        b=int(input("what is the second number you want to perform in modulus?"))
                        speak(mod(a,b))
                        print(mod(a,b))
                    elif 'square' in topic:
                        speak("what is the number you want to perform square?")
                        a=int(input("what is the number you want to perform square?"))
                        speak(square(a))
                        print(square(a))
                    elif 'cube' in topic:
                        speak("what is the number you want to perform cube?")
                        a=int(input("what is the number you want to perform cube?"))
                        speak(cube(a))
                        print(cube(a))
                    continue
                elif 'no' in topic:
                    print("Thankyou for using calculator! have a nice day ;D")
                    speak("Thankyou for using calculator! have a nice day")
                    exit()
            except Exception as e:
                # print(e)
                print("have a nice day sir ;D")
                speak("have a nice day sir")