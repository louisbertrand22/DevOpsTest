from flask import Flask, render_template_string

app = Flask(__name__)

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

@app.route("/")
def documentation():
    return render_template_string(HTML_TEMPLATE)