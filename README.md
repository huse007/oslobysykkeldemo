### Oslo Bysykkel Demo
A python Qt5 desktop app for checking available bikes and locks from Oslo Bysykkel at a given station.

## Getting started
```sh
python3 oslobysykkeldemo.py
```
### Prerequisities
The program requires the following dependencies/python libraries:  
requests==2.18.4  
PyQt5==5.11.2

and valid Client-Identifier from https://oslobysykkel.no/api.
Replace "MY-CLIENT-IDENTIFIER" with your api key.
```sh
headers = {"Client-Identifier":" MY-CLIENT-IDENTIFIER "}
```

```sh
pip3 install requests PyQt5 --user
```
or
```sh
pip3 install requests  
sudo apt install python3-pyqt5  
```
### Comments
The application requires internet connectivity, since it uses 
public REST API from http://oslobysykkel.no/api

## Authors
* **Anders Pedersen** - *Initial work* -[huse007](https://github.com/huse007)