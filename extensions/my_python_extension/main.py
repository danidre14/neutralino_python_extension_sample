#!/usr/bin/env python

import websocket
import uuid
import json
import os

# helper functions
def writeToFile(filename, message):
	outFile = open(filename, "wb")
	outFile.write(bytes(message, "UTF-8"))
	outFile.close()

def readFromFile(filename):
    inFile = open(filename, "rb")
    message = inFile.read()
    message = str(message, "UTF-8")
    inFile.close()
    return message
    

# get authentication info from the file that is regenerated each time the app is launched
authInfo = readFromFile(".tmp/auth_info.json")
authInfo = json.loads(authInfo)

NL_PORT = authInfo["port"]
NL_TOKEN = authInfo["accessToken"]
NL_EXTID = "js.neutralino.sample.my_python_extension"
WS_URL = "ws://localhost:" + str(NL_PORT) + "?extensionId=" + NL_EXTID


def on_error(ws, error):
    print("There is a connection error!")

def on_open(ws):
    print("Connected to application!")

def on_close(ws, close_status_code, close_msg):
    print("Connection has been closed")
    # Make sure to exit the extension process when WS extension is closed (when Neutralino app exits)
    os._exit(0)

def on_message(ws, contents):
    # the typical message sent from the neu application is a string in the form {"data": value, "event": "dispatchedEventName"} so we parse the data here
    if(isinstance(contents, str)):
        message = json.loads(contents)

        # some messages received do not have the "event" key, so safely ignore ethose
        key = "event"
        if key in message:
            # Use extensions.dispatch or extensions.broadcast from the app,
            # to send an event here

            eventName = message["event"]
            
            # this event is received when the neutralino app's window is closed. Thiis code closes the extension websocket connection.
            if(eventName == "windowClose"):
                ws.close()
            elif(eventName == "fromAppToExtension"):
                data = message["data"]
                print("Message received is: " + str(data))

                # Use Neutralinojs server's messaging protocol to trigger native API functions
                # Use app.broadcast method to send an event to all app instances

                global NL_TOKEN
                ws.send(json.dumps({
                    "id": str(uuid.uuid4()),
                    "method": "app.broadcast",
                    "accessToken": NL_TOKEN,
                    "data": {
                        "event": "fromExtensionToApp",
                        "data": "Hey neu app. Python here. You sent me: " + str(data)
                    }
                }))
            


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(WS_URL,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()