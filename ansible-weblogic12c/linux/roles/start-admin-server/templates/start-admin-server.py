nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', '{{ node_manager_address }}', '{{ node_manager_port }}', '{{ domain_name }}');
nmStart('{{ admin_server_name }}');

nmDisconnect();
