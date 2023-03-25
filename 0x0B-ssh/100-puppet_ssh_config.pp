# configure ssh with puppet
file {'/etc/ssh/sshd_config':
ensure => file,
content => "Host 54.144.144.194\n  User ubuntu\n  PasswordAuthentication no\n  IdentityFile ~/.ssh/school",
}
