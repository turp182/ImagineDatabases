#SPDX-License-Identifier: CC-BY-4.0
#Copyright (c) 2024 Jason W. Turpin
#This work is licensed under a Creative Commons Attribution 4.0 International License.

import gradio as gr
import ImagineDatabasesMethods

def database_script_generator(database_desc):        
    database_desc = ImagineDatabasesMethods.generateCreativeDatabaseDescription_LLM(database_desc)
    database_script = ImagineDatabasesMethods.generateDatabase_LLM(database_desc)
    yield database_script

prompt = gr.TextArea(label="Describe your database.", value="Antique toys by category with country of origin, age, and owner.")
generatedScripts = gr.TextArea(label="Generated Scripts", interactive=True)

with gr.Blocks() as demo:
    prompt = prompt
    generatedScripts = generatedScripts

demo = gr.Interface(
    database_script_generator,
    [ prompt ],
    generatedScripts,    
    title="Imagine Databases!",
    description='''\
    So I hear you are looking a database script.  You've come to the right place.  Tell me about this... database.

    A concept is sufficient, I'll elicidate, elaborlate, and expand on whatever you provide.
    
    Or give me a detailed specification (put "Just generate this." at the top to skip elaboration).

    If you don't like the results or get an error try again.

    Have a great database!
    ''',live=False,
    examples= [
        ["small business inventory management", True],
        ["baseball cards", True],
        ["there was an old lady who lived in a shoe", True]]
).queue()

demo.launch(share=True) # set share to True to create a temporarly gradio public URL!