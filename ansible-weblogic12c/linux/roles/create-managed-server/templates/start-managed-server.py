#####connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}')
#####start('{{ managed_server_name }}')
######## Det verkar vara problem iom att det är plan text authentication ...
######## WLSTException: Error occurred while performing nmConnect : Cannot connect to Node Manager. : Unrecognized SSL message, plaintext connection?
nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', '{{ node_manager_address }}', '{{ node_manager_port }}', '{{ domain_name }}');
nmStart('{{ managed_server_name }}');
nmDisconnect();
