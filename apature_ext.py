from pydub import AudioSegment
from pydub.playback import play as ps

class ApatureExtensions:
    def stillAlive():
        still_alive_wav = AudioSegment.from_wav('assets/wav/still_alive_8b.wav')

        with open('assets/ascii/apature_logo.txt') as f:
            print(f.read())
        ps(still_alive_wav)
        print("playing song")

def main():
    ApatureExtensions.stillAlive()

if __name__ == "__main__":
    main()