# DevOpsTest

**Author**: Louis BERTRAND

A simple Flask web application demonstrating DevOps practices with Docker and Kubernetes deployment configurations.

## Description

This is a Flask application serving comprehensive DevOps documentation with interactive pages covering Docker, Kubernetes, CI/CD, and deployment practices. It's designed to showcase containerization and orchestration practices using Docker, Docker Compose, and Kubernetes, with automated CI/CD using GitHub Actions.

## Features

- **📚 DevOps Documentation**: Comprehensive guides on Docker, Kubernetes, Ingress, and CI/CD best practices
- **☁️ Azure Deployment Guide**: Detailed explanation of the Azure AKS deployment pipeline
- **🤝 Contribution Page**: Information on how to contribute to the project
- **🏥 Health Check API**: `/api/health` endpoint for Kubernetes liveness/readiness probes
- **📊 Application Info API**: `/api/info` endpoint providing application metadata and uptime
- **🔒 Security Headers**: Implemented security best practices with HTTP headers
- **❌ Custom Error Pages**: User-friendly 404 and 500 error pages

## Technology Stack

- **Python 3.12**: Programming language
- **Flask 3.0.2**: Web framework
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Kubernetes**: Container orchestration platform
- **GitHub Actions**: CI/CD pipeline for automated builds and deployments

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.12 or higher
- pip (Python package manager)
- Docker
- Docker Compose (optional, for Docker Compose deployment)
- Kubernetes cluster (optional, for Kubernetes deployment)
- kubectl (optional, for Kubernetes deployment)

## Project Structure

```
DevOpsTest/
├── src/                     # Application source code
│   ├── app.py              # Main Flask application factory
│   ├── routes/             # Route handlers (blueprints)
│   │   ├── __init__.py
│   │   ├── main_routes.py  # Main page routes (/, /deployment, /contribute)
│   │   ├── api_routes.py   # API endpoints (/api/health, /api/info)
│   │   └── error_handlers.py # Error page handlers (404, 500)
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Base template with common layout
│   │   ├── index.html      # Homepage (DevOps documentation)
│   │   ├── deployment.html # Azure deployment guide
│   │   ├── contribute.html # Contribution page
│   │   ├── 404.html        # 404 error page
│   │   └── 500.html        # 500 error page
│   └── static/             # Static files
│       └── css/
│           └── style.css   # Application styles
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker image configuration
├── docker-compose.yml     # Docker Compose configuration
├── k8s/                   # Kubernetes manifests
│   ├── deployment.yml     # Kubernetes Deployment
│   ├── service.yml        # Kubernetes Service
│   ├── ingress.yml        # Kubernetes Ingress
│   └── kustomization.yaml # Kustomize configuration
└── README.md              # This file
```

## Local Development

### 1. Using Python directly

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application (Flask defaults to port 5000)
export FLASK_APP=src.app
flask run --host=0.0.0.0 --port=8000
```

The application will be available at `http://localhost:8000`

**Note**: Flask's default port is 5000. We specify port 8000 to maintain consistency with the Docker and Kubernetes configurations.

### Available Routes

- **`/`**: Main DevOps documentation page
- **`/deployment`**: Azure deployment guide
- **`/contribute`**: Contribution and contact information
- **`/api/health`**: Health check endpoint (returns JSON with status and timestamp)
- **`/api/info`**: Application metadata (version, uptime, routes)

### API Examples

```bash
# Health check (useful for Kubernetes probes)
curl http://localhost:8000/api/health

# Application information
curl http://localhost:8000/api/info
```

## Docker Deployment

### 1. Using Docker

```bash
# Build the Docker image
docker build -t devopstest-web:latest .

# Run the container
docker run -p 8000:8000 devopstest-web:latest
```

### 2. Using Docker Compose

```bash
# Build and start the container
docker-compose up --build

# Run in detached mode
docker-compose up -d

# Stop the container
docker-compose down
```

