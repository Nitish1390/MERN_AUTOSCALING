pipeline {
    agent any
    environment {
        ECR_REGISTRY = 'your-account-id.dkr.ecr.your-region.amazonaws.com'
        ECR_REPOSITORY_FRONTEND = 'frontend'
        ECR_REPOSITORY_BACKEND = 'backend'
        IMAGE_TAG = "latest"
    }
    stages {
        stage('Checkout') {
            steps {
                git 'codecommit://my-repo-url'
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    docker.build("${ECR_REGISTRY}/${ECR_REPOSITORY_FRONTEND}:${IMAGE_TAG}", 'frontend')
                    docker.build("${ECR_REGISTRY}/${ECR_REPOSITORY_BACKEND}:${IMAGE_TAG}", 'backend')
                }
            }
        }
        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry("https://${ECR_REGISTRY}") {
                        docker.image("${ECR_REGISTRY}/${ECR_REPOSITORY_FRONTEND}:${IMAGE_TAG}").push()
                        docker.image("${ECR_REGISTRY}/${ECR_REPOSITORY_BACKEND}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
    }
}
