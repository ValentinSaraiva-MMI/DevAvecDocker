# TP Docker : Orchestration & Résilience

Ce projet transforme un POC instable en une architecture microservices robuste, sécurisée et scalable pour un Dashboard Étudiant.

## 🚀 Démarrage Rapide

Pré-requis : Docker et Docker Compose installés.

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/ValentinSaraiva-MMI/DevAvecDocker
   cd DevAvecDocker
2. Lancer la stack :
   ```bash
   docker-compose up -d --build
3. Accéder au Dashboard : 👉 http://localhost:8080

## 🛠️ Architecture Technique
- Frontend : Nginx (Port 8080) servant une SPA statique.

- Backend : API Python FastAPI (Port 8000, non exposé publiquement).

- Database : PostgreSQL 15 (Réseau interne).

- Cache : Redis (Réseau interne) pour le comptage de vues temps réel.

- Admin : Adminer disponible sur le port 8081.

## 🛡️ Sécurité & Résilience (Points Forts)
- Non-Root : L'API tourne avec un utilisateur dédié appuser (voir Dockerfile).

- Isolation : DB et Redis ne sont pas exposés sur l'hôte.

- Graceful Degradation : Si Redis tombe, l'API continue de fonctionner (affichage "Vues: N/A").

- Lazy Loading : La connexion DB se fait à la requête pour éviter les crashs au démarrage .

- Persistance : Les données (Postgres) et le cache (Redis) sont persistants via des volumes Docker.

 ### Valentin Saraiva Ynov M2
