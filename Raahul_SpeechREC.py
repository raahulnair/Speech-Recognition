import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)  # Recognize using Google's speech recognition
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your audio.")
        return ""
    except sr.RequestError as e:
        print("Sorry, there was an error with the request to the Google API.")
        return ""


def process_command(command):
    if "hello" in command:
        speak("Hey there how may I be of help today ")
    elif "what is your name" in command:
        speak("I am your voice assistant.")
    elif "goodbye" in command:
        speak(" Bye bye Have a wonderful day.")
        exit()
    else:
        speak("I cant really respond to that .")

while True:
    command = listen()
    if command:
        process_command(command)
