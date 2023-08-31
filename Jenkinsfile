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
            script {
                sh 'docker run --rm -v /app/Test_0/allure-results:/allure-results -v /app/Test_0/allure-report:/allure-report allure-framework/allure-docker:latest generate /allure-results -o /allure-report --clean'
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
