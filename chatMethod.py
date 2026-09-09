from models import *
from handleToolCall import *

system_message = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
"""

# def message_gpt(message, history):
#     messages = [{"role": "system", "content": system_message}, {"role": "user", "content": message}]
#     response = gemini.chat.completions.create(model="gemini-3.6-flash", messages=messages)
#     return response.choices[0].message.content



def message_gpt(history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history
    response = gemini.chat.completions.create(model=MODEL, messages=messages, tools=getpriceTool)
    cities = []
    image = None

    while response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        responses, cities = handle_tool_calls(message)
        messages.append(message)
        messages.extend(responses)
        response = gemini.chat.completions.create(model=MODEL, messages=messages, tools=getpriceTool)

    reply = response.choices[0].message.content
    history += [{"role":"assistant", "content":reply}]

    voice = talker(reply)

    if cities:
        ##image = artist(cities[0])
        print(f"Generating image for {cities[0]}")
    
    return history, "out.wav", image