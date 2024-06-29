# installs flask through pip install
  exec { 'Flask':
command => 'pip3 install flask==2.1.0',
path => '/usr/bin/',
}
