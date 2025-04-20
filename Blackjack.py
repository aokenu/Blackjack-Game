from random import choices
import art

def play_game():
    print(art.logo)

    # Deck of cards (Ace is 11)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_card_outcome = []
    dealer_card_outcome = []


    # Function for dealing cards
    def draw_cards(k=1):
        return choices(cards, k=k)

    # Initial draw
    player_card_outcome.extend(draw_cards(k=2))
    dealer_card_outcome.extend(draw_cards(k=2))

    # Function to calculate score with Ace adjustment
    def calculate_score(hand):
        score = sum(hand)
        if 11 in hand and score > 21:
            hand[hand.index(11)] = 1  # Change one Ace from 11 to 1
            score = sum(hand)
        return score

    # Function to display cards
    def display_cards():
        print(f"Your cards: {player_card_outcome}, current score: {calculate_score(player_card_outcome)}")
        print(f"Computer's first card: {dealer_card_outcome[0]}")

    display_cards()

    # Function to check for blackjack or bust
    def check_game_status():
        player_score = calculate_score(player_card_outcome)
        dealer_score = calculate_score(dealer_card_outcome)

        if player_score == 21 and dealer_score == 21:
            print(f"Draw! Both have Blackjack.")
            return True
        elif player_score == 21:
            print(f"You Win! Blackjack with {player_card_outcome}")
            return True
        elif dealer_score == 21:
            print(f"Computer Wins! Blackjack with {dealer_card_outcome}")
            return True
        elif player_score > 21:
            print("You went over. You lose.")
            return True
        return False

    # Check initial status
    if not check_game_status():
        while True:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card.lower() == 'y':
                player_card_outcome.extend(draw_cards())
                display_cards()
                if check_game_status():
                    break
            else:
                # Let dealer draw until 17 or more
                while calculate_score(dealer_card_outcome) < 17:
                    dealer_card_outcome.extend(draw_cards())
                player_score = calculate_score(player_card_outcome)
                dealer_score = calculate_score(dealer_card_outcome)
                print(f"\nYour final hand: {player_card_outcome}, final score: {player_score}")
                print(f"Computer's final hand: {dealer_card_outcome}, final score: {dealer_score}")
                if dealer_score > 21 or player_score > dealer_score:
                    print("You win!")
                elif player_score == dealer_score:
                    print("It's a draw.")
                else:
                    print("You lose.")
                break

while input("Do you want to play a game of Blackjack? Type 'y' or 'n :") == 'y':
    play_game()