The application will be accessible at `http://localhost:8000`

**Note**: The Docker Compose configuration creates a container named `TDevOpsTestDocker` and enables hot-reloading in development mode by mounting the application directory as a volume.

## Kubernetes Deployment

### Prerequisites for Kubernetes

- A running Kubernetes cluster (local or remote)
- kubectl configured to communicate with your cluster
- **NGINX Ingress Controller** installed in your cluster
- **cert-manager** installed in your cluster (for SSL/TLS certificates)

### Deploy to Kubernetes

The Kubernetes deployment is configured to use the Docker Hub image `docker.io/louisdev22/devopstest:latest`, which is automatically built and pushed by the GitHub Actions CI/CD pipeline.

#### Using the Pre-built Image from Docker Hub

The default configuration pulls the latest image from Docker Hub:

```bash
# The deployment.yml already references: docker.io/louisdev22/devopstest:latest
# No additional image build steps are needed
```

#### Building and Using Your Own Image

If you want to build and use your own image:

```bash
# Build the Docker image
docker build -t devopstest-web:latest .

# Tag the image for your registry
docker tag devopstest-web:latest <your-registry>/devopstest:latest

# Push to your registry (Docker Hub, GCR, ECR, etc.)
docker push <your-registry>/devopstest:latest

# Update the image in k8s/deployment.yml (line 17):
# Change: image: docker.io/louisdev22/devopstest:latest
# To:     image: <your-registry>/devopstest:latest
```

### Setting Up Prerequisites

#### 1. Install NGINX Ingress Controller

If you don't have NGINX Ingress Controller installed:

```bash
# For most Kubernetes clusters
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml

# For Azure AKS (recommended)
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml

# Verify installation
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```

#### 2. Install cert-manager

cert-manager is required for automatic SSL/TLS certificate management with Let's Encrypt:

```bash
# Install cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml

# Verify cert-manager is running
kubectl get pods -n cert-manager

# Wait for cert-manager to be ready
kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=cert-manager -n cert-manager --timeout=300s
```

#### 3. Configure DNS

Ensure your domain points to your cluster's external IP:

```bash
# Get the external IP of your NGINX Ingress Controller
kubectl get svc -n ingress-nginx

# Add an A record in your DNS provider:
# app.lucho-dev.xyz -> <EXTERNAL-IP>

# Verify DNS resolution
nslookup app.lucho-dev.xyz
```

### Apply Kubernetes Manifests

```bash
# Apply all Kubernetes manifests using Kustomize (recommended)
# This will deploy the application, service, ingress, and ClusterIssuers
kubectl apply -k k8s/

# Or apply individually
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
kubectl apply -f k8s/issuer-staging.yaml
kubectl apply -f k8s/cluster-issuer.yaml
kubectl apply -f k8s/ingress.yml

# Check deployment status
kubectl get pods
kubectl get services
kubectl get ingress

# Monitor certificate issuance
kubectl get certificate
kubectl get certificaterequest
kubectl get order
kubectl get challenge
```

### SSL/TLS Certificate Management

This project uses cert-manager with Let's Encrypt to automatically provision SSL/TLS certificates.

#### Certificate Issuers

Two ClusterIssuers are configured:

1. **letsencrypt-staging**: For testing (default in ingress.yml)
   - Uses Let's Encrypt staging environment
   - Certificates are not trusted by browsers but allow testing without rate limits
   - Good for development and troubleshooting

2. **letsencrypt-prod**: For production
   - Uses Let's Encrypt production environment
   - Issues trusted certificates
   - Subject to rate limits (50 certificates per domain per week)

#### Switching to Production Certificates

Once you've verified the staging certificate works, switch to production:

```bash
# Edit the ingress to use the production issuer
kubectl edit ingress devopstest-ingress

# Change this line:
#   cert-manager.io/cluster-issuer: letsencrypt-staging
# To:
#   cert-manager.io/cluster-issuer: letsencrypt-prod

# Or apply the updated ingress.yml after editing it
```

