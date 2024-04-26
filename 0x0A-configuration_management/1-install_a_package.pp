# install flask version 2.1.0 from pip3

exec { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
