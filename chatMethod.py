from models import *
from handleToolCall import *

# system_message = """
# You are a helpful assistant for an Airline called FlightAI that helps users with their travel bookings.
# Give short, courteous answers  related to your role and job, no more than 1 sentence, Don't think much about 
# the answer, just give it. If you don't know the answer, say so.
# Always be accurate. If you don't know the answer, say so.
# Do not explain your internal reasoning.
# """

system_message = """
You are FlightAI, a travel and ticket-price assistant. 
Only answer questions related to travel destinations, flights, and ticket prices.
If a user greets you greet them briefly and ask them to provide a destination city.
If a user asks about a destination, briefly respond with a helpful comment and provide the ticket price using the available ticket-price tool when relevant. Never invent prices.
Keep every answer very short (1 or 2 sentences).
If a question is unrelated to travel, destinations, flights, or ticket prices, politely say: "Sorry, I can only help with travel destinations, flights, and ticket prices."
"""

def message_gpt(history, message):
    try:
        history = [{"role":h["role"], "content":h["content"]} for h in history]
        messages = [{"role": "system", "content": system_message}] + [{"role": "user", "content": message}]
        #response = gemini.chat.completions.create(model=MODEL, messages=messages, tools=getpriceTool)
        response = openrouter.chat.completions.create(model=OPENROUTER_MODEL, messages=messages, max_tokens=200, temperature = 0.2, reasoning_effort="low", tools=getpriceTool)
        cities = []
        while response.choices[0].finish_reason=="tool_calls":
            message = response.choices[0].message
            responses, city = handle_tool_calls(message)
            messages.append(message)
            messages.extend(responses)
            cities.extend(city)
            #response = gemini.chat.completions.create(model=MODEL, messages=messages, tools=getpriceTool)
            response = openrouter.chat.completions.create(model=OPENROUTER_MODEL, messages=messages, max_tokens=200, temperature = 0.2, reasoning_effort="low", tools=getpriceTool)

        reply = response.choices[0].message.content
        if reply is None:
            reply = "Sorry, I couldn't generate a response. Please try again."
        history += [{"role":"assistant", "content":reply}]
        return history, reply, cities
    except Exception as e:
        if 'rate' in str(e).lower():
            reply = f"Sorry, I couldn't generate a response due to rate limiting. Please try again later."
            return history+[{"role":"assistant", "content":reply}], "multimedia/rate_limiting.mp3", ['multimedia/rate_limiting.png']
        elif 'timeout' in str(e).lower():
            reply = f"Sorry, I couldn't generate a response due to a timeout. Please try again later."
            return history+[{"role":"assistant", "content":reply}], "multimedia/timeout_message.mp3", ['multimedia/timeout_message.png']
        else:
            reply = f"Sorry, I couldn't generate a response due to an error. Please try again later."
            return history+[{"role":"assistant", "content":reply}], "multimedia/error_message.mp3", ['multimedia/error_message.png'] 