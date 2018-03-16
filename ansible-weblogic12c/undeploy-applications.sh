#! /bin/bash

ansible-playbook -v wls-deploy-applications.yml --extra-vars "deploy_action=undeploy"
