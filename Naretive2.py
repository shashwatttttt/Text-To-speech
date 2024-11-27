import pyttsx3

def text_to_speech(text, rate=150, voice_type="female"):
    engine = pyttsx3.init()

    # Set speech rate (speed of talking)
    engine.setProperty('rate', rate)

    # Get available voices
    voices = engine.getProperty('voices')

    # Select voice based on voice_type
    if voice_type.lower() == "male":
        engine.setProperty('voice', voices[0].id)  # Typically male
    else:
        engine.setProperty('voice', voices[1].id)  # Typically female

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Example usage
text_to_speech('Hello World, I am Naretive AI and I will talk to you', rate=120, voice_type="female")