pipeline {
    agent any
    stages {
        stage('Deploy to EKS') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_CONTENT')]) {
                        sh 'echo "$KUBECONFIG_CONTENT" > kubeconfig'
                        sh 'kubectl apply -f eks/helm_charts/frontend/templates/deployment.yaml --kubeconfig kubeconfig'
                        sh 'kubectl apply -f eks/helm_charts/backend/templates/deployment.yaml --kubeconfig kubeconfig'
                    }
                }
            }
        }
    }
}
