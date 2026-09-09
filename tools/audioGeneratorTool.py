from models import *
# def talker(message):
#     response = gemini.audio.speech.create(
#       model="tts-1",
#       voice="onyx",    # Also, try replacing onyx with alloy or coral
#       input=message
#     )
#     return response.content


# from google import genai
# import wave
# import base64

# def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
#     with wave.open(filename, "wb") as wf:
#         wf.setnchannels(channels)
#         wf.setsampwidth(sample_width)
#         wf.setframerate(rate)
#         wf.writeframes(pcm)

# client = genai.Client()

# interaction = client.interactions.create(
#     model="gemini-3.1-flash-tts-preview",
#     input="Say cheerfully: Have a wonderful day!",
#     response_format={"type": "audio"},
#     generation_config={
#         "speech_config": [
#             {"voice": "Kore"}
#         ]
#     }
# )

# wave_file('out.wav', base64.b64decode(interaction.output_audio.data))


from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

def talker(message):
    client = genai.Client()

    interaction = client.interactions.create(
        model="gemini-3.1-flash-tts-preview",
        input=message,
        response_format={"type": "audio"},
        generation_config={
            "speech_config": [
                {"voice": "Kore"}
            ]
        }
    )
    return wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
