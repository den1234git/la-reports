import random

def main():
    print("ハイ＆ローゲームを始めます。")
    print("最初の数字が決まりました。")
    current_number = random.randint(1, 100)
    print(f"現在の数字: {current_number}")

    while True:
        try:
            guess = int(input("次の数字が大きい場合は 'h'、小さい場合は 'l' を入力してください: "))
            if guess not in ['h', 'l']:
                print("不正な入力です。'h' または 'l' を入力してください。")
                continue

            next_number = random.randint(1, 100)
            print(f"次の数字: {next_number}")

            if (guess == 'h' and current_number < next_number) or (guess == 'l' and current_number > next_number):
                print("正解です！")
            else:
                print("不正解です。")
                print(f"正解は {next_number} でした。")
                break

            current_number = next_number
        except ValueError:
            print("数値を入力してください。")

if __name__ == "__main__":
    main()