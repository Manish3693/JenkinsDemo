pipeline {
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Manish3693/JenkinsDemo.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Prog.py"
                sh "./Prog.py"
            }
        }
        stage('Passing Test Code') {
            steps {
                sh "chmod u+x Pass_Tests.py"
                sh "./Pass_Tests.py"
            }
        }
        stage('Failing Test Code') {
            steps {
                sh "chmod u+x Fail_Tests.py"
                sh "./Fail_Tests.py"
            }
        }
    }
}
