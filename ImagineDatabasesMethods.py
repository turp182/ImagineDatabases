#SPDX-License-Identifier: CC-BY-4.0
#Copyright (c) 2024 Jason W. Turpin
#This work is licensed under a Creative Commons Attribution 4.0 International License.

from openai import AzureOpenAI
import settings
import time

def CallAzureOpenAI(prompt, temperature = 0.7, top_p = .95, silent = False):

    messages = [{"role": "user", "content": prompt}]        
    
    if not silent:
        print(f"Starting Azure OpenAI Call, prompt length (chars): {len(str(messages))}")
    
    start = time.time()

    # Setting up the deployment name
    client = AzureOpenAI(
        api_key=settings.api_key,  
        api_version=settings.api_version,
        azure_endpoint = settings.azure_endpoint,
        timeout = 10000,
        max_retries = 3,
    )
                

    completion = client.chat.completions.create(
        model=settings.model, 
        temperature=temperature,
        messages=messages,
        max_tokens=2000,    
        top_p=top_p,
        frequency_penalty=0,
        presence_penalty=0,
    )

    response = completion.choices[0].message.content

    end = time.time()

    if not silent:
        print(f"Finished Azure OpenAI Call, duration: {str(end - start)}, response length (chars):{len(str(response))}")
    return response

def generateCreativeDatabaseDescription_LLM(databaseDesc):
    preparedPrompt = '''\
Below is a concept that a database is being built around.

If:
1. The user asks you to NOT be creative, OR
2. The user includes "Just generate this.", OR
3. The concept is already detailed
Then, just return the concept as is.

Otherwise, please use your judgement as a database designer and a business analyst/information specialist to build out a conceptual description prior to database development.  You should:
1.  Note additional fields by concept.
2.  Include related common concepts for the information domain.
3.  Highlight relationships between concepts.

Be a bit creative.  Ask questions such as:
What is the nature of the concept?
What are common aspects or features of the concept (example: weight for a dinosaur)?
What are common related entities, especially ones that are related to more than one of the concepts in the summary (examle: state in an address)?
What are common features that can be grouped, such as status values or communication types?  These are good candidates for separate related database tables.

Ideally we would like to have six or more concepts represented, if this makes sense in the conceptual domain.

Just return an updated database concept, don't include additional words, expressions, or sentences.

If the concept is of a comical nature, be whimsical in your response.

If the concept description is already detailed, leave it alone and just pass it back.

Here's the concept:
{}
    '''.format(databaseDesc)

    print(preparedPrompt)
    database_def = CallAzureOpenAI(preparedPrompt, temperature=1, top_p=1)    

    return database_def


def generateDatabase_LLM(databaseDesc):
    preparedPrompt = '''\
From the Database Description (which is a description or a concept) below, create an ANSI SQL database DDL script to create the tables, fields, 
and relationships (primary and foreign keys) for a database based the description below.  

* Primary keys should be integer values that auto increment.
* Come up with additional fields not mentioned if asked.
* The response should be complete.
* Order table creation to prevent needing ALTER TABLE statements.
* Do not include additional words, descriptive text, or comments.  
* Do not describe the tables or concepts at all outside of the DDL statements.  

The output will be ONLY the DDL SQL statements.

Database Description:
        {}
    '''.format(databaseDesc)

    print(preparedPrompt)
    database_def = CallAzureOpenAI(preparedPrompt, temperature=0, top_p=0)    

    return database_def




