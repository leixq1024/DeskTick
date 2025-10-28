"""
Test script for DeskTick stock fetcher functionality.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.stock_fetcher import StockDataFetcher


def test_stock_fetcher():
    """Test stock data fetching."""
    print("Testing StockDataFetcher...")
    
    fetcher = StockDataFetcher()
    
    # Test with different stock symbols
    test_symbols = ['600000', '000001', 'AAPL']
    
    for symbol in test_symbols:
        print(f"\nFetching data for {symbol}...")
        data = fetcher.fetch_stock_data(symbol)
        
        if data:
            print(f"  ✓ Success!")
            print(f"  Name: {data.get('name', 'N/A')}")
            print(f"  Price: {data.get('price', 0):.2f}")
            print(f"  Change: {data.get('change', 0):.2f} ({data.get('change_percent', 0):.2f}%)")
        else:
            print(f"  ✗ Failed to fetch data")
    
    print("\n" + "="*50)
    print("Stock fetcher test completed!")


def test_sina_format_conversion():
    """Test symbol format conversion."""
    print("\nTesting symbol format conversion...")
    
    fetcher = StockDataFetcher()
    
    test_cases = [
        ('600000', 'sh600000'),
        ('000001', 'sz000001'),
        ('AAPL', 'gb_aapl'),
        ('300001', 'sz300001'),
    ]
    
    for symbol, expected in test_cases:
        result = fetcher._convert_to_sina_format(symbol)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {symbol} -> {result} (expected: {expected})")


if __name__ == '__main__':
    test_sina_format_conversion()
    test_stock_fetcher()
