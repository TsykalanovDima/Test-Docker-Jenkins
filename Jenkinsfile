pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Выполнить проверку кода из репозитория
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Сборка Docker-образа
                sh 'docker build -t dima_1 .'
            }
        }
        stage('Run Tests') {
            steps {
                // Запуск тестов внутри контейнера
                script {
                    docker.image('dima_1:latest').inside {
                        sh 'pytest -s /app/Test_0.py'
                    }
               }
            }
        }
        stage('Generate Allure Reports') {
            steps {
                // Генерация отчетов Allure
                sh 'allure generate /app/allure-results -o /app/allure-report --clean'
            }
        }
        stage('Send Email') {
            steps {
                script {
                    emailext body: '''<html><body>Здесь может быть текст вашего письма с ссылкой на Allure отчет.</body></html>''',
                        subject: 'Отчет Allure',
                        mimeType: 'text/html',
                        to: 'tsykalanovdima@gmail.com',
                        attachmentsPattern: '**/allure-report/*'
                }
            }
        }
    }
}
