import requests, random        # Web Scraper

url= 'https://www.mit.edu/~ecprice/wordlist.10000'
word_list = []
MINIMUM = 5
MAXIMUM = 10
response = requests.get(url)
with open("word_list.txt", "w") as word_file:
    word_file.write(response.text)

with open("word_list.txt", "r") as r_file: 
    for word in r_file:
        word_list.append(word.strip())  #Remove the white space, lstrip() <- remove left space, rstrip()  <- remove right space
#print(word_list)

# C++: ||, &&,    if (true || false) {}, if (true && false) {}
# Python logic operations: or, and,
# |: Binary OR, &: Binary AND
# C++: true, false
# Python: True, False
selected_word = random.choice(word_list)   
while ((len(selected_word) < MINIMUM) or (len(selected_word) > MAXIMUM)): 
    selected_word = random.choice(word_list)
    
print(selected_word)

