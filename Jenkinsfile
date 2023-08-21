pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/StefanIancu/jenkins-ci.git', credentialsId: '3ec7a612-3cd6-4b8d-bd1b-270d108a69f9']]])
                }
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("stefaniancu/qr_gen:${env.BUILD_ID}")
                    dockerImage.push()
                }
            }
        }
    }
}