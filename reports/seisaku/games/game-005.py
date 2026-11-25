def roll_dice():
    import random
    return random.randint(1, 6)

def move_player(current_position):
    dice_roll = roll_dice()
    print(f"サイコロの目: {dice_roll}")
    new_position = current_position + dice_roll
    if dice_roll == 2 and new_position < 60:
        new_position -= 1
        print("ドブル！1マス後ろに戻ります。")
    return new_position

def check_win(player_position):
    return player_position >= 60

def main():
    players = int(input("プレイヤー数を入力してください: "))
    player_positions = [0] * players

    while True:
        for i in range(players):
            print(f"\nプレイヤー{i+1}の番です。")
            input("Enterキーを押してサイコロを振ってください。")
            player_positions[i] = move_player(player_positions[i])
            print(f"プレイヤー{i+1}の現在の位置: {player_positions[i]}")

            if check_win(player_positions[i]):
                print(f"プレイヤー{i+1}が勝ちました！")
                return

if __name__ == "__main__":
    main()