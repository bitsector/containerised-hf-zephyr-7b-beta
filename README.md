# Containerized Zephyr-7b-beta LLM Deployment

This repository demonstrates how to containerize and deploy the Zephyr-7b-beta Large Language Model (LLM) efficiently, addressing challenges such as substantial disk space requirements and time-consuming build processes.

## Overview

The project uses a two-stage Docker build process to optimize the deployment of the Zephyr-7b-beta model:

1. A pre-build stage that installs dependencies and caches the model.
2. A final build stage that creates a lean image with the application.

## Prerequisites

- Docker
- Kubernetes cluster (for deployment)

## Build and Deploy

### 1. Build the pre-cache image
```
docker build -t python-3.12-slim-bookworm-precache-builder:1.0 -f Dockerfile.prebuild .
```
### 2. Build the final image

docker build -t reponame/hf-zephyr:1.0 .

### 3. Test locally

docker run -it -p 5000:5000 --rm reponame/hf-zephyr:1.0

### 4. Push to Docker Hub

docker push reponame/hf-zephyr:1.0

### 5. Deploy to Kubernetes

kubectl apply -f hf-zephyre-service.yaml

### 6. Get the service IP

kubectl get service hf-zephyr-service -o jsonpath='{.status.loadBalancer.ingress.ip}'

## Testing

Use curl to test the deployed service:

curl -X POST http://<SERVICE_IP>:5000/chat \
     -H "Content-Type: application/json" \
     -d '{
         "messages": [
             {
                 "role": "system",
                 "content": "You are a friendly chatbot who always responds in the style of a pirate"
             },
             {
                 "role": "user",
                 "content": "How many helicopters can a human eat in one sitting?"
             }
         ]
     }'

## Key Features

- Efficient containerization of a large language model
- Two-stage Docker build process for optimized deployment
- Kubernetes deployment configuration
- Simple Flask web application for interacting with the model

This project demonstrates how to effectively containerize and deploy a large language model, addressing common challenges such as long build times and substantial resource requirements.