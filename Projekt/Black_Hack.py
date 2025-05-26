import random

def make_deck():
    card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
    cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] 
    deck = [(card, category) for category in card_categories for card in cards_list] 
    return deck

def Double_Down(player_money, bet):
    print("You used Double Down")
    player_money -= bet
    return player_money, bet * 2

def Plus_Minus():
    print("You used Plus & Minus")
    while True:
        choice = input("Do you want to add or subtract 5 from your score? (add/subtract): ").lower()
        if choice == "add":
            return 5      
        elif choice == "subtract":
            return -5
        else:
            print("Invalid choice. Please type add or subtract.")   

def print_command_info():
    print("\nCOMMANDS:")
    print("  play        - Take a new card")
    print("  stop        - Stop playing and let the dealer play")
    print("  double      - Use Double Down (if you've bought one), doubles your bet if you haven't taken another card. Can't be used if bet is more then half of your total")
    print("  plus/minus  - Use Plus & Minus (if you've bought one), add or remove 5 from your player score")
    print("  info        - Show this help text")
    print()


def print_hands():
    print("Cards Dealer Has:", dealer_card) 
    print("Score Of The Dealer:", dealer_score) 
    print("Cards Player Has:", player_card) 
    print("Score Of The Player:", player_score) 

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
    print("2. Plus & Minus ($5)")
    choice = input("Choose an item to buy (or 'exit' to leave): ")    
    if choice == "1":
        if player_money >= 10:
            player_money -= 10
            effect_cards.append("Double_Down") 
            print("You bought Double Down!")
        else:
            print("Not enough money.")
    elif choice == "2":
        if player_money >= 5:
            player_money -= 5
            effect_cards.append("Plus_Minus") 
            print("You bought Plus & Minus!")
        else:
            print("Not enough money.")
    elif choice.lower() == "exit":
        print("Leaving shop.")
    else:
        print("Invalid choice.")        
    return player_money

deck = make_deck()
effect_cards = []

# Läs in pengar från fil
file = open('Projekt/black_hack_bank.txt', 'r')
line = file.readline()
player_money = int(line)
print(f"You have ${player_money} initially.")
file.close()

# Spelar blackjack
while True:
    player_money = shop(player_money)
    print(f"You have ${player_money} left after shopping.")

    # ny runda - välj insats 
    while True:
        try:
            bet = int(input(f"How much do you want to bet? (You have ${player_money}): "))
            if bet <= 0 or bet > player_money:
                print("Invalid bet amount. Please try again.")
            else:
                player_money -= bet
                break
        except ValueError:
            print("Please enter a valid number.")

    # blanda och dela ut kort
    random.shuffle(deck) 
    player_card = [deck.pop(), deck.pop()] 
    dealer_card = [deck.pop(), deck.pop()] 

    score_modifier = 0 # Modifierare för Plus/Minus-kort
    is_playing = True

    while is_playing: 
        player_score = calculate_score(player_card) + score_modifier # räknar ut värdet på korten
        dealer_score = calculate_score(dealer_card) 

        # om spelarens kort överskrider 21 förlorar man automatiskt
        if player_score > 21:
            print("Cards Player Has:", player_card) 
            print("Score of The Player:", player_score) 
            print("\n")
            print_hands()
            print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
            is_playing = False
        else:
        # Skriver ut korten och värdet på de
            print("Cards Player Has:", player_card) 
            print("Score of The Player:", player_score) 
            print("\n") 
        
        #frågar vad du vill göra
            valid_choice = False
            while (not valid_choice):
                choice = input('What do you want to do? ["play", "stop", "double", "plus/minus", "info"]: ').lower() 
                if choice == "play": 
                    new_card = deck.pop() 
                    player_card.append(new_card) 
                    valid_choice = True
                elif choice == "stop": 
                    is_playing = False
                    valid_choice = True
                elif choice == "double":
                    if len(player_card) == 2 and "Double_Down" in effect_cards:
                        if player_money >= bet:
                            player_money, bet = Double_Down(player_money, bet)
                            effect_cards.remove("Double_Down")
                            is_playing = False
                            valid_choice = True
                        else:
                            print("You don't have enough money to double down!")
                            valid_choice = False
                    else:
                        print("You can only double down on your first two cards and if you have the card.")
                        valid_choice = False
                elif choice == "plus/minus":
                    if "Plus_Minus" in effect_cards:
                        score_modifier += Plus_Minus()
                        effect_cards.remove("Plus_Minus")
                        valid_choice = True
                    else:
                        print("You can only use plus/minus if you bought it.")
                        valid_choice = False
                elif choice == "info":
                    print_command_info()
                    valid_choice = False  # Spelaren får välja igen efter info
                else: 
                    print("Invalid choice. Please try again.") 
                    valid_choice = False

    # kollar player score och dealer score
    if not is_playing:
        if player_score <= 21:
            while dealer_score < 17: 
                new_card = deck.pop() 
                dealer_card.append(new_card) 
                dealer_score = calculate_score(dealer_card) 

            print("Cards Dealer Has:", dealer_card)
            print("Score Of The Dealer:", dealer_score) 
            print("\n") 
        # Skriver ut vem som vann och ger pengar om player vann
            if dealer_score > 21: 
                print_hands()
                print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)")
                print("\n")
                player_money += bet * 2
            elif player_score > dealer_score: 
                print_hands()
                print("Player wins (Player Has a Higher Score than Dealer)")
                print("\n")
                player_money += bet * 2
            elif dealer_score > player_score: 
                print_hands()
                print("Dealer wins (Dealer Has a Higher Score than Player)")
                print("\n")
            else: 
                print_hands()
                print("It's a tie.")
                player_money += bet
                print("\n")
            # sparar pengarna till fil    
            file = open('Projekt/black_hack_bank.txt', 'w')
            file.write(str(player_money))
            print(f"You have ${player_money} initially.")
            file.close()
        # Frågar om du vill spela igen
        play_again = input("Do you want to play again? (yes/no): ").lower()
        print("\n")
        if "y" in play_again:
            deck = make_deck()
            is_playing = True
        else:
            break
    else:
        play_again = False