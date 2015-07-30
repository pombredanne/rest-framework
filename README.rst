==========================
Django Rest Framework Talk
==========================

Talk and demo for talk on Django Rest Framework

Setup for the Demo
------------------

I prefer to set this up using Ansible, and I've included playbooks
that will get you setup with just a few commands.  Follow the guide below
to set that up.  However, if you want to skip that, you can also get most of
the way there by booting up a VM or into Ubuntu and usin the instructions
provided.

Setup With Ansible
^^^^^^^^^^^^^^^^^^

- Install `Vagrant <https://www.vagrantup.com>`
- Install `Ansible <http://www.ansible.com/home>`

::

    vagrant up


Setup on Ubuntu
^^^^^^^^^^^^^^^

sudo apt-get update
sudo apt-get install python2.7-dev python3.4-dev python-crypto python-setuptools libxml2-dev libyaml-dev libpq-dev libpq5 python-pip libxslt-dev build-essential

sudo pip install virtualenv
