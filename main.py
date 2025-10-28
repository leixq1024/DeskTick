"""
DeskTick - Real-time Stock Ticker Desktop Widget
Main application entry point.
"""

import sys
from PyQt5.QtWidgets import QApplication
from src.config import Config
from src.widget import DeskTickWidget


def main():
    """Main application entry point."""
    app = QApplication(sys.argv)
    app.setApplicationName("DeskTick")
    
    # Load configuration
    config = Config()
    
    # Create and show main widget
    widget = DeskTickWidget(config)
    widget.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
