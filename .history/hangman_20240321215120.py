word_list = ["Sandhya", "Rimal", "Family"]
import random
chosen_word = random.choice(word_list)
print(f"Psssst, the solution is {chosen_word}.")
display = []
word_length = len(chosen_word)
for _ in range(word_length):
   display +="_"
print(display)  

guess  = input("Guess a letter:").lower()
for position in range(word_length):
  letter =chosen_word[position]
  if letter == guess:
   display[position] = letter
print(display)