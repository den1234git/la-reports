import random

def main():
    total_points = 10
    while True:
        print(f"現在のポイント: {total_points}")
        if total_points <= 0:
            print("ゲームオーバー！")
            break
        
        bet = input("ベットするポイントを入力してください（1-10）: ")
        if not bet.isdigit() or int(bet) < 1 or int(bet) > 10:
            print("無効な入力です。1から10までの整数を入力してください。")
            continue
        
        bet = int(bet)
        
        print("表か裏かを予想してください。入力してください（表: 1, 裏: 2）: ")
        guess = input()
        if guess not in ['1', '2']:
            print("無効な入力です。1か2を選択してください。")
            continue
        
        guess = int(guess)
        result = random.randint(1, 2)
        
        if guess == result:
            total_points += 2
            print(f"正解！あなたの予想が{result}となりました。現在のポイント: {total_points}")
        else:
            total_points -= 1
            print(f"不正解。あなたの予想が{result}となりました。現在のポイント: {total_points}")

if __name__ == "__main__":
    main()