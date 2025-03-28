import time
import random

def generate_match_data():
    teams = ["Equipe A", "Equipe B"]
    return {
        "team": random.choice(teams),
        "action": random.choice(["But", "Passe", "Faute"]),
        "timestamp": time.time()
    }

while True:
    match_data = generate_match_data()
    print(match_data)  # Cela peut être envoyé à Redis ou à l'analyseur
    time.sleep(2)