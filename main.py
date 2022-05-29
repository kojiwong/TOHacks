import cohere
co = cohere.Client('IU4YaG03Odkb7zAcHJ8AHHiYBUUlhPFxPbb7gjhj')

def prediction(text):
    input_text = ''
    input_text += text
    prediction = co.generate(
        model='xlarge',
        prompt=input_text,
        max_tokens=20,
        temperature=0.5,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    return'Prediction: {}'.format(prediction.generations[0].text)
