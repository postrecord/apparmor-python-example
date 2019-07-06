# apparmor interface
# https://pythonprogramminglanguage.com
import subprocess
import json
import os

def profiles():
    result = subprocess.run(['apparmor_status', '--json'], stdout=subprocess.PIPE)
    data = result.stdout.decode('utf-8')
    aa_status = json.loads(data)
    return aa_status

def unconfined():
    result = subprocess.run(['aa-unconfined', '--paranoid'], stdout=subprocess.PIPE)
    data = result.stdout.decode('utf-8')
    lines = data.split("\n")
    apps = []
    for line in lines:
        app = line.split(" ")
        if len(app) > 1:
            apps.append( (app[0],app[1]) )
        
    return apps

def complain(profile):
    os.system("sudo aa-complain " + profile)
    
def enforce(profile):
    os.system("sudo aa-enforce  " + profile)

def disable(profile):
    os.system("sudo ln -s " + profile + " /etc/apparmor.d/disable/")
    

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
    
