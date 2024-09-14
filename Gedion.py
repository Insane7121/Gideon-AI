import datetime
import os
import smtplib
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice to the second voice (female)

# Function to make the assistant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am Gideon. Sir, please tell me how may I help you.")

# Function to listen to user's commands using speech recognition
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "none"
    return query

# Function to send emails (credentials should be handled securely, not hard-coded)
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')  # Use environment variables for credentials
        server.sendmail('your_email@gmail.com', to, content)
        server.close()
        speak("Email has been sent successfully!")
    except Exception as e:
        print(e)
        speak("Sorry, I am unable to send the email.")

# Main function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  # Convert the query to lowercase for easier matching

        # Wikipedia search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open YouTube
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        # Open Google
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        # Open StackOverflow
        elif 'open stackoverflow' in query:
            speak("Opening StackOverflow")
            webbrowser.open("stackoverflow.com")

        # Play Music
        elif 'play music' in query:
            music_dir = 'C:\\Users\\shubham\\Music'
            songs = os.listdir(music_dir)
            if songs:
                print(songs)
                speak("Playing music")
                os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song
            else:
                speak("No music files found in the directory.")

        # Tell the time
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        # Open games directory
        elif 'open games' in query:
            gamepath = "C:\\Games"
            try:
                os.startfile(gamepath)
            except FileNotFoundError:
                speak("Games folder not found")

        # Send an email
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipient_email@gmail.com"  # Replace with the recipient's email
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send the email at this moment.")
