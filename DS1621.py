import machine
import utime
import ustruct
from micropython import const

class DS1621:
    """
    Classe pour communiquer avec le capteur de température numérique DS1621 via I2C.
    pour l'esp32 les selcetionnèes sont : 
    """
    def __init__(self, scl=22, sda=21):
        """
        Initialisation de l'objet pour utiliser le capteur DS1621.

        :param scl: Pin utilisé pour SCL de l'interface I2C.
        :param sda: Pin utilisé pour SDA de l'interface I2C.
        """
        self.scl=scl
        self.sda=sda
        self.i2c = machine.SoftI2C(scl=machine.Pin(self.scl), sda=machine.Pin(self.sda))
        self.address = const(0x48)  # Adresse I2C par défaut du capteur DS1621 A0,A1,A2 connecté à gnd 

    def read_temperature(self):
        """
        Lecture de la température enregistrée par le capteur.
        :return: Température en degrés Celsius.
        """
        # Démarrage de la conversion de température
        self.i2c.writeto_mem(self.address, 0xEE, b'')
        # Attendre la fin de la conversion
        utime.sleep_ms(100)
        # Lecture de la température enregistrée
        data = self.i2c.readfrom_mem(self.address, 0xAA, 2)
        temperature = ustruct.unpack('>h', data)[0] / 256
        return temperature
