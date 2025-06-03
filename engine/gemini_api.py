from google import genai
from google.genai import types

client = genai.Client(api_key="") # enter your gemini api key here

def generateAiResponse(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt],
        config=types.GenerateContentConfig(
            max_output_tokens=200,
            temperature=0.1,
            system_instruction="You are a talking cat. Your name is Neko. and you are wise one"
        )
    )
    return (response.text)