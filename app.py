import sys
import os


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

        # LABELS
        self.dialog_label = QLabel("No File Selected", self.central_widget)


        # This is where all the widgets are layed out on the main interface
        self.layout.addWidget(self.dialog_label, 0,0)



    def get_file(self):
        '''
        this block will open a dialog box to allow the user to select their 
        '''

        """ 
        Note the , _ means to throw away the second value as QFileDialog.getOpenFileName
        returns a tuple but a tuple will not work with os.path.basename
        """ 
        self.file_path, _ = QFileDialog.getOpenFileName(
            caption='Select File',
            #filter='Nucleotide Sequence File (*.fasta, *.fastq)',
            directory=os.getcwd()
        )
        
        print(self.file_path)
        if self.file_path:
            file_name = os.path.basename(self.file_path) # This is the file name
            self.dialog_label.setText(f"Selected File:{file_name}") #Update dialog_label with the correct file
            print(f"Full file path: {self.file_path}")
        

if __name__ == '__main__':
    app = QApplication(sys.argv) #create the application
    gui = Main_GUI() # create an instance of the main GUI
    gui.show() # Show the main GUI
    app.exec() # Start the application 
