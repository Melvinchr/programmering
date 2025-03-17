##  Black jack med twist, Jag ska skapa ett black jack där man kan köpa till bonusar och andra saker till sitt spel med pengar man vunnit.
##  1. skapa ett fungerande black jack
##  2. Skapa fungerande effekt kort som går att använda och extra kort
##  3. skapa en "shop" som man kan köpa dessa effekt kort ifrån
##  Kortlek med fyra 1:or, fyra 2:or, ..., fyra 11
##  Blanda kortleken
##  Dra ett kort ur leken
##  Ge spelaren 2 kort
##  Ge datorn 1 kort
##  Spelaren kan välja hit, stand eller special kort
##  Datorn väljer hit eller stand
##  Vem vinner. Enkel summa. Korten värda 1 - 11.
##  spela om pengar
##  Kunna spela en gång till.
##  Knekt, dam kung värda 10.
##  Ess är värt 1 eller 11 enlig regelboken
##  Implementera fler regler

## Text fil som sparar pengar och tilläggskort, Ace blir 1 om 11 tar en över 21


import random

def print_hands():
    print("Cards Dealer Has:", dealer_card) 
    print("Score Of The Dealer:", dealer_score) 
    print("Cards Player Has:", player_card) 
    print("Score Of The Player:", player_score) 

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] 
deck = [(card, category) for category in card_categories for card in cards_list] 

def calculate_score(hand):
    score = 0
    aces = 0
    
    for card in hand:
        if card[0] in ['Jack', 'Queen', 'King']: 
            score += 10
        elif card[0] == 'Ace': 
            score += 11
            aces += 1
        else: 
            score += int(card[0])
    
    while score > 21 and aces:
        score -= 10
        aces -= 1
    
    return score

def shop(player_money):
    print("Shop Menu:")
    print("1. Double Down ($10)")
    
    choice = input("Choose an item to buy (or 'exit' to leave): ")
    
    if choice == "1":
        if player_money >= 10:
            player_money -= 10
            print("You bought Double Down!")
        else:
            print("Not enough money.")
    elif choice.lower() == "exit":
        print("Leaving shop.")
    else:
        print("Invalid choice.")
        
    return player_money

file = open('Projekt/black_hack_bank.txt', 'r')
line = file.readline()
player_money = int(line)
print(f"You have ${player_money} initially.")
file.close()

def Double_Down(player_money, bet):
    print("You used Double Down")

while True:
    player_money = shop(player_money)
    print(f"You have ${player_money} left after shopping.")

    random.shuffle(deck) 
    player_card = [deck.pop(), deck.pop()] 
    dealer_card = [deck.pop(), deck.pop()] 

    is_playing = True
    while is_playing: 
        player_score = calculate_score(player_card) 
        dealer_score = calculate_score(dealer_card) 
    
        if player_score > 21:
            print("Cards Player Has:", player_card) 
            print("Score of The Player:", player_score) 
            print("\n")
            print_hands()
            print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if "y" in play_again:
                deck = [(card, category) for category in card_categories for card in cards_list]
                random.shuffle(deck)
                player_card = [deck.pop(), deck.pop()]
                dealer_card = [deck.pop(), deck.pop()]
            else:
                is_playing = False
            continue

        print("Cards Player Has:", player_card) 
        print("Score of The Player:", player_score) 
        print("\n") 
    
        choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower() 
        if choice == "play": 
            new_card = deck.pop() 
            player_card.append(new_card) 
        elif choice == "stop": 
            is_playing = False
        else: 
            print("Invalid choice. Please try again.") 
            continue

    if not is_playing:
        while dealer_score < 17: 
            new_card = deck.pop() 
            dealer_card.append(new_card) 
            dealer_score = calculate_score(dealer_card) 

        print("Cards Dealer Has:", dealer_card)
        print("Score Of The Dealer:", dealer_score) 
        print("\n") 

        if dealer_score > 21: 
            print_hands()
            print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)")
            print("\n")
            player_money += 10
        elif player_score > dealer_score: 
            print_hands()
            print("Player wins (Player Has a Higher Score than Dealer)")
            print("\n")
            player_money += 10
        elif dealer_score > player_score: 
            print_hands()
            print("Dealer wins (Dealer Has a Higher Score than Player)")
            print("\n")
        else: 
            print_hands()
            print("It's a tie.")
            print("\n")
        # sparar pengarna på fil
        file = open('Projekt/black_hack_bank.txt', 'w')
        file.write(str(player_money))
        print(f"You have ${player_money} initially.")
        file.close()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        print("\n")
        if "y" in play_again:
            deck = [(card, category) for category in card_categories for card in cards_list]
            random.shuffle(deck)
            is_playing = True
        else:
            break