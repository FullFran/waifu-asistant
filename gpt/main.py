import openai


import openai
openai.api_key = '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'


#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

def generar_respuesta(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    return message

generar_respuesta(input('Fran:'))