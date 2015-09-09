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

- Clone this repo
- Install `Vagrant <https://www.vagrantup.com>`_
- Install `Ansible <http://www.ansible.com/home>`_
- From inside this directory

::

    vagrant up

Setup on Ubuntu
^^^^^^^^^^^^^^^

sudo apt-get update
sudo apt-get install python2.7-dev python3.4-dev python-crypto python-setuptools libxml2-dev libyaml-dev libpq-dev libpq5 python-pip libxslt-dev build-essential

sudo pip install virtualenv

Migrate and Run the Django App
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These instructions assume that you are logging in and using the VM as
described above with Vagrant.

Login to the VM::

    vagrant ssh

Source the virtualenv created by the ansible play book::

    source .virtualenvs/drf_demo/bin/activate

Change dir to the demo directory::

    cd demo

Do the initial migration::

    ./manage.py migrate

Setup the fake data::

    ./manage.py setup_demo

Run the server::

    ./manage.py runserver 0.0.0.0:8000

Open up a browser and point it to localhost:8000 to view the site!
