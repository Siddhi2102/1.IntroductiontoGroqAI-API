import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

Groq_api_key=os.getenv("GROQ_API_KEY")
print(Groq_api_key)

client=Groq()                     #client object

response= client.chat.completions.create(
    model="openai/gpt-oss-20b",

    messages=[
        {
            "role":"user",             #we are telling whose message/prompt is this ,that is user
            "content":"Write a poem on europe",        #and the message/prompt
        }
    ]
)

print(response.choices[0].message.content)
