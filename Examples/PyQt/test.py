import sys
import os
import threading

from time import strftime, gmtime, sleep
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal

class Backend(QObject):
    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(str, arguments=['updater'])
    
    def updater(self, curr_time):
        self.updated.emit(curr_time)

    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()

    def _bootUp(self):
        while True:
            curr_time = strftime("%H:%M:%S", gmtime())
            self.updater(curr_time)
            sleep(0.1)


    

QQuickWindow.setSceneGraphBackend('software')
curr_time = strftime("%H:%M:%S", gmtime())

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

engine.quit.connect(app.quit)
engine.load('Examples/PyQt/UI/main.qml')
engine.rootObjects()[0].setProperty('currTime', curr_time)

back_end = Backend()
engine.rootObjects()[0].setProperty('backend', back_end)
back_end.bootUp()
sys.exit(app.exec())