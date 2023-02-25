#use PIL library to update all images within ~/supplier-data/images directory to Change image resolution from 3000x2000 to 600x400 pixel and Change image format from .TIFF to .JPEG.
#The raw images from images subdirectory contains alpha transparency layers. So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images. Use convert("RGB") method for converting RGBA to RGB image.
#!/usr/bin/env python3
#use PIL library to update all images within ~/supplier-data/images directory to Change image resolution from 3000x2000 to 600x400 pixel and Change image format from .TIFF to .JPEG

from PIL import Image
import os

#set image directory
path = "./supplier-data/images/" 

#loop through all files in the directory
for file in os.listdir(path):
    #check if the file is .tiff
    if file.endswith(".tiff"):
        #open the image
        im = Image.open(path + file)
        #convert RGBA to RGB
        im = im.convert("RGB")
        #resize the image
        im = im.resize((600,400))
        #remove .tiff extension
        file = file.replace(".tiff", ".jpeg")
        #save the image
        im.save(path + file, "JPEG")

# write a script named supplier_image_upload.py that takes the jpeg images from the supplier-data/images directory that you've processed previously and uploads them to the web server fruit catalog
#!/usr/bin/env python3
#use requests library to upload all images within ~/supplier-data/images directory to the web server fruit catalog

import requests
import os

#set image directory
path = "./supplier-data/images/"

#loop through all files in the directory
for file in os.listdir(path):
    #check if the file is .jpeg
    if file.endswith(".jpeg"):
        #open the image
        with open(path + file, 'rb') as opened:
            #post the image
            r = requests.post("http://localhost/upload/", files={'file': opened})

#Write a Python script named run.py to process the text files in the supplier-data/descriptions directory and generate a JSON file named reports.json that contains the following data:
#The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the frui
#and uploading it to http://35.232.115.250/fruits using the requests library. 
#Note that all files are written in the following format, with each piece of information on its own line: name, weight in lbs, description, and image name. 

#!/usr/bin/env python3
#use requests library to upload all images within ~/supplier-data/images directory to the web server fruit catalog

import requests
import os
import json

#set image directory
path = "./supplier-data/descriptions/"

#set json file
json_file = "reports.json"

#set json dictionary
json_dict = {}

#loop through all files in the directory
for file in os.listdir(path):
    #check if the file is .txt
    if file.endswith(".txt"):
        #open the file
        with open(path + file, 'r') as opened:
            #read the file
            lines = opened.readlines()
            #set the image name
            image_name = file.replace(".txt", ".jpeg")
            #set the json dictionary
            json_dict = {"name": lines[0].strip(), "weight": int(lines[1].strip().strip("lbs")), "description": lines[2].strip(), "image_name": image_name}
            #post the json dictionary
            r = requests.post("http://35.232.115.250/fruits/", json=json_dict)

#Using the reportlab Python library, define the method generate_report to build the PDF reports using the data from the JSON file.
# PDF report should be named processed.pdf.

#!/usr/bin/env python3
#use reportlab library to generate a PDF report using the data from the JSON file

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line])



# send the email using the emails.generate_email() and emails.send_email() methods.Define generate_email and send_email methods by importing necessary libraries.

#!/usr/bin/env python3
#use emails library to send an email

import os
import datetime
import reports
import emails

dt = datetime.datetime.now().strftime ("%m/%d/%Y")
names = []
weights = []
path = "./supplier-data/descriptions/"

for file in os.listdir(path):
    if file.endswith(".txt"):
        with open(path + file, 'r') as opened:
            lines = opened.readlines()
            names.append("name: " + lines[0].strip())
            weights.append("weight: " + lines[1].strip())

summary = " "
for name, weight in zip(names, weights):
    summary += name + " " + weight + "<br/>"

if __name__ == "__main__":
    #set the pdf file
    reports.generate_report("/tmp/processed.pdf", "Processed Update on " + dt, summary)
    #set the email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message) 

#send the email using the emails.generate_email() and emails.send_email() methods. 
#Define generate_email and send_email methods by importing necessary libraries.

#!/usr/bin/env python3
#use emails library to send an email

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_filename)

    return message

def generate_error_email(sender, recipient, subject, body):
    """Creates an email without an attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message

def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

#write a Python script that will run in the background monitoring some of your system statistics
#The script should collect the following data:
#CPU usage  
#Disk space
#Memory (RAM) usage and name resolution
#The script should then send an email if any of the measurements are above some threshold:
#CPU usage over 80%
#Available disk space under 20%
#Available memory under 500MB
#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1" 

#!/usr/bin/env python3
#use psutil library to monitor system statistics

import psutil
import emails
import socket
import shutil
import os

sender = "automation@example.com"
receiver = "student-01-918dcb8a423c@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

du = shutil.disk_usage("/")
du_print = du.free / du.total * 100

if du_print < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message) 

cpu_print = psutil.cpu_percent(1)
if cpu_print > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

mem = psutil.virtual_memory()
mem_print = mem.available / 1024 ** 2
if mem_print < 500:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

hostname = socket.gethostbyname('localhost')
if hostname != "127.0.0.1":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

    






















