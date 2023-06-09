########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################

from Functions import AppFunctions

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        # loadJsonStyle(self, self.ui, jsonFiles = {
        #     "mystyle.json", "style.json"
        #     }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        # CHANGE THE THEME NAME IN SETTINGS
        # Use one of the app themes from your JSON file
        #settings = QSettings()
        
        #settings.setValue("THEME", "Default-Dark")
            
        # RE APPLY THE NEW SETINGS
        # CompileStyleSheet might also work
        # CompileStyleSheet.applyCompiledSass(self)
        #QAppSettings.updateAppSettings(self)

        # Database folder and name
        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/DB_0_1.db'))
        # Run main function to create database and table
        AppFunctions.main(dbFolder)
        # Display db rows in table
        AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbFolder))
        # Add new user to database
        self.ui.addUserBtn.clicked.connect(lambda: AppFunctions.addUser(self, dbFolder))


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
