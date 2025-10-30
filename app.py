import sys


from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QToolBar, QMainWindow, QMenu, QDialog
from PyQt6.QtGui import QAction



class Main_GUI(QMainWindow):
    # This function Hold the GUI
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Genetics toolkit')  # Set the title of the main window
        self.setFixedSize(500,500)

        # Create a central widget and layout
        self.central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(self.central_widget)  # Set it as the central widget
        self.layout = QGridLayout(self.central_widget)  # Create a layout for the central widget
               
        # Create a menu bar
        menu_bar = self.menuBar()  # Create the menu bar
        file_menu = menu_bar.addMenu("File")  # Add "File" menu
        help_menu = menu_bar.addMenu("Help")  # Add "Help" menu


        # Create ability to open file and parse data
        open_file_button = QAction("Open File", self)
        open_file_button.setStatusTip("Open a .FASTA or .FASTQ file")

        # Connect the open file action to the menu bar button
        open_file_button.triggered.connect(self.get_file)
        file_menu.addAction(open_file_button)



    def get_file(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv) #create the application
    gui = Main_GUI() # create an instance of the main GUI
    gui.show() # Show the main GUI
    app.exec() # Start the application 