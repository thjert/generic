# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.define "wls" do |wls|

  # Choose Oracle Linux 7.1 or CentOS 7.1
  wls.vm.box = "centos/7"
  #config.vm.box = "boxcutter/oel71"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false
  
  wls.vm.network "private_network", ip: "192.168.56.14"
  wls.vm.hostname = "wls12c-r2-1.private"
###  wls.vm.network "forwarded_port", guest: 7001, host: 7001 id: WLSAS
###  wls.vm.network "forwarded_port", guest: 7002, host: 7002 id: WLSASSSL
	wls.vm.network "forwarded_port", guest: 7001, host: 7001
	wls.vm.network "forwarded_port", guest: 7002, host: 7002
	wls.vm.network "forwarded_port", guest: 5556, host: 5556


# Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  ###wls.vm.network "forwarded_port", guest: 7001, host: 7001 id: WLSEM

  end
  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"
  
  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.
  config.vm.provider "virtualbox" do |vb|  
    vb.memory = "4096"
    vb.cpus = 1
 ###   vb.name = "acslogic12cR2-1"
  end
 

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
###	config.vm.provision "ansible" do |ansible|
###        ansible.playbook = "acslogic-fmw-domain.yml"
###        ansible.inventory_path = "./hosts"
###	ansible.limit = 'all'
###	#ansible.groups = { 
#		"group1" => ["acslogic"]
#	}
###    end
	
	
  config.vm.define "acs" do |acs|
	acs.vm.box = "debian/stretch64"
	acs.vm.hostname = "acs"
	acs.vm.network "private_network", ip: "192.168.56.15"
	acs.vm.network "forwarded_port", guest: 80, host: 8080
	
###	acs.playbook = "acslogic-fmw-domain.yml"
###    acs.inventory_path = "./hosts"
###    acs.limit = 'all'
###	acs.groups = { 
###       "group1" => ["acslogic"]
###	}
  end
  
###  config.vm.define "wlsms" do |wlsms|

  # Choose Oracle Linux 7.1 or CentOS 7.1
###  wlsms.vm.box = "centos/7"
  #config.vm.box = "boxcutter/oel71"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false
  
###  wlsms.vm.network "private_network", ip: "192.168.56.16"
###  wlsms.vm.hostname = "wlsms12c-r2-1.private"
###  wlsms.vm.network "forwarded_port", guest: 8001, host: 8001 id: WLSMS
###  wlsms.vm.network "forwarded_port", guest: 10001, host: 10001 id: WLSMSSSL

# Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  ###wlsms.vm.network "forwarded_port", guest: 7001, host: 7001 id: WLSEM

###  end

end