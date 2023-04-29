import subprocess
import time
import platform

if platform.system() == 'Windows':
    server_start = subprocess.Popen('start cmd /k python components/server.py', shell=True)
    time.sleep(1)
    client_start = subprocess.Popen('start cmd /k python components/client.py', shell=True)

elif platform.system() == 'Linux':
    server_start = subprocess.Popen('start cmd /k python components/server.py', shell=True)
    time.sleep(1)
    client_start = subprocess.Popen('start cmd /k python components/client.py', shell=True)

client_start.wait()
server_start.kill()