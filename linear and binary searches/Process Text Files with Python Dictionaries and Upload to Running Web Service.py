#Process Text Files with Python Dictionaries and Upload to Running Web Service
#! /usr/bin/env python3
import os
import requests

src_dir = "/data/feedback/"

files = os.listdir(src_dir)


def readlines(file):
  with open(src_dir + file) as f:
    lines = f.read().splitlines()
  return lines

feedback=[]
keys = ["title", "name", "date", "feedback"]
for file in files:
  lines=readlines(file)
  feedback.append(dict(zip(keys, lines)))

url= "http://35.193.43.249/feedback/"

for entry in feedback:
  response = requests.post(url, data=entry)
  if response.ok:
    print("loaded entry")
  else:
    print(f"load entry error: {response.status_code}")
