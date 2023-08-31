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
                    def containerId = sh(script: "docker run -d dima_1:latest", returnStdout: true).trim()
                    try {
                        sh "docker exec ${containerId} pytest -s /app/Test_0.py"
                        
                        sh "docker exec ${containerId} allure generate /app/Test_0/allure-results -o /app/Test_0/allure-report --clean"
                        
                        publishHTML([
                            allowMissing: false,
                            alwaysLinkToLastBuild: true,
                            keepAll: true,
                            reportDir: '/app/Test_0/allure-report',
                            reportFiles: 'index.html',
                            reportName: 'Allure Report'
                        ])
                    } finally {
                        sh "docker stop ${containerId}"
                    }
                }
            }
        }
    }
}
