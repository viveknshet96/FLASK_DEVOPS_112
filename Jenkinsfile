pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/viveknshet96/FLASK_DEVOPS_112.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t flask-swarm-app:1.0 .'
            }
        }

        stage('Deploy to Docker Swarm') {
            steps {
                sh '''
                docker service rm flask-swarm-service || true

                docker service create \
                  --name flask-swarm-service \
                  -p 5000:5000 \
                  flask-swarm-app:1.0
                '''
            }
        }
    }
}
