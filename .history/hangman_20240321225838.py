word_list = ["sandhya", "rimal", "family"]
import random
chosen_word = random.choice(word_list)
print(f"Psssst, the solution is {chosen_word}.")
display = []
word_length = len(chosen_word)
for _ in range(word_length):
   display +="_"
print(display)  
end_of_game = False
while not end_of_game:
   guess  = input("Guess a letter:").lower()
   for position in range(word_length):
     letter =chosen_word[position]
     print(f"Current position : {position} \n current letter:{letter}\n Guessed letter : {guess}")
     if letter == guess:
      display[position] = letter
   print(display)
   if "_" not in display:
     end_of_game = True
     print("You win")