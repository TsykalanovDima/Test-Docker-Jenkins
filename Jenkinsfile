pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build('dima_1')
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'docker run -it --rm dima_1 pytest -s /app/Test_0.py'
            }
        }
    }
}
