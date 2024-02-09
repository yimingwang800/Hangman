import requests, random        # Web Scraper

def stickman_fucntion(num_tries):

    if num_tries == 7:
        print("  ______ \n","  |    | \n","  |    | \n","  |     \n","  |     \n","  |    \n","  |    \n","__|__\n")

    if num_tries == 6:
        print("  ______ \n","  |    | \n","  |    | \n","  |    | \n","  |     \n","  |    \n","  |    \n","__|__\n")

    if num_tries == 5:
        print("  ______ \n","  |    | \n","  |    | \n","  |    | \n","  |    O \n","  |    \n","  |    \n","__|__\n")

    if num_tries == 4:
        print("  ______ \n","  |    | \n","  |    | \n","  |    | \n","  |    O \n","  |   / \n","  |    \n","__|__\n")

    if num_tries == 3:
        print("  ______ \n","  |    | \n","  |    | \n","  |    | \n","  |    O \n","  |   /| \n","  |    \n","__|__\n")

    if num_tries == 2:
        print("  ______ \n","  |    | \n","  |    | \n","  |    | \n","  |    O \n","  |   /|\ \n","  |    \n","__|__\n")

    if num_tries == 1:
        print("  ______ \n","  |    | \n","  |    | \n","  |    | \n","  |    O \n","  |   /|\ \n","  |   /  \n","__|__\n")

    if num_tries == 0:
        print("  ______ \n","  |    | \n","  |    | \n","  |    | \n","  |    O \n","  |   /|\ \n","  |   / \ \n","__|__\n")

url= 'https://www.mit.edu/~ecprice/wordlist.10000'
word_list = []
MINIMUM = 5
MAXIMUM = 10
response = requests.get(url)
with open("word_list.txt", "w") as word_file:
    word_file.write(response.text)

with open("word_list.txt", "r") as r_file: 
    for word in r_file:
        word_list.append(word.strip())  

selected_word = random.choice(word_list)   
while ((len(selected_word) < MINIMUM) or (len(selected_word) > MAXIMUM)): 
    selected_word = random.choice(word_list)
    
print(selected_word) 
#Dont forget uppercase comment
word_underscore = "_" * len(selected_word)
print(word_underscore) 

num_tries = 7
guessed = False
guessed_letters = []
word_as_list = []

while (not guessed and num_tries > 0):
    print("Please enter a letter (non-uppercase)")
    input_letter = input()
    if (input_letter in selected_word):
        guessed_letters.append(input_letter)
        print("The letters that have been tried are: ")
        print(guessed_letters)
        word_as_list = list(word_underscore)
        indices = [i for i, letter in enumerate(selected_word) if letter == input_letter]
        for index in indices:
            word_as_list[index] = input_letter
        word_underscore = "".join(word_as_list)
        print(word_underscore)
        #print(selected_word.rfind(input_letter))

    else:
       num_tries -= 1
       stickman_fucntion(num_tries)
       guessed_letters.append(input_letter)
       print("The letters that have been tried are: ")
       print(guessed_letters)
    
    if word_underscore == selected_word:
        print("You win!")
        guessed = True
    if num_tries == 0:
        print("You lose!")
    
    


