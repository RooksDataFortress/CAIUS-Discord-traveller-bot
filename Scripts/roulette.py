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
        if bet_type == 'number' and bet_value == result_number:
            return bet_amount * 35
        elif bet_type == 'color' and bet_value == result_color:
            return bet_amount * 2
        elif bet_type == 'odd_even' and ((bet_value == 'odd' and result_number % 2 == 1) or (bet_value == 'even' and result_number % 2 == 0)):
            return bet_amount * 2
        else:
            return 0