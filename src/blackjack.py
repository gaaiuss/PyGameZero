'''Rules:
The dealer and player are dealt two cards each. The dealer's first card is
hidden from the player.

The player can hit (i.e. take another card) or stand (i.e. stop taking cards).

If the total value of the player's hand goes over 21, then they have gone bust.

Face cards (king, queen and jack) have a value of 10, and aces have a value of
11 unless this would make the total value of the hand go above 21, in which case
they have a value of 1.

After the player has stood or gone bust, the dealer takes cards until the total
of their hand is 17 or over.

The round is then over, and the hand with the highest total (if the total is 21
or under) wins the round.

Controls:

Left click	Click on hit or stand button
'''
import random

import pygame


def update():
    pass


deck = []
for suit in ('club', 'diamond', 'heart', 'spade'):
    for rank in range(1, 14):
        deck.append({'suit': suit, 'rank': rank})


def take_card(hand):
    hand.append(deck.pop(random.randrange(len(deck))))


def reset():
    global deck
    global player_hand
    global dealer_hand
    global round_over

    deck = []
    for suit in ('club', 'diamond', 'heart', 'spade'):
        for rank in range(1, 14):
            deck.append({'suit': suit, 'rank': rank})

    player_hand = []
    take_card(player_hand)
    take_card(player_hand)

    dealer_hand = []
    take_card(dealer_hand)
    take_card(dealer_hand)

    round_over = False


reset()


def get_total(hand):
    total = 0
    has_ace = False

    for card in hand:
        if card['rank'] > 10:
            total += 10
        else:
            total += card['rank']

        if card['rank'] == 1:
            has_ace = True

    if has_ace and total <= 11:
        total += 10

    return total


def on_key_down(key):
    global round_over

    if not round_over:
        if key == keys.H:
            take_card(player_hand)
            if get_total(player_hand) >= 21:
                round_over = True
        elif key == keys.S:
            round_over = True

        if round_over:
            while get_total(dealer_hand) < 17:
                take_card(dealer_hand)
    else:
        reset()


def draw():
    screen.fill((0, 0, 0))
    card_spacing = 60
    margin_x = 10

    for card_index, card in enumerate(dealer_hand):
        image = card['suit'] + '_' + str(card['rank'])
        if not round_over and card_index == 0:
            image = 'card_face_down'
        screen.blit(image, (card_index * card_spacing + margin_x, 30))

    for card_index, card in enumerate(player_hand):
        screen.blit(card['suit'] + '_' + str(card['rank']),
                    (card_index * card_spacing + margin_x, 140))

    if round_over:
        screen.draw.text('Total: ' + str(get_total(dealer_hand)),
                         (margin_x, 10), color=(255, 255, 255))

        def has_hand_won(this_hand, other_hand):
            return (
                get_total(this_hand) <= 21
                and (
                    get_total(other_hand) > 21
                    or get_total(this_hand) > get_total(other_hand)
                )
            )

        def draw_winner(message):
            screen.draw.text(message, (margin_x, 268), color=(255, 255, 255))

        if has_hand_won(player_hand, dealer_hand):
            draw_winner('Player wins')
        elif has_hand_won(dealer_hand, player_hand):
            draw_winner('Dealer wins')
        else:
            draw_winner('Draw')
    else:
        screen.draw.text('Total: ?', (margin_x, 10), color=(255, 255, 255))

    screen.draw.text('Total: ' + str(get_total(player_hand)),
                     (margin_x, 120), color=(255, 255, 255))

    def draw_button(text, button_x, button_width, text_offset_x):
        button_y = 230
        button_height = 25

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if (
            mouse_x >= button_x
            and mouse_x < button_x + button_width
            and mouse_y >= button_y
            and mouse_y < button_y + button_height
        ):
            color = (255, 202, 75)
        else:
            color = (255, 127, 57)

        screen.draw.filled_rect(
            Rect(button_x, button_y, button_width, button_height),
            color=color
        )
        screen.draw.text(text, (button_x + text_offset_x, button_y + 6))

    draw_button('Hit!', 10, 53, 13)
    draw_button('Stand', 70, 53, 4)
    # draw_button('Play again', 10, 113, 17)
