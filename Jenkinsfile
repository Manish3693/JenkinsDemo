pipeline {
    agent any
    stages {
        stage('Build Code') {
            steps {
                sh "chmod u+x Main_func.py"
                sh "./Main_func.py"
            }
        }
        stage('Passed Testcases') {
            steps {
                sh "chmod u+x Pass_Tests.py"
                sh "./Pass_Tests.py"
            }
        }
        stage('Failed Testcases') {
            steps {
                sh "chmod u+x Fail_Tests.py"
                sh "./Fail_Tests.py"
            }
        }
    }
}
