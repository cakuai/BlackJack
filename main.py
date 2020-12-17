import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# 計算起手牌是否hit blackjack 若是 則以0表達 若否 則回傳總和 若有ace且總和>21則調整


def calculate_scores(cards):
    '''Return the score calculated from the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# 創立比較函數 比出最後大小
def comparison(guest_scores, cpu_scores):
    if guest_scores == cpu_scores:
        return "Draw"
    elif guest_scores == 0:
        return "Win! BlackJack"
    elif cpu_scores == 0:
        return "Lose! CPU got the BlackJack"
    elif guest_scores > 21:
        return "Lose! beyond 21!"
    elif cpu_scores > 21:
        return "Win! CPU got over 21."
    elif guest_scores < cpu_scores:
        return "Lose"
    elif guest_scores > cpu_scores:
        return "Win!"

# 主程式運行段


def play_game():
    cpu = []
    guest = []
    is_game_over = False
    # 開始抽牌
    for i in range(0, 2):
        cpu.append(deal_cards())
        guest.append(deal_cards())

    while not is_game_over:
        cpu_scores = calculate_scores(cpu)
        guest_scores = calculate_scores(guest)
        print(f"Your card is {guest}, and the total is {guest_scores}.")
        print(f"CPU's first card is {cpu[0]}.")
        if guest_scores == 0 or cpu_scores == 0 or guest_scores > 21:
            is_game_over = True
        else:
            new_card = input(
                "Type 'y' to get a new card, type 'n' to pass: ").lower()
            if new_card == "y":
                guest.append(deal_cards())
            else:
                is_game_over = True

    while cpu_scores != 0 and cpu_scores > 17:
        cpu.append(deal_cards())
        cpu_scores = calculate_scores(cpu)

    print(
        f" Your final hand is {guest}, and the final score is {guest_scores} ")
    print(f" CPU's final hand is {cpu}, and the final score is {cpu_scores} ")
    print(comparison(guest_scores, cpu_scores))


while input("Play game now? Y/N : ").lower() == "y":
    play_game()
