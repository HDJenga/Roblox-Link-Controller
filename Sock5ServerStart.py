import random
import os
import requests
import json
import socket
import time

curr_time = time.ctime()
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
url = "https://httpbin.org/get"
ip = print(socket.gethostbyaddr(IPAddr))
curr_dir = os.getcwd()
dir_config = "\config.txt"

print(curr_time, ": starting sock5 server on... ", curr_dir)
time.sleep(1)
print(curr_time,": Configuration file", curr_dir, "using reasonable defaults.")
time.sleep(.25)
print(": Path for GeoIPFile (<default>) is relative and will resolve to", curr_dir)
time.sleep(.25)
print("Is this what you wanted?")
time.sleep(.25)
print(curr_time, "[warn] Path for GeoIPFile (<default>) is relative and will resolve to" , curr_dir)
time.sleep(.25)
print("Is this what you wanted?")
time.sleep(1)
print(curr_time, "[notice] Opening Socks listener on", IPAddr)
time.sleep(1)
print(curr_time, "[notice] Opened Socks listener connection (ready) on", IPAddr)
time.sleep(1)
print(curr_time, "[notice] Bootstrapped 0% (starting): Starting")
time.sleep(1)
print(curr_time, "[notice] Bootstrapped 10% (conn_done): Connected to a relay")
time.sleep(2)
print(curr_time, "[notice] Bootstrapped 14% (handshake): Handshaking with a relay")
time.sleep(1)
print(curr_time, "[notice] Bootstrapped 15% (handshake_done): Handshake with a relay done")
time.sleep(4)
print(curr_time, "[notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits")
time.sleep(1)
print(curr_time, "[notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits")
time.sleep(1)
print(curr_time, "[notice] Bootstrapped 95% (circuit_create): Establishing a host circuit")
time.sleep(3)
print(curr_time, "[notice] Bootstrapped 100% (done): Done")











