#Create VM template and Automate deployment 
git clone https://www.github.com/google/it-cert-automation-practice.git 

cd ~/it-cert-automation-practice/Course5/Lab3
list
sudo cp hello_cloud.py /usr/local/bin/
sudo cp hello_cloud.service /etc/systemd/system
sudo systemctl enable hello_cloud.service

#gcommand line interface 

Welcome to Cloud Shell! Type "help" to get started.
Your Cloud Platform project in this session is set to qwiklabs-gcp-03-db5dc7bf0b8e.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.
student_01_5aaccb383420@cloudshell:~ (qwiklabs-gcp-03-db5dc7bf0b8e)$ gcloud compute ssh --zone "us-east1-b" "vm1"  --project "qwiklabs-gcp-03-db5dc7bf0b8e"gcloud compute instances create --zone us-west1-b --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8

student_01_5aaccb383420@cloudshell:~ (qwiklabs-gcp-03-db5dc7bf0b8e)$ gcloud compute instances list
NAME: vm1
ZONE: us-east1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.142.0.2
EXTERNAL_IP: 35.237.40.157
STATUS: RUNNING
student_01_5aaccb383420@cloudshell:~ (qwiklabs-gcp-03-db5dc7bf0b8e)$ gcloud compute instances create --zone us-west1-b --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8


student_01_5aaccb383420@cloudshell:~ (qwiklabs-gcp-03-db5dc7bf0b8e)$ gcloud compute instances list
NAME: vm2
ZONE: us-west1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.138.0.7
EXTERNAL_IP: 34.105.92.0
STATUS: RUNNING

NAME: vm3
ZONE: us-west1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.138.0.6
EXTERNAL_IP: 34.127.99.64
STATUS: RUNNING

NAME: vm4
ZONE: us-west1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.138.0.8
EXTERNAL_IP: 35.185.203.237
STATUS: RUNNING

NAME: vm5
ZONE: us-west1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.138.0.2
EXTERNAL_IP: 34.127.119.64
STATUS: RUNNING

NAME: vm6
ZONE: us-west1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.138.0.3
EXTERNAL_IP: 34.168.221.28
STATUS: RUNNING

NAME: vm7
ZONE: us-west1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.138.0.5
EXTERNAL_IP: 35.230.33.182
STATUS: RUNNING

NAME: vm8
ZONE: us-west1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.138.0.4
EXTERNAL_IP: 34.127.28.162
STATUS: RUNNING

NAME: vm1
ZONE: us-east1-b
MACHINE_TYPE: n1-standard-1
PREEMPTIBLE:
INTERNAL_IP: 10.142.0.2
EXTERNAL_IP: 35.237.40.157
STATUS: RUNNING
student_01_5aaccb383420@cloudshell:~ (qwiklabs-gcp-03-db5dc7bf0b8e)$ gcloud compute ssh --zone "us-east1-b" "vm1"  --project "qwiklabs-gcp-03-db5dc7bf0b8e"gcloud compute instances create --zone us-west1-b --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8^C
student_01_5aaccb383420@cloudshell:~ (qwiklabs-gcp-03-db5dc7bf0b8e)$