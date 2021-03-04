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
                  stage('rest_app.py') {
            steps {
                script {
                    bat 'start /min python rest_app.py'
                    bat 'echo success dockker'
                }
            }
        }
        stage('Backend_testing') {
            steps {
                script {
                    bat 'python3 Backend_testing.py'
                    bat 'echo success Backend_testing'
                }
            }
        }
        stage('clean_environemnt') {
            steps {
                script {
                    bat 'start/min python3 clean_environemnt.py'
                    bat 'echo success clean_environemnt'
                   }
            }
        }
        stage ('Build Docker image - locally'){
            steps {
                script{
                    bat "docker build -t \"$BUILD_NUMBER\" ."
                    bat "start/min docker run \"$BUILD_NUMBER\""
                }
            }
        }
        stage('build and push image') { 	
            steps { 	
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {	
                    dockerImage.push() 	
                    }	
                }  	
            }	
        }	
        stage('set version') { 	
            steps {	
                bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"   
			    bat "more .env"
            }	
         }
        stage ('docker'){
            steps {
                script{
                    bat 'docker-compose up -d'
                    bat 'echo hellp'
                    }
                }
           }       
        stage ('docker_backend_testing'){
            steps{
                script{
                    bat 'python3 docker_backend_testing.py'
                    bat 'echo success docker_backend_testing.py'
                    }
                }
            }
        stage('docker-compose down & delete image') { 
            steps {
                script{
                bat 'docker-compose down '
                bat "docker image rm  ${BUILD_NUMBER}"      		
                bat 'echo docker-compose down + delete image'
		bat 'start/min python3 clean_environemnt.py'
                }
            }
        }  
	stage ('Deploy HELM'){
            steps{
                script{
		    bat 'minikube start'
                    bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/lior/templates/deployment.yaml'
	            bat 'kubectl get deployments'
	            bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/lior/templates/service.yaml'
                    bat 'echo succes HELM.py'
	            bat 'start/min minikube service hello-python-service --url'
                    }
                }
            }
        }
  post {	
      always {	
             bat "docker rmi $registry:${BUILD_NUMBER}"	
          }	
  }
}
