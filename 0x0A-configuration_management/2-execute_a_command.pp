#!/usr/bin/env bash
#Using Puppet, create a file in /tmp.
exec { 'killmenow':
    command  => 'pkill -f killmenow',
    path    => '/usr/bin',
}
