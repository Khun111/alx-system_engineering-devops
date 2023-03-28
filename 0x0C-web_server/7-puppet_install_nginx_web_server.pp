# Use puppet to configure nginx
package { 'nginx':
    ensure => installed,
  }

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!i\n'
}
# Set up custom 404 error page
file { '/usr/share/nginx/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
}

# Configure Nginx
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => '
    server {
        listen 80;
        listen [::]:80;
        root /var/www/html;
        index index.html index.htm;
        server_name 54.144.144.194;

        error_page 404 /404.html;
        location = /404.html {
            internal;
        }

        location /redirect_me {
            return 301 https://oluwatobialure.hashnode.dev;
        }

        location / {
            try_files $uri $uri/ =404;
        }
    }',
}

# Enable the default Nginx site

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => [
    File['/etc/nginx/sites-enabled/default'],
    File['/usr/share/nginx/html/404.html'],
  ],
}
