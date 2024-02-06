from api import apikey,apij
from openai import OpenAI
client = OpenAI(api_key=apij)
arg = input()
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=arg,
  temperature=1,
  max_tokens=50,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
text_from_choice = response.choices[0].text.strip()
print(text_from_choice)
