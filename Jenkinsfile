pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/StefanIancu/jenkins-ci.git']]])
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