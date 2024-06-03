import os

from embedchain import  App 
from dotenv import load_dotenv

load_dotenv()

app = App()
app.add('https://en.wikipedia.org/wiki/Alan_Turing')

ans = app.query('Wo is Alan Turing?')
print(ans)
