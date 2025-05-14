# Importing necessary libraries
import speech_recognition as sr  # for recognizing speech input
import webbrowser                # for opening web pages
import pyttsx3                   # for text-to-speech conversion
import musiclibrary              # custom music library with song names and URLs

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)           # Queue the text to be spoken
    engine.runAndWait()        # Process and play the queued speech

# Function to process the spoken command
def processcomand(c):
    # If the command is to open Google
    if c.lower() == "open google":
        webbrowser.open("https://google.com")

    # If the command is to open YouTube
    elif c.lower() == "open youtube":
        webbrowser.open("https://youtube.com")

    # If the command starts with "play", play the requested song
    elif c.lower().startswith("play"):
        song = c[5:].strip().lower()  # Extract song name from command
        link = musiclibrary.music.get(song)  # Get song URL from custom music library
        webbrowser.open(link)  # Open the song link in browser

# Speak initial greeting
speak("Hey, I'm your personal assistant Jarvis")

# Continuous loop to keep listening for the keyword "Jarvis"
while True:
    # Create a Recognizer instance to convert speech to text
    r = sr.Recognizer()

    try:
        # Use the microphone as the source of input
        with sr.Microphone() as source:
            print("Listening sir...")
            # Listen for speech input with a timeout
            audio = r.listen(source, timeout=2, phrase_time_limit=2)

        # Convert audio to text using Google's speech recognition
        word = r.recognize_google(audio)

        # If the wake-word "Jarvis" is detected
        if word.lower() == "jarvis":
            speak("Yaa")  # Respond to activation

            # Listen again for the actual command
            with sr.Microphone() as source:
                print("Jarvis active...")
                audio = r.listen(source, phrase_time_limit=2)
                command = r.recognize_google(audio)  # Convert audio command to text

                processcomand(command)  # Process the spoken command

    # Handle exceptions such as timeout, unrecognized speech, etc.
    except Exception as e:
        print("Error; {0}".format(e))
