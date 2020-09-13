#!/home/mamaah/development/HMG/bin/python3
 import random

def hide_word(word):
    return len(word)*'-'
#Create a word list
WordList = ['Kumba','Mbanga','Okoroba','Besongabang','Mondoni','Tombel','Djottin','Bafut','Noni','Bali','Bakossi']
#Randomly pick a word from the word list
word = random.choice(WordList)
#Print underscores representing the chosen word. 
hidden_word = hide_word(word)
print (hidden_word)
word_count = len(word)
count = 0
chances_left= len(word)
letters = []
while count != word_count:
    print("\n")

    letter = input('Please guess a letter: ')
    if letter not in word:
        print('Try again')
        chances_left -= 1
        count += 1
        print("you've made",count, "mistakes so far")
        print('you have', chances_left,'chances left')
    else:
        letters.append(letter)
        for i in word:
            if i in letters:
                print(i, end="")
            else:
                print('-', end="")
    if count == word_count:
        print("You're a duma ss!")
        break