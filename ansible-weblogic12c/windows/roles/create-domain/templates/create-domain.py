domain_name = '{{ domain_name }}';
weblogic_home = '{{ weblogic_home }}';
domain_application_home = '{{ applications_home }}/{{ domain_name }}';
domain_configuration_home = '{{ domains_home }}/{{ domain_name }}';
node_manager_home = '{{ nodemanager_home }}';
java_home = '{{ jdk_folder }}';
middleware_home = '{{ middleware_home }}';
#weblogic_template = weblogic_home + '/common/templates/wls/wls.jar';
weblogic_template = '{{ oracle_base }}' + '/common/templates/domains/wls.jar';

### Används ej Thomas Hjert - em_template=middleware_home + '/em/common/templates/wls/oracle.em_wls_template.jar';

# Load the default domain template
readTemplate(weblogic_template);
#
setOption('DomainName', domain_name);
setOption('OverwriteDomain', 'true');
setOption('ServerStartMode', 'prod');
cd('/Security/base_domain/User/weblogic');
cmo.setName('{{ weblogic_admin }}');
cmo.setUserPassword('{{ weblogic_admin_pass }}');

cd('/');

print "Save domain";

writeDomain(domain_configuration_home);
closeTemplate();

print 'Read domain ';
readDomain(domain_configuration_home);

print 'Add Template';
# addTemplate(em_template);
# Ställer troligtvis till det ...
# setOption('AppDir', domain_application_home);

cd("/SecurityConfiguration/" + domain_name);
cmo.setNodeManagerUsername('{{ nodemanager_username }}');
cmo.setNodeManagerPasswordEncrypted('{{ nodemanager_password }}');

cd('/Server/' + '{{ admin_server_name }}');
set ('ListenPort', {{ admin_server_port }});

try:
  create('{{ admin_server_name }}','SSL');
except ValueError:
  print "SSL already exist, skipping ..."

cd('SSL/' + '{{ admin_server_name }}');
set ('Enabled', 'True');
set ('ListenPort', {{ admin_server_port_ssl }});
cmo.setHostnameVerificationIgnored(true);
cmo.setHostnameVerifier(None);
cmo.setTwoWaySSLEnabled(false);
cmo.setClientCertificateEnforced(false);

cd('/SecurityConfiguration/'+ domain_name +'/Realms/myrealm');
### Thomas Hjert - DefaultAuthenticator finns ej, måste skapas OM den absolut behövs.
###cd('AuthenticationProviders/DefaultAuthenticator');
###set('ControlFlag', 'SUFFICIENT');
cd('../../');
# set('Arguments','-Xms=2048m -Xmx=2048m -XX:NewSize=512M -XX:MaxNewSize=512M -XX:PermSize=256M -XX:MaxPermSize=256M');
print "Update domain";
updateDomain();
closeDomain();
