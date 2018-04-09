nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', '{{ node_manager_address }}', '{{ node_manager_port }}', '{{ domain_name }}','{{ domain_home }}', '{{ node_manager_type }}');
nmStart('{{ admin_server_name }}');

nmDisconnect();
