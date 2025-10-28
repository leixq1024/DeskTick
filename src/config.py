"""
Configuration management for DeskTick.
"""

import json
import os
from typing import List, Dict


class Config:
    """Manages application configuration."""
    
    DEFAULT_CONFIG = {
        'stocks': ['000001', '600000', 'AAPL'],
        'refresh_interval': 5000,  # milliseconds
        'window_opacity': 0.9,
        'window_width': 300,
        'window_height': 200,
        'window_x': 100,
        'window_y': 100,
        'always_on_top': True,
        'font_size': 12,
    }
    
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> Dict:
        """Load configuration from file or use defaults."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    return {**self.DEFAULT_CONFIG, **config}
            except Exception as e:
                print(f"Error loading config: {e}, using defaults")
                return self.DEFAULT_CONFIG.copy()
        return self.DEFAULT_CONFIG.copy()
    
    def save_config(self):
        """Save current configuration to file."""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default=None):
        """Get configuration value."""
        return self.config.get(key, default)
    
    def set(self, key: str, value):
        """Set configuration value."""
        self.config[key] = value
    
    def get_stocks(self) -> List[str]:
        """Get list of stock symbols to monitor."""
        return self.config.get('stocks', [])
    
    def add_stock(self, symbol: str):
        """Add a stock symbol to the watchlist."""
        stocks = self.get_stocks()
        if symbol not in stocks:
            stocks.append(symbol)
            self.config['stocks'] = stocks
            self.save_config()
    
    def remove_stock(self, symbol: str):
        """Remove a stock symbol from the watchlist."""
        stocks = self.get_stocks()
        if symbol in stocks:
            stocks.remove(symbol)
            self.config['stocks'] = stocks
            self.save_config()
