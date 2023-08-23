pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    def creds = credentials('github-token')
                    checkout([$class: 'GitSCM', userRemoteConfigs: [[url: 'https://github.com/TsykalanovDima/Test_0.git']], branches: [[name: '*/master']], extensions: [[$class: 'GitLFSPull']], userRemoteConfigs: [[credentialsId: creds.id]]])
                }
            }
        }
        
        stage('Build and Test in Container') {
            steps {
                script {
                    docker.image("python:3.9").inside("-v ${PWD}:/app") {
                        sh "pip install -r requirements.txt"
                        sh "pytest Test_0.py --alluredir=./allure-results"
                    }
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                sh "allure generate ./allure-results --clean -o ./allure-report"
            }
        }
    }
}
