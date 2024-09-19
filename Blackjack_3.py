# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

print('-----------\nYOUR TURN\n-----------')

def fcard_name(card_rank):
    if card_rank == 1:
    # A 1 stands for an ace.
        card1_name = "Ace"
    elif card_rank == 11:
    # An 11 stands for a jack.
        card1_name = "Jack"
    elif card_rank == 12:
    # A 12 stands for a queen.
        card1_name = "Queen"
    elif card_rank == 13:
    # A 13 stands for a king.
        card1_name = "King"
    else:
    # All other cards are named by their number, or rank.
        card1_name = str(card_rank)

    if card_rank < 1 or card_rank > 13:
        return 'BAD CARD'
    elif card_rank == 1 or card_rank == 8:
        return 'Drew an ' + card1_name
    else:
        return 'Drew a ' + card1_name

def fcard_value(card_rank):
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
        return 10
    elif card_rank == 1:
    # Aces are worth 11.
        return 11
    else:
    # All other cards are worth the same as their rank.
        return card_rank

def fhand_value(hand_value):
    card = randint(1,13)
    card_name = fcard_name(card) 
    card_value = fcard_value(card)
    print(card_name)
    hand_value += card_value
    return hand_value

def final_hand_test(hand_value):
    print(f'Final hand: {hand_value}.')        
    if hand_value == 21:
        print('BLACKJACK!')
    elif hand_value > 21 and hand_value <= 31:
        print('BUST.')
    elif hand_value > 31 or hand_value < 4:
        print('BAD HAND VALUE!')

i=1
p_hand_value = 0
while i <=2:
    p_hand_value= fhand_value(p_hand_value)
    i += 1

# The user has the option to keep drawing if their hand is below 21.
while p_hand_value < 21:
    ans=input(f'You have {p_hand_value}. Hit (y/n)? ')
    if ans == 'y':
        p_hand_value = fhand_value(p_hand_value)
    elif ans == 'n':
        break
    else:
        print("Sorry I didn't get that.")
final_hand_test(p_hand_value)

#Dealer's Turn
print('-----------\nDEALER TURN\n-----------')

d_hand_value = 0
num_cards = 1
while d_hand_value < 17:
    d_hand_value = fhand_value(d_hand_value)
    if num_cards > 1 and d_hand_value < 17:
        print(f'Dealer has {d_hand_value}.')
    num_cards += 1
final_hand_test(d_hand_value) 


#Game Result
print('-----------\nGAME RESULT\n-----------')

if p_hand_value > 21 or p_hand_value < d_hand_value :
    print('Dealer wins!')
elif p_hand_value < 21 and p_hand_value > d_hand_value:
    print('You win!')
else:
    print('Push.')

#End_of_Program



