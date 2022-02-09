import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import touch

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am assistant.")
    print("I am assistant.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query.lower()}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'print current directory' in query:
            speak("you are currently working on this directory")
            print("you are currently working on this directory")
            cmd = 'pwd'
            os.system(cmd)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'list' in query:
            speak("listing all the files and folders")
            print("listing all the files and folders")
            cmd = 'ls -l'
            os.system(cmd)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'available directories' in query:
            speak("these are all the available directories")
            print("these are all the available directories")
            cmd = 'dir'
            os.system(cmd)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'change folder' in query:
            speak("which folder you want to select")
            print("which folder you want to select")
            cmd = 'ls -l'
            os.system(cmd)
            command = ""
            temp1 = takeCommand().lower()
            command += temp1
            os.chdir(command)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'make directory' in query:
            speak("what should be the name of the directory")
            print("what should be the name of the directory")

            command = ""
            temp1 = takeCommand().lower()
            command += temp1
            os.makedirs(command)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)


        elif 'create file' in query:
            speak("what should be the name of the file")
            print("what should be the name of the file")
            temp1 = takeCommand().lower()
            touch.touch(temp1)
            listing = 'ls -l'
            os.system(listing)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'remove file' in query:
            speak("which file you want to remove")
            print("which file you want to remove")
            command = ""
            temp1 = takeCommand().lower()
            command += temp1
            os.remove(command)
            listing = 'ls -l'
            os.system(listing)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'remove directory' in query:
            speak("which directory you want to remove")
            print("which directory you want to remove")
            command = ""
            temp1 = takeCommand().lower()
            command += temp1
            os.rmdir(command)
            listing = 'ls -l'
            os.system(listing)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'copy' in query:
            speak("name the first file")
            print("name the first file")
            file1 = takeCommand().lower()
            f1 = ""
            f1 += file1
            speak("name the second file")
            print("name the second file")
            file2 = takeCommand().lower()
            f2 = ""
            f2 += file2
            flag = f1 + " " + f2
            cmd = 'cp ' + flag
            os.system(cmd)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'move' in query:
            speak("name the first file")
            print("name the first file")
            file1 = takeCommand().lower()
            f1 = ""
            f1 += file1
            speak("name the second file")
            print("name the second file")
            file2 = takeCommand().lower()
            f2 = ""
            f2 += file2
            flag = f1 + " " + f2
            os.rename(f1, f2)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'update' in query:
            speak("updating")
            print("updating")
            cmd = 'sudo apt update'
            os.system(cmd)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'go to home directory' in query:
            speak("moving to home directory")
            print("moving to home directory")
            cmd = 'cd '
            os.system(cmd)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'executable' in query:
            speak("which file you want to make executable")
            print("which file you want to make executable")
            listing = 'ls -l'
            os.system(listing)
            temp = takeCommand().lower()
            filename = ""
            filename += temp
            temporary = "chmod " + "+x " + filename
            cmd = temporary
            os.system(cmd)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'locate' in query:
            speak("which file you want to locate")
            print("which file you want to locate")
            temp = takeCommand().lower()
            filename = ""
            filename += temp
            temporary = "locate " + filename
            cmd = temporary
            os.system(cmd)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

        elif 'open google' in query:
            speak("opening google")
            print("opening google")
            url = 'www.google.com'
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url)
            shell = os.environ.get('SHELL', '/bin/sh')
            os.execl(shell, shell)

       

