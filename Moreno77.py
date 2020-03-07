# -*- coding: utf-8 -*-
# coding=utf-8
import time,os,sys,requests

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)
	os.system('rm -f login.py;rm -f 2')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s%s ,_     _‚
 |\\\___//|      %sAuthor  : Moreno77%s
 |=6   6=|      %sYoutube : youtube.com/c/DarkCurut08%s
 \=._Y_.=/      %sGithub  : github.com/DarkCurut08%s
  )  `  (    ,  %sTEAM    : Curut BlackHat%s
 /       \  ((
 |       |   ))
/| |   | |\_// %s %s 
\| |._.| |/-`
 '"'   '"' """%(c,r,g,r,g,r,g,r,g,r,w,r))
def regis():
	slowprint('\x1b[00m\033[041m Termux Scurity Login V3 \033[00m')
	u = raw_input('\x1b[00mMasukan Username  : \x1b[33m')
	if u == '' in u:
		regis()
	else:
		p = raw_input('\x1b[00mMasukan Password  : \x1b[33m')
		if p == '' in p:
			regis()
		else:
			slowprint('\033[041m REGISTRATION SUCCESS \033[00m')
			slowprint('\x1b[00m File saved as \x1b[33m/TSLv3/login.py')
			os.system('sleep 3')
			users ="usr='"+u+"'"
			passd ="pwd='"+p+"'"
			os.system('print "'+users+'" > 2;print "'+passd+'" >> 2')
			os.system('print "cd TSLv3" > 4;print "python login.py" >> 4;')
			os.system('cat 1 > login.py;cat 2 >> login.py;cat 3 >> login.py;python login.py')
			os.system('cat 4 > 5;cat $HOME/.bashrc >> 5;mv 5 $HOME/.bashrc;rm -f 2;rm -f 4;cd $HOME')

regis()
