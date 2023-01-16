from kivy.app import App # import the App class from kivy.app module
from kivy.uix.label import Label # import the Label class from kivy.uix.label module
from kivy.uix.boxlayout import BoxLayout # import the BoxLayout class from kivy.uix.boxlayout module
import paho.mqtt.client as mqtt # import the mqtt library

class TemperatureApp(App):
    def build(self):
        # Create a vertical box layout to hold the widgets
        self.layout = BoxLayout(orientation='vertical')
        # Create a label widget to display the temperature
        self.temp_label = Label(text='Température : ' , font_size=32, color=[0,1,0,1])
        # Add the label widget to the layout
        self.layout.add_widget(self.temp_label)
        # Create an MQTT client object
        self.mqtt = mqtt.Client()
        # Set the MQTT username and password
        self.mqtt.username_pw_set("solo67100", "Orel2006")
        # Connect to the MQTT broker
        self.mqtt.connect("192.168.1.71",1883,5)
        # Subscribe to the "temp/ds1621" topic
        self.mqtt.subscribe("temp/ds1621")
        # Set the on_message callback function
        self.mqtt.on_message = self.on_message
        # Start the MQTT loop
        self.mqtt.loop_start()
        # Return the layout
        return self.layout
    
    def on_message(self, client, userdata, message):
        # Decode the message payload and convert it to a float
        self.temperature = float(message.payload.decode())
        # Update the temperature label text
        self.temp_label.text = "Température : {}°c".format(self.temperature)
        
    def test_connection(self):
        # Check if the application is connected to the MQTT broker
        if self.mqtt.is_connected():
            # Subscribe to the "temp/ds1621" topic
            self.mqtt.subscribe("temp/ds1621")
        else:
            # Connect to the MQTT broker
            self.mqtt.connect("192.168.1.71", 1883, 2)
            # Subscribe to the "temp/ds1621" topic
            self.mqtt.subscribe("temp/ds1621")
            
    def on_connect(self, client, userdata, flags, rc):
        # Check if the connection is successful
        if rc==0:
            # Subscribe to the "temp/ds1621" topic
            self.mqtt.subscribe("temp/ds1621")
        else:
            # Print a message if the connection failed
            print("Connection failed")

if __name__ == '__main__':
    TemperatureApp().run()

       
