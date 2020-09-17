#coding=utf-8
#this tool was made for all termux users to understand how termux works
#incase yu wont understand what am doing in this script well SORRY!! 
import os,time,sys
g='\033[1;32m'
p='\033[1;35m'
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
os.system('clear')

print(red+'AUTHOR:Nathan')
time.sleep(0.50)
print('whatsap number:+260978535360')
time.sleep(0.50)
print('Tools name:Termux')
time.sleep(0.50)
print('Features of Tool:Teachers how to use Termux app')
time.sleep(5)
os.system('clear')
banner='''





░░█▀░░░░░░░░░░░▀▀███████░░░░
░░█▌░░░░░░░░░░░░░░░▀██████░░░
░█▌░░░░░░░░░░░░░░░░███████▌░░
░█░░░░░░░░░░░░░░░░░████████░░
▐▌░░░░░░░░░░░░░░░░░▀██████▌░░
░▌▄███▌░░░░▀████▄░░░░▀████▌░░
▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░
▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌
▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌
▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌
░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░
░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░
░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░
░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░
░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░
░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░
░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░
░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░
░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░
▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░
░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄
░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░
░░▄▌████████▄▄▄███████▌░░░░░▄
░▄▀░██████████████████▌▀▄░░░░
▀░░░█████▀▀░░░▀███████░░░▀▄░░
░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░
░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀
░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░
░╔╗║░╔═╗░═╦═░░░░░╔╗░░╔═╗░╦═╗░
░║║║░║░║░░║░░░░░░╠╩╗░╠═╣░║░║░
░║╚╝░╚═╝░░║░░░░░░╚═╝░║░║░╩═╝░'''



def menu():
	os.system('clear')
	time.sleep(1)
	print(banner)
	print(yellow+'TABLE OF CONTENTS')
	time.sleep(1)
	print('[1]Frequently asked questions')
	time.sleep(0.50)
	print('[2]Basic Termux commands')
	time.sleep(0.60)
	print('[3]Basics of Termux packages')
	time.sleep(0.70)
	print('[4]Programming languages in Termux')
	time.sleep(1)
	print('[5]Exit')
	time.sleep(0.80)
	user=int(input('choose a number:'))
	if user==1:
		freq()
	elif user==2:
		Basics_of_Termux()
	elif user==3:
		Basics_of_packages()
	elif user==4:
		 programming_in_termux()
	elif user==5:
		exit()
	else:
		print(red+'invalid option')
		os.system('clear')
		exit()

def freq():
	time.sleep(0.90)
	os.system('clear')
	print(blue+'Frequently asked Questions')
	time.sleep(0.95)
	print('[0]Is Termux easy to use')

	time.sleep(1)
	print('[1]Does Termux require root permission')

	time.sleep(0.50)
	print('[2]Can i become a hacker using Termux app')

	time.sleep(0.30)
	print('[3]is Termux usefu for programmers')
	time.sleep(0.60)
	print('[4]can i use Termux to hack websites')
	time.sleep(0.80)
	print('[5]can i use Termux to hack social media')
	time.sleep(0.90)
	print('[6]Can Termux hack wifi')
	time.sleep(0.35)
	print('[7]Menu')
	user=int(input('choose a question:'))
	if user==0:
		zero()
	elif user==1:
		one()
	elif user==2:
		two()
	elif user==3:
		three()
	elif user==4:
		four()
	elif user==5:
		five()
	elif user==6:
		six()
	elif user==7:
		menu()
	else:
		print(red+'invalid')
		menu()	
def zero():
	time.sleep(0.90)
	print(blue+'well it depends on the experience you have with it and how familia you are with situations if you are new to it yes it can be hard but after some time you will get used and know how to use it ')
	time.sleep(12)
	freq()
def one():
	time.sleep(0.80)
	print(blue+'not really it doesnt but some tools need root to run or should i say operate so if you want to get the most out of the app go ahead and root your device but if you dont wanna go through the rooting risk then stay like that dont root your device you van still hack without root')
	time.sleep(16)
	freq()
