import random as rm

logo = """
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                       
    """
print(logo)
level_1_words = [
    "elephant", "pineapple", "butterfly", "chocolate", "sunflower", 
    "blackberry", "blueberry", "kangaroo", "strawberry", "waterfall", 
    "crocodile", "adventure", "challenge", "tangerine", "honeycomb",
    "windscreen", "motorbike", "overboard", "telegraph", "watermelon"
]

level_2_words = [
    "backpacker", "telescope", "bookkeeper", "lighthouse", "snowboard",
    "adrenaline", "explosion", "restaurant", "basketball", "volleyball",
    "microscope", "directional", "pineapples", "adventurer", "remarkable",
    "government", "windscreen", "conference", "atmosphere", "megaphone"
]

level_3_words = [
    "congratulation", "friendliness", "outstandingly", "communication", "misunderstood", 
    "counterattack", "photographer", "understanding", "demonstration", "revolutionary", 
    "unbelievable", "multinational", "organization", "uncomfortable", "relationship", 
    "determination", "appreciation", "transportation", "unpredictable", "investigation"
]


level = input("Choose a level (1, 2, 3): ")

if level == "1":
    hangman_words =  level_1_words
elif level == "2":
    hangman_words  = level_2_words
elif level == "3":
    hangman_words= level_3_words
else:
    print("Invalid level, defaulting to Level 3.")
    hangman_words = level_3_words



hangman_stages = [
    """
      ------
      |    |
      |    
      |    
      |    
      |    
    -----
    """,
    """
      ------
      |    |
      |    O
      |    
      |    
      |    
    -----
    """,
    """
      ------
      |    |
      |    O
      |    |
      |    
      |    
    -----
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |    
      |    
    -----
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |    
      |    
    -----
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / 
      |    
    -----
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |    
    -----
    """
]

random_word = rm.choice(hangman_words)

blank_place =""
for position in range(0,len(random_word)):
    blank_place +="_"


lives =6
vowels = "aeiou"

correct_letters = []
game_over = False

display = ""
for letter in random_word:
    if   letter in vowels:
        display+=letter
          
    else :
        display += "_"
print(display)

while  not game_over:
    guess =input("Guess a letter.")

    
    new_display = ""
    for letter in random_word:
        if letter in vowels or letter in correct_letters or letter == guess:
            new_display += letter
            correct_letters+=guess
        else:
            new_display +=  "_"
    

      

    print(new_display) 
    if guess  not in random_word:
        lives-=1
        print(hangman_stages[6 - lives])
        print(f"Lives left :{lives}") 
        if lives ==0 :
            game_over =True
            print(f"Word was {random_word}")
            print("You lose! , Try again.")
              

    if "_" not in new_display:
        game_over = True
        print("You win")

print(hangman_stages[6-lives])
if lives==6 :
    print("Hurray! ,You are the Champion.")     




