import random
import platform

class slotmachine:
    def __init__(self):            
        # Tuple of (symbol, weight)
        self.symbol_weights = [
            ('🍎', 40),
            ('🍊', 40),
            ('🍋', 40),
            ('🍇', 40),
            ('🍒', 40),
            ('7️⃣', 20),  # Rare symbol with low weight
            ('💎', 1)   # Super rare diamond
        ]
        self.symbols = [s[0] for s in self.symbol_weights]
        self.weights = [s[1] for s in self.symbol_weights]
        self.grid = [['' for _ in range(3)] for _ in range(3)]

    def single_spin(self, bet_amount):
        # Generate new grid using weighted choice
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = random.choices(
                    self.symbols, 
                    weights=self.weights,
                    k=1
                )[0]
        
        winnings = self._calculate_winnings(bet_amount)
        return self.grid, winnings

    def _calculate_winnings(self, bet):
        winnings = 0
        
        # Count diamonds for bonus
        diamond_count = sum(row.count('💎') for row in self.grid)
        winnings += diamond_count * (bet * 5)
        
        # Check rows
        for row in self.grid:
            if len(set(row)) == 1:
                if row[0] == '7️⃣':
                    winnings += bet * 10
                else:
                    winnings += bet * 3

        # Check columns
        for j in range(3):
            column = [self.grid[i][j] for i in range(3)]
            if len(set(column)) == 1:
                if column[0] == '7️⃣':
                    winnings += bet * 10
                else:
                    winnings += bet * 3

        # Check diagonals
        diagonal1 = [self.grid[i][i] for i in range(3)]
        diagonal2 = [self.grid[i][2-i] for i in range(3)]
        
        for diagonal in [diagonal1, diagonal2]:
            if len(set(diagonal)) == 1:
                if diagonal[0] == '7️⃣':
                    winnings += bet * 15
                else:
                    winnings += bet * 5

        return winnings