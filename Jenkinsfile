pipeline {
agent none
stages {
    stage('Build') {
        agent {
            docker {
                image 'python:2-alpine'
            
            }
        }
        steps {
            sh 'python -m py_compile variables.py'
            stash(name: 'compiled-results',includes: 'sources/*.py*')
    
          }
      }  
  }
  }
