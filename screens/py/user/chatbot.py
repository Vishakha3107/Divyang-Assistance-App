from openai import OpenAI

client = OpenAI(api_key="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")

def ask_ai(question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful accessibility assistant for navigation and services."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content