ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

edit();
startEdit();
# applyJRF(target='{{ managed_server_name }}', domainDir='{{ domain_home }}');
cd('/')

try: cmo.createMachine('{{ managed_server_address }}')
except Exception:
    print "Machine already exists"

cd('/Machines/' + '{{ managed_server_address }}' + '/NodeManager/' + '{{ managed_server_address }}')
cmo.setListenAddress('{{ node_manager_address }}')
cmo.setListenPort('{{ node_manager_port }}')
cmo.setNMType('{{ node_manager_type }}')

cd('/')
cmo.createServer('{{ managed_server_name }}')

cd('/Servers/' + '{{ managed_server_name }}')
cmo.setListenAddress('{{ managed_server_address }}')
cmo.setListenPort({{ managed_server_port }})
cmo.setMachine(getMBean('/Machines/' + '{{ managed_server_address }}'))
#
cd('/')

#
# Temporärt ligger det här får flyttas senare när det fungerar ...
#
cd('/Servers/' + '{{ admin_server_name }}')
#####cmo.setListenAddress('{{ admin_server_address }}')
#####cmo.setListenPort({{ admin_server_port }})
cmo.setMachine(getMBean('/Machines/' + '{{ admin_server_address }}'))

# applyJRF(target='{{ managed_server_name }}', domainDir='{{ domain_home }}');

# applyJRF wil call save and activate
save();
activate(block='true');

# Pga problem med att få upp allting efter den första starten som görs i samband med installationen provar jag med att hårdkoda och lägga in detta.
nmGenBootStartupProps('{{ admin_server_name }}');
nmGenBootStartupProps('{{ managed_server_name }}');

disconnect();
