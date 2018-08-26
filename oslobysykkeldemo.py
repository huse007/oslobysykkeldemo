import requests
import json
import locale
import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QComboBox, QVBoxLayout, QMessageBox

""" Credentials and urls """
headers = {"Client-Identifier":" MY-CLIENT-IDENTIFIER "}
url = 'https://oslobysykkel.no/api/v1'
_stations = "/stations"
_availability = "/stations/availability"

""" Get requests for both endpoints, 
depending on whether the function is called 
with or without an id. """
def getData(id=None):
    endpoint=_stations if id==None else _availability
    try:
        response = requests.get(url+endpoint,headers=headers)
        data = response.json()
        list = data["stations"]
        if id == None:
            return list
        else:
            for i in list:
                if i["id"] == id:
                    return i
            raise Exception("Need to update station list")
    except:
        warning()
        return None
    
""" Warning pop-up window with error message.
Close app on Close and window collapse. """
def warning():
    msgBox = QMessageBox(QMessageBox.Warning,"Warning","Can't connect to Oslo Bysykkel. \nCheck your network connection",QMessageBox.Close|QMessageBox.Retry)
    if  msgBox.exec() != QMessageBox.Retry:
        sys.exit()

""" App main loop """        
class OsloBysykkelDemo(QDialog):
    def __init__(self, stations, parent=None):
        super().__init__(parent)

        self.stations = stations
        self.label = QLabel("Choose a station:")
        self.info = QLabel()        
        self.button_combo = QComboBox()
        self.button_combo.setMaxVisibleItems(10)
        self.button_combo.activated.connect(lambda: self.loadData(self.button_combo.currentText()))
        self.button_close = QPushButton("Quit")
        self.button_close.setFixedWidth(60)
        self.button_close.clicked.connect(sys.exit)
        self.fillComboBox("title")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_combo)
        layout.addWidget(self.info)
        layout.addWidget(self.button_close)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)        
        self.setWindowTitle("Oslo Bysykkel Demo")
        self.resize(400,400)
    
    def fillComboBox(self,title):
        self.button_combo.clear()
        for i in self.stations:
            self.button_combo.addItem(i[title])

    """ Get availability object of given station """
    def loadData(self,station_name):
        status = None
        for i in self.stations:
            if i["title"] == station_name:
                status = getData(i["id"])
        if status == None:
            self.info.setText("Information currently unavailable. \nTry again later...")
            """ Uncomment if stations are not permanent """
            #stations = getData()
            self.fillComboBox("title")
        else:
            self.info.setText("Station: "+station_name
                            +"\nAvailable bikes: "+str(status["availability"]["bikes"])
                            +"\nAvailable locks: "+str(status["availability"]["locks"]))
            
def main():
    app = QApplication(sys.argv)
    app.setStyle("windows")
    """ Checks if connected to api """
    while True:
        stations = getData()
        if stations != None:
            break
    win = OsloBysykkelDemo(stations)
    win.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
