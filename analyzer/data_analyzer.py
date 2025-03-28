def analyze_data(data):
    # Exemple : compter les buts par équipe
    stats = {}
    for entry in data:
        team = entry["team"]
        action = entry["action"]
        if action == "But":
            stats[team] = stats.get(team, 0) + 1
    return stats