CODE_CHANGES = getGitChanges()
pipeline {

    agent any   

    stages {

        stage("build") {
            when {
                expression {
                    BRANCH_NAME = "dev" && CODE_CHANGES == true
                }
            }
            // executing only if criteria above is reached
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
            when {
                expression {
                    BRANCH_NAME == "dev" || BRANCH_NAME = "main"
                }
            }
            // steps executing only if when expression is true
            // BRANCH_NAME = env var from jenkins
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

// Environmental Variables 
// jenkins -> localhost:8080/env-vars.htmls
// can also be defined 
// for credentials variables you need Credentials and Credentials Binding plugins

pipeline {
    agent any
    environment {
        NEW_VERSION = "1.3.0"
        SERVER_CREDENTIALS = credentials('credentialId')
    }
    stages {
        stage("test") {
            steps {
                echo "testing the application..."
                echo "build verions ${NEW_VERSION}"
            }
        }
        stage("build") {
            steps {
                echo "building the application..."
            }
        }
        stage("deploy") {
            steps {
                echo "deploying the application..."
                withCredentials([
                    usernamePassword("credentialsId", usernameVariable: USER, passwordVariable: PASSWORD)
                ]) {
                    sh "some script with credentials ${USER} ${PASSWORD}"
                }
            }
        }
    }
}

// access build tools 

pipeline {
    agent any
    tools {
        maven "Maven"
    }
    stages {
        stage("buid") {
            steps {
                echo "building..."
                sh "mvn install"
            }
        }
        stage("test") {
            steps {
                echo "testing..."
            }
        }
        stage("deploy") {
            steps {
                echo "deploying..."
            }
        }
    }
}

// parameters and functions
def gv 

pipeline {
    agent any
    parameters {
        string(name: "VERSION", defaultValue: "", description: "version to deploy on prod")
        choice(name: "VERSION", choices: ["1.1.0", "1.1.1"], description: "blahblah")
        booleanParam(name: "executeTests", defaultValue: true, description: "lala")
    }
    stages {
        stage("init") {
            steps {
                script {
                    // import a groovy function from another file
                    gv = load "script.groovy"
                }
            }
        }
        stage("build") {
            steps {
                script {
                    gv.buildApp()
                }
            }
        }
        stage("test") {
            when {
                expression {
                    // if executeTests is set to true, this will execute
                    params.executeTests == true 
                }
            }
            steps {
                script {
                    gv.testApp()
                }
            }
        }
        stage("deploy") {
            steps {
                script {
                    gv.deployApp()
                }
            }
        }
    }
}
