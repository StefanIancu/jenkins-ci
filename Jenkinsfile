pipeline {
    agent any
    stages {
        /* "Build" and "Test" stages omitted */

        stage('Deploy - Staging') {
            steps {
                echo "deploying - staging"
            }
        }

        stage('Sanity check') {
            steps {
                input "Does the staging environment look ok?"
            }
        }

        stage('Deploy - Production') {
            succes {
              echo "deploying to production..."
            }
        }
    }
    post {
        echo "pipeline finished"
    }
}
