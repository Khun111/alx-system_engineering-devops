# configure ssh with puppet
file {'/etc/ssh/sshd_config':
ensure => present,
content => "  PasswordAuthentication no\n  IdentityFile ~/.ssh/school",
}
