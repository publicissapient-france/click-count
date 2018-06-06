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
    stage('Staging deployment') {
      steps {
        sh 'docker run -d  -p 8088:8080 -e XEBIA_CLICK_COUNT_REDIS_HOST=35.156.31.64 -e XEBIA_CLICK_COUNT_REDIS_PORT=6379  --name click-count-test click-count'
      }
    }
    stage('Staging test') {
      steps {
        dir(path: 'APITest') {
          sh 'docker build -t click-count-api-test .'
        }

        sh 'docker run --rm --name click-count-api-test click-count-api-test'
      }
    }
  }
}