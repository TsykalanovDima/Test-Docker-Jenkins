pipeline {
    agent any
    
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            steps {
                script {
                    docker.build("dima_1")
                    def container = docker.image("dima_1").run("-v /app/Test_0.py:/app/Test_0.py dima_1")
                    try {
                        sh 'pytest -s /app/Test_0.py'
                    } finally {
                        container.stop()
                    }
                }
            }
        }
        
        stage('Generate and Display Allure Report') {
            steps {
                script {
                    sh 'allure generate -c /var/jenkins_home/workspace/Pros/allure-results -o /var/jenkins_home/workspace/Pros/allure-report'
                    sh 'allure open /var/jenkins_home/workspace/Pros/allure-report'
                }
            }
        }
    }
}
