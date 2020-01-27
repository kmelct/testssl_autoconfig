from subprocess import Popen, PIPE, call
import json
import sys

domain = sys.argv[1]

call(['./testssl.sh', '--quiet', '--fast', '--jsonfile-pretty=file.json', domain])
p = Popen(['cat', 'file.json'],
          stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
result = json.loads(out.decode("utf-8"))

vulnerabilities = result['scanResult'][0]['vulnerabilities']

res = []
for vuln in vulnerabilities:
  if vuln['severity'] == 'OK' or vuln['severity'] == 'INFO':
    continue
  res.append({
    'title': vuln['id'], 
    'description': vuln['finding'], 
  	'solution': "Update your ssl certs or contact us for support",
    'status': vuln['severity'].lower().capitalize(),
    'tool': 'testssl.sh',
    'color': 'yellow',
    'group': "Online Services Results"
  })

serverDefaults = result['scanResult'][0]['serverDefaults']
days = [x for x in serverDefaults if x['id'] == 'cert_validityPeriod']
if (len(days) > 0):
  day = int(days[0]['finding'].split(' ')[0])

  if (day < 60):
    res.append({
      'title': 'The certificate will expire soon', 
      'description': 'The certificate will expire in less then {} days'.format(day), 
  	  'solution': "Update your ssl certs or contact us for support",
      'status': 'High',
      'tool': 'testssl.sh',
      'position': 'top',
      'color': 'red',
      'group': "Online Services Results"
    })
  elif (day < 1500):
    res.append({
      'title': 'The certificate will expire', 
      'description': 'The certificate will expire in {} days'.format(day), 
  	  'solution': "Update your ssl certs or contact us for support",
      'status': 'Low',
      'tool': 'testssl.sh',
      'position': 'top',
      'color': 'yellow',
      'group': "Online Services Results"
    })
  
print(json.dumps(res))