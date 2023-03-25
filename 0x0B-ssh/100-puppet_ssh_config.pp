# configure ssh with puppet
include stdlib
file_line {'Refuse auth':
ensure => present,
path   => '/etc/ssh/sshd_config',
line   => '  PasswordAuthentication no',
}

file_line {'Specifies private key':
ensure => present,
path   => '/etc/ssh/sshd_config',
line   => '  IdentityFile ~/.ssh/school',
}
