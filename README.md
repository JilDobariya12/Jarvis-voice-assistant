# 🧠 Jarvis - Voice Assistant in Python

Jarvis is a simple voice-controlled assistant built using Python. It listens to your voice commands and performs tasks like opening Google, YouTube, and playing songs from a custom music library.

## 🔧 Features
- 🎙 Voice recognition using SpeechRecognition
- 🗣 Text-to-speech with pyttsx3
- 👂 Wake-word detection ("Jarvis")
- 🌐 Opens Google and YouTube by voice command
- 🎵 Plays songs using a custom Python music library

## 🚀 Technologies Used
- Python
- speech_recognition
- pyttsx3
- webbrowser
- A custom Python dictionary for music URLs

## 💻 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/JiDobariya12/Jarvis-voice-assistant.git
   cd Jarvis-voice-assistant
2. Install the required Python libraries:
    ```bash
    pip install SpeechRecognition pyttsx3 pyaudio
3. Run the assistant:
   ```bash
   python jarvis.py

## Sample Music Library Code:
  ```python
  music = {
    "blue eyes" : "https://youtu.be/NbyHNASFi6U?si=NdExvnxP17tIozhX",
    "love dose" : "https://youtu.be/TvngY4unjn4?si=Klb9ajmUNw62F9C0"
  }
