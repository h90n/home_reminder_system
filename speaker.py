from gtts import gTTS
import paho.mqtt.client as mqtt
import os

topic = 'netapphome/alert/0'

#message callback function
def on_message(client, userdata, message):
	serverMessage = str(message.payload.decode("utf-8"))
	tts = gTTS(text=serverMessage, lang='en', slow=False)		#serverMessage into google's text to speech data type
	tts.save("alert.mp3")										#save the tts file 
	os.system("omxplayer alert.mp3")							#play the mp3 file
	
def on_connect(client, userdata, flags, rc):
	client.subscribe(topic)

#MQTT client setup
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.connect("m2m.eclipse.org", 1883)


#look for messages
client.loop_forever()


