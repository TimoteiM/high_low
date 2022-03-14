
import random
from High_lower_data import data
from logo_high_lower import logo
def game():
    game_over=False
    k=0
    result_a=random.choice(data)
    while not game_over:
        result_b=random.choice(data)
        while(result_a["name"]==result_b["name"]):
            result_b=random.choice(data)
        print("Compare A: " + result_a["name"] + ", " + result_a["description"] + " from " + result_a["country"])
        print(logo)
        print("Compare B: " + result_b["name"] + ", " + result_b["description"] + " from " + result_b["country"])
        guess=input("Who has more followers? 'A' or 'B'?")
        if(guess=='A' and result_a["follower_count"]>result_b["follower_count"]):
            k+=1
            print(f"Your score is {k}")
        elif guess=='B' and result_b["follower_count"]>result_a["follower_count"]:
            k+=1
            print(f"Your score is {k}")
        else:
            print(f"Your score is {k}, game over")
            game_over=True
        result_a=result_b
    question=input("Type 'y' to play another game")
    if(question=="y"):
        game()
game()
#Testing git