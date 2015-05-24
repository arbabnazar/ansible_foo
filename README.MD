## Mucking around with ansible

This is my little sandbox environment for building sand castles with ansible.

It's currently got 
* a vagrantfile for spinning up different distros and private ip's specified, 
* an inventory file, with relative private_key paths
* various playbooks
* an example filter_plugin
* an example custom module to gather more facts

_Note the optional use of vagrant-cachier, and the fact centos66 is the primary, all others are disabled by default._ 

To use:
* install virtualbox and vagrant
* start the relevant box(es)

     vagrant up
     # or
     vagrant up centos70

* run a playbook, e.g.

     ansible-playbook plays/yaml_syntax.yml --limit centos66

