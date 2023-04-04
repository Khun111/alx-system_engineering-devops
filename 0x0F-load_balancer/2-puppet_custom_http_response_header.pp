# Create Custom header with puppet
package { 'nginx':
  ensure => 'installed',
}

file_line { 'custom_header':
  path => '/etc/nginx/sites-enabled/default',
  line => '    add_header X-Served-By \$hostname',
  match => '^    listen 80 default_server;$',
  require => Package['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enabled => 'true'
}
