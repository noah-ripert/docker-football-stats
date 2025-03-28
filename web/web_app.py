from flask import Flask, jsonify

# Simuler des statistiques (à remplacer par une vraie connexion plus tard)
mock_stats = {
    "Equipe A": 3,
    "Equipe B": 1
}

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Statistiques des matches en temps réel"})

@app.route("/stats")
def stats():
    return jsonify(mock_stats)  # Remplacer par des données dynamiques plus tard

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)