import openai
import gradio as gr
import modules
from modules import script_callbacks
import json
import os

#os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
#os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

#def get_api_key():
#    openai_key_file = '../envs/openai_key'
#    with open(openai_key_file, 'r', encoding='utf-8') as f:
#        openai_key = json.loads(f.read())
#    return openai_key['api']
openai.api_key = "your-api-key"

class ChatGPT:
    def __init__(self, user):
        self.user = user
        self.messages = [{"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"}]

    def ask_gpt(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        rsp = openai.ChatCompletion.create(
          model="gpt-3.5-turbo-0613",
          messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": rsp.get("choices")[0]["message"]["content"]})
        return rsp.get("choices")[0]["message"]["content"]

def on_ui_tabs():
    chat_gpt = ChatGPT("user")

    with gr.Blocks(analytics_enabled=False) as prompt_generator:
        with gr.Column():
            with gr.Row():
                prompt_textbox = gr.Textbox(
                    lines=2, elem_id="promptTxt", label="Start of the prompt")
        with gr.Column():
            with gr.Row():
                generate_button = gr.Button(
                    value="Generate", elem_id="generate_button")

        with gr.Tab("Results"):
            with gr.Column():
                result_textbox = gr.Textbox(label="", lines=3)

        generate_button.click(fn=chat_gpt.ask_gpt, inputs=[
            prompt_textbox
        ], outputs=result_textbox)

    return (prompt_generator, "Prompt Generator", "Prompt Generator"),

script_callbacks.on_ui_tabs(on_ui_tabs)
