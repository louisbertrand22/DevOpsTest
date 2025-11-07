from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for the documentation
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Documentation</title>
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
            <h1>🚀 DevOps Documentation Hub</h1>
            <p>Your comprehensive guide to modern DevOps practices</p>
        </header>
        
        <nav>
            <a href="#docker">Docker</a>
            <a href="#kubernetes">Kubernetes</a>
            <a href="#ingress">Ingress</a>
            <a href="#cicd">CI/CD</a>
            <a href="#best-practices">Best Practices</a>
        </nav>
        
        <div class="content">
            <section id="docker" class="section">
                <h2>🐳 Docker</h2>
                <p>Docker is a platform for developing, shipping, and running applications in containers. Containers package software with all dependencies, ensuring consistency across environments.</p>
                
                <h3>Key Concepts</h3>
                <ul>
                    <li><strong>Images:</strong> Read-only templates containing application code and dependencies</li>
                    <li><strong>Containers:</strong> Running instances of Docker images</li>
                    <li><strong>Dockerfile:</strong> Script defining how to build a Docker image</li>
                    <li><strong>Docker Hub:</strong> Cloud-based registry for storing and sharing Docker images</li>
                </ul>
                
                <h3>Common Commands</h3>
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
                    <strong>💡 Pro Tip:</strong> Use multi-stage builds to reduce image size and improve security by excluding build dependencies from production images.
                </div>
            </section>
            
            <section id="kubernetes" class="section">
                <h2>☸️ Kubernetes</h2>
                <p>Kubernetes (K8s) is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications.</p>
                
                <h3>Core Components</h3>
                <ul>
                    <li><strong>Pods:</strong> Smallest deployable units that contain one or more containers</li>
                    <li><strong>Deployments:</strong> Manage the desired state of your application</li>
                    <li><strong>Services:</strong> Expose your application on a network</li>
                    <li><strong>ConfigMaps & Secrets:</strong> Manage configuration and sensitive data</li>
                    <li><strong>Namespaces:</strong> Virtual clusters for resource isolation</li>
                </ul>
                
                <h3>Essential kubectl Commands</h3>
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
                
                <h3>Deployment Example</h3>
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
                <p>Ingress manages external access to services in a Kubernetes cluster, typically HTTP/HTTPS. It provides load balancing, SSL termination, and name-based virtual hosting.</p>
                
                <h3>Why Use Ingress?</h3>
                <ul>
                    <li>Single entry point for multiple services</li>
                    <li>SSL/TLS termination</li>
                    <li>Path-based and host-based routing</li>
                    <li>Load balancing across pods</li>
                    <li>Reduced cloud load balancer costs</li>
                </ul>
                
                <h3>Ingress Controller</h3>
                <p>An Ingress Controller is required to implement the Ingress rules. Popular options include:</p>
                <ul>
                    <li><strong>NGINX Ingress Controller:</strong> Most widely used</li>
                    <li><strong>Traefik:</strong> Modern reverse proxy with automatic SSL</li>
                    <li><strong>HAProxy:</strong> High-performance load balancer</li>
                    <li><strong>AWS ALB:</strong> Integrated with AWS Application Load Balancer</li>
                </ul>
                
                <h3>Ingress Configuration Example</h3>
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
                <h2>🔄 CI/CD Pipelines</h2>
                <p>Continuous Integration and Continuous Deployment (CI/CD) automate the software delivery process from code commit to production deployment.</p>
                
                <h3>CI/CD Workflow</h3>
                <ul>
                    <li><strong>Continuous Integration:</strong> Automatically build and test code changes</li>
                    <li><strong>Continuous Delivery:</strong> Automatically prepare releases for deployment</li>
                    <li><strong>Continuous Deployment:</strong> Automatically deploy to production</li>
                </ul>
                
                <h3>Popular CI/CD Tools</h3>
                <ul>
                    <li><strong>GitHub Actions:</strong> Native to GitHub repositories</li>
                    <li><strong>GitLab CI/CD:</strong> Integrated with GitLab</li>
                    <li><strong>Jenkins:</strong> Open-source automation server</li>
                    <li><strong>CircleCI:</strong> Cloud-based CI/CD platform</li>
                    <li><strong>ArgoCD:</strong> GitOps continuous delivery for Kubernetes</li>
                </ul>
                
                <h3>GitHub Actions Workflow Example</h3>
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
                <h2>✨ Best Practices</h2>
                
                <h3>Docker Best Practices</h3>
                <ul>
                    <li>Use official base images</li>
                    <li>Minimize layer count and image size</li>
                    <li>Use .dockerignore to exclude unnecessary files</li>
                    <li>Run containers as non-root users</li>
                    <li>Use specific version tags, not <code>latest</code></li>
                    <li>Scan images for vulnerabilities regularly</li>
                </ul>
                
                <h3>Kubernetes Best Practices</h3>
                <ul>
                    <li>Define resource requests and limits</li>
                    <li>Use health checks (liveness and readiness probes)</li>
                    <li>Implement proper logging and monitoring</li>
                    <li>Use namespaces for resource isolation</li>
                    <li>Store secrets securely, never in plain text</li>
                    <li>Use ConfigMaps for configuration management</li>
                    <li>Implement RBAC for access control</li>
                    <li>Regular cluster updates and security patches</li>
                </ul>
                
                <h3>Security Best Practices</h3>
                <ul>
                    <li>Scan container images for vulnerabilities</li>
                    <li>Use network policies to control traffic</li>
                    <li>Implement pod security policies</li>
                    <li>Regularly rotate secrets and credentials</li>
                    <li>Enable audit logging</li>
                    <li>Use service mesh for encrypted communication (e.g., Istio)</li>
                </ul>
                
                <div class="highlight">
                    <strong>🔒 Security First:</strong> Always follow the principle of least privilege and regularly update your dependencies to patch known vulnerabilities.
                </div>
            </section>
        </div>
        
        <footer>
            <p>&copy; 2024 DevOps Documentation Hub | Built with Flask & Docker</p>
            <p>Deployed on Kubernetes with ❤️</p>
        </footer>
    </div>
</body>
</html>
'''

@app.route("/")
def documentation():
    return render_template_string(HTML_TEMPLATE)