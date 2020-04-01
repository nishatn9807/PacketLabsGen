import random
import string
from random import shuffle
import sys
import pytz
import json
import time

def remove(string): 
    return string.replace(" ", "") 
	
def randompass(n):

    password = []
    out = " "

    [password.append(random.choice(string.hexdigits)) for i in range(n)]
    password.append(random.choice(string.hexdigits))
    shuffle(password)
    return (remove(out.join(password)))

def main():
	#Amount = int(sys.argv[1])
	#Region = pytz.country_names[str(sys.argv[2])]
	print('@neeshat6 on twitter')
	print('PacketStream Mass Residential Proxy Gen')
	with open("config.json","r") as config_file:
		data = json.load(config_file)
		Hostname = data['host']
		Port = int(data['port'])
		u = str(data['username'])
		p = data['password']
	print("\nLogged in: {}:{}:{}:{}\n".format(Hostname,Port,u,p))
	print()
	correct = input('Is this correct? True or False: ').lower().strip()
	print()
	if(correct == 'true'):	
		Amount = int(input('Proxy Amount: '))
		reg = str(input('Region: '))
		Region  = pytz.country_names[reg]
		type = input('Sticky or rotating: ').lower().strip()
		f = open("proxylist.txt", "a")
		f.truncate(0)
		if(type == 'sticky'):
			for i in range(Amount):
				password = randompass(8)
				f.write("{}:{}:{}:{}_country-{}_session-{}\n".format(Hostname,Port,u,p,(remove(Region)),password))
		elif(type == 'rotating'):
			for i in range(Amount):
				password = randompass(8)
				f.write("{}:{}:{}:{}_country-{}\n".format(Hostname,Port,u,p,(remove(Region))))
		f.close()
		print()
		print("Generated: {} {} proxies   Region: {}  ".format(Amount,type,Region))
		time.sleep(10)
	else:
		print("\nFIX CONFIG FILE\n")
		print("FIX CONFIG FILE")
		time.sleep(5)
		exit()
main()