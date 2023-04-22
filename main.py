from game_data import data
from art import logo
from art import vs
import random
import replit

def game():
  current_score = 0
  end_game = True
  compare_A = random.randint(0, len(data) - 1)
  print(logo)
  while end_game:
    compare_B = random.randint(0, len(data) - 1)
    #Stop same random integer 
    while compare_B == compare_A:
      compare_B = random.randint(0, len(data) - 1)
    data_A = data[compare_A]
    data_B = data[compare_B]
    print(f"Compare A: {data_A['name']}, a {data_A['description']}, from {data_A['country']}.")
    #test print(data_A['follower_count'])
    print(vs)
    print(f"Against B: {data_B['name']}, a {data_B['description']}, from {data_B['country']}.")
    #test print(data_B['follower_count'])
    higher_or_lower = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if data_A["follower_count"] > data_B["follower_count"] and higher_or_lower == 'a':
      current_score += 1
      replit.clear()
      print(logo)
      print(f"You're right! Current score: {current_score}.")
    elif data_A["follower_count"] < data_B["follower_count"] and higher_or_lower == 'b':
      compare_A = compare_B
      current_score += 1
      replit.clear()
      print(logo)
      print(f"You're right! Current score: {current_score}.")
    else:
      replit.clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {current_score}")
      end_game = False
    
game()

