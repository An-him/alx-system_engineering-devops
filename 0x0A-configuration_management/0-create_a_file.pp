# Creates a file called school with I LOVE PUPPET as the content
file { '/tmp/school':
content => 'I love Puppet',
group   => 'www-data',
owner   => 'www-data',
mode    => '0744',
}
