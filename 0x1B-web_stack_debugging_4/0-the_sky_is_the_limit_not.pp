#Increase ULIMIT
exec { 'fix--for-nginx':
  command => "sed -i -E 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin',
  before  => Exec['restart'],
}

exec { 'restart':
  command     => 'service nginx restart',
  path        => ['/usrlocal/bin', '/usr/bin'],
  refreshonly => true,
}
