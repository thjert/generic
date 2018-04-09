ADMIN_SERVER_URL = 't3://' + '{{ admin_server_address }}' + ':' + '{{ admin_server_port }}';
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL)
start('{{ managed_server_name }}')
disconnect();
