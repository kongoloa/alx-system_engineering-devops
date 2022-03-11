# a manifest that kills a process named killmenow
exec { 'pkill killmenow':
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  returns => [0, 1],
}
