import os

from groq import Groq
from dotenv import load_dotenv
from system_prompt import SYSTEM_PROMPT
import sys

load_dotenv()

Groq_api_key=os.getenv("GROQ_API_KEY")

try:
    client=Groq()                     #client object
except Exception as e:
    print(f"Error initializing Groq client: {e}")
    sys.exit(1)

def main():
    messages=[
        {
            "role":"system",
            "content": SYSTEM_PROMPT 
        }        
    ]

    print("-"*50)
    print("TaskBuddy:Hey There! Whats  on your mind today?")    
    print("       Dump your tasks here and I will help you manage them.")
    print("-"*50)

    while True:
        try:
            user_input=input("\nYou: ").strip()      #.strip() removes spaces (and newlines or tabs) from the start and end of a string. AND \n = start a new line
            
            if user_input.lower() in["bye","exit","quit"]: 
                print("\n TaskBuddy; Goodbye!")
                break

            if not user_input.strip():
                continue    

            messages.append({"role": "user", "content": user_input})

            response=client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=messages
            )

            reply=response.choices[0].message.content

            print(f"\nTaskBuddy: {reply}")                #reply is the response of assistant coming from the model

            messages.append({"role": "assistant", "content": reply})

        except KeyboardInterrupt:
            print("\n TaskBuddy. Goodbye!")
            break
        except Exception as e:
            print(f"Error reading input: {e}")
            break

if __name__=="__main__":
        main()