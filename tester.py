from random import shuffle

#define the card set
ranks = [_ for _ in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']

def get_deck():
    return [[rank, suit] for rank in ranks for suit in suits]

deck = get_deck()
shuffle(deck)

#Set to determine if a the player is still in play
player_in = True

#deals to all
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

#Returns value of first(single) card
def card_value(card):
    rank = card[0]
    if rank in ranks[0:-4]:
        return int(rank)
    elif ranks is 'ACE':
        return 11
    else:
        return 10
#Returns value of delt card set
def hand_value(hand):
    tmp_value = sum(card_value(_) for _ in hand)#Counts entire deck
    num_aces = len([_ for _ in hand if _[0] is 'ACE'])#Counts number of aces in hand.
#Aces can count for 1 or 11. If possible to bring value of hand under 21 by substituting 11 for 1
while num_aces > 0:

        if tmp_value > 21 and 'ACE' in ranks:
            tmp_value -= 10
            num_aces -= 1
        else:
            break
#