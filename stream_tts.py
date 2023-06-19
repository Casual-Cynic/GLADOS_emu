import sys
from elevenlabs import set_api_key, generate, play

audio = generate(
  text=str(sys.argv[1]),
  api_key="cd1d02e15c60d923d70581f3b6eda3c7",
  voice="SX4RvpkwlzfN6wip0Ejh",
  model="eleven_monolingual_v1"
)
play(audio)