import os, random

def play_blackjack():
    os.system("clear")
    print("🃏 Mini Blackjack")
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    player = random.sample(cards,2)
    dealer = random.sample(cards,2)
    print(f"Your cards: {player}, Total: {sum(player)}")
    while sum(player)<21:
        choice = input("Hit or Stand? ").lower()
        if choice=="hit":
            player.append(random.choice(cards))
            print(f"Your cards: {player}, Total: {sum(player)}")
        else:
            break
    print(f"Dealer: {dealer}, Total: {sum(dealer)}")
    if sum(player)>21:
        print("❌ You Bust! Dealer wins")
    elif sum(dealer)>21 or sum(player)>sum(dealer):
        print("🎉 You win!")
    elif sum(player)==sum(dealer):
        print("Draw! 🤝")
    else:
        print("❌ Dealer wins")
