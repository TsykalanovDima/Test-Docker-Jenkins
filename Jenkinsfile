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
                    docker.image('dima_1:latest').inside {
                        sh 'pytest -s /app/Test_0.py'
                    }
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    sh 'curl -o allure-2.14.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.tgz'
                    sh 'tar -zxvf allure-2.14.0.tgz -C /opt/'
                    sh 'allure generate /app/Test_0/allure-results -o /app/Test_0/allure-report --clean'
                }
            }
        }
        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: '/app/Test_0/allure-results']],
                    reportBuildPolicy: 'ALWAYS',
                    report: 'allure-report'
                ])
            }
        }
    }
}
