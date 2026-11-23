import random

def get_user_choice():
    print("あなたの選択肢: 1 (グー) 2 (チョキ) 3 (パー)")
    user_choice = input("あなたの選択 (1/2/3): ")
    return int(user_choice)

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "あなたの勝ち"
    else:
        return "コンピュータの勝ち"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"あなたの選択: {user_choice}")
    print(f"コンピュータの選択: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()