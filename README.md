# Football Analyzer – Analyse des Statistiques de Football en Temps Réel

Ce projet utilise des microservices conteneurisés avec Docker pour collecter, analyser et afficher des statistiques de football en temps réel. Il s'agit d'un projet éducatif conçu pour comprendre l'architecture de microservices et la manipulation de données simulées ou réelles.

## 🚀 Objectif

L'objectif principal est de :
- Collecter des données de matches de football (réelles ou simulées).
- Analyser ces données pour produire des statistiques détaillées (buts, passes, fautes, etc.).
- Les afficher dans une interface web simple et accessible.

## 🛠️ Installation et Utilisation

### **Prérequis**
- **Docker** et **Docker Compose** doivent être installés sur votre machine.
- Un éditeur de code comme Visual Studio Code (optionnel).

### **Étapes**
1. Clonez le dépôt Git du projet :
   ```bash
   git clone <url-du-depot>
   cd football-analyzer

2. Construisez et lancez les services avec Docker Compose :
    docker-compose up --build

3. Accédez à l'application web :
    Ouvrez un navigateur et rendez vous sur http://localhost:5000/stats
    