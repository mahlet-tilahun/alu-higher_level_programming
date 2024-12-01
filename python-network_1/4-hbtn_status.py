#!/usr/bin/python3
"""
script that fetches https://alu-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    
    r = requests.get('https://alu-intranet.hbtn.io/status')
    
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
