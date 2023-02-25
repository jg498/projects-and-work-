#Debug a problem with a Cloud Deployment and Fix it
#Informational responses (100–199)
#Successful responses (200–299)
#Redirects (300–399)
#Client errors (400–499)
#Server errors (500–599) 

#student-01-40ae4df02a30@ws01:~$ sudo systemctl status apache2
● apache2.service - The Apache HTTP Server
   Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset:
  Drop-In: /lib/systemd/system/apache2.service.d
           └─apache2-systemd.conf
   Active: failed (Result: exit-code) since Wed 2023-02-15 02:30:21 UTC; 1min 44

Feb 15 02:30:21 ws01 systemd[1]: Starting The Apache HTTP Server...
Feb 15 02:30:21 ws01 apachectl[3564]: (98)Address already in use: AH00072: make_
Feb 15 02:30:21 ws01 apachectl[3564]: (98)Address already in use: AH00072: make_
Feb 15 02:30:21 ws01 apachectl[3564]: no listening sockets available, shutting d
Feb 15 02:30:21 ws01 apachectl[3564]: AH00015: Unable to open logs
Feb 15 02:30:21 ws01 apachectl[3564]: Action 'start' failed.
Feb 15 02:30:21 ws01 apachectl[3564]: The Apache error log may have more informa
Feb 15 02:30:21 ws01 systemd[1]: apache2.service: Control process exited, code=e
Feb 15 02:30:21 ws01 systemd[1]: apache2.service: Failed with result 'exit-code'
Feb 15 02:30:21 ws01 systemd[1]: Failed to start The Apache HTTP Server.
lines 1-16/16 (END)...skipping...
● apache2.service - The Apache HTTP Server
   Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
  Drop-In: /lib/systemd/system/apache2.service.d
           └─apache2-systemd.conf
   Active: failed (Result: exit-code) since Wed 2023-02-15 02:30:21 UTC; 1min 44s ago

Feb 15 02:30:21 ws01 systemd[1]: Starting The Apache HTTP Server...
Feb 15 02:30:21 ws01 apachectl[3564]: (98)Address already in use: AH00072: make_sock: could not bind to address [::]:80
Feb 15 02:30:21 ws01 apachectl[3564]: (98)Address already in use: AH00072: make_sock: could not bind to address 0.0.0.0:80
Feb 15 02:30:21 ws01 apachectl[3564]: no listening sockets available, shutting down
Feb 15 02:30:21 ws01 apachectl[3564]: AH00015: Unable to open logs
Feb 15 02:30:21 ws01 apachectl[3564]: Action 'start' failed.
Feb 15 02:30:21 ws01 apachectl[3564]: The Apache error log may have more information.
Feb 15 02:30:21 ws01 systemd[1]: apache2.service: Control process exited, code=exited status=1
Feb 15 02:30:21 ws01 systemd[1]: apache2.service: Failed with result 'exit-code'.
Feb 15 02:30:21 ws01 systemd[1]: Failed to start The Apache HTTP Server.
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~

student-01-40ae4df02a30@ws01:~$ sudo systemctl restart apache2
Job for apache2.service failed because the control process exited with error code.
See "systemctl status apache2.service" and "journalctl -xe" for details.
student-01-40ae4df02a30@ws01:~$ sudo systemctl status apache2
● apache2.service - The Apache HTTP Server
   Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
  Drop-In: /lib/systemd/system/apache2.service.d
           └─apache2-systemd.conf
   Active: failed (Result: exit-code) since Wed 2023-02-15 02:32:35 UTC; 22s ago
  Process: 4274 ExecStart=/usr/sbin/apachectl start (code=exited, status=1/FAILURE)

Feb 15 02:32:35 ws01 systemd[1]: Starting The Apache HTTP Server...
Feb 15 02:32:35 ws01 apachectl[4274]: (98)Address already in use: AH00072: make_sock: could not bind to address [::]:80
Feb 15 02:32:35 ws01 apachectl[4274]: (98)Address already in use: AH00072: make_sock: could not bind to address 0.0.0.0:80
Feb 15 02:32:35 ws01 apachectl[4274]: no listening sockets available, shutting down
Feb 15 02:32:35 ws01 apachectl[4274]: AH00015: Unable to open logs
Feb 15 02:32:35 ws01 apachectl[4274]: Action 'start' failed.
Feb 15 02:32:35 ws01 apachectl[4274]: The Apache error log may have more information.
Feb 15 02:32:35 ws01 systemd[1]: apache2.service: Control process exited, code=exited status=1
Feb 15 02:32:35 ws01 systemd[1]: apache2.service: Failed with result 'exit-code'.
Feb 15 02:32:35 ws01 systemd[1]: Failed to start The Apache HTTP Server.
student-01-40ae4df02a30@ws01:~$ sudo netstat -nlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2622/python3
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      929/systemd-resolve
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1601/sshd
tcp6       0      0 :::22                   :::*                    LISTEN      1601/sshd
udp        0      0 127.0.0.1:323           0.0.0.0:*                           2249/chronyd
udp        0      0 127.0.0.53:53           0.0.0.0:*                           929/systemd-resolve
udp        0      0 10.128.0.2:68           0.0.0.0:*                           902/systemd-network
udp6       0      0 ::1:323                 :::*                                2249/chronyd
raw6       0      0 :::58                   :::*                    7           902/systemd-network
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
unix  2      [ ACC ]     STREAM     LISTENING     19095    1/init               /run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     14823    1/init               /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     14100    1/init               /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     14106    1/init               /run/systemd/fsck.progress
unix  2      [ ACC ]     STREAM     LISTENING     14108    1/init               /run/lvm/lvmetad.socket
unix  2      [ ACC ]     STREAM     LISTENING     14114    1/init               /run/systemd/journal/stdout
unix  2      [ ACC ]     STREAM     LISTENING     14575    1/init               /run/lvm/lvmpolld.socket
unix  2      [ ACC ]     STREAM     LISTENING     19038    1/init               /var/lib/lxd/unix.socket
unix  2      [ ACC ]     STREAM     LISTENING     19078    1/init               @ISCSIADM_ABSTRACT_NAMESPACE
unix  2      [ ACC ]     STREAM     LISTENING     19074    1/init               /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     19079    1/init               /run/uuidd/request
unix  2      [ ACC ]     STREAM     LISTENING     19081    1/init               /run/snapd.socket
unix  2      [ ACC ]     STREAM     LISTENING     19083    1/init               /run/snapd-snap.socket
student-01-40ae4df02a30@ws01:~$ ^C
student-01-40ae4df02a30@ws01:~$ ps -ax | grep python3
 1142 ?        Ssl    0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
 1166 ?        Ssl    0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
 2622 ?        Ss     0:00 python3 /usr/local/bin/jimmytest.py
 4733 pts/0    S+     0:00 grep --color=auto python3
