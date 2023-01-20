import os
import openai

#openai.organization = ""
openai.api_key = "sk-KEY"
model_engine = "text-davinci-003"

def article_block_generate(prompt:str)->str:

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature = 0.5
    )

    response = completion.choices[0].text
    print(response)
    return response
    

def article_title_generate(prompt:str)->str:
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature = 0.5
    )

    response = completion.choices[0].text
    print()
    print(f" TITLE: {response}")
    return response
