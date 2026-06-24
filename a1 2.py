import httpcore
if not hasattr(httpcore, "SyncHTTPTransport"):
    setattr(httpcore, "SyncHTTPTransport", httpcore.connectionPool)
import speech_recognition as sr
import pyttsx3
from googletrans import Translator 
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate, 150')
    voice = engine.getProperty("voices")
    if language == "en":
        engine.setProperty("voice",voice[0].id)
    else:
        if len(voice) > 1:
            engine.setProperty("voice", voice[1].id)
        else:
            engine.setProperty("voice", voice[0].id)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("please speak now in english ")
        audio = recognizer.listen(source)
    try:
        print("recognizing speech")
        text= recognizer.recognize_google(audio, language="en-US")
        print("you said: {text}")
        return text
    except sr.UnknownValueError:
        print("could not understand the audio")
    except sr.RequestError as e:
        print(f"api error{e}")
    return ""

def translate_text(text, target_language="es"):
    translator = Translator()
    translation = translator.translalate(text, des=target_language)
    print(f"translated text: {translation.text}")
    return translation.text

def display_language_options():

    print("🌍 Available translation languages: ")

    print("1. Hindi (hi)")

    print("2. Tamil (ta)")

    print("3. Telugu (te)")

    print("4. Bengali (bn)")

    print("5. Marathi (mr)")

    print("6. Gujarati (gu)")

    print("7. Malayalam (ml)")

    print("8. Punjabi (pa)")

# User selects language

    choice = input("Please select the target language number (1-8): ")

    language_dict = {

    "1": "hi",

    "2": "ta",

    "3": "te",

    "4": "bn",

    "5": "mr",

    "6": "gu",

    "7": "ml",

    "8": "pa"

    }


    return language_dict.get(choice, "es") # Default to Spanish if invalid input

# Main function to combine all steps

def main():

# Step 1: Display language options and get user's choice

    target_language = display_language_options()


# Step 2: Speech-to-Text (recognizing English speech)

    original_text = speech_to_text()


    if original_text:

# Step 3: Translate to selected target language

        ranslated_text = translate_text(original_text, target_language=target_language)


# Step 4: Text-to-Speech (Translate output and speak it)

        speak(translated_text, language=target_language) # Updated to target language voice code

        print("✅ Translation spoken out!")

if __name__ == "__main__":

    main()