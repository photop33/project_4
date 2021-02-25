pipeline { 
    environment { 
        registry = "photop/project-3" 
        registryCredential = 'docker_hub' 
       dockerImage = "
    } 
         stage('build and push image') { 
            steps { 
                script { 
                    dockerImage = project + ":$1" 
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push() 
                          }
                     }
                }
            }
        }
    agent any
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

        stage('make env file') { 
            steps {

                     bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
                  post {
                  always {

                          bat "docker rmi $registry:$1“ 

        stage('Deploy our image') { 
            steps { 
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                } 
            }
        } 
        stage('make env file') { 
            steps {
                     bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
                  post {
                  always {

                          bat "docker rmi $registry:$1“ 
                      }
                  }
       stage('docker run ') {
            steps {
                script {
                    bat 'docker run shalom'
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

    }
}

 


