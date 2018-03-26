#nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', '{{ node_manager_listen_address }}', '{{ node_manager_listen_port }}', '{{ domain_name }}');
#nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', '192.168.108.110', '{{ node_manager_listen_port }}', '{{ domain_name }}');
nmConnect('weblogic', '{{ nodemanager_password }}', '192.168.108.110', '{{ node_manager_listen_port }}', '{{ domain_name }}');
#nmConnect('{{ nodemanager_username }}', '{{ nodemanager_password }}', 'localhost', '{{ node_manager_listen_port }}', '{{ domain_name }}');
nmStart('{{ admin_server_name }}');

nmDisconnect();
