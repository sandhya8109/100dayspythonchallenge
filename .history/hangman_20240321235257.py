import random
from list import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
from hang import logo
print(logo)
print(f"Psssst, the solution is {chosen_word}.")
display = []
for _ in range(word_length):
   display +="_"
while not end_of_game:
   guess  = input("Guess a letter:").lower()
   if guess in display:
     print(f"you'have already guessed {guess}.")
   for position in range(word_length):
     letter =chosen_word[position]
     #print(f"Current position : {position} \n current letter:{letter}\n Guessed letter : {guess}")
     if letter == guess:
       display[position] = letter
   if guess not in chosen_word: 
        print(f"you guessed {guess}, that's not in th word. You lose a life.")
        lives-= 1
        if lives == 0:
         end_of_game = True
         print("you lose")     

   print(f"{''.join(display)}")  
   if "_" not in display:
     end_of_game = True
     print("You win")
   from hang import stages  
   print(stages[lives])  