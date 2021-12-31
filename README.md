# lavrigon
### A Python Webservice to check the status of any given local service via a REST call (*eg. using uptime kumar*)

## Purpose
Applications such as [Uptime Kuma](https://github.com/louislam/uptime-kuma) help monitoring web applications by making REST Api calls (*and other fancy stuff*). 
This Project extends this functionality to all services running locally. This is archieved by running scripts locally that check the functionality of the requested service and returning an appropriate html return code.
The project is built on scripts users write to check whether a service is functioning. Those scripts have to registered in the `config.yml`.

## Setup
Clone the repository and enter the directory
```bash
git clone https://github.com/LordBurtz/lavrigon.git && cd lavrigon
```
Then run the flask app
```bash
cd app && flask run 
```
Alternatively you can specify port and host:
```bash
flask run -h 0.0.0.0 -p 5007
```

## Contributing
Feel free to share the scripts you use and create a pull requests for them to be added to this git repo under [scripts](https://github.com/LordBurtz/lavrigon/tree/main/app/scripts).
