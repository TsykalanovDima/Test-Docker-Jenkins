pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/TsykalanovDima/Test_0.git']]])
            }
        }
        
        stage('Build and Test in Container') {
            steps {
                script {
                    docker.build("my-test-container")
                    docker.image("my-test-container").withRun("-v /Users/dimatsy/PycharmProjects/pythonProject5/Test_0:/app") {
                        sh "pytest Test_0.py --alluredir=./allure-results"
                    }
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    sh "allure generate /app/allure-results --clean -o /Users/dimatsy/PycharmProjects/pythonProject5/Test_0/allure-report"
                }
            }
        }
    }
    
    post {
        always {
            emailext attachLog: true,
                    subject: "Test Results",
                    body: "Find the attached test results and Allure report.",
                    attachmentsPattern: '**/allure-report/**',
                    recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                    to: 'tsykalanovdima@gmail.com' // Ваша электронная почта
        }
    }
}
