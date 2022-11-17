'''
Created on Oct 20, 2022

Course work: 

@author: Sivaraam

Source:
    
'''

import requests


def random_num():
    #random_number=random.randint(0,100)
    #return random_number
    final_url="http://127.0.0.1:8002"
    resp = requests.get(final_url)
    return resp.json()['random_number']