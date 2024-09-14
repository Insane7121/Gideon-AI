# Gideon-AI
- Gedion is a Python-based personal assistant GUI project developed as a final year university project. The assistant can respond to voice commands, provide information from Wikipedia, open websites, tell the time, send emails, and offer time-based greetings. This project utilizes speech recognition, text-to-speech, and other useful Python libraries to automate basic tasks via voice commands.

## Features
- **Voice Input**: Uses the microphone to capture voice commands.
- **Text-to-Speech**: Responds to user commands using a speech engine.
- **Wikipedia Search**: Provides quick summaries from Wikipedia based on voice queries.
- **Email Sending**: Allows users to send emails by voice command (using Gmail SMTP).
- **Web Browsing**: Opens popular websites like YouTube, Google, and StackOverflow.
- **Time Information**: Tells the current time when asked.
- **Greeting Based on Time**: Greets the user based on the current time (morning, afternoon, or evening).

## Technologies Used
- **Python 3.x**
- **pyttsx3**: Text-to-speech conversion.
- **speech_recognition**: Captures and processes voice commands.
- **wikipedia**: Fetches summaries from Wikipedia.
- **smtplib**: Used for sending emails.
- **webbrowser**: Opens websites based on voice commands.
- **datetime**: Used to get the current time and date for time-based greetings.

## Setup and Installation
1. **Clone the repository** (or download the Gedion.py file):
    ```bash
    git clone https://github.com/your-repo/Gedion.git

2. **Install the required Python libraries**: Run the following command in the terminal or command prompt to install the necessary libraries:
   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia smtplib

3. **Run the project**: After installing the dependencies, you can run the project using Python:
   ```bash
   python Gedion.py

## How to Use
Once the program is running, Gedion will listen for commands and respond accordingly. Some of the available commands are:

- **Wikipedia Search**: Say "Wikipedia" followed by the topic you want to search. Example: "Wikipedia Python programming".
- **Open YouTube**: Say "Open YouTube".
- **Open Google**: Say "Open Google".
- **Open StackOverflow**: Say "Open StackOverflow".
- **Play Music**: Say "Play music" to play a song from the specified folder.
- **Check the Time**: Say "What is the time?" or "Tell me the time", and Gedion will respond with the current time.
- **Send Email**: Say "Send an email", and Gedion will guide you through sending an email.

## Email Configuration
To enable the email feature, you need to configure your email credentials in the Gedion.py file:

1. Replace the email and password in the sendEmail function with your own Gmail credentials:
   ```bash
   server.login('your_email@gmail.com', 'your_password')
- **Important**: It is recommended to use environment variables or other secure methods to handle your email credentials rather than hardcoding them in the script.

2. Ensure that less secure apps is enabled on your Gmail account, or use an app-specific password for better security.

## Customization
You can extend or modify the project by:

- Adding more voice commands for different tasks.
- Integrating additional APIs to provide more functionality (e.g., weather information, news updates).
- Improving the user interface by adding a graphical user interface (GUI) using libraries like Tkinter or PyQt.

## Troubleshooting
- **Microphone Issues**: Ensure your microphone is working properly and is recognized by the system. You may need to configure your microphone settings.
- **Speech Recognition Issues**: Ensure you have a stable internet connection, as the recognize_google function in speech_recognition uses Google’s speech recognition API.

## GUI
- This is a graphical user interface (GUI) built using **Tkinter** for the Gedion personal assistant project. The GUI allows users to interact with Gedion through buttons and text inputs instead of relying solely on voice commands.

## Installation

1. **Clone or Download the Project**:
   ```bash
   git clone https://github.com/your-repo/Gedion_GUI.git
   cd Gedion_GUI
