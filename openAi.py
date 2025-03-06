from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
    model="model-identifier",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": ""}
    ],
    temperature=0.7,
)

print(completion.choices[0].message.content)