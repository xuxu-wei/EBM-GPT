# %%
from elekit import *
import openai
import os


openai.api_key_path = './api-key.txt'
openai.Model.list()

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)



