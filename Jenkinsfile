pipeline {

    agent any   

    stages {

        stage("build") {

            steps {
                echo "building the application..."
                echo "Application built"
            }
        }

         stage('Containerize') {
            steps {
                // Build a Docker image
                script {
                    def imageName = "database_image"
                    def imageTag = "${env.BUILD_NUMBER}"
                    
                    sh "docker build -t ${imageName}:${imageTag} ."
                }
            }
        }
        
        stage('Publish') {
            steps {
                // Publish the Docker image to a registry (replace with your Docker registry information)
                script {
                    def imageName = "database_image"
                    def imageTag = "${env.BUILD_NUMBER}"
                    def registryURL = "stefaniancu/database"
                    
                    sh "docker login -u <username> -p <password> ${registryURL}"
                    sh "docker tag ${imageName}:${imageTag} ${registryURL}/${imageName}:${imageTag}"
                    sh "docker push ${registryURL}/${imageName}:${imageTag}"
                }
            }
        }

        stage("test") {

            steps {
                echo "testing the application..."
            }
        }    

        stage("deploy") {

            steps {
                echo "deploying the application..."
            }
        }
    }
    post {
        // after all the stages are done, post is executing 
        always {
            // executing always, no matter the status of the build 
        }
        success {
            // executing if the build succeded
        }
        failure {
            // executing if the build failed
        }    
    }
}
