import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, 
    QPushButton, QLabel, QCheckBox, QRadioButton, QComboBox,
    QSlider, QProgressBar, QDial, QSpinBox, QLineEdit,
    QTextEdit, QCalendarWidget, QLCDNumber, QListWidget,
    QTreeWidget, QTreeWidgetItem, QTableWidget, QTableWidgetItem,
    QGroupBox, QScrollArea, QToolBox, QStackedWidget, QDateTimeEdit,
    QMenuBar, QStatusBar, QFileDialog, QMessageBox
)
from PySide6.QtGui import QFont, QPixmap, QColor


class QtComponentsDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Components Showcase")
        self.resize(1000, 700)
        
        # Central Widget and Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Tab Widget for Component Categories
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Create demo pages
        self._create_basic_controls_tab()
        self._create_input_widgets_tab()
        self._create_display_widgets_tab()
        self._create_container_widgets_tab()
        self._create_dialogs_demo()
        
        # Status Bar
        self.statusBar().showMessage("Ready")
        
        # Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        
        help_menu = menubar.addMenu("Help")
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self._show_about)

    def _create_basic_controls_tab(self):
        """Buttons, Checkboxes, Radio Buttons"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Buttons
        group_buttons = QGroupBox("Buttons")
        btn_layout = QVBoxLayout()
        
        btn_normal = QPushButton("Normal Button")
        btn_normal.clicked.connect(lambda: self._show_message("Normal button clicked!"))
        
        btn_toggle = QPushButton("Toggle Button")
        btn_toggle.setCheckable(True)
        btn_toggle.toggled.connect(lambda state: self._show_message(f"Toggle: {state}"))
        
        btn_disable = QPushButton("Disabled Button")
        btn_disable.setEnabled(False)
        
        btn_layout.addWidget(btn_normal)
        btn_layout.addWidget(btn_toggle)
        btn_layout.addWidget(btn_disable)
        group_buttons.setLayout(btn_layout)
        
        # Checkboxes & Radio Buttons
        group_selections = QGroupBox("Selections")
        select_layout = QVBoxLayout()
        
        self.checkbox = QCheckBox("Checkbox")
        self.checkbox.stateChanged.connect(self._update_status)
        
        radio1 = QRadioButton("Option 1")
        radio2 = QRadioButton("Option 2")
        radio1.toggled.connect(lambda: self._show_message("Option 1 selected"))
        radio2.toggled.connect(lambda: self._show_message("Option 2 selected"))
        radio1.setChecked(True)
        
        select_layout.addWidget(self.checkbox)
        select_layout.addWidget(radio1)
        select_layout.addWidget(radio2)
        group_selections.setLayout(select_layout)
        
        layout.addWidget(group_buttons)
        layout.addWidget(group_selections)
        layout.addStretch()
        
        self.tabs.addTab(tab, "Basic Controls")

    def _create_input_widgets_tab(self):
        """Sliders, Spinboxes, Comboboxes, Text Input"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Sliders and Dials
        group_sliders = QGroupBox("Sliders & Dials")
        slider_layout = QVBoxLayout()
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self._update_progress)
        
        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.valueChanged.connect(self._update_lcd)
        
        slider_layout.addWidget(QLabel("Horizontal Slider:"))
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(QLabel("Dial Control:"))
        slider_layout.addWidget(self.dial)
        group_sliders.setLayout(slider_layout)
        
        # Text Input
        group_text = QGroupBox("Text Input")
        text_layout = QVBoxLayout()
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Type something...")
        self.line_edit.textChanged.connect(self._update_status)
        
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Multi-line text here...")
        
        text_layout.addWidget(QLabel("Single Line:"))
        text_layout.addWidget(self.line_edit)
        text_layout.addWidget(QLabel("Multi Line:"))
        text_layout.addWidget(self.text_edit)
        group_text.setLayout(text_layout)
        
        layout.addWidget(group_sliders)
        layout.addWidget(group_text)
        layout.addStretch()
        
        self.tabs.addTab(tab, "Input Widgets")

    def _create_display_widgets_tab(self):
        """Labels, LCD, Calendar, Progress Bars"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Progress
        group_progress = QGroupBox("Progress")
        progress_layout = QVBoxLayout()
        
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.slider.valueChanged.connect(self.progress.setValue)
        
        progress_layout.addWidget(self.progress)
        group_progress.setLayout(progress_layout)
        
        # LCD and Calendar
        group_display = QGroupBox("Displays")
        display_layout = QVBoxLayout()
        
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(3)
        self.dial.valueChanged.connect(self.lcd.display)
        
        self.calendar = QCalendarWidget()
        
        display_layout.addWidget(QLabel("LCD Display:"))
        display_layout.addWidget(self.lcd)
        display_layout.addWidget(QLabel("Calendar:"))
        display_layout.addWidget(self.calendar)
        group_display.setLayout(display_layout)
        
        layout.addWidget(group_progress)
        layout.addWidget(group_display)
        layout.addStretch()
        
        self.tabs.addTab(tab, "Display Widgets")

    def _create_container_widgets_tab(self):
        """Tabs, Groups, Scroll Areas, Lists, Tables"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Tab Widget inside Tab Widget (meta!)
        inner_tabs = QTabWidget()
        
        # List Widgets
        tab_lists = QWidget()
        list_layout = QVBoxLayout(tab_lists)
        
        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])
        list_widget.currentItemChanged.connect(
            lambda item: self._show_message(f"Selected: {item.text()}"))
        
        tree_widget = QTreeWidget()
        tree_widget.setHeaderLabels(["Tree Items"])
        top_level = QTreeWidgetItem(tree_widget, ["Parent"])
        QTreeWidgetItem(top_level, ["Child 1"])
        QTreeWidgetItem(top_level, ["Child 2"])
        tree_widget.expandAll()
        
        list_layout.addWidget(QLabel("List Widget:"))
        list_layout.addWidget(list_widget)
        list_layout.addWidget(QLabel("Tree Widget:"))
        list_layout.addWidget(tree_widget)
        
        # Table Widget
        tab_tables = QWidget()
        table_layout = QVBoxLayout(tab_tables)
        
        table = QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(["A", "B", "C"])
        for row in range(3):
            for col in range(3):
                table.setItem(row, col, QTableWidgetItem(f"{row+1}-{col+1}"))
        
        table_layout.addWidget(QLabel("Table Widget:"))
        table_layout.addWidget(table)
        
        inner_tabs.addTab(tab_lists, "Lists & Trees")
        inner_tabs.addTab(tab_tables, "Tables")
        
        layout.addWidget(inner_tabs)
        self.tabs.addTab(tab, "Containers")

    def _create_dialogs_demo(self):
        """Message Boxes and File Dialogs"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        btn_message = QPushButton("Show Message Box")
        btn_message.clicked.connect(self._show_message_box)
        
        btn_file = QPushButton("Open File Dialog")
        btn_file.clicked.connect(self._open_file_dialog)
        
        layout.addWidget(btn_message)
        layout.addWidget(btn_file)
        layout.addStretch()
        
        self.tabs.addTab(tab, "Dialogs")

    # Helper Methods
    def _update_status(self):
        text = self.line_edit.text()
        checked = "Checked" if self.checkbox.isChecked() else "Unchecked"
        self.statusBar().showMessage(f"Status: {text} | Checkbox: {checked}")

    def _update_progress(self, value):
        self.progress.setValue(value)
        self._update_status()

    def _update_lcd(self, value):
        self.lcd.display(value)

    def _show_message(self, text):
        self.statusBar().showMessage(text, 3000)

    def _show_message_box(self):
        QMessageBox.information(self, "Demo", "This is a message box!")

    def _open_file_dialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file:
            self._show_message(f"Selected: {file}")

    def _show_about(self):
        about_text = """<b>Qt Components Showcase</b><br><br>
        This application demonstrates all major Qt widgets<br>
        using PySide6 with Python 3.12.<br><br>
        Created for educational purposes."""
        QMessageBox.about(self, "About", about_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Modern look
    
    window = QtComponentsDemo()
    window.show()
    
    sys.exit(app.exec())
