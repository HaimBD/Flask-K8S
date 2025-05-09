pipeline {
	
	agent any

	
	stages {
		stage('Login to docker') {
			steps {
				withCredentials([
					string(credentialsId: 'Docker_User', variable: 'DOCKER_USER'),
					string(credentialsId: 'Docker_Pass', variable: 'DOCKER_PASS'),
					string(credentialsId: 'Repository_Name', variable: 'REPOSITORY_NAME')
					])
				{
					sh '''
					#!/bin/bash
					set -e
					echo "${DOCKER_PASS}" | docker login -u "${DOCKER_USER}" --password-stdin 
					docker build -t "${REPOSITORY_NAME}":"${BUILD_NUMBER}" app/.
					docker image tag "${REPOSITORY_NAME}":"${BUILD_NUMBER}" "${DOCKER_USER}"/"${REPOSITORY_NAME}":"${BUILD_NUMBER}"
					docker push "${DOCKER_USER}"/"${REPOSITORY_NAME}":"${BUILD_NUMBER}"
					'''
					
					}
				}

			}
		}	
	post {
	// Clean after build
	always {
		cleanWs(cleanWhenNotBuilt: false,
			deleteDirs: true,
			disableDeferredWipeout: true,
			notFailBuild: true,
			patterns: [[pattern: '.gitignore', type: 'INCLUDE']])
            sh 'docker system prune -a -f --filter "until=24h"'
            sh 'echo Adding this...........'
		}
	}
}
					
