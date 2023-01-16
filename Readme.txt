- paho-mqtt est installé  et configuré sur mon raspberry
- et kivy sur mon mac 

- DS1621.py contient une classe pour lire la temperature a 0.5 degre près 
--utilisation :
		import ds1621
		import utime
		# Initialisation du capteur DS1621
		sensor = ds1621.DS1621(scl=(22), sda=(21))
		while True:
    		# Lire la température
    		temperature = sensor.read_temperature()
    		#afficher la temperature
    		print(temperature)
    		utime.sleep(60) #attendre 60 secondes

- 	mqtt_ds1621.py permet de publier la temperature sur le broker
	dans le topic "temp/ds1621"


-	dis_temp.py premet de lancer une iterface kivy en tant que client pour afficher la temperature 
	> Il est possible de test la reception dans le terminal via la commande shell
	$ mosquitto_sub -h IP-raspi_ou_nom-raspi -t "#" -u User_MQTT -P Motdepass_MQTT
	$ mosquitto_pub -h P-raspi_ou_nom-raspi -t hom/info -m "salut" -u User_MQTT -P Motdepass_MQTT 
	cette commande permetta des publications avec le terminal

- 	Dans mon boot.py se trouve mon code connection a mon reseau wifi . il est egalement disponible 