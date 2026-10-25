import os

import gradio as gr
from chatMethod import *


ticket_prices = {"london":799, "paris": 899, "tokyo": 1420, "sydney": 2999}
for city, price in ticket_prices.items():
    set_ticket_price(city, price)
    
#ui = gr.ChatInterface(fn=message_gpt)


def put_message_in_chatbot(message, history):
    return "", message, history + [{"role":"user", "content":message}]

# UI definition

with gr.Blocks() as ui:
    reply = gr.State()
    cities = gr.State(value=[])    
    usermessage = gr.State()
    with gr.Row():
        chatbot = gr.Chatbot(height=300)
        image_output = gr.Image(height=300, interactive=False)
    with gr.Row():
        audio_output = gr.Audio(interactive=False, autoplay=True)
    with gr.Row():
        message = gr.Textbox(label="Chat with our AI Assistant:(Currently has prices for - London, Paris, Tokyo, Sydney)", submit_btn = False)
    with gr.Row():
        button =  gr.Button(value="Send")

# Hooking up events to callbacks
    button.click(put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, usermessage, chatbot]).then(message_gpt, inputs=[chatbot, usermessage], outputs=[chatbot, reply, cities]).then(
        talker, inputs=reply, outputs=audio_output).then(
        lambda cities: artist(cities) if cities else None, inputs=cities, outputs=image_output)

# Launch the local server
if __name__ == "__main__":
    ui.launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", "7860")),
    )


    
