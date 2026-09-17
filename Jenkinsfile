pipeline {
    agent any

    parameters {
        booleanParam(
            name: 'RUN_EXTRA_CHECK',
            defaultValue: true,
            description: 'Run the extra validation stage'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Brama-G/assessment7-conditional-stage.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile exam_system.py'
                echo 'Build successful: exam_system.py compiled with no syntax errors.'
            }
        }

        stage('Extra Check') {
            when {
                expression { params.RUN_EXTRA_CHECK == true }
            }
            steps {
                echo 'Running extra check: validating question bank and scoring...'
                sh 'python3 test_exam.py'
            }
        }
    }
}
