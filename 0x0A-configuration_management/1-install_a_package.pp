# installs flask through pip install
exec { 'flask_installer':
command => 'pip3 install flask==2.1.0',
path => '/usr/bin/',
}
