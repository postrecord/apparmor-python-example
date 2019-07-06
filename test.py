# apparmor interface
# https://pythonprogramminglanguage.com
import subprocess
import json
import os
from apparmor import *

# List all profiles
aa_status = profiles()
print('version: ' + aa_status['version'])
    
for profile in aa_status['profiles']:
   status = aa_status["profiles"][profile]
   print(status + " " + profile)

# Get unconfined profiles
apps = unconfined()
for app in apps:
    print(app[1])
    
