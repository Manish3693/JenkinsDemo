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
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    }
}
