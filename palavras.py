import openai


openai_api_key = input("Chave da OpenAI: ")
client = openai.OpenAI(api_key=openai_api_key)

def escolher_palavra():

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature= 1.5,
        messages=[
            {"role": "user", "content": "Me dê, com apenas uma palavra, uma sugestão de palavra para usar em um jogo de forca."}
        ]
    )

    palavra = (response.choices[0].message.content.strip()).lower().replace(".","").replace(" ","")
    
    return palavra