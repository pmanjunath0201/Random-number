import random

def guess_number():
  """A simple number guessing game."""

  random_number = random.randint(1, 100)
  attempts = 0

  while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))
      attempts += 1

      if guess < random_number:
        print("Too low!")
      elif guess > random_number:
        print("Too high!")
      else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  guess_number()
