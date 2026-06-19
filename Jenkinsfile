pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub'
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-task-app .'
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh '''
                docker save flask-task-app > flask-task-app.tar

                scp -o StrictHostKeyChecking=no flask-task-app.tar ubuntu@3.66.157.209:/home/ubuntu/

                ssh -o StrictHostKeyChecking=no ubuntu@3.66.157.209 "
                docker load < /home/ubuntu/flask-task-app.tar &&
                docker stop flask-task-app || true &&
                docker rm flask-task-app || true &&
                docker run -d --name flask-task-app -p 5000:5000 flask-task-app
                "
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}