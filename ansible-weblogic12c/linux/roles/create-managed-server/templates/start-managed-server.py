###Raderna nedanför är från den som var innan installationen som påbörjades efter 10:05 2018-04-03
###ADMIN_SERVER_URL = 't3://' + '192.168.56.14' + ':' + '7001';
###connect('weblogic', 'welcome1', ADMIN_SERVER_URL);

###connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}')
###start('{{ managed_server_name }}')

nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', '{{ node_manager_address }}', '{{ node_manager_port }}', '{{ domain_name }}');
nmStart('{{ managed_server_name }}');
nmDisconnect();
