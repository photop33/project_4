pipeline { 
    agent any

    environment { 
        registry = "photop/project-3" 
        registryCredential = 'docker_hub'
        dockerImage = ""
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
        stage('build and push image') { 	
            steps { 	
                script {
                    bat "echo ${registry}:${BUILD_NUMBER}"
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    bat "echo ${dockerImage}"
                    docker.withRegistry('', registryCredential) {	
                    dockerImage.push() 	
                    }	
                }  	
            }	
        }	
        stage('set version') { 	
            steps {	
                bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"      		
            }	
         }
        stage ('docker compose'){
            steps {
                script{
                    bat 'docker-compose up -d'
                    bat 'echo docker compuse up'
                    }
                }
           }       
        stage ('docker_backend_testing'){
            steps{
                script{
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\docker_backend_testing.py'
                    bat 'echo success docker_backend_testing.py'
                    }
                }
            }
        stage ('clen'){
            steps{
                script{
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\clean_environemnt.py'
                    bat 'echo success clean_environemnt'
                }
            }
        }
    }
  post {	
      always {	
             bat "docker images"	
             bat "docker rmi $registry:${1}"	
          }	
  }
}
