from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY_HERE")

def ask_ai(question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful accessibility assistant for navigation and services."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content