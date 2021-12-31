from flask import Flask, render_template
import subprocess as sp
import yaml

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

host = config['Server']['host']
port = config['Server']['port']

statusPage = config['Server']['statusPage']
returnCodes = {}

for retCode in config['ReturnCodes']:
    returnCodes[str(config['ReturnCodes'][retCode]['code'])] = {
        'message': config['ReturnCodes'][retCode]['message'],
        'html': config['ReturnCodes'][retCode]['html']
    }

app = Flask(__name__)
# app.config.update(
#    SERVER_NAME=f"{host}:{port}"
# )

@app.route("/")
def main() -> str:
    return "Hello on main!"

@app.route('/greeter/<string:user>')
def greetUser(user):
    return "Hello " + user

@app.route(f'/{statusPage}/<string:service>')
def getStatus(service):
    if not service in config['Scripts']:
        return "Script not registered in config under Scripts", 501
    
    script = sp.run([config['Scripts'][service]['exec'], config['Scripts'][service]['path']])
    return returnCodes[str(script.returncode)]['message'], returnCodes[str(script.returncode)]['html']
    

@app.errorhandler(404)
def error404(error):
    return render_template('404.html', name="error"), 404

