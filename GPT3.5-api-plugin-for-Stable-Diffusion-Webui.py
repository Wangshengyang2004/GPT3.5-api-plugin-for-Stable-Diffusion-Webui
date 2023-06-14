import openai
import gradio as gr
import modules
from modules import script_callbacks

openai.api_key = 'your-api-key'  # Replace with your actual OpenAI API key

def generate_longer_generic(prompt, temperature, max_length, num_return_sequences):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-0613",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_length,
        n=num_return_sequences
    )
    return [choice.text.strip() for choice in response.choices]

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as prompt_generator:
        with gr.Column():
            with gr.Row():
                prompt_textbox = gr.Textbox(
                    lines=2, elem_id="promptTxt", label="Start of the prompt")
        with gr.Column():
            with gr.Row():
                temp_slider = gr.Slider(
                    elem_id="temp_slider", label="Temperature", interactive=True, minimum=0, maximum=1, value=0.9)
                maxLength_slider = gr.Slider(
                    elem_id="max_length_slider", label="Max Length", interactive=True, minimum=1, maximum=200, step=1, value=90)
        with gr.Column():
            with gr.Row():
                numReturnSequences_slider = gr.Slider(
                    elem_id="num_return_sequences_slider", label="How Many To Generate", value=5, minimum=1, maximum=20, interactive=True, step=1)
        with gr.Column():
            with gr.Row():
                generate_button = gr.Button(
                    value="Generate", elem_id="generate_button")

        with gr.Tab("Results"):
            with gr.Column():
                results_txt_list = []
                for i in range(20):
                    with gr.Row():
                        textBox = gr.Textbox(label="", lines=3)
                        results_txt_list.append(textBox)

        generate_button.click(fn=generate_longer_generic, inputs=[
            prompt_textbox, temp_slider, maxLength_slider, numReturnSequences_slider
        ], outputs=results_txt_list)

    return (prompt_generator, "Prompt Generator", "Prompt Generator"),

script_callbacks.on_ui_tabs(on_ui_tabs)

