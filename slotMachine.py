import random  # Import the random module for random symbol selection

# Constants for the slot machine
MAX_LINES = 3           # Maximum number of lines to bet on
MAX_BET = 100           # Maximum bet per line
MIN_BET = 1             # Minimum bet per line

ROW = 3                 # Number of rows in the slot machine
COL = 3                 # Number of columns in the slot machine

# Dictionary storing the count of each symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dictionary storing the value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    """
    Checks for winning lines and calculates total winnings.
    columns: List of columns with symbols.
    lines: Number of lines to check.
    bet: Bet amount per line.
    values: Dictionary of symbol values.
    Returns total winnings and list of winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  # Take the symbol from the first column for this line
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  # If any symbol in the line doesn't match, break
        else:
            winnings += values[symbol]*bet  # Add winnings if all symbols match
            winning_lines.append(lines + 1)  # Record the winning line (bug: should be line+1)

    return winnings, winning_lines

def get_slot_machine_Spin(rows, cols, symbols):
    """
    Generates a random spin for the slot machine.
    rows: Number of rows.
    cols: Number of columns.
    symbols: Dictionary of symbol counts.
    Returns a list of columns, each containing symbols.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Copy all symbols for this column

        for _ in range(rows):
            value = random.choice(current_symbols)  # Randomly select a symbol
            current_symbols.remove(value)           # Remove selected symbol to avoid repeats
            column.append(value)
        columns.append(column)  # Add the column to the slot machine

    return columns

def print_slot_machine(columns):
    """
    Prints the slot machine columns in a row-wise format.
    columns: List of columns with symbols.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    """
    Prompts the user to deposit money and returns the amount.
    """
    while True:
        amount = input("How much would you like to deposit? R")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be more than 0.")
        else:
            print("Please enter a number.") 
    return amount

def get_number_of_lines():
    """
    Prompts the user to enter the number of lines to bet on.
    Returns the number of lines.
    """
    while True:
        lines = input(
            "Enter number of lines to place bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number.") 
    return lines

def get_bet():
    """
    Prompts the user to enter the bet amount per line.
    Returns the bet amount.
    """
    while True:
        amount = input("How much would you like to bet on each line? R")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"Amount must be between R{MIN_BET} - R{MAX_BET}.")
        else:
            print("Please enter a number.") 
    return amount

def spin(balance):
    """
    Handles a single spin of the slot machine.
    balance: Current user balance.
    Returns the net winnings (winnings - total bet).
    """
    lines = get_number_of_lines()
    while True:  
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, because your current balance is R{balance}")
        else:
            break
    print(
        f"You are betting R{bet} on {lines} line. Total bet is equal to: R{total_bet}")
    
    slots = get_slot_machine_Spin(ROW, COL, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Congratulations, you won R{winnings}.")
    print(f"You won on:", *winning_lines)
    return winnings - total_bet

def main():
    """
    Main game loop. Handles user balance and game flow.
    """
    balance = deposit()
    while True:
        print(f"Current balance is R{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with R{balance}")
    
main()  # Start the game