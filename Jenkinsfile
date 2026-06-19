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
                echo 'Deploying to staging server'
            }
        }
    }
}