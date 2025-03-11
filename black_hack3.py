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

player_money = 0
print(f"You have ${player_money} initially.")

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
        if play_again == "yes":
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
    	elif player_score > dealer_score: 
    	    print_hands()
    	    print("Player wins (Player Has a Higher Score than Dealer)")
    	elif dealer_score > player_score: 
    	    print_hands()
    	    print("Dealer wins (Dealer Has a Higher Score than Player)")
    	else: 
    	    print_hands()
    	    print("It's a tie.")

    	play_again = input("Do you want to play again? (yes/no): ").lower()
    	if play_again == "yes":
    	    deck = [(card, category) for category in card_categories for card in cards_list]
    	    random.shuffle(deck)
    	    is_playing = True
    	else:
    	    is_playing = False