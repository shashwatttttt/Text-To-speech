
import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

    def list_voices(self):
        """List all available voices."""
        return [{"id": idx, "name": voice.name} for idx, voice in enumerate(self.voices)]

    def speak(self, text, rate=150, voice_id=None):
        """
        Convert text to speech.

        :param text: The text to speak.
        :param rate: The speed of speech (default: 150).
        :param voice_id: The ID of the voice to use (default: system default).
        """
        self.engine.setProperty('rate', rate)

        # Set voice
        if voice_id is not None and 0 <= voice_id < len(self.voices):
            self.engine.setProperty('voice', self.voices[voice_id].id)
        else:
            self.engine.setProperty('voice', self.voices[0].id)  # Default to first voice

        # Speak the text
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    tts = TextToSpeech()

    print("Welcome to Text-to-Speech Automation!")
    print("Available Voices:")
    for voice in tts.list_voices():
        print(f"{voice['id']}: {voice['name']}")

    # User input
    text = input("\nEnter the text you want to convert to speech: ")
    rate = int(input("Enter the speaking rate (e.g., 150): "))
    voice_id = int(input("Enter the voice ID from the list above (default: 0): ") or 0)

    # Speak the text
    print("\nSpeaking the text...")
    tts.speak(text, rate=rate, voice_id=voice_id)
    print("Done!")

