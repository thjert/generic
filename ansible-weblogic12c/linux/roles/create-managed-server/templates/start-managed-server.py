connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}')
start('{{ managed_server_name }}')

# nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', '{{ node_manager_address }}', '{{ node_manager_port }}', '{{ domain_name }}');
# nmStart('{{ managed_server_name }}');
# nmDisconnect();
