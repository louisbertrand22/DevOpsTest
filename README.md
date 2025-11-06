# DevOpsTest

A simple Flask web application demonstrating DevOps practices with Docker and Kubernetes deployment configurations.

## Description

This is a minimal Flask application that serves a "Hello World!" message. It's designed to showcase containerization and orchestration practices using Docker, Docker Compose, and Kubernetes.

## Technology Stack

- **Python 3.12**: Programming language
- **Flask 3.0.2**: Web framework
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Kubernetes**: Container orchestration platform

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
├── app.py                  # Main Flask application
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
export FLASK_APP=app
flask run --host=0.0.0.0 --port=8000
```

The application will be available at `http://localhost:8000`

**Note**: Flask's default port is 5000. We specify port 8000 to maintain consistency with the Docker and Kubernetes configurations.

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

## Kubernetes Deployment

### Prerequisites for Kubernetes

- A running Kubernetes cluster (local or remote)
- kubectl configured to communicate with your cluster

### Deploy to Kubernetes

#### Option 1: Using Local Images (for local clusters like minikube)

```bash
# Build the Docker image locally
docker build -t devopstest-web:latest .

# For minikube, load the image into minikube's Docker daemon
# minikube image load devopstest-web:latest

# The deployment uses imagePullPolicy: Never for local images
```

#### Option 2: Using a Container Registry (for remote clusters)

```bash
# Tag the image for your registry
docker tag devopstest-web:latest <your-registry>/devopstest-web:latest

# Push to your registry (Docker Hub, GCR, ECR, etc.)
docker push <your-registry>/devopstest-web:latest

# Update k8s/deployment.yml to use your registry image and change imagePullPolicy
# image: <your-registry>/devopstest-web:latest
# imagePullPolicy: Always
```

### Apply Kubernetes Manifests

```bash
# Apply Kubernetes manifests using kubectl
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
kubectl apply -f k8s/ingress.yml

# Or use Kustomize
kubectl apply -k k8s/

# Check deployment status
kubectl get pods
kubectl get services
kubectl get ingress
```

### Access the Application

The application is exposed through:
- **Service**: NodePort on port 8000
- **Ingress**: Accessible via `http://devopstest.local` (requires Ingress Controller like nginx-ingress)

To access via Ingress, add to your `/etc/hosts`:
```
<YOUR_CLUSTER_IP> devopstest.local
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

## Development

To modify the application:

1. Edit `app.py` to add new routes or functionality
2. Update `requirements.txt` if adding new dependencies
3. Rebuild Docker image if using containers
4. Reapply Kubernetes manifests if deployed to a cluster

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a Pull Request

## License

This project is intended for educational and demonstration purposes.
