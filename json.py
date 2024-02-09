import requests
import json

#! Offlines version
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)

# #! Text Method
# with open('words.txt') as w_file:
#     w_file.write(response.text)

# with open('words.json', 'w') as r_file:
#     words = r_file.read().splitlines()  

#! JSON method          
words = response.text.splitlines()          #! ASCII '\n'
with open('words.json', 'w') as w_file:
    w_file.write(json.dumps(words))         #! Convert List to string

string_list = '[1, 2, 4]'
my_list = json.loads(string_list)           #! my_list is JSON


with open('words.json', 'w') as w_file:
    w_file.dump(my_list, w_file)            #! Dump JSON to file   
with open('words.json', 'r') as r_file:
    words = json.load(r_file)               #! Read directly from JSON file
print(words)

# Method 2
# with open('words.json', 'r') as r_file:
#    words = r_file.read().splitlines()
# print(words)

#? string <> JSON          <- string
#? json.loads & json.dumps

#? file <> JSON          
#? json.load & json.dump

#! json.load vs json.loads      # s: String
#! json.dump vs json.dumps      # s: String