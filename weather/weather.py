import xmltodict
import json
import pprint
import sys

if len(sys.argv) < 2:
  print('To few arguments, please specify a filename')
else:    
  f=open(str(sys.argv[1]),"r")
  xml=f.read()

  pp = pprint.PrettyPrinter(indent=4)
  out=json.dumps(xmltodict.parse(xml),indent=4).replace("@","")
  s=json.loads(out)['current']

  with open('weather.json', 'w') as out:
    json.dump(s, out,indent=4)
  #print (json.dumps(s, indent=4))


