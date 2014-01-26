import time
import random 
 
print "Hello! It's time to play hangman!"
time.sleep(1) 

print "All of the items in this list have to do with programming in Python. Have fun!"
time.sleep(1)

print "Start guessing..."
time.sleep(0.5)

wordlist = ["python", "programming", "pyladies", "strings", "variables", "input", "list", "loop", "module", "developer"]

keep_going = ""

while keep_going != "no":
    word = random.choice(wordlist)
    turns = 10
    guesses = ""

    while turns > 0:         
        not_guessed = 0

        for char in word:      
            if char in guesses:    
                print char,    
            else:
                print "_",     
                not_guessed = not_guessed + 1   

        if not_guessed == 0:        
            print "You won! Good job!!"
            keep_going = raw_input("Would you like to play again? ")
            break         
 
        guess = raw_input("Guess a character: ") 
        guesses = guesses + guess    

        if guess not in word:  
            turns = turns - 1       
            print "Wrong."   
            print "You have", turns, "more guesses."

            if turns == 0:           
                print "You lose. The word was", word
                keep_going = raw_input("Would you like to play again? ") 
                
