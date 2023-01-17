"""
This is a game of black Jack. Get as close to 21 as you can without going over
and beat the dealer doing it.
"""
import random
import sys
print('Welcome to Blackjack!')
print (f'{"":-^50}')

start = input('Would you like to play blackjack? y/n:')
if start == ('y'):
    print("let's play")
if start == ('n'):
    print('No worries. Have a great day!')
    sys.exit()

player_card = random.randint(1,10)
player_total1 = player_card + player_card
dealer_card1 = random.randint(1,10)
print(f'you draw a {player_card} and a {player_card}. Your total is {player_total1}')
print(f'Dealer draws a {dealer_card1} and a hidden card')
#Players turn
counter = player_total1

while True:
    flip_card = random.randint(1,10)
    if counter == 21:
        print("you can't hit again on 21")
        break
    if counter >=22:
        print('You busted!')
        sys.exit()
    player_drawing = input('Would you like to hit or stand? h/s:')

    if player_drawing == 's':
        break

    if player_drawing == 'h':
        counter += flip_card
        print(f'you drew a {flip_card} you total is {counter}')
        continue

deal_second_card = random.randint(1,10)
print(f'The dealer flipped a {deal_second_card}')

counter_dealer = dealer_card1
#dealer flips
while True:
    dealer_flip = random.randint(1,10)
    dealers_hand = dealer_card1 + deal_second_card
    if counter_dealer > 17:
        break
    if dealers_hand < 17:
        counter_dealer += dealer_flip
        print(f'The dealer drew a {dealer_flip} their total is {counter_dealer}')
    if counter_dealer >=22:
        print('Dealer busted, you win')
        sys.exit()
        continue

if counter_dealer > counter:
    print('Dealer wins!')
    print('Thanks for playing')
if counter_dealer < counter:
    print('Congratulations, You win!')
if counter_dealer == counter:
    print('It is a draw')
