pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials-id' // Replace with Jenkins credential ID
        DOCKERHUB_USERNAME = 'pragya1401'     // Replace with your Docker Hub username
        IMAGE_NAME = 'diamond-price-app'
        IMAGE_TAG = 'latest'
        FULL_IMAGE_NAME = "${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
        CONTAINER_NAME = 'diamond-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch:'main', url:'https://github.com/PragyaChauhan1401/Diamond-price-prediction.git' // Replace with your repo
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${FULL_IMAGE_NAME} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) 
                {
                    bat '''
                        docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                        docker push %FULL_IMAGE_NAME%
                        docker logout
                    '''
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                    docker rm -f %CONTAINER_NAME% || true
                    docker run -d -p 8501:8501 --name %CONTAINER_NAME% %FULL_IMAGE_NAME%
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline executed successfully!'
        }
        failure {
            echo 'CI/CD pipeline failed. Please check the logs!'
        }
    }
}
