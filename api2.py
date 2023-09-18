import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt='¿Cómo estás?',
    max_tokens=50
)

print(response.choices[0].text)
