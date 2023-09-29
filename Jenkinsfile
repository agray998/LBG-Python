pipeline {
    environment {
        PORT = 9000
    }
    agent any
    stages {
        stage('build image') {
            steps {
                sh '''
                docker build -t gcr.io/lbg-mea-14/ag-lbg-python-api:v${BUILD_NUMBER} .
                docker tag gcr.io/lbg-mea-14/ag-lbg-python-api:v${BUILD_NUMBER} gcr.io/lbg-mea-14/ag-lbg-python-api
                '''
            }
        }
        stage('run unit tests') {
            steps {
                sh '''
                pip3 install -r requirements.txt
                ./deploy.sh
                python3 lbg.test.py
                '''
            }
        }
        stage('push image') {
            steps {
                sh '''
                docker push gcr.io/lbg-mea-14/ag-lbg-python-api:v${BUILD_NUMBER}
                docker push gcr.io/lbg-mea-14/ag-lbg-python-api
                '''
            }
        }
        stage('cleanup jenkins') {
            steps {
                sh '''
                docker stop sample-app \
                && (docker rm sample-app) \
                || (docker rm sample-app && sleep 1 || sleep 1)
                docker rmi gcr.io/lbg-mea-14/ag-lbg-python-api
                docker rmi gcr.io/lbg-mea-14/ag-lbg-python-api:v${BUILD_NUMBER}
                '''
            }
        }
        stage('deploy') {
            steps {
                sh '''
                ssh jenkins@agray-appserver < deploy.sh
                '''
            }
        }
    }
}