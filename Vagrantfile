Vagrant.configure("2") do |config|
  ## Choose your base box
  config.vm.box = "trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.synced_folder "./demo", "/home/vagrant/demo"

  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 5555, host: 5555
  config.ssh.forward_agent = true

  config.vm.host_name = 'rest-framework'
end
