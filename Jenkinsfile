pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'my-test-container'
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    def creds = credentials('github-credentials')
                    checkout([$class: 'GitSCM', userRemoteConfigs: [[url: 'git@github.com:TsykalanovDima/Test_0.git', credentialsId: creds.id]], branches: [[name: '*/main']]])
                }
            }
        }
        
        stage('Build and Test in Container') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                    docker.image(DOCKER_IMAGE).withRun('-v /Users/dimatsy/PycharmProjects/pythonProject5/Test_0:/app') {
                        sh "pytest"
                    }
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    sh "docker run --rm -v /Users/dimatsy/PycharmProjects/pythonProject5/Test_0:/app ${DOCKER_IMAGE} allure generate /app/allure-results --clean -o /app/allure-report"
                }
            }
        }
    }
}
