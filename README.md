# neutralinojs-python-extension-sample
A simple neu application that connects to a python extension file. Started off with the default neu template in cli version `9.2.0`, binary version `4.4.0`, client version `3.3.0`.

## Setup
- Include `"extensions.*"` in the `"nativeAllowList"` inside your `neutralino.config.json` file. <br /> This is so you can call `Neutralino.extension` methods in your client-code.
- Set the option `"enableExtensions": true` inside your `neutralino.config.json` file. <br /> This is so your app tries to use websocket extensions when launched.
- Set the option `"exportAuthInfo": true` inside your `neutralino.config.json` file. <br /> This is what we read from in the extension file to get the necessary information for the websocket connection.

## Alter
- Create a python file in the extensions folder in a folder name of your choice. The extensions folder is in the same directory as your `neutralino.config.json` file. <br /> Check the `extensions/my_python_extension/main.py` for our python extension code.
- Check the existing `resources/index.html` file for modifications to communicate with the extension.
- Check the existing `resources/js/main.js` file for modifications to communicate with the extension.

## Experimental (but works)
- Check the `neutralino.config.json` file for the `"extensions"` array which shows the format of how to call the extension. You'd realize I used a relative path, because I was never successful using the absolute path and including `${NL_PATH}` like specified in the docs. <br /> Also notice that the `"id"` of our extension in this file matches the `NL_EXTID` we use in the python extension file when connecting to the websocket, as well as the `extensionId` in the javascript client file when dispatching (communicating with the extension folder).

## Disclaimers
- There may be better ways to define many of my python functions. I'm a python noob, and just tried converting my nodejs extensions version over to python with the limited knowledge I had.
- You may need to do error handling in your python extension so that it does not crash.
- This python extension uses `websocket_client` to work. You may have to check their [docs](https://pypi.org/project/websocket-client/) to see how to install it <br />(I had lots of problems before it finally worked and had to restart the VSCode for the changes to be recognized, but a familiar python user may experience no problems at all)
- **Distribution:** Not every computer may have python, so you should bundle the python application as an `.exe` when distributing. Don't forget to adjust your `"command"` in your `neutralino.config.json` file to launch that `.exe` instead. <br />I have no idea how to bundle python applications but someone suggested "Module pyinstaller to get a single exe". I have a feeling familiar python users may already know how to do that.
- I removed unnecessary things from the `neutralino.config.json` file for this sample. Your configuration file may differ based on what you need for your own application.

# Icon credits

- `trayIcon.png` - Made by [Freepik](https://www.freepik.com) and downloaded from [Flaticon](https://www.flaticon.com)
