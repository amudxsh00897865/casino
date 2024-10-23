import random

# Slot Machine
def spin_slot_machine():
    symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '⭐']
    return random.choices(symbols, k=3)

def check_win(spin_result):
    return len(set(spin_result)) == 1

# Blackjack
def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)  # Convert Ace from 11 to 1
    return sum(hand)

def blackjack():
    print("\nWelcome to Blackjack!")
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if player_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True

    while calculate_score(computer_hand) < 17:
        computer_hand.append(deal_card())

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {calculate_score(computer_hand)}")

    if player_score > 21:
        print("You went over. You lose!")
    elif calculate_score(computer_hand) > 21 or player_score > calculate_score(computer_hand):
        print("You win!")
    elif player_score == calculate_score(computer_hand):
        print("It's a draw!")
    else:
        print("You lose!")

# Roulette
def roulette():
    print("\nWelcome to Roulette!")
    numbers = list(range(37))  # 0-36
    while True:
        bet_number = input("Place your bet (0-36) or type 'exit' to quit: ")
        if bet_number.lower() == 'exit':
            break
        if not bet_number.isdigit() or int(bet_number) not in numbers:
            print("Invalid bet! Please choose a number between 0 and 36.")
            continue

        winning_number = random.choice(numbers)
        print(f"The winning number is: {winning_number}")

        if int(bet_number) == winning_number:
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose!")

# Rummy (simple version)
def rummy():
    print("\nWelcome to Rummy!")
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    player_hand = deck[:10]
    print(f"Your hand: {player_hand}")

    print("Try to form a valid set or sequence.")
    input("Press Enter to draw a card...")
    drawn_card = deck[10]
    print(f"You drew: {drawn_card}")

    player_hand.append(drawn_card)
    print(f"Your new hand: {player_hand}")

    # Here, we can add more rules for winning in Rummy.
    print("In this simple version, let's just display your hand!")

# Tic Tac Toe
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def tic_tac_toe():
    print("\nWelcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[row][col] = current_player

        if winner := check_winner(board):
            print_board(board)
            print(f"Player {winner} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

# Main function
def main():
    print("Welcome to the Casino!")
    balance = 100  # Starting balance

    while balance > 0:
        print(f"\nYour current balance is: ${balance}")
        print("Choose a game to play:")
        print("1. Slot Machine")
        print("2. Blackjack")
        print("3. Roulette")
        print("4. Rummy")
        print("5. Tic Tac Toe")
        print("6. Exit")

        choice = input("Enter the number of the game you want to play: ")

        if choice == '1':
            bet = int(input("Enter your bet amount: "))
            if bet > balance:
                print("You cannot bet more than your balance!")
                continue
            spin_result = spin_slot_machine()
            print("Result:", " | ".join(spin_result))
            if check_win(spin_result):
                print("Congratulations, you win!")
                balance += bet
            else:
                print("Sorry, you lose.")
                balance -= bet

        elif choice == '2':
            blackjack()

        elif choice == '3':
            roulette()

        elif choice == '4':
            rummy()

        elif choice == '5':
            tic_tac_toe()

        elif choice == '6':
            print("Thank you for playing! Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid game.")

        if balance == 0:
            print("You're out of money! Game over.")
            break

if __name__ == "__main__":
    main()