#### Troubleshooting Certificate Issues

If the certificate challenge shows as "invalid":

```bash
# Check the certificate status
kubectl describe certificate devopstest-tls

# Check certificate request
kubectl describe certificaterequest

# Check ACME order and challenges
kubectl get order
kubectl describe order <order-name>

# Check challenges (this shows the HTTP-01 validation status)
kubectl get challenge
kubectl describe challenge <challenge-name>

# Check cert-manager logs
kubectl logs -n cert-manager deploy/cert-manager

# Common issues and solutions:
# 1. DNS not pointing to cluster: Verify with 'nslookup app.lucho-dev.xyz'
# 2. Ingress controller not receiving traffic: Check ingress controller service external IP
# 3. Firewall blocking port 80: Ensure port 80 is open for HTTP-01 challenge
# 4. Wrong ingress class: Verify ingress.class is 'nginx' in ClusterIssuer
```

#### Forcing Certificate Renewal

If you need to recreate the certificate:

```bash
# Delete the certificate secret and certificate resource
kubectl delete secret devopstest-tls
kubectl delete certificate devopstest-tls

# Delete the ingress and reapply to trigger new certificate request
kubectl delete ingress devopstest-ingress
kubectl apply -f k8s/ingress.yml

# Monitor the new certificate issuance
kubectl get certificate --watch
```

### Access the Application

The application is exposed through:
- **Service**: ClusterIP on port 8000 (internal cluster access only)
- **Ingress**: Accessible via `https://app.lucho-dev.xyz` (requires DNS configuration and SSL certificate)

#### Accessing via HTTPS (Production)

Once DNS is configured and the certificate is issued:

```bash
# Check if certificate is ready
kubectl get certificate devopstest-tls

# Access the application
curl https://app.lucho-dev.xyz
# Or open in browser: https://app.lucho-dev.xyz
```

#### Accessing via HTTP (Development/Testing)

For local testing without DNS:

```bash
# Get the external IP of the ingress controller
kubectl get svc -n ingress-nginx

# Add to your /etc/hosts (Linux/Mac) or C:\Windows\System32\drivers\etc\hosts (Windows)
<EXTERNAL-IP> app.lucho-dev.xyz

# Test with curl (use -k to ignore staging certificate warning)
curl -k https://app.lucho-dev.xyz
```

### Clean Up Kubernetes Resources

```bash
# Delete all resources
kubectl delete -k k8s/

# Or delete individually
kubectl delete -f k8s/deployment.yml
kubectl delete -f k8s/service.yml
kubectl delete -f k8s/ingress.yml
```

## Configuration

### Environment Variables

- `FLASK_APP`: Set to `app` (already configured in Dockerfile and docker-compose.yml)
- `FLASK_ENV`: Set to `development` in docker-compose.yml for development mode

### Ports

- Application runs on port **8000** by default
- Can be modified in Dockerfile, docker-compose.yml, and Kubernetes manifests

## CI/CD Pipeline

This project includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automatically:

1. **Builds** the application when code is pushed to `main` or `master` branches
2. **Tests** the application (placeholder for future tests)
3. **Builds and pushes** the Docker image to Docker Hub
4. **Deploys** the application to a Kubernetes cluster

### Required GitHub Secrets

To use the CI/CD pipeline, configure the following secrets in your GitHub repository:

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token
- `KUBECONFIG`: Your Kubernetes cluster configuration file content

### Workflow Triggers

The workflow automatically runs on:
- Push to `main` branch
- Push to `master` branch

## Development

To modify the application:

1. Edit `app.py` to add new routes or functionality
2. Update `requirements.txt` if adding new dependencies
3. Rebuild Docker image if using containers
4. Reapply Kubernetes manifests if deployed to a cluster
5. Push changes to `main` or `master` branch to trigger the CI/CD pipeline

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a Pull Request

## License

This project is intended for educational and demonstration purposes.
