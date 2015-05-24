# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  ### Define options for all VMs ###
  # Using vagrant-cachier improves performance if you run repeated yum/apt updates
  if defined? VagrantPlugins::Cachier
    config.cache.auto_detect = true
  end

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "512", "--cpus", "2", "--ioapic", "on"]
  end

  config.vm.define "centos66", primary: true do |node|
    node.vm.box = "chef/centos-6.6"
    node.vm.network :private_network, ip: "192.168.35.21"
  end

  config.vm.define "centos70", autostart: false do |node|
    node.vm.box = "chef/centos-7.0"
    node.vm.network :private_network, ip: "192.168.35.22"
  end

  config.vm.define "ubuntu1204", autostart: false do |node|
    node.vm.box = "chef/ubuntu-12.04"
    node.vm.network :private_network, ip: "192.168.35.31"
  end

  config.vm.define "ubuntu1410", autostart: false do |node|
    node.vm.box = "chef/ubuntu-14.10"
    node.vm.network :private_network, ip: "192.168.35.32"
  end

#  config.vm.provision "ansible" do |ansible|
#    ansible.playbook = "play.yml"
#  end

end
