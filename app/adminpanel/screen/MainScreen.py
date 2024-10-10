from PyQt5.QtWidgets import QMainWindow, QAction, QMenuBar, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and icon
        self.setWindowTitle("Ayush Vision")
        self.setWindowIcon(QIcon("D:\\Research\\Ayushvision\\app\\adminpanel\\asserts\\logo.jpg"))  # Path to your logo image

        # Set window dimensions and theme
        self.setMinimumSize(800, 600)
        self.setStyleSheet("background-color: green;")  # Apply green theme

        # Create layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Dynamic content area
        self.content_area = QWidget(self)
        self.layout.addWidget(self.content_area)

        # Show the onboarding screen first
        self.show_onboarding_screen()

        # Create a menu bar with 3 menus
        self.create_menu_bar()

    def create_menu_bar(self):
        # Create the menu bar
        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu("File")
        new_action = QAction("New", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)  # Close the application on clicking Exit

        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

        # Edit Menu
        edit_menu = menubar.addMenu("Edit")
        copy_action = QAction("Copy", self)
        paste_action = QAction("Paste", self)
        cut_action = QAction("Cut", self)

        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(cut_action)

        # Help Menu
        help_menu = menubar.addMenu("Help")
        about_action = QAction("About", self)

        help_menu.addAction(about_action)

    def show_onboarding_screen(self):
        # Placeholder function for showing onboarding screen
        self.onboarding_screen = QWidget(self)
        self.layout.addWidget(self.onboarding_screen)
        self.onboarding_screen.setStyleSheet("background-color: white;")
        self.setCentralWidget(self.onboarding_screen)

    def show_home_screen(self):
        # Placeholder function for showing home screen
        self.home_screen = QWidget(self)
        self.layout.addWidget(self.home_screen)
        self.setCentralWidget(self.home_screen)