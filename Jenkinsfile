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
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\rest_app.py'
                    bat 'echo success rest_app'

                }
            }
        }
        stage('Backend_testing') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\project1\\Backend_testing.py'
                    bat 'echo success Backend_testing'
                }
            }
        }
        stage('clean_environemnt') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\clean_environemnt.py'
                    bat 'echo success clean_environemnt'
                }
            }
        }
        stage('Build') {
             steps {
                sh 'mvn -B'
                }
             }
        }
    }
}


node {
      def app
      stage('Clone repository') {

            checkout scm
      }
      stage('Build image') {

            app = docker.build("brandonjones085/test")
       }
      stage('Test image') {
            app.inside {

             sh 'echo "Tests passed"'
            }
        }
       stage('Push image') {
                                                  docker.withRegistry('https://hub.docker.com/repository/docker/photop/my-repo', 'git') {
       app.push("${env.BUILD_NUMBER}")
       app.push("latest")
              }
           }
        }

pipeline {
    agent any
    stage('Running Docker Container') {
        steps {
         bat " "docker-compose up -d""
         }
    }
    stage('rest_app') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\docker_backend_testing.py'
                    bat 'docker_backend_testing.py'

                }
            }
        }
        stage('clean_environment') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\project1\\clean_environment.py'
                    bat 'echo success clean_environment'
                }
            }
        }
}
