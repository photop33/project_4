pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
                git 'https://github.com/photop33/project3.git'
            }
        }
        stage('rest_app') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\rest_app.py'
                    bat 'echo success rest_app'
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
        stage('IMAGE dockerfile') {
            steps {
                script {
                    bat 'docker build -t shalom .'
                    bat 'echo success IMAGE'
                }
           }
       }
       stage('docker run ') {
            steps {
                script {
                    bat 'docker run -d -p 80:88 --name KING shalom'
                    bat 'echo success dockker'
                }
            }
       }
    }
}

 


