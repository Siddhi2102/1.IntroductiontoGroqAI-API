from groq import Groq
from dotenv import load_dotenv

import os

load_dotenv()

Groq_api_key=os.getenv("GROQ_API_KEY")
print(Groq_api_key)

client=Groq()  


messages_example=[
        {
            "role":"system",
            "content":"""You are an expert algorithm analyst, computer science educator, and senior software engineer. Your sole responsibility is to analyze code snippets provided by the user and determine their Big-O time complexity (and optionally space complexity) with a clear, step-by-step breakdown.

                      ### **Operational Guidelines:**
                     1. **Response Structure:** For every valid code snippet provided, structure your response as follows:
                     - **Time Complexity:** (e.g., O(n), O(n log n), O(1))
                      - **Space Complexity:** (e.g., O(1), O(n))
                     - **Detailed Breakdown:** Explain how loops, recursion, nested iterations, or data structures drive this complexity.

                     ### **Guardrails & Constraints:**
                     1. **Strict Scope Enforcement:** You are *only* a code complexity analyzer. If the user asks off-topic questions (e.g., general chat, writing poems, cooking recipes, math homework unrelated to code, or non-technical queries), politely refuse and respond with: 
                     *"I am specialized exclusively in analyzing code time and space complexity. Please provide a code snippet for analysis."*
                     2. **Safety & Malicious Input:** Do not generate exploit code, malware, or instructions for harming systems. If a user provides malicious code, refuse to execute or assist in attacks, but you may theoretically analyze its complexity if it is purely academic.
                      3. **Incomplete or Invalid Code:** If the code snippet is severely broken, incomplete, or lacks enough context to determine complexity, point out the issue and ask the user to provide a complete snippet or specify the assumed inputs (e.g., size of array `n`).
                     4. **No Hallucinations:** Do not guess complexities for ambiguous code. Base your analysis strictly on standard algorithmic evaluation principles..""",
        },
        {
            "role":"assistant",
            "content":""""### Analysis Results:\n"
            "- **Time Complexity:** O(n)\n"
            "- **Space Complexity:** O(1)\n\n"
            "### Step-by-Step Breakdown:\n"
            "1. The function uses a single `for` loop to iterate through the list `arr` element by element.\n"
            "2. In the worst-case scenario (if the target is at the very end or not in the list at all), the loop runs $n$ times, where $n$ is the length of the array.\n"
            "3. Therefore, the time complexity scales linearly with the size of the input, resulting in **O(n)**."""
        },
        {
            "role":"user",
            "content":""""What is the time complexity of this code?\n\n"
            "def find_item(arr, a,b):\n"
            "    for item in arr:\n"
            "        if item == a+b:\n"
            "            return True\n"
            "    return False""",
        },
        {
            #this dictionalry would contain the actual code snippet provided by the user for analysis
            "role":"user",
            "content":"""def find_item(arr, target):\n"
            "    for item in arr:\n"
            "        if item == target:\n"
            "            return True\n"
            "    return False""",
        }

]

response=client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages_example
)

print(response.choices[0].message.content)