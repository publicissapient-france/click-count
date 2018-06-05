pipeline {
  agent any
  stages {
    stage('Build') {
      agent {
        docker {
          image 'maven:3-alpine'
          args '-v /root/.m2:/root/.m2'
        }

      }
      steps {
        sh 'mvn clean package'
      }
    }
    stage('Package') {
      steps {
        sh 'docker build -f docker/runtime/Dockerfile -t click-count target'
      }
    }
  }
}