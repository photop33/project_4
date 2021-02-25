pipeline { 
    agent any

    environment { 
        registry = "photop/project-3" 
        registryCredential = 'docker_hub' 
        dockerImage =''
    } 
    stages {
        stage('properties') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
                git 'https://github.com/photop33/project3.git'
            }
        }     
        stage('rest_app.py') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\3\\rest_app.py'
                    bat 'echo success dockker'
                }
            }
        }
        stage('Backend_testing') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\3\\Backend_testing.py'
                    bat 'echo success Backend_testing'
                }
            }
        }
        stage('clean_environemnt') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\clean_environemnt.py'
                    bat 'echo success clean_environemnt'
                   }
            }
        }
        stage('build and push image') { 
            steps { 
                script { 
                    dockerImage = "project" + "${n1}"
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push() 
                        }
                     }
                }
        }
    }
    post {
        always {
            bat "docker rmi $registry:${n1}" 
            bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
            bat 'docker compuse up -d'
            bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\clean_environemnt.py'
            bat 'echo success clean_environemnt'                    
        } 
    }
}
