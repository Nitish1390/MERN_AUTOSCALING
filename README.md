# MERN Deployment Project

This project demonstrates the deployment of a MERN stack (MongoDB, Express, React, Node.js) application using AWS services, Jenkins for CI/CD, Docker for containerization, and Kubernetes (EKS) for orchestration.

# MERN Deployment Project

This project demonstrates the deployment of a MERN stack application using AWS services, Jenkins for CI/CD, Docker for containerization, and Kubernetes (EKS) for orchestration. 

#deployment_guide.md attached 


## Project Structure

- `frontend/`: Contains the React frontend application.
- `backend/`: Contains the Node.js backend application.
- `infrastructure/`: Contains scripts for setting up AWS infrastructure using Boto3.
- `lambda_functions/`: Contains AWS Lambda functions.
- `eks/`: Contains configuration for EKS cluster and Helm charts.
- `jenkins/`: Contains Jenkins configuration and job definitions.
- `docs/`: Contains documentation for the project.



## Project Structure

```plaintext
mern-deployment-project/
├── .gitignore
├── README.md
├── .vscode/
│   └── settings.json
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js
│       └── index.js
├── backend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│       ├── app.js
│       └── index.js
├── infrastructure/
│   ├── create_infrastructure.py
│   └── requirements.txt
├── lambda_functions/
│   └── backup_db/
│       ├── lambda_function.py
│       ├── requirements.txt
│       └── lambda_function.zip (not provided, would be generated)
├── eks/
│   ├── eksctl_config.yaml
│   └── helm_charts/
│       ├── frontend/
│       │   ├── Chart.yaml
│       │   ├── values.yaml
│       │   └── templates/
│       │       └── deployment.yaml
│       └── backend/
│           ├── Chart.yaml
│           ├── values.yaml
│           └── templates/
│               └── deployment.yaml
├── jenkins/
│   ├── Dockerfile
│   └── jenkins_jobs/
│       ├── build_and_push_docker_images.groovy
│       └── deploy_to_eks.groovy
├── docs/
│   ├── architecture.md
│   └── deployment_guide.md
