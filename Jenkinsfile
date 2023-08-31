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
        
        stage('Run Tests and Generate Allure Report') {
            steps {
                script {
                    def container = docker.image('dima_1:latest').inside {
                        return containerName // Get the container ID or name
                    }
                    
                    sh "pytest -s /app/Test_0.py"
                    
                    sh "allure generate /app/Test_0/allure-results -o /app/Test_0/allure-report --clean"
                    
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: '/app/Test_0/allure-report',
                        reportFiles: 'index.html',
                        reportName: 'Allure Report'
                    ])
                }
            }
        }
    }
}
