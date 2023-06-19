from pydub import AudioSegment
from pydub.playback import play as ps
from colorama import init as colorama_init
from colorama import Fore, Style

class ApatureExtensions:
    def stillAlive():
        still_alive_wav = AudioSegment.from_wav('assets/wav/still_alive_8b.wav')

        print(f"\n{Fore.GREEN}=====================================================================================\n")
        with open('assets/ascii/apature_logo.txt') as f:
            print(f.read())
        print(f"\n====================================================================================={Style.RESET_ALL}")
        ps(still_alive_wav)

def main():
    ApatureExtensions.stillAlive()

if __name__ == "__main__":
    main()