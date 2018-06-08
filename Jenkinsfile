pipeline {
  agent any
  options {
    disableConcurrentBuilds()
  }
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
        sh 'cp -f ${JENKINS_HOME}/jobs/click-count/branches/${GIT_BRANCH}/builds/${BUILD_NUMBER}/archive/target/*.war docker/runtime/'
        sh 'docker build -f docker/runtime/Dockerfile -t click-count-${GIT_BRANCH} docker/runtime'
        sh 'rm -f docker/runtime/*.war'
      }
    }
    stage('Staging') {
      steps {
        sh 'set +e; docker stop click-count-test-${GIT_BRANCH}; docker rm click-count-test-${GIT_BRANCH}; set -e'
        sh 'docker run -d  -p 8088:8080 -e XEBIA_CLICK_COUNT_REDIS_HOST=35.156.31.64 -e XEBIA_CLICK_COUNT_REDIS_PORT=6379  --name click-count-test-${GIT_BRANCH} click-count-${GIT_BRANCH}'
        sleep 5
      }
    }
    stage('Staging test') {
      steps {
        dir(path: 'APITest') {
          sh 'docker build -t click-count-api-test-${GIT_BRANCH} .'
        }

        sh 'docker run --rm --name click-count-api-test-${GIT_BRANCH} --env WEBAPP_ADDR="http://localhost" --env WEPAPP_PORT=8088 click-count-api-test-${GIT_BRANCH}'
      }
    }
    stage('Production') {
      when {
        branch 'master'
      }
      steps {
        sh 'set +e; docker stop click-count-${GIT_BRANCH}; docker rm click-count-${GIT_BRANCH}; set -e'
        sh 'docker run -d  -p 80:8080 -e XEBIA_CLICK_COUNT_REDIS_HOST=18.184.113.138 -e XEBIA_CLICK_COUNT_REDIS_PORT=6379  --name click-count-${GIT_BRANCH} click-count-${GIT_BRANCH}'
      }
    }
  }
}