student-01-40ae4df02a30@ws01:~$ cat /usr/local/bin/jimmytest.py
#!/usr/bin/env python3
'''    Testing program for socket
      Author: Jimmy
'''
import http.server
import socketserver
import http

port = 80
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(http.HTTPStatus.INTERNAL_SERVER_ERROR)
        self.end_headers()

        mystring = "500 Internal Server Error!\n"
        self.data = bytes(mystring, 'utf-8')
        self.wfile.write(self.data)

with socketserver.TCPServer(("", port), Handler) as httpd:
    httpd.serve_forever()

student-01-40ae4df02a30@ws01:~$ sudo kill [process-id]
kill: failed to parse argument: '[process-id]'
student-01-40ae4df02a30@ws01:~$ ps -ax | grep python3
 1142 ?        Ssl    0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
 1166 ?        Ssl    0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
 2622 ?        Ss     0:00 python3 /usr/local/bin/jimmytest.py
 4878 pts/0    S+     0:00 grep --color=auto python3
student-01-40ae4df02a30@ws01:~$ sudo kill [2622/python3]
kill: failed to parse argument: '[2622/python3]'
student-01-40ae4df02a30@ws01:~$ sudo kill [2622]
kill: failed to parse argument: '[2622]'
student-01-40ae4df02a30@ws01:~$ sudo kill [1166]
kill: failed to parse argument: '[1166]'
student-01-40ae4df02a30@ws01:~$ sudo kill 1166
student-01-40ae4df02a30@ws01:~$ sudo kill 1142
student-01-40ae4df02a30@ws01:~$ sudo kill 2622
student-01-40ae4df02a30@ws01:~$ sudo kill 4733
kill: (4733): No such process
student-01-40ae4df02a30@ws01:~$ ps -ax | grep python3
 6057 pts/0    S+     0:00 grep --color=auto python3
student-01-40ae4df02a30@ws01:~$ sudo systemctl --type=service | grep jimmy
● jimmytest.service                              loaded failed failed  Jimmy python test service
student-01-40ae4df02a30@ws01:~$ sudo systemctl stop jimmytest && sudo systemctl disable jimmytest
Removed /etc/systemd/system/default.target.wants/jimmytest.service.
student-01-40ae4df02a30@ws01:~$ sudo netstat -nlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      929/systemd-resolve
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1601/sshd
tcp6       0      0 :::22                   :::*                    LISTEN      1601/sshd
udp        0      0 127.0.0.1:323           0.0.0.0:*                           2249/chronyd
udp        0      0 127.0.0.53:53           0.0.0.0:*                           929/systemd-resolve
udp        0      0 10.128.0.2:68           0.0.0.0:*                           902/systemd-network
udp6       0      0 ::1:323                 :::*                                2249/chronyd
raw6       0      0 :::58                   :::*                    7           902/systemd-network
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
unix  2      [ ACC ]     STREAM     LISTENING     19095    1/init               /run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     14823    1/init               /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     14100    1/init               /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     14106    1/init               /run/systemd/fsck.progress
unix  2      [ ACC ]     STREAM     LISTENING     14108    1/init               /run/lvm/lvmetad.socket
unix  2      [ ACC ]     STREAM     LISTENING     14114    1/init               /run/systemd/journal/stdout
unix  2      [ ACC ]     STREAM     LISTENING     14575    1/init               /run/lvm/lvmpolld.socket
unix  2      [ ACC ]     STREAM     LISTENING     19038    1/init               /var/lib/lxd/unix.socket
unix  2      [ ACC ]     STREAM     LISTENING     19078    1/init               @ISCSIADM_ABSTRACT_NAMESPACE
unix  2      [ ACC ]     STREAM     LISTENING     19074    1/init               /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     19079    1/init               /run/uuidd/request
unix  2      [ ACC ]     STREAM     LISTENING     19081    1/init               /run/snapd.socket
unix  2      [ ACC ]     STREAM     LISTENING     19083    1/init               /run/snapd-snap.socket
student-01-40ae4df02a30@ws01:~$ sudo systemctl start apache2

