
# Notify me! when web is up

Script to check if a website is down  or up .  
It notifies when the website is down and when the website has recovered through voice and push notification

## Summary

  - [Getting Started](#getting-started)
  - [Running Notify Me!](#running-notify-me)
  - [Built With](#built-with)
  - [Authors](#authors)


## Getting Started

### Prerequisites
_First of all you need to have installed python3 and pip3_

```
# pip3 installation
sudo apt-get install python3-pip
```

### Installing
_You can install it at your python **or** at your python [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)_


_Installation at the virtual environment:_
```
# Rapid guide python3 virtual environment
python3 -m pip install --user virtualenv

# Installation (in your project folder)
python3 -m venv env
source env/bin/activate
pip install requests
pip3 install -r requirements.txt
```
_Installation at python3:_
```
pip3 install -r requirements.txt
```

## Running Notify Me!
```
$ python3 notify_me_web.py
```
### Common issues

- **geckodriver** wrong permissions

```
Traceback (most recent call last):
 ...
PermissionError: [Errno 13] Permission denied: '/home/sys-walker/notifymeweb/geckodriver'
...
Traceback (most recent call last):
  ...
    raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable may have wrong permissions.
```
```
chmod u+x geckodriver
```


## Built With
* [Python](https://www.python.org/) - Coding language
* [Selenium](https://www.selenium.dev/) - an  automated testing framework used
* [Down for Everyone or Just Me](https://downforeveryoneorjustme.com/)- Website used to check website status

## Authors

  - [**sys-walker**](https://github.com/sys-walker)

