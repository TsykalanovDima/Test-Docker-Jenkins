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
                    docker.image('dima_1:latest').inside('--privileged') {
                        sh 'pytest -s /app/Test_0.py'
                        
                        // Установка Allure
                        sh 'apt-get update && apt-get install -y allure'
                        
                        // Генерация и открытие отчетов Allure
                        sh 'allure generate /app/allure-results -o /app/allure-report --clean'
                        sh 'allure open /app/allure-report'
                    }
                }
            }
        }
    }
}
