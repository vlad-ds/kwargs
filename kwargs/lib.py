import requests
from time import sleep

def kw():
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    while True:
        quote = requests.get('https://api.kanye.rest').json()['quote']
        print(f"KANYE: {quote}")
