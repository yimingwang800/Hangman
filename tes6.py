import requests, random        # Web Scraper

def stickman_fucntion(num_tries):

    if num_tries == 6:
        print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |      \n"
        "  |     \n"
        "  |     \n"
        "__|__\n")

    if num_tries == 5:
        print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |     \n"
        "  |     \n"
        "__|__\n")

    if num_tries == 4:
        print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    / \n"
        "  |     \n"
        "__|__\n")

    if num_tries == 3:
        print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    /| \n"
        "  |     \n"
        "__|__\n")

    if num_tries == 2:
        print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |      \n"
        "__|__\n")

    if num_tries == 1:
        print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |    /  \n"
        "__|__\n")

    if num_tries == 0:
        print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |    / \ \n"
        "__|__\n")

def get_word_fucntion():
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
    
    return selected_word 

selected_word=get_word_fucntion()

   