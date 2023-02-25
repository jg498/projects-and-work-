'''Ubuntu configuration fixing permissions'''
student-01-08693404a8cb@puppet:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/loc                                           al/games:/snap/bin
student-01-08693404a8cb@puppet:~$ ls /
bin   dev  home        initrd.img.old  lib64       media  opt   root  sbin  srv  tmp  var      vmlinuz.old
boot  etc  initrd.img  lib             lost+found  mnt    proc  run   snap  sys  usr  vmlinuz
student-01-08693404a8cb@puppet:~$ cd /etc/puppet/code/environments/production/modules/profile/manifests
student-01-08693404a8cb@puppet:/etc/puppet/code/environments/production/modules/profile/manifests$ cat init.pp
class profile {
        file { '/etc/profile.d/append-path.sh':
                owner   => 'root',
                group   => 'root',
                mode    => '0646',
                content => "PATH=/java/bin\n",
        }
}
student-01-08693404a8cb@puppet:/etc/puppet/code/environments/production/modules/profile/manifests$ sudo nano init.pp
student-01-08693404a8cb@puppet:/etc/puppet/code/environments/production/modules/profile/manifests$ sudo puppet agent -v --test
Info: Using configured environment 'production'
Info: Retrieving pluginfacts
Info: Retrieving plugin
Info: Retrieving locales
Info: Caching catalog for puppet.us-central1-a.c.qwiklabs-gcp-03-7c3417d6469b.internal
Info: Applying configuration version '1675890426'
Notice: /Stage[main]/Profile/File[/etc/profile.d/append-path.sh]/content:
--- /etc/profile.d/append-path.sh       2023-02-08 21:00:14.180304730 +0000
+++ /tmp/puppet-file20230208-4759-zucaev        2023-02-08 21:07:06.278225286 +0000
@@ -1 +1 @@
-PATH=/java/bin
+PATH=$PATH:/java/bin 


Info: Computing checksum on file /etc/profile.d/append-path.sh
Info: /Stage[main]/Profile/File[/etc/profile.d/append-path.sh]: Filebucketed /etc/profile.d/append-path.sh to puppet with sum b1ca50e93b6ea92bd7b3eeb02c69f109
Notice: /Stage[main]/Profile/File[/etc/profile.d/append-path.sh]/content: content changed '{md5}b1ca50e93b6ea92bd7b3eeb02c69f109' to '{md5}30a2bc8929446ce04807cd3c5921cb14'
Notice: /Stage[main]/Profile/File[/etc/profile.d/append-path.sh]/mode: mode changed '0646' to '0644'
Notice: Applied catalog in 0.06 seconds
student-01-08693404a8cb@puppet:/etc/puppet/code/environments/production/modules/profile/manifests$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
student-01-08693404a8cb@puppet:/etc/puppet/code/environments/production/modules/profile/manifests$
