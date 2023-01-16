import machine
import utime
import ustruct

# Initialisation de l'interface I2C en utilisant soft I2C
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

# Adresse I2C du capteur DS1621
DS1621_I2C_ADDRESS = const(0x48)

# Commande pour lire la température
DS1621_CMD_READ_TEMP = const(0xAA)

# Démarrage de la conversion de température
i2c.writeto_mem(DS1621_I2C_ADDRESS, 0xEE, b'')

# Attendre la fin de la conversion
utime.sleep_ms(1000)

# Lecture de la température
data = i2c.readfrom_mem(DS1621_I2C_ADDRESS, DS1621_CMD_READ_TEMP, 2)
temperature = ustruct.unpack('>h', data)[0] / 256
print("La température est de : ",temperature,"C")