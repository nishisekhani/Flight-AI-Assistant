import os

import gradio as gr
from chatMethod import *


ticket_prices = {"london":799, "paris": 899, "tokyo": 1420, "sydney": 2999}
for city, price in ticket_prices.items():
    set_ticket_price(city, price)
    
#ui = gr.ChatInterface(fn=message_gpt)


def put_message_in_chatbot(message, history):
    print(message)
    return "", history + [{"role":"user", "content":message}]

# UI definition

with gr.Blocks() as ui:
    with gr.Row():
        chatbot = gr.Chatbot(height=300)
        image_output = gr.Image(height=300, interactive=False)
    with gr.Row():
        audio_output = gr.Audio(interactive=False, autoplay=True)
    with gr.Row():
        message = gr.Textbox(label="Chat with our AI Assistant:", submit_btn = True)
        button =  gr.Button()

# Hooking up events to callbacks
    button.click(put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, chatbot]).then(message_gpt, inputs=chatbot, outputs=[chatbot, audio_output, image_output]
    )

# Launch the local server
if __name__ == "__main__":
    ui.launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", "7860")),
    )


    
