pipeline {
    agent {
        label 'test'
    }
    stages {
        stage('Clone simple-api repository') {
            steps {
                git url: 'https://github.com/nichaOrg/simple-api-registry.git', branch: 'main'
            }
        }

        stage('Build and Test API') {
            steps {
                script {
                    // Build and test API
                    
                    // sh 'pip install -r requirements.txt' // Install dependencies
                    sh 'pip install --no-cache-dir --upgrade -r requirements.txt'
                    sh 'python3 app.py'
                    
                    // sh 'sleep 5' // Wait for API to start

                    // Run unit tests
                    sh 'python3 test_unit.py'
                }
            }
        }
        stage('Create Images of Simple API') {
            steps {
                sh 'docker stop simple-api-container | true'
                sh 'docker rm simple-api-container | true'
                sh 'docker build -t simple-api .'
            // Build Docker image using provided Dockerfile
            }
        }
        stage('Create Container of Simple API') {
            steps {
                sh 'docker run -d -p 5000:5000 --name simple-api-container simple-api'
            // Create Docker container from the built image
            }
        }

         stage('Build and Test Robot Framework') {
            steps {
                script {
                    dir('./robot3/') {
                        git url: 'https://github.com/nichaOrg/simple-api-robot-registry.git', branch: 'main'
                    }
                    sh 'cd ./robot3 && robot test_robot.robot'
                }
            }
        }

         // Build and push image to GitHub Container Registry
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Authenticate to GitHub Container Registry
                    withCredentials([string(credentialsId: 'my-github-token', variable: 'GITHUB_TOKEN')]) {
                        sh 'echo $GITHUB_TOKEN | docker login ghcr.io -u Horiiya --password-stdin'
                    }

                    // Build and tag the Docker image
                    sh 'docker build -t ghcr.io/horiiya/simple-api-registry:latest .'

                    // Push the image to GitHub Container Registry
                    sh 'docker push ghcr.io/horiiya/simple-api-registry:latest'
                }
            }
        }

        stage('Running Preprod') {
            agent {
                label 'preprod'
            }
            steps {
                script {
                // เข้าสู่ระบบ GitHub Container Registry
                withCredentials([string(credentialsId: 'my-github-token', variable: 'GITHUB_TOKEN')]) {
                    sh 'echo $GITHUB_TOKEN | docker login ghcr.io -u Horiiya --password-stdin'
                }

                // ดึงภาพจาก GitHub Container Registry
                sh 'docker pull ghcr.io/horiiya/simple-api-registry:latest'

                // นำขึ้นคอนเทนเนอร์ด้วยภาพที่ดึงมา
                sh 'docker compose down && docker system prune -a -f && docker compose up -d --build'
                }
            }
        }
    }
}
