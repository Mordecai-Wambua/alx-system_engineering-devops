# install flask version 2.1.0 from pip3

exec { 'install_flask':
  require => Exec['python-check'],
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/bin', '/usr/bin']
}

exec {'python-check':
  command => '/usr/bin/which python3'
}
