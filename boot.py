# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import network
import time

SSID = "SSID_WIFI"
PASSWORD = "MP_WIFI"

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

# Déconnecter l'ESP32 s'il est connecté en mode point d'accès
if ap_if.active():
    ap_if.active(False)

# Connecter l'ESP32 au réseau Wi-Fi
sta_if.active(True)
sta_if.connect(SSID, PASSWORD)

# Vérifier la connexion toutes les secondes pendant 40 secondes
timeout = time.time() + 40
while not sta_if.isconnected():
    if time.time() > timeout:
        print("Connexion échouée, quitter le code.")
        break
    time.sleep(1)
else:
    print('Connecté à ' + SSID)
    print('Adresse IP :', sta_if.ifconfig()[0])
    
    
import gc
gc.collect()