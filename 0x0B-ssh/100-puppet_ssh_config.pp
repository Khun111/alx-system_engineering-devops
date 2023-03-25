# configure ssh with puppet
include stdlib
file_line {'Turn off passwd auth':
ensure => present,
path   => '/etc/ssh/sshd_config',
line   => '  PasswordAuthentication no',
}

file_line {'Declare identity file':
ensure => present,
path   => '/etc/ssh/sshd_config',
line   => '  IdentityFile ~/.ssh/school',
}
