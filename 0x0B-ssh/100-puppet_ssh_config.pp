#using Puppet to make changes to our configuration file.
file { '/root/.ssh/config':
  owner   => 'root',
  group   => 'root',
  content => "
 	Host web-01
		HostName 52.91.118.63
		User ubuntu
		IdentityFile ~/.ssh/school
		PasswordAuthentication no",
  mode    => '0600'
}
