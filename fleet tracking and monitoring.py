import wiotp.sdk.device
import time
import random
myConfig = {
    "identity":{
        "orgId":"qf6ml5",
        "typeId":"GEC",
        "deviceId":"123456"
     },
     "auth":{
         "token":"12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(button == 1)
    else
    button == 0
    
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def pub(data):
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    
while True:
    myData={'name':'driver','num':7932308456,'lat': 8.0883,'lon': 77.5385}
    pub(myData)
    time.sleep(2)
    myData={'name':'driver','num':7932308456,'lat': 13.0827,'lon': 80.2707}
    pub(myData)
    time.sleep(2)
    myData={'name':'driver','num':7932308456,'lat': 12.9716,'lon': 77.5946}
    pub(myData)
    time.sleep(2)
    myData={'name':'driver','num':7932308456,'lat': 17.3850,'lon': 78.4867}
    pub(myData)
    time.sleep(2)
    myData={'name':'driver','num':7932308456,'lat': 23.2599,'lon': 77.4126}
    pub(myData)
    time.sleep(2)
    myData={'name':'driver','num':7932308456,'lat': 28.7041,'lon': 77.1025}
    pub(myData)
    time.sleep(2)
    myData={'name':'driver','num':7932308456,'lat': 33.2778,'lon': 75.3412}
    pub(myData)
    time.sleep(2)
    client.commandCallback = myCommandCallback
client.disconnect()
