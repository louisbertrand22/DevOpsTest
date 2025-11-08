from flask import Flask, render_template_string, jsonify
import datetime
import os

app = Flask(__name__)

# Application metadata
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
START_TIME = datetime.datetime.now()

# HTML template for the documentation
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation DevOps</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        nav {
            background: #f8f9fa;
            padding: 20px 40px;
            border-bottom: 2px solid #e9ecef;
        }
        nav a {
            display: inline-block;
            padding: 10px 20px;
            margin: 5px;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 6px;
            border: 2px solid #667eea;
            font-weight: 600;
            transition: all 0.3s;
        }
        nav a:hover {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        .content {
            padding: 40px;
        }
        .section {
            margin-bottom: 40px;
        }
        .section h2 {
            color: #667eea;
            font-size: 2em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }
        .section h3 {
            color: #764ba2;
            font-size: 1.5em;
            margin: 25px 0 15px 0;
        }
        .section p {
            margin-bottom: 15px;
            font-size: 1.1em;
        }
        .section ul {
            margin: 15px 0 15px 30px;
        }
        .section li {
            margin-bottom: 10px;
            font-size: 1.05em;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #e83e8c;
        }
        .code-block {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
        }
        .highlight {
            background: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ffc107;
            margin: 20px 0;
            border-radius: 4px;
        }
        footer {
            background: #2d3748;
            color: white;
            text-align: center;
            padding: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 Hub de Documentation DevOps</h1>
            <p>Votre guide complet des pratiques DevOps modernes</p>
        </header>
        
        <nav>
            <a href="/">Accueil</a>
            <a href="/deployment">Déploiement Azure</a>
            <a href="/contribute">Contribuer</a>
            <a href="#docker">Docker</a>
            <a href="#kubernetes">Kubernetes</a>
            <a href="#ingress">Ingress</a>
            <a href="#cicd">CI/CD</a>
            <a href="#best-practices">Bonnes Pratiques</a>
        </nav>
        
        <div class="content">
            <section id="docker" class="section">
                <h2>🐳 Docker</h2>
                <p>Docker est une plateforme pour développer, expédier et exécuter des applications dans des conteneurs. Les conteneurs empaquètent les logiciels avec toutes leurs dépendances, garantissant la cohérence entre les environnements.</p>
                
                <h3>Concepts Clés</h3>
                <ul>
                    <li><strong>Images&nbsp;:</strong> Modèles en lecture seule contenant le code de l'application et les dépendances</li>
                    <li><strong>Conteneurs&nbsp;:</strong> Instances en cours d'exécution des images Docker</li>
                    <li><strong>Dockerfile&nbsp;:</strong> Script définissant comment construire une image Docker</li>
                    <li><strong>Docker Hub&nbsp;:</strong> Registre cloud pour stocker et partager des images Docker</li>
                </ul>
                
                <h3>Commandes Courantes</h3>
                <div class="code-block">
# Build an image from Dockerfile
docker build -t myapp:latest .

# Run a container
docker run -d -p 8000:8000 myapp:latest

# List running containers
docker ps

# View logs
docker logs container_id

# Stop a container
docker stop container_id
                </div>
                
                <div class="highlight">
                    <strong>💡 Astuce Pro&nbsp;:</strong> Utilisez des builds multi-étapes pour réduire la taille de l'image et améliorer la sécurité en excluant les dépendances de build des images de production.
                </div>
            </section>
            
            <section id="kubernetes" class="section">
                <h2>☸️ Kubernetes</h2>
                <p>Kubernetes (K8s) est une plateforme d'orchestration de conteneurs open-source qui automatise le déploiement, la mise à l'échelle et la gestion des applications conteneurisées.</p>
                
                <h3>Composants Principaux</h3>
                <ul>
                    <li><strong>Pods&nbsp;:</strong> Plus petites unités déployables contenant un ou plusieurs conteneurs</li>
                    <li><strong>Déploiements&nbsp;:</strong> Gèrent l'état souhaité de votre application</li>
                    <li><strong>Services&nbsp;:</strong> Exposent votre application sur un réseau</li>
                    <li><strong>ConfigMaps & Secrets&nbsp;:</strong> Gèrent la configuration et les données sensibles</li>
                    <li><strong>Namespaces&nbsp;:</strong> Clusters virtuels pour l'isolation des ressources</li>
                </ul>
                
                <h3>Commandes kubectl Essentielles</h3>
                <div class="code-block">
# Apply configuration from file
kubectl apply -f deployment.yml

# Get resources
kubectl get pods
kubectl get services
kubectl get deployments

# Describe resource details
kubectl describe pod pod-name

# View logs
kubectl logs pod-name

# Execute command in container
kubectl exec -it pod-name -- /bin/bash

# Scale deployment
kubectl scale deployment/myapp --replicas=3

# Delete resources
kubectl delete -f deployment.yml
                </div>
                
                <h3>Exemple de Déploiement</h3>
                <div class="code-block">
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 8000
                </div>
            </section>
            
            <section id="ingress" class="section">
                <h2>🌐 Kubernetes Ingress</h2>
                <p>Ingress gère l'accès externe aux services dans un cluster Kubernetes, généralement HTTP/HTTPS. Il fournit l'équilibrage de charge, la terminaison SSL et l'hébergement virtuel basé sur le nom.</p>
                
                <h3>Pourquoi Utiliser Ingress ?</h3>
                <ul>
                    <li>Point d'entrée unique pour plusieurs services</li>
                    <li>Terminaison SSL/TLS</li>
                    <li>Routage basé sur le chemin et l'hôte</li>
                    <li>Équilibrage de charge entre les pods</li>
                    <li>Réduction des coûts d'équilibreur de charge cloud</li>
                </ul>
                
                <h3>Contrôleur Ingress</h3>
                <p>Un contrôleur Ingress est nécessaire pour implémenter les règles Ingress. Les options populaires incluent&nbsp;:</p>
                <ul>
                    <li><strong>Contrôleur NGINX Ingress&nbsp;:</strong> Le plus largement utilisé</li>
                    <li><strong>Traefik&nbsp;:</strong> Proxy inverse moderne avec SSL automatique</li>
                    <li><strong>HAProxy&nbsp;:</strong> Équilibreur de charge haute performance</li>
                    <li><strong>AWS ALB&nbsp;:</strong> Intégré avec AWS Application Load Balancer</li>
                </ul>
                
                <h3>Exemple de Configuration Ingress</h3>
                <div class="code-block">
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-service
            port:
              number: 8000
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
                </div>
            </section>
            
            <section id="cicd" class="section">
                <h2>🔄 Pipelines CI/CD</h2>
                <p>L'Intégration Continue et le Déploiement Continu (CI/CD) automatisent le processus de livraison logicielle du commit de code au déploiement en production.</p>
                
                <h3>Flux de Travail CI/CD</h3>
                <ul>
                    <li><strong>Intégration Continue&nbsp;:</strong> Construire et tester automatiquement les modifications de code</li>
                    <li><strong>Livraison Continue&nbsp;:</strong> Préparer automatiquement les versions pour le déploiement</li>
                    <li><strong>Déploiement Continu&nbsp;:</strong> Déployer automatiquement en production</li>
                </ul>
                
                <h3>Outils CI/CD Populaires</h3>
                <ul>
                    <li><strong>GitHub Actions&nbsp;:</strong> Natif aux dépôts GitHub</li>
                    <li><strong>GitLab CI/CD&nbsp;:</strong> Intégré avec GitLab</li>
                    <li><strong>Jenkins&nbsp;:</strong> Serveur d'automatisation open-source</li>
                    <li><strong>CircleCI&nbsp;:</strong> Plateforme CI/CD basée sur le cloud</li>
                    <li><strong>ArgoCD&nbsp;:</strong> Livraison continue GitOps pour Kubernetes</li>
                </ul>
                
                <h3>Exemple de Flux de Travail GitHub Actions</h3>
                <div class="code-block">
name: Deploy to Kubernetes

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Build Docker image
      run: docker build -t myapp:${% raw %}{{ github.sha }}{% endraw %} .
    
    - name: Push to registry
      run: docker push myapp:${% raw %}{{ github.sha }}{% endraw %}
    
    - name: Deploy to Kubernetes
      run: kubectl apply -f k8s/
                </div>
            </section>
            
            <section id="best-practices" class="section">
                <h2>✨ Bonnes Pratiques</h2>
                
                <h3>Bonnes Pratiques Docker</h3>
                <ul>
                    <li>Utiliser des images de base officielles</li>
                    <li>Minimiser le nombre de couches et la taille de l'image</li>
                    <li>Utiliser .dockerignore pour exclure les fichiers inutiles</li>
                    <li>Exécuter les conteneurs en tant qu'utilisateurs non-root</li>
                    <li>Utiliser des tags de version spécifiques, pas <code>latest</code></li>
                    <li>Scanner régulièrement les images pour les vulnérabilités</li>
                </ul>
                
                <h3>Bonnes Pratiques Kubernetes</h3>
                <ul>
                    <li>Définir les demandes et limites de ressources</li>
                    <li>Utiliser des contrôles de santé (sondes de vivacité et de disponibilité)</li>
                    <li>Implémenter une journalisation et une surveillance appropriées</li>
                    <li>Utiliser des namespaces pour l'isolation des ressources</li>
                    <li>Stocker les secrets en toute sécurité, jamais en texte brut</li>
                    <li>Utiliser ConfigMaps pour la gestion de la configuration</li>
                    <li>Implémenter RBAC pour le contrôle d'accès</li>
                    <li>Mises à jour régulières du cluster et correctifs de sécurité</li>
                </ul>
                
                <h3>Bonnes Pratiques de Sécurité</h3>
                <ul>
                    <li>Scanner les images de conteneurs pour les vulnérabilités</li>
                    <li>Utiliser des politiques réseau pour contrôler le trafic</li>
                    <li>Implémenter des politiques de sécurité des pods</li>
                    <li>Faire une rotation régulière des secrets et identifiants</li>
                    <li>Activer la journalisation d'audit</li>
                    <li>Utiliser un service mesh pour la communication chiffrée (par ex., Istio)</li>
                </ul>
                
                <div class="highlight">
                    <strong>🔒 Sécurité d'Abord&nbsp;:</strong> Suivez toujours le principe du moindre privilège et mettez à jour régulièrement vos dépendances pour corriger les vulnérabilités connues.
                </div>
            </section>
        </div>
        
        <footer>
            <p>&copy; 2025 Hub de Documentation DevOps | Louis BERTRAND</p>
        </footer>
    </div>
</body>
</html>
'''

# HTML template for deployment documentation
DEPLOYMENT_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guide de Déploiement - DevOps Azure</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #0078d4 0%, #00bcf2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        header {
            background: linear-gradient(135deg, #0078d4 0%, #00bcf2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        nav {
            background: #f8f9fa;
            padding: 20px 40px;
            border-bottom: 2px solid #e9ecef;
        }
        nav a {
            display: inline-block;
            padding: 10px 20px;
            margin: 5px;
            background: white;
            color: #0078d4;
            text-decoration: none;
            border-radius: 6px;
            border: 2px solid #0078d4;
            font-weight: 600;
            transition: all 0.3s;
        }
        nav a:hover {
            background: #0078d4;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 120, 212, 0.4);
        }
        .content {
            padding: 40px;
        }
        .section {
            margin-bottom: 40px;
        }
        .section h2 {
            color: #0078d4;
            font-size: 2em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #0078d4;
        }
        .section h3 {
            color: #00bcf2;
            font-size: 1.5em;
            margin: 25px 0 15px 0;
        }
        .section h4 {
            color: #005a9e;
            font-size: 1.2em;
            margin: 20px 0 10px 0;
        }
        .section p {
            margin-bottom: 15px;
            font-size: 1.1em;
        }
        .section ul, .section ol {
            margin: 15px 0 15px 30px;
        }
        .section li {
            margin-bottom: 10px;
            font-size: 1.05em;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #e83e8c;
        }
        .code-block {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            line-height: 1.5;
        }
        .highlight {
            background: #e3f2fd;
            padding: 15px;
            border-left: 4px solid #0078d4;
            margin: 20px 0;
            border-radius: 4px;
        }
        .info-box {
            background: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ffc107;
            margin: 20px 0;
            border-radius: 4px;
        }
        .success-box {
            background: #d4edda;
            padding: 15px;
            border-left: 4px solid #28a745;
            margin: 20px 0;
            border-radius: 4px;
        }
        .flow-diagram {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 8px;
            margin: 25px 0;
            text-align: center;
        }
        .flow-step {
            display: inline-block;
            background: white;
            padding: 15px 25px;
            margin: 10px;
            border-radius: 8px;
            border: 2px solid #0078d4;
            font-weight: 600;
            color: #0078d4;
        }
        .flow-arrow {
            display: inline-block;
            font-size: 2em;
            color: #0078d4;
            margin: 0 10px;
        }
        footer {
            background: #2d3748;
            color: white;
            text-align: center;
            padding: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>☁️ Guide de Déploiement Azure</h1>
            <p>Comment cette application est déployée sur Azure Kubernetes Service</p>
        </header>
        
        <nav>
            <a href="/">Accueil</a>
            <a href="/contribute">Contribuer</a>
            <a href="#overview">Vue d'ensemble</a>
            <a href="#github-actions">GitHub Actions</a>
            <a href="#docker">Build Docker</a>
            <a href="#aks">Déploiement AKS</a>
            <a href="#networking">Réseau & Domaine</a>
            <a href="#ssl">SSL/TLS</a>
        </nav>
        
        <div class="content">
            <section id="overview" class="section">
                <h2>🎯 Vue d'ensemble du Déploiement</h2>
                <p>Cette application Flask est déployée sur Azure Kubernetes Service (AKS) et accessible via le domaine <code>app.lucho-dev.xyz</code>. Le processus de déploiement est entièrement automatisé grâce à GitHub Actions.</p>
                
                <h3>Architecture de Déploiement</h3>
                <div class="flow-diagram">
                    <div class="flow-step">GitHub Push</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">GitHub Actions</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">Build Docker</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">Push vers Registres</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">Déploiement AKS</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">Ingress NGINX</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">app.lucho-dev.xyz</div>
                </div>
                
                <h3>Composants Clés</h3>
                <ul>
                    <li><strong>GitHub Actions</strong> : Pipeline CI/CD automatisé</li>
                    <li><strong>Docker Hub</strong> : Registre d'images public (docker.io/louisdev22/devopstest)</li>
                    <li><strong>Azure Container Registry (ACR)</strong> : Registre privé Azure (devopstestaksregistry.azurecr.io)</li>
                    <li><strong>Azure Kubernetes Service (AKS)</strong> : Cluster Kubernetes managé</li>
                    <li><strong>NGINX Ingress Controller</strong> : Routage du trafic HTTP/HTTPS</li>
                    <li><strong>cert-manager</strong> : Gestion automatique des certificats SSL</li>
                    <li><strong>Let's Encrypt</strong> : Certificats SSL gratuits</li>
                </ul>
            </section>
            
            <section id="github-actions" class="section">
                <h2>🔄 Pipeline GitHub Actions</h2>
                <p>Le fichier <code>.github/workflows/deploy.yml</code> définit un pipeline CI/CD en deux étapes : <strong>Build</strong> et <strong>Deploy</strong>.</p>
                
                <h3>Étape 1 : Build</h3>
                <p>Cette étape s'exécute à chaque push sur les branches <code>main</code> ou <code>master</code>.</p>
                
                <h4>1.1 Préparation de l'environnement</h4>
                <div class="code-block">
- name: Checkout code
  uses: actions/checkout@v4

- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.12'

- name: Install dependencies
  run: |
    pip install -r requirements.txt
</div>
                <p>Le code source est récupéré, Python 3.12 est installé, et les dépendances Flask sont installées.</p>
                
                <h4>1.2 Tests (placeholder)</h4>
                <div class="code-block">
- name: Run tests
  run: |
    echo "No tests yet, skipping..."
    # pytest
</div>
                <p>Actuellement, aucun test n'est exécuté, mais l'étape est prête pour intégrer pytest à l'avenir.</p>
                
                <h4>1.3 Authentification aux registres</h4>
                <div class="code-block">
- name: Log in to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${% raw %}{{ secrets.DOCKERHUB_USERNAME }}{% endraw %}
    password: ${% raw %}{{ secrets.DOCKERHUB_TOKEN }}{% endraw %}

- name: Log in to Azure Container Registry
  uses: azure/docker-login@v2
  with:
    login-server: devopstestaksregistry.azurecr.io
    username: ${% raw %}{{ secrets.AZURE_ACR_USERNAME }}{% endraw %}
    password: ${% raw %}{{ secrets.AZURE_ACR_PASSWORD }}{% endraw %}
</div>
                <p>Le pipeline s'authentifie auprès de Docker Hub et d'Azure Container Registry en utilisant des secrets GitHub sécurisés.</p>
                
                <div class="info-box">
                    <strong>💡 Secrets GitHub requis :</strong>
                    <ul style="margin-top: 10px;">
                        <li><code>DOCKERHUB_USERNAME</code> et <code>DOCKERHUB_TOKEN</code></li>
                        <li><code>AZURE_ACR_USERNAME</code> et <code>AZURE_ACR_PASSWORD</code></li>
                        <li><code>KUBECONFIG</code> (pour l'étape de déploiement)</li>
                    </ul>
                </div>
                
                <h4>1.4 Génération du tag de version</h4>
                <div class="code-block">
- name: Generate version tag
  id: version
  run: |
    VERSION=$(git rev-parse --short HEAD)
    echo "VERSION=$VERSION" >> $GITHUB_OUTPUT
    echo "Generated version: $VERSION"
</div>
                <p>Un tag de version basé sur le hash du commit Git (ex: <code>a1b2c3d</code>) est généré pour identifier chaque build de manière unique.</p>
                
                <h4>1.5 Build et Push des images Docker</h4>
                <div class="code-block">
- name: Build and push Docker images
  run: |
    VERSION=${% raw %}{{ steps.version.outputs.VERSION }}{% endraw %}
    
    # Build l'image avec le tag de version
    docker build -t ${% raw %}{{ secrets.DOCKERHUB_USERNAME }}{% endraw %}/devopstest:${VERSION} .
    
    # Tag pour Docker Hub (latest + version)
    docker tag ${% raw %}{{ secrets.DOCKERHUB_USERNAME }}{% endraw %}/devopstest:${VERSION} \\
               ${% raw %}{{ secrets.DOCKERHUB_USERNAME }}{% endraw %}/devopstest:latest
    
    # Tag pour Azure Container Registry (latest + version)
    docker tag ${% raw %}{{ secrets.DOCKERHUB_USERNAME }}{% endraw %}/devopstest:${VERSION} \\
               devopstestaksregistry.azurecr.io/devopstest:${VERSION}
    docker tag ${% raw %}{{ secrets.DOCKERHUB_USERNAME }}{% endraw %}/devopstest:${VERSION} \\
               devopstestaksregistry.azurecr.io/devopstest:latest
    
    # Push vers Docker Hub
    docker push ${% raw %}{{ secrets.DOCKERHUB_USERNAME }}{% endraw %}/devopstest:${VERSION}
    docker push ${% raw %}{{ secrets.DOCKERHUB_USERNAME }}{% endraw %}/devopstest:latest
    
    # Push vers Azure Container Registry
    docker push devopstestaksregistry.azurecr.io/devopstest:${VERSION}
    docker push devopstestaksregistry.azurecr.io/devopstest:latest
</div>
                <p>L'image Docker est construite puis poussée vers <strong>deux registres</strong> avec deux tags (<code>latest</code> et le hash du commit) :</p>
                <ul>
                    <li><strong>Docker Hub</strong> : Registre public accessible à tous</li>
                    <li><strong>Azure ACR</strong> : Registre privé optimisé pour AKS</li>
                </ul>
                
                <h3>Étape 2 : Deploy</h3>
                <p>Cette étape déploie l'application sur le cluster AKS après le succès du build.</p>
                
                <h4>2.1 Configuration de kubectl</h4>
                <div class="code-block">
- name: Set up kubectl
  uses: azure/setup-kubectl@v4
  with:
    version: 'latest'

- name: Configure Kubeconfig
  run: |
    mkdir -p ~/.kube
    echo "${% raw %}{{ secrets.KUBECONFIG }}{% endraw %}" > ~/.kube/config
    chmod 600 ~/.kube/config
</div>
                <p>L'outil <code>kubectl</code> est installé et configuré avec le fichier kubeconfig stocké dans les secrets GitHub.</p>
                
                <h4>2.2 Mise à jour du déploiement</h4>
                <div class="code-block">
- name: Update image in Kubernetes deployment
  run: |
    VERSION=${% raw %}{{ needs.build.outputs.version }}{% endraw %}
    kubectl set image deployment/devopstest-deployment \\
      devopstest=devopstestaksregistry.azurecr.io/devopstest:${VERSION}
</div>
                <p>Le déploiement Kubernetes est mis à jour avec la nouvelle version de l'image depuis Azure ACR.</p>
                
                <h4>2.3 Application des manifests</h4>
                <div class="code-block">
- name: Apply Kubernetes manifests
  run: |
    kubectl apply -f k8s/service.yml
    kubectl apply -f k8s/ingress.yml
    kubectl rollout status deployment/devopstest-deployment
</div>
                <p>Les manifests Kubernetes (Service et Ingress) sont appliqués, et le pipeline attend que le rollout soit terminé.</p>
            </section>
            
            <section id="docker" class="section">
                <h2>🐳 Build de l'Image Docker</h2>
                <p>L'application est empaquetée dans une image Docker légère basée sur Python 3.12.</p>
                
                <h3>Dockerfile</h3>
                <div class="code-block">
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

ENV FLASK_APP=app
EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
</div>
                
                <h3>Explication ligne par ligne</h3>
                <ol>
                    <li><code>FROM python:3.12-slim</code> : Image de base légère avec Python 3.12</li>
                    <li><code>WORKDIR /app</code> : Définit le répertoire de travail</li>
                    <li><code>COPY requirements.txt .</code> : Copie les dépendances</li>
                    <li><code>RUN pip install ...</code> : Installe Flask sans cache pour réduire la taille</li>
                    <li><code>COPY app.py .</code> : Copie le code source</li>
                    <li><code>ENV FLASK_APP=app</code> : Configure Flask</li>
                    <li><code>EXPOSE 8000</code> : Expose le port 8000</li>
                    <li><code>CMD [...]</code> : Lance Flask sur toutes les interfaces</li>
                </ol>
            </section>
            
            <section id="aks" class="section">
                <h2>☸️ Déploiement sur Azure Kubernetes Service</h2>
                <p>L'application s'exécute dans un cluster AKS avec les manifests Kubernetes suivants :</p>
                
                <h3>Deployment (k8s/deployment.yml)</h3>
                <div class="code-block">
apiVersion: apps/v1
kind: Deployment
metadata:
  name: devopstest-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: devopstest
  template:
    metadata:
      labels:
        app: devopstest
    spec:
      imagePullSecrets:
        - name: acr-auth
      containers:
        - name: devopstest
          image: devopstestaksregistry.azurecr.io/devopstest:latest
          ports:
            - containerPort: 8000
</div>
                
                <h4>Points clés :</h4>
                <ul>
                    <li><strong>replicas: 1</strong> : Une seule instance de l'application</li>
                    <li><strong>imagePullSecrets</strong> : Secret <code>acr-auth</code> pour s'authentifier à Azure ACR</li>
                    <li><strong>image</strong> : Image depuis Azure Container Registry</li>
                    <li><strong>containerPort: 8000</strong> : Port exposé par Flask</li>
                </ul>
                
                <div class="info-box">
                    <strong>💡 Configuration du Secret ACR :</strong><br>
                    Le secret <code>acr-auth</code> doit être créé dans le cluster pour permettre à Kubernetes de tirer des images depuis Azure ACR :
                    <div class="code-block" style="margin-top: 10px;">
kubectl create secret docker-registry acr-auth \\
  --docker-server=devopstestaksregistry.azurecr.io \\
  --docker-username=&lt;username&gt; \\
  --docker-password=&lt;password&gt; \\
  --docker-email=&lt;email&gt;
</div>
                </div>
                
                <h3>Service (k8s/service.yml)</h3>
                <div class="code-block">
apiVersion: v1
kind: Service
metadata:
  name: devopstest-service
spec:
  selector:
    app: devopstest
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
  type: ClusterIP
</div>
                
                <h4>Points clés :</h4>
                <ul>
                    <li><strong>type: ClusterIP</strong> : Service interne au cluster (pas d'IP publique directe)</li>
                    <li><strong>port: 8000</strong> : Port du service</li>
                    <li><strong>targetPort: 8000</strong> : Port du conteneur</li>
                    <li><strong>selector</strong> : Connecte le Service aux Pods avec le label <code>app: devopstest</code></li>
                </ul>
            </section>
            
            <section id="networking" class="section">
                <h2>🌐 Réseau et Configuration du Domaine</h2>
                <p>Le trafic externe vers l'application passe par un contrôleur NGINX Ingress qui route les requêtes vers le Service Kubernetes.</p>
                
                <h3>Ingress (k8s/ingress.yml)</h3>
                <div class="code-block">
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: devopstest-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - app.lucho-dev.xyz
    secretName: devopstest-tls
  rules:
  - host: app.lucho-dev.xyz
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: devopstest-service
            port:
              number: 8000
</div>
                
                <h4>Explication :</h4>
                <ul>
                    <li><strong>kubernetes.io/ingress.class: nginx</strong> : Utilise le contrôleur NGINX Ingress</li>
                    <li><strong>cert-manager.io/cluster-issuer</strong> : Demande un certificat SSL automatique</li>
                    <li><strong>host: app.lucho-dev.xyz</strong> : Le domaine qui pointe vers l'application</li>
                    <li><strong>tls</strong> : Active HTTPS avec le certificat stocké dans <code>devopstest-tls</code></li>
                    <li><strong>backend</strong> : Route vers <code>devopstest-service:8000</code></li>
                </ul>
                
                <h3>Flux du Trafic</h3>
                <div class="flow-diagram">
                    <div class="flow-step">Client</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">DNS (app.lucho-dev.xyz)</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">IP Publique AKS</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">NGINX Ingress</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">Service K8s</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-step">Pod Flask</div>
                </div>
                
                <h3>Configuration DNS</h3>
                <p>Le domaine <code>app.lucho-dev.xyz</code> doit être configuré avec un enregistrement DNS de type <strong>A</strong> pointant vers l'IP publique du Load Balancer du cluster AKS.</p>
                
                <div class="info-box">
                    <strong>💡 Obtenir l'IP publique :</strong>
                    <div class="code-block" style="margin-top: 10px;">
kubectl get service -n ingress-nginx ingress-nginx-controller
</div>
                    <p style="margin-top: 10px;">Cherchez la colonne <code>EXTERNAL-IP</code> pour trouver l'IP publique à utiliser dans la configuration DNS.</p>
                </div>
            </section>
            
            <section id="ssl" class="section">
                <h2>🔒 Certificats SSL/TLS avec cert-manager</h2>
                <p>Les certificats SSL sont gérés automatiquement par <strong>cert-manager</strong> et émis gratuitement par <strong>Let's Encrypt</strong>.</p>
                
                <h3>ClusterIssuer (k8s/cluster-issuer.yaml)</h3>
                <div class="code-block">
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    email: louis.development22@gmail.com
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
</div>
                
                <h4>Explication :</h4>
                <ul>
                    <li><strong>ClusterIssuer</strong> : Ressource cert-manager qui demande des certificats</li>
                    <li><strong>acme.email</strong> : Email pour les notifications Let's Encrypt</li>
                    <li><strong>acme.server</strong> : Serveur de production Let's Encrypt (limite de 50 certificats/semaine)</li>
                    <li><strong>http01</strong> : Validation par challenge HTTP-01 via Ingress NGINX</li>
                </ul>
                
                <h3>Processus d'émission du certificat</h3>
                <ol>
                    <li><strong>Création de l'Ingress</strong> : L'annotation <code>cert-manager.io/cluster-issuer</code> déclenche cert-manager</li>
                    <li><strong>Demande ACME</strong> : cert-manager contacte Let's Encrypt pour demander un certificat</li>
                    <li><strong>Challenge HTTP-01</strong> : Let's Encrypt envoie une requête à <code>app.lucho-dev.xyz/.well-known/acme-challenge/...</code></li>
                    <li><strong>Validation</strong> : cert-manager répond via Ingress NGINX, prouvant le contrôle du domaine</li>
                    <li><strong>Émission</strong> : Let's Encrypt émet le certificat SSL valide pour 90 jours</li>
                    <li><strong>Stockage</strong> : Le certificat est stocké dans le Secret <code>devopstest-tls</code></li>
                    <li><strong>Renouvellement automatique</strong> : cert-manager renouvelle le certificat avant expiration</li>
                </ol>
                
                <div class="success-box">
                    <strong>✅ Résultat :</strong> L'application est accessible en HTTPS sur <a href="https://app.lucho-dev.xyz" target="_blank">https://app.lucho-dev.xyz</a> avec un certificat SSL valide !
                </div>
                
                <h3>Vérifier le certificat</h3>
                <div class="code-block">
# Vérifier l'état du certificat
kubectl get certificate

# Voir les détails du certificat
kubectl describe certificate devopstest-tls

# Voir le contenu du Secret TLS
kubectl get secret devopstest-tls -o yaml
</div>
            </section>
            
            <section class="section">
                <h2>📋 Récapitulatif du Déploiement</h2>
                
                <h3>Étapes Complètes</h3>
                <ol style="font-size: 1.05em; line-height: 1.8;">
                    <li><strong>Développement local</strong> : Code Python/Flask avec Dockerfile</li>
                    <li><strong>Push sur GitHub</strong> : Modifications poussées sur <code>main</code> ou <code>master</code></li>
                    <li><strong>GitHub Actions - Build</strong> :
                        <ul>
                            <li>Installation des dépendances Python</li>
                            <li>Exécution des tests (placeholder)</li>
                            <li>Build de l'image Docker</li>
                            <li>Push vers Docker Hub et Azure ACR avec tag de version</li>
                        </ul>
                    </li>
                    <li><strong>GitHub Actions - Deploy</strong> :
                        <ul>
                            <li>Configuration de kubectl avec le kubeconfig</li>
                            <li>Mise à jour du Deployment avec la nouvelle image</li>
                            <li>Application du Service et de l'Ingress</li>
                        </ul>
                    </li>
                    <li><strong>Azure AKS</strong> :
                        <ul>
                            <li>Pull de l'image depuis Azure ACR</li>
                            <li>Création/Mise à jour du Pod Flask</li>
                            <li>Exposition via Service ClusterIP</li>
                        </ul>
                    </li>
                    <li><strong>NGINX Ingress</strong> :
                        <ul>
                            <li>Réception du trafic HTTP/HTTPS</li>
                            <li>Routage basé sur le host <code>app.lucho-dev.xyz</code></li>
                            <li>Terminaison TLS avec certificat Let's Encrypt</li>
                        </ul>
                    </li>
                    <li><strong>cert-manager</strong> :
                        <ul>
                            <li>Demande automatique du certificat SSL</li>
                            <li>Validation via challenge HTTP-01</li>
                            <li>Renouvellement automatique tous les 60 jours</li>
                        </ul>
                    </li>
                    <li><strong>Accès public</strong> : Application accessible sur <code>https://app.lucho-dev.xyz</code></li>
                </ol>
                
                <h3>Commandes Utiles</h3>
                <div class="code-block">
# Vérifier l'état du déploiement
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get ingress

# Voir les logs de l'application
kubectl logs -f deployment/devopstest-deployment

# Redémarrer le déploiement
kubectl rollout restart deployment/devopstest-deployment

# Vérifier l'historique des rollouts
kubectl rollout history deployment/devopstest-deployment

# Vérifier les certificats SSL
kubectl get certificate
kubectl describe certificate devopstest-tls
</div>
            </section>
        </div>
        
        <footer>
            <p>&copy; 2025 Guide de Déploiement DevOps | Louis BERTRAND</p>
        </footer>
    </div>
</body>
</html>
'''

@app.route("/")
def documentation():
    return render_template_string(HTML_TEMPLATE)

@app.route("/deployment")
def deployment():
    return render_template_string(DEPLOYMENT_TEMPLATE)

# API Endpoints
@app.route("/api/health")
def health_check():
    """Health check endpoint for Kubernetes liveness/readiness probes"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    }), 200

@app.route("/api/info")
def app_info():
    """Application information endpoint"""
    uptime = datetime.datetime.now() - START_TIME
    return jsonify({
        "application": "DevOps Documentation Hub",
        "version": APP_VERSION,
        "author": "Louis BERTRAND",
        "uptime_seconds": int(uptime.total_seconds()),
        "start_time": START_TIME.isoformat(),
        "routes": {
            "documentation": "/",
            "deployment_guide": "/deployment",
            "health": "/api/health",
            "info": "/api/info"
        }
    }), 200

# Contact/Contribution page
@app.route("/contribute")
def contribute():
    """Contribution and contact page"""
    CONTRIBUTE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contribuer - DevOps Documentation Hub</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        nav {
            background: #f8f9fa;
            padding: 20px 40px;
            border-bottom: 2px solid #e9ecef;
        }
        nav a {
            display: inline-block;
            padding: 10px 20px;
            margin: 5px;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 6px;
            border: 2px solid #667eea;
            font-weight: 600;
            transition: all 0.3s;
        }
        nav a:hover {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        .content {
            padding: 40px;
        }
        .section {
            margin-bottom: 30px;
        }
        .section h2 {
            color: #667eea;
            font-size: 2em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }
        .section h3 {
            color: #764ba2;
            font-size: 1.5em;
            margin: 20px 0 10px 0;
        }
        .section p {
            margin-bottom: 15px;
            font-size: 1.1em;
        }
        .section ul {
            margin: 15px 0 15px 30px;
        }
        .section li {
            margin-bottom: 10px;
            font-size: 1.05em;
        }
        .info-box {
            background: #e3f2fd;
            padding: 20px;
            border-left: 4px solid #667eea;
            margin: 20px 0;
            border-radius: 4px;
        }
        .code-block {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
        }
        .contact-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }
        .contact-card h4 {
            color: #667eea;
            margin-bottom: 10px;
        }
        footer {
            background: #2d3748;
            color: white;
            text-align: center;
            padding: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🤝 Contribuer au Projet</h1>
            <p>Rejoignez la communauté DevOps</p>
        </header>
        
        <nav>
            <a href="/">Accueil</a>
            <a href="/deployment">Déploiement Azure</a>
            <a href="/contribute">Contribuer</a>
        </nav>
        
        <div class="content">
            <section class="section">
                <h2>💡 Comment Contribuer</h2>
                <p>Ce projet est open-source et les contributions sont les bienvenues&nbsp;! Voici comment vous pouvez participer&nbsp;:</p>
                
                <h3>1. Signaler des Problèmes</h3>
                <p>Si vous trouvez un bug ou avez une suggestion d'amélioration, créez une issue sur GitHub.</p>
                <div class="code-block">
# Accédez au dépôt GitHub
https://github.com/louisbertrand22/DevOpsTest/issues
                </div>
                
                <h3>2. Proposer des Améliorations</h3>
                <p>Suivez ces étapes pour contribuer du code&nbsp;:</p>
                <ul>
                    <li><strong>Fork</strong> le dépôt sur votre compte GitHub</li>
                    <li>Créez une branche pour votre fonctionnalité (<code>git checkout -b feature/nouvelle-fonctionnalite</code>)</li>
                    <li>Commitez vos modifications (<code>git commit -am 'Ajout d'une nouvelle fonctionnalité'</code>)</li>
                    <li>Poussez vers la branche (<code>git push origin feature/nouvelle-fonctionnalite</code>)</li>
                    <li>Créez une <strong>Pull Request</strong></li>
                </ul>
                
                <h3>3. Améliorer la Documentation</h3>
                <p>La documentation peut toujours être améliorée. N'hésitez pas à&nbsp;:</p>
                <ul>
                    <li>Corriger les fautes de frappe</li>
                    <li>Ajouter des exemples</li>
                    <li>Clarifier des sections confuses</li>
                    <li>Traduire dans d'autres langues</li>
                </ul>
            </section>
            
            <section class="section">
                <h2>📋 Bonnes Pratiques</h2>
                <div class="info-box">
                    <strong>💡 Directives de Contribution&nbsp;:</strong>
                    <ul style="margin-top: 10px;">
                        <li>Assurez-vous que votre code suit le style existant</li>
                        <li>Testez vos modifications localement</li>
                        <li>Écrivez des messages de commit clairs et descriptifs</li>
                        <li>Documentez les nouvelles fonctionnalités</li>
                        <li>Soyez respectueux dans vos interactions</li>
                    </ul>
                </div>
            </section>
            
            <section class="section">
                <h2>📧 Contact</h2>
                <div class="contact-card">
                    <h4>GitHub Repository</h4>
                    <p><a href="https://github.com/louisbertrand22/DevOpsTest" target="_blank">github.com/louisbertrand22/DevOpsTest</a></p>
                </div>
                <div class="contact-card">
                    <h4>Auteur</h4>
                    <p>Louis BERTRAND</p>
                    <p>Email: louis.development22@gmail.com</p>
                </div>
            </section>
            
            <section class="section">
                <h2>🌟 Technologies Utilisées</h2>
                <p>Ce projet utilise les technologies suivantes&nbsp;:</p>
                <ul>
                    <li><strong>Python 3.12</strong> - Langage de programmation</li>
                    <li><strong>Flask 3.0.2</strong> - Framework web</li>
                    <li><strong>Docker</strong> - Conteneurisation</li>
                    <li><strong>Kubernetes</strong> - Orchestration de conteneurs</li>
                    <li><strong>GitHub Actions</strong> - CI/CD</li>
                    <li><strong>Azure AKS</strong> - Déploiement cloud</li>
                </ul>
            </section>
        </div>
        
        <footer>
            <p>&copy; 2025 DevOps Documentation Hub | Louis BERTRAND</p>
        </footer>
    </div>
</body>
</html>
'''
    return render_template_string(CONTRIBUTE_TEMPLATE)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    ERROR_404_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Non Trouvée</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .error-container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 60px 40px;
            text-align: center;
            max-width: 600px;
        }
        .error-code {
            font-size: 8em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 20px;
        }
        h1 {
            color: #333;
            font-size: 2em;
            margin-bottom: 20px;
        }
        p {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .btn {
            display: inline-block;
            padding: 15px 30px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s;
            margin: 5px;
        }
        .btn:hover {
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-code">404</div>
        <h1>Page Non Trouvée</h1>
        <p>Désolé, la page que vous recherchez n'existe pas.</p>
        <a href="/" class="btn">🏠 Retour à l'accueil</a>
        <a href="/contribute" class="btn">📧 Signaler un problème</a>
    </div>
</body>
</html>
'''
    return render_template_string(ERROR_404_TEMPLATE), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error page"""
    ERROR_500_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 - Erreur Serveur</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .error-container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 60px 40px;
            text-align: center;
            max-width: 600px;
        }
        .error-code {
            font-size: 8em;
            font-weight: bold;
            color: #dc3545;
            margin-bottom: 20px;
        }
        h1 {
            color: #333;
            font-size: 2em;
            margin-bottom: 20px;
        }
        p {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .btn {
            display: inline-block;
            padding: 15px 30px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s;
            margin: 5px;
        }
        .btn:hover {
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-code">500</div>
        <h1>Erreur Serveur</h1>
        <p>Une erreur interne s'est produite. Veuillez réessayer plus tard.</p>
        <a href="/" class="btn">🏠 Retour à l'accueil</a>
        <a href="/contribute" class="btn">📧 Signaler le problème</a>
    </div>
</body>
</html>
'''
    return render_template_string(ERROR_500_TEMPLATE), 500

# Security headers middleware
@app.after_request
def add_security_headers(response):
    """Add security headers to all responses"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response