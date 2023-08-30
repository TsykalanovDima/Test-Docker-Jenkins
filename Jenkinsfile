pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Сборка Docker-образа
                    def dockerImage = docker.build('dima_1')
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                // Запуск тестов внутри контейнера
                sh 'docker run -it --rm dima_1'
            }
        }
    }
}
