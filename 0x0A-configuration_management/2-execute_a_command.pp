#!/usr/bin/env bash
#Using Puppet, create a manifest that kills.
exec { 'killmenow':
    command => 'pkill -f killmenow',
    path    => '/usr/bin',
}
