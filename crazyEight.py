import cards
import packOfCards

# 初始化卡牌,设置卡牌为8时的分值情况.


class init_cards():
    deck = []
    for suit in range(1, 5):
        for rank in range(1, 14):
            new_card = Card(suit, rank)
            if new_card.rank == 8:
                new_card.value = 50
                deck.append(new_card)


# 让游戏一直处于循环
while True:
    done = False
    p_total = c_total = 0

    while not done:
        init_cards()
    # 判断游戏是否结束
        while not game_done:
            blocked = 0
            player_turn()
            if len(p_hand) == 0:
                game_done = True
                print
                print("You won!")
            if not game_done:
                computer_turn()
            if len(c_hand) == 0:
                game_done = True
                print
                print("Computer won!")
            if blocked >= 2:
                game_done = True
                print("Both players blocked. GAME OVER.")
    # 游戏重新开始
    play_again = raw_input("Play again (Y/N)? ")
       if play_again.lower().startswith('y'):
            done = False
        else:
            done = True
        else:
            wrong

