# install flask version 2.1.0 from pip3

exec { 'install_flask':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
