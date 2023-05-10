# Puppet file for editing wp config file
exec { 'replace_content':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
