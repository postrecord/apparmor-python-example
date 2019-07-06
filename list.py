# apparmor interface
# https://pythonprogramminglanguage.com
import subprocess
import json

def getProfiles():
    result = subprocess.run(['apparmor_status', '--json'], stdout=subprocess.PIPE)
    data = result.stdout.decode('utf-8')
    aa_status = json.loads(data)
    return aa_status

def getUnconfined():
    result = subprocess.run(['aa-unconfined', '--paranoid'], stdout=subprocess.PIPE)
    data = result.stdout.decode('utf-8')
    lines = data.split("\n")
    apps = []
    for line in lines:
        app = line.split(" ")
        if len(app) > 1:
            apps.append( (app[0],app[1]) )
        
    return apps

# List all profiles
aa_status = getProfiles()
print('version: ' + aa_status['version'])
    
for profile in aa_status['profiles']:
   status = aa_status["profiles"][profile]
   print(status + " " + profile)

# Get unconfined profiles
apps = getUnconfined()
for app in apps:
    print(app[1])
    
