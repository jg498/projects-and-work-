#Qwiklabs VM Fleet update 
student-01-9d54c5d16799@puppet:~$ cd /etc/puppet/code/environments/production/mo                                                                                                             dules/packages
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ cat ma                                                                                             nifests/init.pp
class packages {

    package { 'python-requests':
        ensure => installed,
    }


}
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ sudo c                                                                                             hmod 646 manifests/init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ if $fa                                                                                             cts[os][family] == "Debian" {
> # Resource entry to install golang package
> }
-bash: syntax error near unexpected token `}'
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ nano
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ cat manifests/init.pp
class packages {

    package { 'python-requests':
        ensure => installed,
    }


}
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ sudo chmod 646 manifests/init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ if $facts[os][family] == "Debian" {
> # Resource entry to install golang package
> }
-bash: syntax error near unexpected token `}'
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ ls
manifests
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages$ cd manifests/
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages/manifests$ ls
init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages/manifests$ nano init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages/manifests$ gcloud compute instances describe linux-instan                                           ce --zone=us-central1-a --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
104.198.50.68
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages/manifests$ sudo puppet agent -v --test
Info: Using configured environment 'production'
Info: Retrieving pluginfacts
Info: Retrieving plugin
Info: Retrieving locales
Info: Caching catalog for puppet.us-central1-a.c.qwiklabs-gcp-04-089ea20693eb.internal
Info: Applying configuration version '1676074571'
apt policy golangNotice: /Stage[main]/Packages/Package[golang]/ensure: created
Notice: /Stage[main]/Machine_info/File[/tmp/machine_info.txt]/content:
--- /tmp/machine_info.txt       2023-02-11 00:01:39.797410943 +0000
+++ /tmp/puppet-file20230211-4912-1iq31yq       2023-02-11 00:16:45.249466274 +0000
@@ -1,6 +1,6 @@
 Machine Information
 -------------------
 Disks: {"sda"=>{"model"=>"PersistentDisk", "size"=>"10.00 GiB", "size_bytes"=>10737418240, "vendor"=>"Google"}}
-Memory: {"system"=>{"available"=>"3.29 GiB", "available_bytes"=>3537760256, "capacity"=>"8.24%", "total"=>"3.59 GiB", "total_bytes"=>3855265792,                                            "used"=>"302.80 MiB", "used_bytes"=>317505536}}
+Memory: {"system"=>{"available"=>"3.29 GiB", "available_bytes"=>3529289728, "capacity"=>"8.46%", "total"=>"3.59 GiB", "total_bytes"=>3855265792,                                            "used"=>"310.88 MiB", "used_bytes"=>325976064}}
 Processors: {"count"=>1, "isa"=>"x86_64", "models"=>["Intel(R) Xeon(R) CPU @ 2.30GHz"], "physicalcount"=>1}
 }

Info: Computing checksum on file /tmp/machine_info.txt
Info: /Stage[main]/Machine_info/File[/tmp/machine_info.txt]: Filebucketed /tmp/machine_info.txt to puppet with sum fad526d1eb834ebfceb8e279fa846a6                                           e
Notice: /Stage[main]/Machine_info/File[/tmp/machine_info.txt]/content: content changed '{md5}fad526d1eb834ebfceb8e279fa846a6e' to '{md5}b7f8cd710f                                           0be95a940e8d692caa3cdb'
Notice: Applied catalog in 33.37 seconds
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages/manifests$ apt policy golang
golang:
  Installed: 2:1.10~4ubuntu1
  Candidate: 2:1.10~4ubuntu1
  Version table:
 *** 2:1.10~4ubuntu1 500
        500 http://us-central1.gce.archive.ubuntu.com/ubuntu bionic/main amd64 Packages
        100 /var/lib/dpkg/status
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/packages/manifests$ cd /etc/puppet/code/environments/production/modules/machine_info
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ cat manifests/init.pp
class machine_info {

