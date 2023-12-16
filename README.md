# Jarvis AI

This project implements a simple AI assistant named Jarvis using the OpenAI API. The assistant is capable of various functionalities and uses several libraries and modules.

## Functionalities

### Speech and Interaction
- Utilizes `pyttsx3` for speech synthesis and `speech_recognition` for voice interaction.
- Greets the user based on the time of the day.
- Listens to user commands and responds accordingly.

### Time and Date
- Fetches the current time and date using `datetime`.

### System Information
- Retrieves CPU usage and battery information via `psutil`.
- Takes screenshots using `pyautogui`.

### Web Interaction
- Opens web browsers to search for queries using `webbrowser`.
- Opens specific websites like YouTube, Google, and Wikipedia.

### Language Processing
- Translates voice input to text using `googletrans`.

## Libraries Used
- `os`: Operating system functionalities.
- `webbrowser`: For accessing web URLs.
- `googletrans`: Translation of text.
- `pyttsx3`: Text-to-speech conversion.
- `datetime`: Fetching date and time.
- `speech_recognition`: Speech recognition functionality.
- `wikipedia`: Accessing Wikipedia data.
- `smtplib`: Sending emails (currently commented out).
- `pyautogui`: Taking screenshots.
- `psutil`: Retrieving system information.

## How to Use
1. Run the main script.
2. Jarvis will greet and await commands.
3. Speak commands for functionalities like time, date, system info, web searches, etc.
4. Exit by saying "stop."

## Note
- Some functionalities (like sending emails, Wikipedia search, etc.) are commented out or not fully implemented.

Feel free to contribute or expand upon the functionalities!
