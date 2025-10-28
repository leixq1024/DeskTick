"""
Stock data fetcher module for DeskTick.
Fetches real-time stock data from public APIs.
"""

import requests
import json
from typing import Dict, Optional


class StockDataFetcher:
    """Fetches stock data from various sources."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_stock_data(self, symbol: str) -> Optional[Dict]:
        """
        Fetch stock data for a given symbol.
        
        Args:
            symbol: Stock symbol (e.g., 'AAPL', '000001.SZ')
            
        Returns:
            Dictionary containing stock data or None if fetch fails
        """
        try:
            # Try multiple data sources for better reliability
            data = self._fetch_from_sina(symbol)
            if data:
                return data
            
            # Fallback to other sources if needed
            return None
            
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None
    
    def _fetch_from_sina(self, symbol: str) -> Optional[Dict]:
        """Fetch data from Sina Finance API."""
        try:
            # Convert symbol format for Sina API
            sina_symbol = self._convert_to_sina_format(symbol)
            
            url = f"https://hq.sinajs.cn/list={sina_symbol}"
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            
            # Parse the response
            content = response.text
            if 'var hq_str_' not in content:
                return None
            
            # Extract data between quotes
            start = content.find('"') + 1
            end = content.rfind('"')
            if start <= 0 or end <= start:
                return None
            
            data_str = content[start:end]
            parts = data_str.split(',')
            
            if len(parts) < 32:
                return None
            
            # Parse stock data
            name = parts[0]
            open_price = float(parts[1]) if parts[1] else 0
            close_price = float(parts[2]) if parts[2] else 0
            current_price = float(parts[3]) if parts[3] else 0
            
            # Calculate change
            change = current_price - close_price if close_price > 0 else 0
            change_percent = (change / close_price * 100) if close_price > 0 else 0
            
            return {
                'symbol': symbol,
                'name': name,
                'price': current_price,
                'open': open_price,
                'close': close_price,
                'change': change,
                'change_percent': change_percent,
                'high': float(parts[4]) if parts[4] else 0,
                'low': float(parts[5]) if parts[5] else 0,
                'volume': int(parts[8]) if parts[8] else 0,
            }
            
        except Exception as e:
            print(f"Sina fetch error for {symbol}: {e}")
            return None
    
    def _convert_to_sina_format(self, symbol: str) -> str:
        """
        Convert stock symbol to Sina Finance format.
        
        Examples:
            '000001' -> 'sz000001' (Shenzhen)
            '600000' -> 'sh600000' (Shanghai)
            'AAPL' -> 'gb_aapl' (US stocks)
        """
        symbol = symbol.upper().strip()
        
        # If already has exchange prefix, return as is
        if '.' in symbol:
            exchange, code = symbol.split('.')
            if exchange == 'SZ':
                return f'sz{code}'
            elif exchange == 'SH':
                return f'sh{code}'
        
        # Chinese A-shares
        if symbol.isdigit():
            if symbol.startswith('6'):
                return f'sh{symbol}'  # Shanghai
            elif symbol.startswith(('0', '3')):
                return f'sz{symbol}'  # Shenzhen
        
        # US stocks and others
        return f'gb_{symbol.lower()}'
