## Mucking around with ansible

This is my little sandbox environment for building sand castles with ansible.

It's currently got 
* a vagrantfile for spinning up different distros and private ip's specified, 
* an inventory file, with relative private_key paths
* various playbooks
* an example filter_plugin
* an example custom module to gather more facts

_Note the optional use of vagrant-cachier, and the fact centos66 is the primary, all others are disabled by default._ 

_Note I use a static inventory file, this is so I can easily place group_vars and host_vars relative to it, rather than using the vagrant provisioner generated one. Though I could probably do a symlink... (tbd)._

_Note I'm not using the vagrant ansible provisioner at present, this is because I have a habit of creating random plays to try stuff, and it's easier to just run them from the command line in an adhoc fashion._

###To use
* install ansible
* install virtualbox and vagrant
* start the relevant box(es)

        vagrant up
        # or
        vagrant up centos70

* run a playbook, e.g.

         ansible-playbook plays/yaml_syntax.yml --limit centos66

