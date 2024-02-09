import requests, random         # Web Scraper


url = 'https://www.mit.edu/~ecprice/wordlist.10000'

response = requests.get(url)

word = random.choice(response.text.split())
print(word)

word_in_char = list(word)
print(word_in_char)

