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
        archiveArtifacts(artifacts: 'target/clickCount.war', caseSensitive: true)
      }
    }
    stage('Package') {
      steps {
        sh 'cp ${JENKINS_HOME}/jobs/click-count/branches/${GIT_BRANCH}/builds/${BUILD_NUMBER}/archive/target/*.war docker/runtime/'
        sh 'docker build -f docker/runtime/Dockerfile -t click-count docker/runtime'
        sh 'rm -f docker/runtime/*.war'
      }
    }
  }
}