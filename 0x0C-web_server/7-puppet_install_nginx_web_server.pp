#Server configuration using Puppet
exec { 'update server':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update server']
}

file {'home':
  path    => '/var/www/html/index.html',
  content => 'Hello World!'
}

exec {'redirects':
  command  => sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default,
  provider => 'shell'
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
