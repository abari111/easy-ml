import os

from embedchain import  App 
from dotenv import load_dotenv

load_dotenv()

# create a bot instance
app = App()

# Embed online resources
app.add('https://en.wikipedia.org/wiki/Alan_Turing')

# Query the app
ans = app.query('Wo is Alan Turing?')
print(ans)