    file { '/tmp/machine_info.txt':
        content => template('machine_info/info.erb'),
    }


}
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ sudo chmod 646 manifests/init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ ls
manifests  templates
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ cd manifests
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/manifests$ nano init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/manifests$ cd..
cd..: command not found
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/manifests$ cat templates/info.erb
cat: templates/info.erb: No such file or directory
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/manifests$ nano init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/manifests$ cat templates/info.erb
cat: templates/info.erb: No such file or directory
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/manifests$ cd ..
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ ls
manifests  templates
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ sudo chmod 646 templates/info.erb
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ Network Interfaces: <%= @interfaces %>
-bash: syntax error near unexpected token `newline'
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ ls
manifests  templates
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info$ cd templates/
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/templates$ nano
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/templates$ ls
info.erb
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/templates$ nano
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/templates$ nano info.erb
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/templates$ sudo mkdir -p /etc/puppet/code/environments/production/modules/reboot/manifests
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/templates$ cd manifests
-bash: cd: manifests: No such file or directory
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/templates$ cd manifests/
-bash: cd: manifests/: No such file or directory
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/machine_info/templates$ cd /etc/puppet/code/environments/production/modules/reboot/manifests
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/reboot/manifests$ sudo touch init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/reboot/manifests$ sudo nano init.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/reboot/manifests$ sudo nano /etc/puppet/code/environments/production/manifests/site.pp
student-01-9d54c5d16799@puppet:/etc/puppet/code/environments/production/modules/reboot/manifests$




#VM Fleet
student-01-9d54c5d16799@linux-instance:~$ sudo puppet agent -v --test
Info: Using configured environment 'production'
Info: Retrieving pluginfacts
Info: Retrieving plugin
Warning: Facter: Unable to fetch metadata from http://metadata/computeMetadata/v1beta1/?recursive=true&alt=json: 404 Not Found
Info: Caching catalog for linux-instance.us-central1-a.c.qwiklabs-gcp-04-089ea20693eb.internal
Info: Applying configuration version '1676075095'
Notice: /Stage[main]/Packages/Package[golang]/ensure: created
Notice: Applied catalog in 26.40 seconds
student-01-9d54c5d16799@linux-instance:~$ apt policy golang
golang:
  Installed: 2:1.7~5
  Candidate: 2:1.7~5
  Version table:
     2:1.11~1~bpo9+1 100
        100 http://deb.debian.org/debian stretch-backports/main amd64 Packages
 *** 2:1.7~5 500
        500 http://deb.debian.org/debian stretch/main amd64 Packages
        100 /var/lib/dpkg/status
student-01-9d54c5d16799@linux-instance:~$ sudo puppet agent -v --test
Info: Using configured environment 'production'
Info: Retrieving pluginfacts
Info: Retrieving plugin
Warning: Facter: Unable to fetch metadata from http://metadata/computeMetadata/v1beta1/?recursive=true&alt=json: 404 Not Found
Info: Caching catalog for linux-instance.us-central1-a.c.qwiklabs-gcp-04-089ea20693eb.internal
Info: Applying configuration version '1676076006'
Notice: /Stage[main]/Machine_info/File[machine_info]/content:
--- /tmp/machine_info.txt       2023-02-11 00:03:36.013298754 +0000
+++ /tmp/puppet-file20230211-2149-olq9z8        2023-02-11 00:40:07.335869501 +0000
@@ -3,4 +3,5 @@
 Disks:
 Memory:
 Processors: {"models"=>["Intel(R) Xeon(R) CPU @ 2.20GHz", "Intel(R) Xeon(R) CPU @ 2.20GHz"], "count"=>2, "physicalcount"=>1}
+Network Interfaces: eth0,lo
 }

Info: Computing checksum on file /tmp/machine_info.txt
Info: /Stage[main]/Machine_info/File[machine_info]: Filebucketed /tmp/machine_info.txt to puppet with sum de29b0c5befac94ee8b456f942d62aae
Notice: /Stage[main]/Machine_info/File[machine_info]/content: content changed '{md5}de29b0c5befac94ee8b456f942d62aae' to '{md5}91015a43c863e143f8d3a8ea8fc4ed08'
Notice: Applied catalog in 0.09 seconds
student-01-9d54c5d16799@linux-instance:~$ cat /tmp/machine_info.txt
Machine Information
-------------------
Disks:
Memory:
Processors: {"models"=>["Intel(R) Xeon(R) CPU @ 2.20GHz", "Intel(R) Xeon(R) CPU @ 2.20GHz"], "count"=>2, "physicalcount"=>1}
Network Interfaces: eth0,lo
}
student-01-9d54c5d16799@linux-instance:~$ sudo puppet agent -v --test
Info: Using configured environment 'production'
Info: Retrieving pluginfacts
Info: Retrieving plugin
Warning: Facter: Unable to fetch metadata from http://metadata/computeMetadata/v1beta1/?recursive=true&alt=json: 404 Not Found
Info: Caching catalog for linux-instance.us-central1-a.c.qwiklabs-gcp-04-089ea20693eb.internal
Info: Applying configuration version '1676076380'
Notice: Applied catalog in 0.04 seconds
