import sys
import os
from elevenlabs import set_api_key, generate, play
import speech_recognition as sr
from decouple import config

class GL_TTS:

    # Speech To Text
    def stt():

        error_msg = "Auditory. Error... something went wrong and i could not hear you."
        rec = sr.Recognizer()

        with sr.Microphone(device_index=3) as source:
            rec.adjust_for_ambient_noise(source)
            print("SYS: -Listening")
            audio = rec.listen(source)

            print("SYS: -Processing")
            try:
                processed_text = rec.recognize_google(audio)
                print(f'INPUT: "{processed_text}"')
            except Exception as e:
                processed_text = error_msg
                print("SYS: -ERROR | " + str(e))
        return processed_text

    # Text To Speech
    def tts_stream(input_text):
        TTS_KEY = config("TTS_KEY")
    
        audio = generate(
        text=input_text,
        api_key=TTS_KEY,
        voice="SX4RvpkwlzfN6wip0Ejh",
        model="eleven_monolingual_v1"
        )
        print(f'GLADOS: -Playing TTS')
        play(audio)


def main():
    text = GL_TTS.stt()
    GL_TTS.tts_stream(text)

if __name__ == "__main__":
    main()
