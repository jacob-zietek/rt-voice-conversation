from openai import OpenAI
from pydub.playback import play
import playsound

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.wav")

playsound.playsound("output.wav", block=True)
