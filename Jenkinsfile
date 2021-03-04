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
