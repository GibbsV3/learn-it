from openai import OpenAI
from dotenv import dotenv_values

if __name__ == "__main__":
    config = dotenv_values()
    client = OpenAI(api_key=config['OPENAI_API_KEY'])
    response = client.responses.create(model='gpt-6-luna',input='Give me a fun brain teaser that an adult can solve within 5 minutes', )
    print(response.output_text)
