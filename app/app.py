from flask import Flask, config
import subprocess as sp
import traceback
import yaml

mainMessage =  "You are on the main page"
statusPage = ""
config = ""
returnCodes = ""
setup = False

def badException(reason):
    global setup
    global mainMessage

    mainMessage += f"<br>something went wrong whilst {reason}<br>please contact the maintainer"
    setup = False

def log(ex: Exception):
    global setup

    traceback.print_exception(type(ex), ex, ex.__traceback__)
    setup = False

def loadConfig():
    global mainMessage
    global config
    global setup

    try:
        with open('config.yml', 'r') as file:
            config = yaml.safe_load(file)
        setup = True

    except FileNotFoundError as ex:
        mainMessage += "<br>config.yml not found, please check your config file"
        log(ex)

    except Exception as ex:
        badException("opening the config file")
        log(ex)

def parseConfig():
    global mainMessage
    global statusPage
    global returnCodes
    global setup

    try:
        host = config['Server']['host']
        port = config['Server']['port']
        statusPage = config['Server']['statusPage']
        setup = True

    except KeyError as ex:
        mainMessage += "<br>The config [Server] section is faulty<br>please double check"
        log(ex)

    except Exception as ex:
        badException("loading the [Server] section")
        log(ex)

    returnCodes = {}

    try:
        for retCode in config['ReturnCodes']:
            returnCodes[str(config['ReturnCodes'][retCode]['code'])] = {
                'message': config['ReturnCodes'][retCode]['message'],
                'html': config['ReturnCodes'][retCode]['html']
            }
        setup = True if setup else False
    except KeyError as ex:
        mainMessage += "<br>The config [Return Codes] section is faulty<br>please double check"
        log(ex)
    except Exception as ex:
        badException("loading the [Return Codes] section")
        log(ex)

loadConfig()
parseConfig()

app = Flask(__name__)
@app.route("/")
def main():
    return mainMessage, (200 if setup else 501)

@app.route('/greeter/<string:user>')
def greetUser(user):
    return "Hello " + user

@app.route(f'/{statusPage}/<string:service>')
def getStatus(service):
    if not service in config['Scripts']:
        return "Script not registered in config under Scripts", 501

    if not config['Scripts'][service]['enabled']:
        return "This script is disabled", 501
    
    script = sp.run([config['Scripts'][service]['exec'], config['Scripts'][service]['path']])
    return returnCodes[str(script.returncode)]['message'], returnCodes[str(script.returncode)]['html']
    

@app.errorhandler(404)
def error404(error):
    return "This page does not seem to exist, check your call and/or your config", 404
