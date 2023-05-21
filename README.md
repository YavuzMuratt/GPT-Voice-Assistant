
# Audio Transcription and Response Generation using OpenAI's Chat Model

This project is a Python program that transcribes audio input to text, generates a response using the OpenAI GPT-3.5 Turbo model, and speaks the response out loud using the pyttsx3 library.

## Requirements

- Python 3.x
- speech_recognition library
- openai library
- pyttsx3 library

## Setup and Usage

1. Clone the repository or download the source code.

2. Obtain an OpenAI API key by signing up on the OpenAI website and create an environment variable OPENAI_API_KEY with your API key.

- The program will prompt you to provide audio input. Speak into your microphone, and the program will transcribe it to text.

- The generated text is then used as input to the OpenAI GPT-3.5 Turbo model to generate a response.

- The response is spoken out loud using the default text-to-speech voice provided by the pyttsx3 library.

# Configuration
- To adjust the speech rate, modify the rate parameter in the speak_response() method in main.py.

- You can explore different models available in the OpenAI API by modifying the model parameter in the generate_response() method in main.py.

- Additional customization options for pyttsx3, such as changing the voice or adjusting the volume, can be explored using the library's documentation.

# License
This project is licensed under the MIT License.

Acknowledgements
OpenAI for providing the GPT-3.5 Turbo model.

pyttsx3 for the text-to-speech functionality.

speech_recognition for audio transcription.

# Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# Disclaimer
This project is for educational purposes and serves as a basic example of using speech recognition, natural language processing, and text-to-speech functionality. It may not be suitable for production environments or handle all possible scenarios.

Always use the OpenAI API responsibly and adhere to the usage guidelines and terms provided by OpenAI.
