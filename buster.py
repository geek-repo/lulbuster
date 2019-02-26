import asyncio
import aiohttp
import time
import os
import time

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



os.system("clear")
print (bc.FAIL+"=========================================================\n")
print (bc.FAIL+"                DIRECTORY BUSTER\n")
print (bc.WARNING+bc.BOLD+"                         MADE BY:- SARTHAK \n")
print (bc.FAIL+"=========================================================\n")

print(bc.HEADER)
url=input("enter the site:")
target=url
target = target.replace('https://', '')
target = target.replace('http://', '')
#target = target.replace('/', '')
target = 'http://' + target
url=target

print (bc.ENDC)
print ("CHOOSE THE WORDLIST:\nEnter 1 for common.txt\nEnter 2 for directory-list-2.3-medium.txt\n")
wordlist=input(">")

async def fetch(client,url,no):
	async with client.get(url) as resp:
		#print ("sending request no. {} to {} and resp code is {}".format(no,url,resp.status))
		if resp.status !=404:
			print ("TARGET FOUND :: {}/ :: STATUS CODE :: {}".format(url,resp.status))
		
		
		
tasks=[]
if wordlist == '1':
	words="/usr/share/wordlists/dirb/common.txt"
	lines="This Wordlist will take upto 3 sec so sit tight for the show"
elif wordlist == '2':
	words="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
	lines="This Wordlist will take upto 30 sec to make all objects..grab some coffee"
files=open(words,"r")
word=[]
for i in files:
	word.append(i)



		
async def main():
	no = 0
	urls = url
	
	async with aiohttp.ClientSession() as client:
		print (bc.BOLD+bc.OKBLUE+"\nCONSTRUCTING THE OBJECTS TO FIRE THE LAZER IN ONE GO ..SIT TIGHT FOR THE LULZ <3\n")
		print (bc.FAIL+"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print (bc.OKBLUE+"Wordlist:{}\n".format(words))
		print (bc.HEADER+"Target :{}\n".format(url))
		print (bc.HEADER+lines)
		print (bc.FAIL+"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		print (bc.OKGREEN)
		for i in word:
			
			urls=urls+"/"
			urls=urls+i
			urls=urls.replace("\n","")
			
			
			no+=1
			task=asyncio.ensure_future(fetch(client,urls,no))
			tasks.append(task)
			urls=url
			#print (tasks)
		await asyncio.gather(*tasks)
		

def start():
	try:
		times=time.time()
		loop = asyncio.get_event_loop()
		loop.run_until_complete(main())
		times2=time.time()
		
	except:
		times2=time.time()
		sub=times2-times
		
		if sub < 5.00:
			
			print (bc.BOLD+"\n\nLeaving me Without even using me ~ onichan")
		
		elif sub <15.00:
			print (bc.BOLD+"Wait Wait if you are using big wordlist it will take time to construct that doesn't mean its crashed lol ;_;")
		
		else:
			print (bc.FAIL+"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print ("TIME TAKEN :- {}".format(sub))
		exit(0)
		
start()
