pipeline {
    agent any
    stages {
        stage('Build Code') {
            steps {
                sh "chmod u+x Code.py"
                sh "./Code.py"
            }
        }
        stage('Passed Testcases') {
            steps {
                sh "chmod u+x Pass.py"
                sh "./Pass.py"
            }
        }
        stage('Failed Testcases') {
            steps {
                sh "chmod u+x Fail.py"
                sh "./Fail.py"
            }
        }
    }
}
