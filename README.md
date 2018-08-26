## Oslo Bysykkel Demo
A python Qt5 desktop app for checking available bikes and locks from Oslo Bysykkel at a given station.

### Getting started
Clone the project:
```sh
git clone https://github.com/huse007/oslobysykkeldemo.git
```
### Prerequisites
The program requires a python3 interpreter and the following dependencies/python libraries:     
* requests==2.18.4  
* PyQt5==5.11.2    
  
and a valid Client-Identifier from https://developer.oslobysykkel.no/api.  
Replace "MY-CLIENT-IDENTIFIER" with your api key.  
```sh
headers = {"Client-Identifier":" MY-CLIENT-IDENTIFIER "}
```

Installation using pip:
```sh
pip3 install requests PyQt5 --user
```
Alternatively, using Ubuntu:
```sh
sudo apt install python3-requests python3-pyqt5
```
### Usage  
Run code:
```sh
python3 oslobysykkeldemo.py
```

### Comments
The application requires internet connectivity, since it uses 
public REST API endpoint https://oslobysykkel.no/api/v1

## Authors
* **Anders Pedersen** - *Initial work* -[huse007](https://github.com/huse007)