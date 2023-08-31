pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t dima_1 .'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def allurePath = sh(script: 'which allure', returnStdout: true).trim()
                    
                    docker.image('dima_1:latest').inside('--privileged') {
                        sh 'pytest -s /app/Test_0.py'
                        
                        sh 'apt-get update && apt-get install -y allure'
                        
                        // Генерация и открытие отчетов Allure с использованием полного пути
                        sh "${allurePath} generate /app/allure-results -o /app/allure-report --clean"
                        sh "${allurePath} open /app/allure-report"
                    }
                }
            }
        }
    }
}
