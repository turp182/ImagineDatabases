# Wecome to Imagine Databases!  

Imagine Databases is a prototype generative AI application that demonstrates the power of current large language models via engineered prompts.

It takes a concept provided by the user, elaborates on it in the conceptual space, and then produces a relational database definition script around it.  Deceptively simple and powerful.

System and Environment details are below.  

Once those are sorted, just run ImagineDatabases.py.

Alternatively, you can just use the prompts manually, see Full "Debug" Mode below for instructions.

## YouTube Deep Dive

Here's a video that provides several demonstrations and a deep dive into the prompts and the user interface implementation:  https://www.youtube.com/watch?v=Cb2wCi4zJPc

## Python:

I used Python 3.11.8 but it should work with any of the newer versions.

## Python Environment:

I would highly recommend using an Anaconda environment or a python virtual environment:
Conda:  https://conda.io/projects/conda/en/latest/user-guide/getting-started.html
Python virtual environments (venv): https://realpython.com/python-virtual-environments-a-primer/

## Requirements

Install the requirements.txt which includes the user interface package gradio and various dependencies.

Reminder:  pip install -r requirements.txt

## API Configuration

This is based on Azure OpenAI Services (from openai import AzureOpenAI).  Challenge:  Add OpenAI API capabilities!

Copy or rename settings.py.example and update the values to reflect your environment.

## Full "Debug" Mode

You don't really need the API or user interface to see the prommpts in action.  You can just copy and paste the prompts into an editor and then 
  a) Take the first prompt, add your concept in the placeholder, and run it (high creativity using ChatGPT, CopilotPro, whatever), 
  b) Take the results from the first and paste them into the placeholder in the second.  Run this with low creativity.

Enjoy!


