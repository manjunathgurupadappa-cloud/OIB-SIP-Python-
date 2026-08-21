import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is currently offline.")
        return ""

def run_assistant():
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        command = listen_command()
        
        if not command:
            continue

        if "hello" in command or "hi" in command:
            speak("Hello! Hope you are having a great day.")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}.")

        elif "date" in command:
            today = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {today}.")

        elif "search" in command or "open browser" in command:
            speak("What topic would you like to search for?")
            query = listen_command()
            if query:
                url = f"https://www.google.com/search?q={query}"
                speak(f"Searching Google for {query}")
                webbrowser.open(url)

        elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

if __name__ == "__main__":
    run_assistant()
