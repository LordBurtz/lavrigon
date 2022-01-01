# lavrigon
### *A Python Webservice to check the status of any given local service via a REST call (eg. using uptime kumar)*
<br>

## Purpose
Applications such as [Uptime Kuma](https://github.com/louislam/uptime-kuma) help monitoring web applications by making REST Api calls (*and other fancy stuff*). 
This Project extends this functionality to all services running locally. This is archieved by running scripts locally that check the functionality of the requested service and returning an appropriate html return code.
The project is built on scripts users write to check whether a service is functioning. Those scripts have to registered in the `config.yml`.
<br><br>

## Disclaimer
This is not designed to be exposed to the internet or used in a production deployment. 
But it is designed to be run at home for applications such as uptime kumar or similar apps.
The app should work perfectly well in small environments.
<br><br>

## Setup
Clone the repository and enter the directory
```bash
git clone https://github.com/LordBurtz/lavrigon.git && cd lavrigon
```
<br>

Install the requiered dependencies via pip
```bash
pip install -r requierements.txt 
```
<details>
<summary>Flask install Errors</summary>
If pip or pip3 fails to install Flask correctly try installing it via your package manager<br>
</details><br>

Then run the flask app
```bash
cd app && flask run 
```
<br>

Alternatively you can specify port and host:
```bash
flask run -h 0.0.0.0 -p 5007
```
<br><br>

## Le config options
All config options are specified in the `config.yml`.
```yml
Server:
  statusPage: 'status'
  ```
  `statusPage` refers to the page you have to access a service eg. `localhost:5000/{statusPage}/service`

  ```yml
  ReturnCodes:
    working:
        #return code of the script
        code: 0 
        #optional html message returned
        message: "Service up and runnning" 
        #html return code, important for eg. uptime kumar
        html: 200 
    error:
        code: 1
        message: "Service unreachable"
        html: 501
```
```yml
#This is where the actual scripts are registered
Scripts:
  # A short description
  # This script tests the basic functionality
  # The name defines the URL by which the service can checked eg 
  # localhost:5000/status/default in this case
  default:
    # whether the script is enabled or not
    enabled: true
    # executable used, eg bash for a script, python for a .py       
    exec: "/bin/bash" 
    # path of the script as seen by the flask app
    path: "scripts/defaultTest.sh" 
```
<br><br>

## Contributing
Feel free to share the scripts you use and create a pull requests for them to be added to this git repo under [scripts](https://github.com/LordBurtz/lavrigon/tree/main/app/scripts).
