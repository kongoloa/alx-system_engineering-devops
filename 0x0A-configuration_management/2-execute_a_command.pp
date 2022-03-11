# Kill a process

exec { 'pkill killmenow':
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  returns => [0, 1],
}
