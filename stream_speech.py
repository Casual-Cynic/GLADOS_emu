import speech_recognition as sr
import pyaudio

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
        print("SYS: -ERROR | " + str(e))