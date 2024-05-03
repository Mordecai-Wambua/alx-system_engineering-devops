#setup a custom HTTP header
exec { 'update':
  command  => '/usr/bin/apt-get -y update',
  provider => 'shell'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update']
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!'
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

file_line { 'header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By $hostname;'
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
