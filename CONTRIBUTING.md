# Contributing to DeskTick

Thank you for your interest in contributing to DeskTick! This document provides guidelines for contributing to the project.

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/leixq1024/DeskTick.git
   cd DeskTick
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests**
   ```bash
   python tests/test_config.py
   python tests/test_fetcher.py
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## Project Structure

```
DeskTick/
├── main.py              # Application entry point
├── src/
│   ├── config.py        # Configuration management
│   ├── stock_fetcher.py # Stock data fetching
│   └── widget.py        # PyQt5 UI implementation
├── tests/               # Test suite
├── requirements.txt     # Python dependencies
├── setup.py            # Package setup
└── README.md           # Documentation
```

## Coding Standards

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings for all functions and classes
- Keep functions focused and modular
- Write tests for new features

## Adding New Features

1. Create a new branch for your feature
2. Implement the feature with appropriate tests
3. Update documentation as needed
4. Ensure all tests pass
5. Submit a pull request

## Adding New Stock Data Sources

To add a new stock data source:

1. Add a new method in `src/stock_fetcher.py`
2. Follow the pattern of existing methods
3. Return data in the standard format:
   ```python
   {
       'symbol': str,
       'name': str,
       'price': float,
       'change': float,
       'change_percent': float,
       ...
   }
   ```

## Reporting Issues

When reporting issues, please include:
- DeskTick version
- Python version
- Operating system
- Steps to reproduce the issue
- Expected vs actual behavior
- Any error messages or logs

## Pull Request Process

1. Update README.md with details of changes if needed
2. Update tests to cover new functionality
3. Ensure code follows project standards
4. Update version number if applicable
5. The PR will be merged once approved by maintainers

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Maintain a harassment-free environment

## License

By contributing to DeskTick, you agree that your contributions will be licensed under the MIT License.
