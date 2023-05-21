import openai
import pyttsx3
import speech_recognition as sr


def transcribe_audio_to_text():
    recognizer = sr.Recognizer()

    # Capture audio from the user
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise levels
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio input
        audio = recognizer.listen(source)

    try:
        # Convert audio to text
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None

    except sr.RequestError as e:
        print("Error: ", e)
        return None


def generate_response(input_text):
    # Set up OpenAI API credentials
    openai.api_key = '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'

    # Set the parameters for the API call
    prompt = input_text
    model = 'gpt-3.5-turbo'
    max_tokens = 50  # Response length

    try:
        # Generate the response using the OpenAI API
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,  # Generate a single response
            stop=None,  # Stop token(s) to end the response
            temperature=0.7,  # Temperature for response randomness
        )

        # Extract the generated text from the API response
        generated_text = response.choices[0].text.strip()

        return generated_text

    except Exception as e:
        print("Error:", e)
        return None


def speak_response(response_text):

    engine = pyttsx3.init()

    # Set the speech rate
    engine.setProperty('rate', 150)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)

    try:
        # Speak the response text
        engine.say(response_text)
        engine.runAndWait()

    except Exception as e:
        print("Error:", e)


def main():

    input_text = transcribe_audio_to_text()

    if input_text:
        response_text = generate_response(input_text)

        if response_text:
            speak_response(response_text)
        else:
            print("Failed to generate response.")
    else:
        print("Failed to transcribe audio.")


if __name__ == '__main__':
    main()