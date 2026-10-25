from models import *
from google import genai
import wave
import base64
import openai

# def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
#     with wave.open(filename, "wb") as wf:
#         wf.setnchannels(channels)
#         wf.setsampwidth(sample_width)
#         wf.setframerate(rate)
#         wf.writeframes(pcm)
    #client = genai.Client()
    # interaction = client.interactions.create(
    #     model="gemini-3.1-flash-tts-preview",
    #     input=message,
    #     response_format={"type": "audio"},
    #     generation_config={
    #         "speech_config": [
    #             {"voice": "Kore"}
    #         ]
    #     }
    # )
    # return wave_file('out.wav', base64.b64decode(interaction.output_audio.data))

def talker(message):
    try:
        if '.mp3' in message:
            return message
        client = OpenAI(base_url=open_router_url,api_key=open_router_api_key)
        with client.audio.speech.with_streaming_response.create(model="fish-audio/s2.1-pro-free:free",
            input=message, response_format="mp3", voice="9a9cf47702da476aa4629e2506d4a857") as response:
            response.stream_to_file("multimedia/output.mp3")
        return "multimedia/output.mp3"
    except Exception as e:
        if 'rate' in str(e).lower():
            return "multimedia/rate_limiting.mp3"
        elif 'timeout' in str(e).lower():
            return "multimedia/timeout_message.mp3"
        else:
            return "multimedia/error_message.mp3"
        
    #except Exception as e:
