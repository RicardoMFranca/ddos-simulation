import requests
import threading
import time

def flood():
    while True:
        try:
            requests.get("http://192.168.0.105:5000/", timeout=1)
        except:
            pass
        time.sleep(0.05)  # evita travar o sistema com sleep leve

# Só 30 threads impactando sem matar o servidor
for _ in range(30):
    t = threading.Thread(target=flood)
    t.start()