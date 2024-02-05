import gradio as gr
import google.generativeai as key

key.configure(api_key='AIzaSyCfwsFgerjucVWZy2V6ZU76dMMPuYZ7Dag')

models = [m for m in key.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def generate_code(prompt):
    response =generate_code
    if model:
        completion=key.generate_text(
            model=model,
            prompt=prompt,
            temperature=0,
            max_output_tokens=800,
        )
        response = completion.result
        return response
    else:
        return "No module found"
 
with gr.Blocks() as demo:
    gr.Markdown('<center>**CodeGen App**</center>')
    input = gr.Textbox()
    output = gr.Textbox()
    button = gr.Button("Submit")
    button.click(fn=generate_code, inputs=input, outputs=output)
 
demo.launch(share=True)
