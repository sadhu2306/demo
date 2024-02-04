import gradio as gr
import openai
 
openai.api_key="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"
 
def code_gen_openai(prompt):
    try:
        # Use the OpenAI GPT-3 API to generate code
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a chat-based model
            messages=[
            {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
       
        # Extract the generated code from the API response
        generated_code = response['choices'][0]['message']['content'].strip()
       
        return generated_code
    except Exception as e:
        return f"Error: {e}"
 
with gr.Blocks() as demo:
    gr.Markdown('<center>**CodeGen App**</center>')
    input = gr.Textbox()
    output = gr.Textbox()
    button = gr.Button("Submit")
    button.click(fn=code_gen_openai, inputs=input, outputs=output)
 
demo.launch(share=True)
