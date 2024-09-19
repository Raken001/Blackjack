# Blackjack Game

This Python script simulates a simplified version of the Blackjack card game. The game involves a player and a dealer, each taking turns drawing cards to build a hand value as close as possible to 21 without exceeding it. The winner is determined based on the hand values.

## How the Game Works

1. **Player's Turn**:
   - The player is initially dealt two cards, and their total hand value is displayed.
   - The player can choose to "Hit" (draw another card) as long as their hand value is less than 21, or they can choose to "Stand" (end their turn).

2. **Dealer's Turn**:
   - The dealer must continue drawing cards ("Hit") until their hand value is at least 17. The dealer's hand is displayed after each draw.

3. **Game Outcome**:
   - After both the player and the dealer have taken their turns, the hand values are compared.
   - If the player's hand exceeds 21, they bust, and the dealer wins.
   - If the player's hand is closer to 21 than the dealer's, the player wins.
   - If both hands are equal, the game results in a push (tie).

## Code Breakdown

- **Card Naming and Values**:
  - `fcard_name(card_rank)`: Determines the name of a card (e.g., Ace, King, Queen) based on its rank.
  - `fcard_value(card_rank)`: Returns the point value of a card based on its rank. Face cards (Jack, Queen, King) are worth 10, aces are worth 11, and other cards are worth their rank.

- **Player and Dealer Actions**:
  - `fhand_value(hand_value)`: Draws a random card, updates the hand value, and prints the card's name.
  - `final_hand_test(hand_value)`: Checks if the hand is a Blackjack, bust, or invalid and prints the appropriate message.

- **Game Flow**:
  - The player and dealer take turns drawing cards. The player decides whether to keep drawing based on their hand value, while the dealer must draw until reaching a minimum hand value of 17.

- **Game Results**:
  - After both the player and dealer have finished drawing, the hand values are compared to determine the winner.


