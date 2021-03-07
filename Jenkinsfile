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
         stage ('Deploy HM'){
            steps{
                script{
                    bat 'cd project-helm'
		    bat	'helm install project-4 --dry-run  --debug --set image.repostitory=photop33/Project3,image.tag=${BUILD_NUMBER} project-helm'
		    bat 'helm repo update'
		    bat 'helm list --all'
		    }  
                }
            }
	 stage ('Deploy HELM'){
            steps{
                script{
                   bat """ start /min /b minikube service project-4-lior --url >  k8s_url-test.txt
		   ping -n 10 127.0.0.1 
                   (type  k8s_url-test.txt | findstr "^http") >  k8s_url.txt
                    type k8s_url.txt """		   
		    }  
                }
            }
	stage ('push git k8s_url.txt'){
	    steps{
                script{
		    bat 'git commit -m "First commit"'
		    bat 'git push origin main'
		   }
                }
	    }
	stage ('K8S_backend_testing.py'){
	    steps{
                script{
		    bat 'python3 K8S_backend_testing.py'
		    bat 'echo succes K8S_backend_testing.py'
		   }
                }
	    }
        }
 }

