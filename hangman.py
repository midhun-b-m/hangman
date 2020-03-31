from nltk.corpus import words
import random
import string
game = 'y'
bagOfWords = words.words()


def hang(chance):
    if (chance == 9):
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('         ----')

    if (chance == 8):
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('         ----')

    if (chance == 7):
        print('    -------| ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('         ----')
        
    if (chance == 6):
        print('    -------| ')
        print('    |      | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('         ----')
    if (chance == 5):
        print('    -------| ')
        print('    |      | ')
        print('    0      | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('           | ')
        print('         ----')
    if (chance == 4):
        print('    -------| ')
        print('    |      | ')
        print('    0      | ')
        print('    |      | ')
        print('    |      | ')
        print('           | ')
        print('           | ')
        print('         ----')

    if (chance == 3):
        print('    -------| ')
        print('    |      | ')
        print('    0      | ')
        print('   /|      | ')
        print('    |      | ')
        print('           | ')
        print('           | ')
        print('         ----')

    if (chance == 2):
        print('    -------| ')
        print('    |      | ')
        print('    0      | ')
        print('   /|\     | ')
        print('    |      | ')
        print('           | ')
        print('           | ')
        print('         ----')
    if (chance == 1):
        print('    -------| ')
        print('    |      | ')
        print('    0      | ')
        print('   /|\     | ')
        print('    |      | ')
        print('     \     | ')
        print('           | ')
        print('         ----')
    if (chance == 0):
        print('    -------| ')
        print('    |      | ')
        print('    0      | ')
        print('   /|\     | ')
        print('    |      | ')
        print('   / \     | ')
        print('           | ')
        print('         ----')
        print( '\n' )
        print('You lost!!')
        print( '\n' )
        print('ANSWER :',target)
        print( '\n' )

while(game == 'y'):
    print('\n')
    print('=============================')
    print('Hangaman game by Midhun B M')
    print('=============================')
    
    
    rand = random.randint(0,236736)
    target = bagOfWords[rand]
    answer = []
    used = []
    chance = 10

    for dash in range(0,len(target)):
            answer.append('_ ')
            
        
    while(chance > 0):
        print('\n')
        print('Find the word ')
        
        for dash in range(0,len(target)):
            print(answer[dash],end=' ')
            
        
        print('\n')
        guess = input("Guess the word with less than 10 mistakes : ")
        used.append(guess)
        if (guess.lower() in target): 
            for i in range (0,len(target)):
                if (target[i]== guess.lower()):
                    answer[i] = guess.lower()      

        else:
            chance -=1
            

        
        if ("".join(answer) == target) :
            print('\n')  
            for dash in range(0,len(target)):
                print(answer[dash],end=' ')
            print('\n')            
            print("Congrats!! You found the word!! ") 
            game = input("Press y to play again !!") 
            game = game.lower()
            print('\n')
            break
            


        else:
            print('\n')
            print('You have {} chances left'.format(chance))
            print('\n')
            print('used letters',used)
            print('\n')
            hang(chance)
            print('----------------------------------------------------------------------------------')
            if (chance == 0):
                game = input("Press y to play again !!") 
                game = game.lower()
                print('\n')
