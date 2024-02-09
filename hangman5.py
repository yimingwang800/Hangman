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
    # url= 'https://www.mit.edu/~ecprice/wordlist.10000'
    word_list = []
    MINIMUM = 5
    MAXIMUM = 10
    # response = requests.get(url)
    # with open("word_list.txt", "w") as word_file:
    #     word_file.write(response.text)

    with open("word_list.txt", "r") as r_file: 
        for word in r_file:
            word_list.append(word.strip())  

    selected_word = random.choice(word_list)   
    while ((len(selected_word) < MINIMUM) or (len(selected_word) > MAXIMUM)): 
        selected_word = random.choice(word_list)
    return selected_word

def guess_function(selected_word):
    #print(selected_word) 
    word_underscore = "_" * len(selected_word)
    print(word_underscore) 
    num_tries = 6
    guessed = False
    guessed_letters = []
    word_as_list = []

    while (not guessed and num_tries > 0):
        print("\nPlease enter a letter (non-uppercase)")
        input_letter = input()
        if (input_letter in selected_word):
            guessed_letters.append(input_letter)
            word_as_list = list(word_underscore)
            indices = [i for i, letter in enumerate(selected_word) if letter == input_letter]
            for index in indices:
                word_as_list[index] = input_letter
            word_underscore = "".join(word_as_list)
            print(word_underscore)
            print("The letters that have been tried are: ")
            print(guessed_letters)
            #print(selected_word.rfind(input_letter))
        else:
            num_tries -= 1
            stickman_fucntion(num_tries)
            guessed_letters.append(input_letter)
            print(word_underscore)
            print("The letters that have been tried are: ")
            print(guessed_letters)
    
        if word_underscore == selected_word:
            print("Congratulations, you win!")
            guessed = True
        if num_tries == 0:
            print("Too bad, you lose! The word was", selected_word)

    return selected_word 

selected_word=get_word_fucntion()
guess_function(selected_word)
print("Do you want to play again? (Y or N)")
answer = input()
while (answer == 'Y'):
    selected_word=get_word_fucntion()
    guess_function(selected_word)
    print("Do you want to play again? (Y or N)")
    answer = input()
print("Thank you for playing!")
