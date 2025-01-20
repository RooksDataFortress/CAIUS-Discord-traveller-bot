import random

class Beetle:
    def __init__(self, color, odds):
        self.color = color
        self.name = self._generate_name()
        self.odds = odds
        self.position = 0

    def _generate_name(self):
        prefixes = ["Spice", "Swift", "Mighty", "Thunder", "Lightning", "Speedy", "Buzzing", 
                   "Turbo", "Zoom", "Dash", "Flash", "Turbo", "Nitro", "Blitz", "Killer", "Lord", "Lady", "Master", "Solid"]
        suffixes = ["Crusher", "Runner", "Zapper", "Bolt", "Wing", "Chungus", "Mandible", 
                   "Pincer", "Spike", "Shell", "Legs", "Racer", "Warrior", "Bingus", "Dingus", "Shenanigan", "Doggo", "Booty", "Laya"]
        return f"{random.choice(prefixes)} {random.choice(suffixes)}"

    def move(self):
        self.position += random.randint(1, 6)

class BeetleRace:
    def __init__(self):
        self.beetles = [
            Beetle("🔴", 2.5),  
            Beetle("💚", 3.0),   
            Beetle("🔵", 3.5),    
            Beetle("💛", 4.0),  
            Beetle("🟣", 4.5)   
        ]
        self.race_length = 60
        
    def run_race(self):
        winner = None
        race_progress = []
        
        while not winner:
            for beetle in self.beetles:
                beetle.move()
                if beetle.position >= self.race_length:
                    winner = beetle
                    break
        
        # Record final positions with names
        final_positions = sorted(self.beetles, key=lambda x: x.position, reverse=True)
        race_progress = [f"{b.color} {b.name}: {'▸' * (b.position // 5)}" for b in final_positions]
        
        return winner, race_progress

    def get_race_display(self, race_log):
        return "🏁 FINAL RESULTS! 🏁\n" + "\n".join(race_log)

    def get_odds_display(self):
        return "\n".join([f"{b.color} {b.name}: {b.odds}:1" for b in self.beetles])

    def calculate_winnings(self, bet_amount, chosen_color, winner):
        chosen_emoji = {
            "red": "🔴", 
            "green": "💚", 
            "blue": "🔵", 
            "yellow": "💛", 
            "purple": "🟣"
        }[chosen_color]
        
        if chosen_emoji == winner.color:
            return int(bet_amount * winner.odds)
        return 0