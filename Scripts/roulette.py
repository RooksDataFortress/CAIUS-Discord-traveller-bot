import random

class roulette:
    def __init__(self):
        self.numbers = list(range(37))  # 0 to 36
        self.colors = ['🟢'] + ['🔴' if i % 2 == 1 else '⚫' for i in range(1, 37)]

    def spin(self, bet_amount, bet_type, bet_value):
        result_number = random.choice(self.numbers)
        result_color = self.colors[result_number]
        winnings = self._calculate_winnings(bet_amount, bet_type, bet_value, result_number, result_color)
        return result_number, result_color, winnings

    def _calculate_winnings(self, bet_amount, bet_type, bet_value, result_number, result_color):
        if bet_type == 'number':
            if isinstance(bet_value, list):
                # Calculate bet per number only at point of win
                bet_per_number = bet_amount // len(bet_value)
                if result_number in bet_value:
                    winnings = bet_per_number * 35  # Only divide bet here
                    print(f"WIN! {bet_per_number}Cr * 35 = {winnings}Cr")
                    return winnings
                return 0
        elif bet_type == 'color' and bet_value == result_color:
            return bet_amount * 2
        elif bet_type == 'odd_even':
            # Zero is neither odd nor even in roulette
            if result_number == 0:
                return 0
            elif (bet_value == 'odd' and result_number % 2 == 1) or \
                (bet_value == 'even' and result_number % 2 == 0):
                return bet_amount * 2
        return 0