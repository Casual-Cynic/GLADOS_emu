import sys
from elevenlabs import set_api_key, generate, play
from decouple import config

TTS_KEY = config("TTS_KEY")

audio = generate(
  text=str(sys.argv[1]),
  api_key=TTS_KEY,
  voice="SX4RvpkwlzfN6wip0Ejh",
  model="eleven_monolingual_v1"
)
play(audio)