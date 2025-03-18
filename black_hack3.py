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
    print("2. Insurance ($5)")
    
    choice = input("Choose an item to buy (or 'exit' to leave): ")
    
    if choice == "1":
        if player_money >= 10:
            player_money -= 10
            print("You bought Double Down!")
        else:
            print("Not enough money.")
    elif choice == "2":
        if player_money >= 5:
            player_money -= 5
            print("You bought Insurance!")
        else:
            print("Not enough money.")
    elif choice.lower() == "exit":
        print("Leaving shop.")
    else:
        print("Invalid choice.")
        
    return player_money

def double_down(player_money, bet):
    print("You chose to double down!")
    player_money -= bet  # Take out an additional bet
    return player_money, bet * 2  # Return updated money and doubled bet

player_money = 100
print(f"You have ${player_money} initially.")

while True:
    player_money = shop(player_money)
    print(f"You have ${player_money} left after shopping.")
    
    # Betting
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
            break

        print("Cards Player Has:", player_card) 
        print("Score of The Player:", player_score) 
        print("\n") 
        
        choice = input('What do you want? ["play" to request another card, "stop" to stop, "double" to double down]: ').lower() 
        if choice == "play": 
            new_card = deck.pop() 
            player_card.append(new_card) 
        elif choice == "stop": 
            is_playing = False
        elif choice == "double":
            if len(player_card) == 2:  # Double down is only allowed on the first two cards
                player_money, bet = double_down(player_money, bet)
                new_card = deck.pop()
                player_card.append(new_card)
                is_playing = False  # Player must stand after double down
            else:
                print("You can only double down on your first two cards.")
        else: 
            print("Invalid choice. Please try again.") 
            continue

    # Dealer's turn
    if player_score <= 21:
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
            player_money += bet * 2  # Win double the bet
        elif player_score > dealer_score: 
            print_hands()
            print("Player wins (Player Has a Higher Score than Dealer)")
            player_money += bet * 2  # Win double the bet
        elif dealer_score > player_score: 
            print_hands()
            print("Dealer wins (Dealer Has a Higher Score than Player)")
        else: 
            print_hands()
            print("It's a tie.")
            player_money += bet  # Return the bet on a tie

    print(f"You now have ${player_money}.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print(f"Thanks for playing! You leave with ${player_money}.")
