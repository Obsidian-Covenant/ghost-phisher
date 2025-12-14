#!/usr/bin/env python3

import os
import sys

from PyQt6 import QtCore, QtWidgets

# Set Working directory
if 'core' not in os.listdir(os.getcwd()):
    variable = sys.argv[0]
    direc = variable.replace('ghost.py', "")
    os.chdir(direc)

from gui import *

def require_root():
    if os.getenv("LOGNAME", "none").lower() != "root":
        print("Ghost Phisher requires root priviledges to function properly, please run as root.")
        sys.exit(1)

if __name__ == '__main__':
    require_root()

    app = QtWidgets.QApplication(sys.argv)
    run = ghost_phisher.Ghost_phisher()
    run.show()
    sys.exit(app.exec())
