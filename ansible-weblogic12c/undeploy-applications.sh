#! /bin/bash

ansible-playbook -v deploy_applications.yml --extra-vars "deploy_action=undeploy"