def two():
	time.sleep(0.95)
	print(blue+'yes you can but for you to be a hacker you need to know how to use the app and which tools to use take your time and learn the app if you rush you may crash')
	time.sleep(12)
	freq()
def three():
	time.sleep(0.70)
	print(blue+'yes it is but limited')
	time.sleep(3)
	freq()
def four():
	time.sleep(0.78)
	print(blue+'yes you can use it to hack websites but only if you knpw how its done')
	time.sleep(8)
	freq()
def five():
	time.sleep(0.28)
	print(blue+'yes but.... ok its all about knowing which tools to use and how to use them thats when you gonna be sucessful with hacking with termux')
	time.sleep(10)
	freq()
def six():
	time.sleep(0.90)
	print(blue+'yes you can but only if you know which tools to use and :-) ..... finish up :-)')
	time.sleep(10)
	freq()
def exit():
	os.system('exit')
def Basics_of_Termux():
	os.system('clear')
	print(green+'Termux commands are intructions given to the  terminal to perform a specific task')
	time.sleep(1)
	print('please note that for a command to be exexcuted after typing it you will need to hit the enter on your keyboard')
	time.sleep(0.78)
	print(green+'[1]Cool commands')
	time.sleep(1)
	print('[2]Accessing and managing files in termux')
	time.sleep(0.70)
	print('[3]Text editors')
	time.sleep(0.21)
	print('[4]Networking')
	time.sleep(0.30)
	print('[5]main Menu')
	user=int(input('choose a number:'))
	if user==1:
		cool_commands()
	elif user==2:
		managingfiles()
	elif user==3:
		texteditors()
	elif user==4:
		 networking()
	elif user==5:
		menu()
	else:
		print('thats so invalid')
		time.sleep(1)		
		Basics_of_Termux()
		
def cool_commands():
	os.system('clear')
	time.sleep(0.89)
	print(green+'''cmatrix
	what it does:makes the app have a hacker look
	how to install:pkg install cmatrix
	how to run:cmatrix to stop the process make the following combinations ctrl+c
	 sl
	what it does:shows a small cool movin train in termux
	how to install:pkg install sl
	how to run:sl
	top
	what it does:shows the backround running apps in termux
	how to install:its already installed
	how to run:top
	factor
	what it does:outputs the factor of any numbe
	how to install:pkg install coreutils
	how to run:factor 100 thts the commands used to find factor of 100 to find thebrequired number replace 100 with required number
	figlet
	what it does:prints a word in a stylish manner
	how to install:pkg install figlet
	how to run:figlet hi that will display hi in a stylish manner to display your requires word in a stylish manner replace hi with required word
	toilet 
	yep you read that right its toilet the first time i heard it i also had the reaction you have
	what it does:outputs word in a stylish manner
	how to install:pkg install toilet
	how to run:toilet hi replace hi with your required word
	'update
	what it does:it updates build in packages
	how to install:already installed
	how to run:apt update
	'upgrade
	what it does:upgrades your packages to latest
	how to install:already installed
	how to run:apt upgrade''')
	user=int(input('press 0 for menu:'))
	if user == 0:
		Basics_of_Termux()
	else:
		print('Invalid ')
		menu()
