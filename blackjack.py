import string
import random

#replaces the letters with symbols
def symbol_repl(card_str):
    return card_str.replace('S', '\u2660').replace('H', '\u2665').replace('C', '\u2663').replace('D', '\u2666')

#Creates the deck 
def create_deck():
    deck = []
    suits = ['C', 'D', 'H', 'S']
    card_val = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for suit in suits:
        for card in card_val:
            deck += [card + suit]
    return deck

#This will evaluate the score for the dealer and the player
def eval(hand):
    score = 0
    card_val = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
                '2': 2}
    for card in hand:
        score += card_val[card[0]]
    for card in hand:
        if 'A' in card and score > 21:
            score -= 10
    return score

#return the first value in the list
def dealcard():
    return deck.pop(0)

#this will show the players score
def showplayerhand(player_hand):
    for card in player_hand:
        print(symbol_repl(card), end=" ")
    print()

    print("Player score:", eval(player_hand))

#this will show the dealers score
def showdealerhand(dealer_hand):
  print("Dealer score: ", eval(dealer_hand))

#this shows the dealers cards in the end    
def showthedealersfinaldeck():
    print("Dealers hand:",symbol_repl(card), end = " ")

while (True):
    deck = create_deck()

    random.shuffle(deck)
    print("Shuffled deck: ", deck)
    print('first item: ' + deck[0])

    dealer_hand = []
    player1_hand = []

    cardnum = 0

    #These will add random cards to the players and the dealers deck
    player1_hand += [symbol_repl(deck[cardnum])]
    cardnum += 1
    dealer_hand += [symbol_repl(deck[cardnum])]
    cardnum += 1
    player1_hand += [symbol_repl(deck[cardnum])]
    cardnum += 1
    dealer_hand += [symbol_repl(deck[cardnum])]
    cardnum += 1

    print('your cards:', player1_hand[0], player1_hand[1])
    print('dealer cards: ??', dealer_hand[1])
    print("Player score:", eval(player1_hand))

    #Hit or STAY loop
    while eval(player1_hand) <= 21:
        response = input("Do you want to hit or stay(h/s) ?")
        if response == "h":
            # DO SOMETHING
            player1_hand.append(dealcard())
            showplayerhand(player1_hand)
        # showplayerhand(dealer_hand)
        else:
            showplayerhand(player1_hand)
            # showplayerhand(dealer_hand)
            break
        
    # DEALER PLAYING

    while eval(dealer_hand) < 16:
        dealer_hand.append(dealcard())
    print("Dealers hand was: ",symbol_repl(dealer_hand[0]),symbol_repl(dealer_hand[1]))
    showdealerhand(dealer_hand)
    #Finally who wins
    if eval(player1_hand) <= 21 and eval(dealer_hand) <= 21:
        if eval(player1_hand) > eval(dealer_hand):
            print("Player wins!!!!")
        if eval(player1_hand) < eval(dealer_hand):
            print("Dealer wins!!!!")
        if eval(player1_hand) == eval(dealer_hand):
            print("PUSH!!!!!!")
    
    if eval(player1_hand) > 21 or eval(dealer_hand) > 21:
        if eval(player1_hand) > 21:
            print("BUST!!! \nPlayer loses!!!! \nDealer wins!!!!")
        if eval(dealer_hand) > 21:
            print("BUST!!! \nDealer loses!!! \nPlayer Wins!!!")

    if eval(player1_hand) > 21 and eval(dealer_hand) > 21:
        print("IT'S A PUSH !!!!!!")

    response = input("Do you want to play again?(y/n): ")
    if response == 'y':
        continue
    if response == 'n':
        print("Thanks for playing. \nBYE!")
        break
