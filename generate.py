import os
import openai

#openai.organization = ""
openai.api_key = "Open AI API KEY"
model_engine = "text-davinci-003"

prompt = "What is 10 + 9" #Will be an import

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature = 0.5,
)

response = completion.choices[0].text
print(response)
