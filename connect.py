import server.mqtt as connector
import numberGenerator

client = connector.mqtt.Client()
client.on_connect = connector.on_connect
client.on_message = connector.on_message
client.connect("10.10.10.29", 1883, 60)
client.loop_start()

while True:
    for x in range(1,500):
        numberGenerator.time.sleep(.5)
        client.publish('test',numberGenerator.getTempature(x/30))
