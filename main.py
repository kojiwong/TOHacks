import cohere
co = cohere.Client('IU4YaG03Odkb7zAcHJ8AHHiYBUUlhPFxPbb7gjhj')
prediction = co.generate(
    model='xlarge',
    prompt='This program will extract relevant information from contracts. Here are some examples:\n\nContract: This influencer Marketing Agreement (“Agreement”) dated on the 23 day of August, 2022 (the “Effective Date”) is made between Oren & Co (the “Influencer”) and Brand Capital (the “Company”) regarding. The Company will compensate the Influencer with five thousand dollars ($5000.00) for the overall Services rendered. This Agreement is effective upon its signing until July 31, 2023, when the final LinkedIn post is uploaded and all Services and compensation are exchanged.\n\nExtracted Text:\nInfluencer: Oren & Co\nCompany: Brand Capital\n--\nContract: This Music Recording Agreement (\"Agreement\") is made effective as of the 13 day of December, 2021 by and between Good Kid, a Toronto-based musical group (“Artist”) and Universal Music Group, a record label with license number 545345 (“Recording Label\"). Artist and Recording Label may each be referred to in this Agreement individually as a \"Party\" and collectively as the \"Parties.\" Work under this Agreement shall begin on March 15, 2022.\n\nExtracted Text:',
    max_tokens=20,
    temperature=0.5,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=["--"],
    return_likelihoods='NONE')
print('Prediction: {}'.format(prediction.generations[0].text))
