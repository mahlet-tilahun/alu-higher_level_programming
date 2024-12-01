#!/usr/bin/python3
"""fetches https://alu-intranet.hbtn.io/status using requests"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:$")
    print("\t- type: <class 'str'>$")
    print("\t- content: {}$".format(response.text.strip()))

