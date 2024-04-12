import os
import time 
import sys
from io import BytesIO
import requests
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
# print(os.environ['OPENAI_API_KEY'])

def setUp():
    load_dotenv()
    client = OpenAI()
    return client

def generate_text(prompt:str, temperature:float=None) ->str:
    client = setUp()
    if temperature is None:
        response = client.chat.completions.create(
                            model='gpt-3.5-turbo',
                            messages=[{'role': 'user', 'content': prompt}])
        return response.choices[0].message.content
    
    response = client.chat.completions.create(
                            model='gpt-3.5-turbo',
                            messages=[{'role': 'user', 'content': prompt}], temperature=0)
    return response.choices[0].message.content


def generate_image(prompt:str, model:str=None) -> None:
    client = setUp()
    response = client.images.generate(model='dall-e-3',
                                      prompt=prompt, 
                                      size='1024x1024')
    
    img_url = response.data[0].url
    data = requests.get(img_url)
    img = BytesIO(data.content)
    img = Image.open(img)
    return img
    
if __name__=='__main__':
    output_format = """" {Q1: {label: question, options: [opt1, opt2, opt3, opt3], 
                          'Correct': correct response}, Q2: ...........}"""
    prompt = f" create a quizz on Computer vision the answers." \
                f" Follow the following format {output_format}"
    # prompt = sys.argv[1]
    # generated_img = generate_image(prompt)
    # generated_img.show()
    text = generate_text(prompt)
    print(text)