def managingfiles():
	os.system('clear')
	time.sleep(1)
	print(green+'Managing files In Termux')
	time.sleep(6)
	print('''cd
	its used to acess a directory or enter inside a directory e.g cd Virus4 will take us into the Virus4 directory
	pwd
	its used to show the path or the directory we are in its usefull when hacking with bruteforce and you want to see the path of the wordlist ls
	its used to see the list of sub directories in a directory e.g  after typing cd Virus4 you won\'t see a thing because you need to type ls to see the sub directories
	rm -rf 
	it deletes a directory e.g when you are  in the home directory maybe for some reason i dont know you want to remove the Virus4 directory just typed rm -rf Virus4 and it will delete it
	mkdir
	it makes a directory e.g mkdir Nathan will create a directory Nathan after hitting enter
	cp
	it copies files from one directory to another e.g cp -r /file path of file you want to copy  leave space /file path of where its going e.g cp -r /$HOME/wordlist.txt /$HOME/Nathan with that command ive moved the wordlist.txt which is in the home directory to the Nathan directory 
	mv 
	mv workd like cp the only difernce is cp copies mv moves 
	zip/unzip
	they zip and unzip files e.g i want to zip Nathan ill type zip Nathan similarily ill do the same when i want to unzip e.g unzip Nathan.zip''')
	user=int(input('press 0 for menu'))
	if user==0:
		Basics_of_Termux()	

def texteditors():
	os.system('clear')
	time.sleep(1)
	print(green+'Text Editors')
	time.sleep(1)
	print('''i honestly just know two text editors in Termux but maybe they are more i dont know''')
	time.sleep(1)
	print(''' the two text editors are nano and vim''')
	time.sleep('type pkg install nano/vim to install either of them')
	time.sleep(1)
	print('type nano or vim to open either of them')
	time.sleep(1)
	print('you can also see the source codes of some tools by typing nano and the file tool')
def networking():
	os.system('clear')
	time.sleep(1)
	print(green+'Let\'s talk about Networking')
	time.sleep(1)
	print('''ifconfig Command is used to get all the information regarding to your Network IP 
address To check a particular website is accessible or not in your ISP then you can check
that through termux by typing
ping website
Eg: ping google.com The Interesting thing is you can access the internet through termux, directly in
command line Firstly you have to install w3m package by typing
pkg install w3m After that type below command to access any website
w3m website
eg: w3m google.com Lynx is similar to w3m
To install lynx, type pkg install lynx
After that type lynx google.com Not Only These you can use many other commands such as cat, man etc. on termux''')
	user=int(input('Press 0 to go to menu:'))
	if user==0:
		Basics_of_Termux()
	else:
		print('invalid option')
		time.sleep(1)
		menu()
def Basics_of_packages():
	os.system('clear')
	time.sleep(1)
	print(green+'Basics of Termux packages')
	time.sleep(1)
	print('''Termux Packages are more Interesting, in order to manage them we have to use pkg
command Termux Packages Comes With all the necessary scripts as required to run a specific
program.For example
what should usually we do when we have to install and use python on our system we goto
python.org and download the required python version and we use an IDLE as compatible to
our device architecture while linux users have pre installed But in termux we can install python just by typing pkg install python just typing pkg help you will know how to use pkg commandsNot only this, Termux also have a lot helpful packages such as nmap, hydra and a lot.''')
	user=int(input('press 0 for menu:'))
	if user==0:
		Basics_of_Termux()
	else:
		print('Wrong option')
		time.sleep(1)	
		menu()
def programming_in_termux():
	os.system('clear')
	time.sleep(1)
	print(blue+'Programming Languages')
	time.sleep(1)
	print('''You may think C, C++, Java, Python, Ruby, Php,Perl etc.Exactly the same Termux is such a powerful linux environment that can handle the above
Programming Languages.
● C
● C++
● Python 3.x
● Python 2.7
● Ruby
● Perl
● PHP
● And So On To install and use We have to just type pkg install clang During installation you will be asked that Termux Will use some space just type y and similarly we can install Python 2.7 by typing pkg install python2''')
	time.sleep(1)
	print('for Ruby:pkg install ruby')
	time.sleep(1)
	print('for php:pkg install php')
	time.sleep(1)
	print('for perl:pkg install perl')
	time.sleep(1)
	print('''for python3:pkg install python''')
	user =int(input('press 0 to go to menu:'))
	if user == 0:
		menu()
	else:
			print(red+'wrong option')
			menu()
	
print(menu())
