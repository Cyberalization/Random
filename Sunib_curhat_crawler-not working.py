import requests
from os import system
from bs4 import BeautifulSoup
import re
from time import *
gender=[]
age=[]
desc=[]
page=[]
index=0
index_of_page=1
url1 = 'http://sunibcurhat.com/'
p = ''
flag = 0
def crawl(url,angka):
	global gender
	global age
	global desc
	global page
	global index
	#url = "http://sunibcurhat.com/"
	#print p.status_code
	p = requests.get(url)
	s = BeautifulSoup(p.content,'html.parser')
	allUsers = s.findAll('div',class_='card-body py-4')
	
	for i in allUsers:
		j = i.findAll('h5') 
		for k in j:
			page.append(angka)
			jenis,umur = k.text.split(',') 
			gender.append(jenis)
			age.append(umur)

		l = i.findAll('p',class_='description mt-3')
		for m in l:
			desc.append(m.text.encode('ascii', 'ignore'))
		
			
def menu1():
	print''
	limiter=0
	while limiter==0:
		try:
			limiter = int(raw_input(' input limiter for target url: '))
		except :
			limiter=0
	print ' Crawling start!!!...'
	global p
	global index_of_page
	global url1
	global flag
	global index
	print ''
	index_of_page = 1
	while True:
		url1 = ' http://sunibcurhat.com/?page='+str(index_of_page)
		p = requests.get(url1)
		if p.status_code==200:
			print " crawling page-"+url1+" ..."
			crawl(url1,index_of_page)
			index_of_page+=1
			if index_of_page > limiter:#limiter soalnya ga abis abis awkawkawk
				print ' Crawling Done!'
				raw_input(' press enter to continue..')
				flag=1
				system(' cls')
				break
		sleep(2) # biar ga di 'reset' sama sunib curhat 
		


def menu2():
	global gender
	global age
	global desc
	global flag
	global page
	global index
	if flag==0:
		print ' Please crawl the website first!'
		raw_input(' press enter to continue..')
		system('cls')
		return 
	for x in range(len(gender)):
		gdr =''
		if re.search('Male',gender[x]):
			gdr = '\t'
		print" ================================================================"
		print ' | '+str(x+1)+' | Page: '+str(page[x])+' | gender: '+gender[x]+gdr+'\t| Age: '+age[x]+"   \t\t|"
		print ' ----------------------------------------------------------------'
		print ' | curhatan:                                      	\t|'
		temp = list(re.findall('.{1,50}',desc[x]))

		for d in list(temp):
			if len(d)<50:
				a = 50-len(d)
				for i in range(a):
					d+=' '
			print ' | '+d+"       \t|"
		print ' ================================================================'
		print ''
	print" that's all!"
	raw_input(' press enter to continue..')

def menu():
	while True:
		ch=0
		system('cls')
		print ''
		print' Web Crawler made by Serein :3'
		print' ============================='
		print' 1. crawl SunibCurhat!'
		print' 2. view all data from that url'
		print' 3. exit'
		while ch==0:
			try:
				ch = int(raw_input(' >> '))
			except:
				ch=0
		if ch==1:
			menu1()
		elif ch==2:
			menu2()

		else:
			break
			system('cls')
			exit()


if __name__ == "__main__":
	menu()



