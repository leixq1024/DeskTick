"""
Desktop widget UI for DeskTick.
PyQt5-based transparent, always-on-top stock ticker window.
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                              QScrollArea, QFrame, QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QFont, QColor, QPalette
from typing import List, Dict
from .stock_fetcher import StockDataFetcher
from .config import Config


class StockWidget(QFrame):
    """Individual stock display widget."""
    
    def __init__(self, symbol: str, parent=None):
        super().__init__(parent)
        self.symbol = symbol
        self.data = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI components."""
        self.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.setLineWidth(1)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(2)
        
        # Stock name and symbol
        self.name_label = QLabel(f"{self.symbol}")
        self.name_label.setAlignment(Qt.AlignLeft)
        font = QFont()
        font.setBold(True)
        self.name_label.setFont(font)
        
        # Price information
        self.price_label = QLabel("--")
        self.price_label.setAlignment(Qt.AlignLeft)
        price_font = QFont()
        price_font.setPointSize(14)
        price_font.setBold(True)
        self.price_label.setFont(price_font)
        
        # Change information
        self.change_label = QLabel("--")
        self.change_label.setAlignment(Qt.AlignLeft)
        
        layout.addWidget(self.name_label)
        layout.addWidget(self.price_label)
        layout.addWidget(self.change_label)
        
        self.setLayout(layout)
    
    def update_data(self, data: Dict):
        """Update widget with new stock data."""
        if not data:
            return
        
        self.data = data
        
        # Update name
        name = data.get('name', self.symbol)
        self.name_label.setText(f"{name} ({self.symbol})")
        
        # Update price
        price = data.get('price', 0)
        self.price_label.setText(f"¥{price:.2f}" if price > 0 else "--")
        
        # Update change
        change = data.get('change', 0)
        change_percent = data.get('change_percent', 0)
        
        if change > 0:
            change_text = f"+{change:.2f} (+{change_percent:.2f}%)"
            color = "#FF3333"  # Red for increase
        elif change < 0:
            change_text = f"{change:.2f} ({change_percent:.2f}%)"
            color = "#33FF33"  # Green for decrease
        else:
            change_text = "0.00 (0.00%)"
            color = "#CCCCCC"  # Gray for no change
        
        self.change_label.setText(change_text)
        self.change_label.setStyleSheet(f"color: {color}; font-weight: bold;")


class DeskTickWidget(QWidget):
    """Main desktop widget window."""
    
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.fetcher = StockDataFetcher()
        self.stock_widgets = {}
        self.dragging = False
        self.drag_position = QPoint()
        
        self.init_ui()
        self.init_timer()
    
    def init_ui(self):
        """Initialize the main window UI."""
        # Window properties
        self.setWindowTitle("DeskTick - Stock Ticker")
        self.setWindowFlags(
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Set window geometry
        width = self.config.get('window_width', 300)
        height = self.config.get('window_height', 200)
        x = self.config.get('window_x', 100)
        y = self.config.get('window_y', 100)
        self.setGeometry(x, y, width, height)
        
        # Main container
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background-color: rgba(30, 30, 30, 230);
                border-radius: 10px;
                border: 1px solid rgba(100, 100, 100, 200);
            }
        """)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Title bar
        title_layout = QHBoxLayout()
        title_label = QLabel("DeskTick")
        title_label.setStyleSheet("color: white; font-weight: bold; font-size: 14px;")
        
        close_btn = QPushButton("×")
        close_btn.setFixedSize(20, 20)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 50, 50, 200);
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: rgba(255, 80, 80, 250);
            }
        """)
        close_btn.clicked.connect(self.close)
        
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        title_layout.addWidget(close_btn)
        
        # Stock display area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                border: none;
            }
        """)
        
        self.stock_container = QWidget()
        self.stock_layout = QVBoxLayout()
        self.stock_layout.setSpacing(5)
        self.stock_container.setLayout(self.stock_layout)
        scroll_area.setWidget(self.stock_container)
        
        # Add widgets for configured stocks
        for symbol in self.config.get_stocks():
            self.add_stock_widget(symbol)
        
        main_layout.addLayout(title_layout)
        main_layout.addWidget(scroll_area)
        
        container.setLayout(main_layout)
        
        # Set main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(container)
        self.setLayout(layout)
    
    def add_stock_widget(self, symbol: str):
        """Add a stock widget to the display."""
        if symbol not in self.stock_widgets:
            widget = StockWidget(symbol)
            widget.setStyleSheet("""
                QFrame {
                    background-color: rgba(50, 50, 50, 200);
                    border-radius: 5px;
                    border: 1px solid rgba(80, 80, 80, 200);
                }
                QLabel {
                    color: white;
                }
            """)
            self.stock_widgets[symbol] = widget
            self.stock_layout.addWidget(widget)
    
    def init_timer(self):
        """Initialize the update timer."""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_all_stocks)
        interval = self.config.get('refresh_interval', 5000)
        self.timer.start(interval)
        
        # Do initial update
        self.update_all_stocks()
    
    def update_all_stocks(self):
        """Update data for all stocks."""
        for symbol, widget in self.stock_widgets.items():
            data = self.fetcher.fetch_stock_data(symbol)
            if data:
                widget.update_data(data)
    
    def mousePressEvent(self, event):
        """Handle mouse press for dragging."""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move for dragging."""
        if self.dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release."""
        if event.button() == Qt.LeftButton:
            self.dragging = False
            # Save window position
            self.config.set('window_x', self.x())
            self.config.set('window_y', self.y())
            self.config.save_config()
            event.accept()
    
    def closeEvent(self, event):
        """Handle window close event."""
        # Save window size and position
        self.config.set('window_x', self.x())
        self.config.set('window_y', self.y())
        self.config.set('window_width', self.width())
        self.config.set('window_height', self.height())
        self.config.save_config()
        event.accept()
