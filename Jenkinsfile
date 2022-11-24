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
                sh "chmod u+x Code.py"
                sh "./Code.py"
            }
        }
        stage('Pass Testcases') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    }
}
