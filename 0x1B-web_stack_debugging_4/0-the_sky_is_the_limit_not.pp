#Increase ULIMIT
exec { 'fix--for-nginx':
  command => "sed -i -E 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => 'usr/local/bin/:/bin',
}

service { 'nginx':
  ensure => running,
  enable => true,
}
