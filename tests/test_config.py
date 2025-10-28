"""
Test script for DeskTick configuration management.
"""

import sys
import os
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import Config


def test_config():
    """Test configuration management."""
    print("Testing Config class...")
    
    # Test with a temporary config file
    test_config_file = '/tmp/test_config.json'
    
    # Clean up if exists
    if os.path.exists(test_config_file):
        os.remove(test_config_file)
    
    # Test 1: Create new config with defaults
    print("\n1. Testing default config creation...")
    config = Config(test_config_file)
    stocks = config.get_stocks()
    print(f"  ✓ Default stocks: {stocks}")
    assert len(stocks) > 0, "Should have default stocks"
    
    # Test 2: Add stock
    print("\n2. Testing add_stock...")
    config.add_stock('TSLA')
    stocks = config.get_stocks()
    print(f"  ✓ After adding TSLA: {stocks}")
    assert 'TSLA' in stocks, "TSLA should be in stocks"
    
    # Test 3: Remove stock
    print("\n3. Testing remove_stock...")
    config.remove_stock('TSLA')
    stocks = config.get_stocks()
    print(f"  ✓ After removing TSLA: {stocks}")
    assert 'TSLA' not in stocks, "TSLA should not be in stocks"
    
    # Test 4: Get/Set values
    print("\n4. Testing get/set...")
    config.set('test_key', 'test_value')
    value = config.get('test_key')
    print(f"  ✓ Get test_key: {value}")
    assert value == 'test_value', "Should get correct value"
    
    # Test 5: Config persistence
    print("\n5. Testing config persistence...")
    config.save_config()
    
    config2 = Config(test_config_file)
    value2 = config2.get('test_key')
    print(f"  ✓ Loaded test_key from saved config: {value2}")
    assert value2 == 'test_value', "Should load saved value"
    
    # Clean up
    if os.path.exists(test_config_file):
        os.remove(test_config_file)
    
    print("\n" + "="*50)
    print("Configuration test completed successfully!")


if __name__ == '__main__':
    test_config()
