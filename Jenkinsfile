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
        stage('Pass Testcases') {
            steps {
                sh "chmod u+x Pass.py"
                sh "./Pass.py"
            }
        }
        stage('Fail Testcases') {
            steps {
                sh "chmod u+x Fail.py"
                sh "./Fail.py"
            }
        }
    }
}
