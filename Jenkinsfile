pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
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