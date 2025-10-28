# DeskTick

<div align="center">

**实时股票盯盘桌面小组件** | **Real-time Stock Ticker Desktop Widget**

一个专为投资者设计的实时股票/ETF盯盘桌面小组件。实时显示价格、涨跌幅，支持多股票同时监控。

A desktop widget designed for investors to monitor real-time stock/ETF prices with live updates of price changes and percentage movements.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://pypi.org/project/PyQt5/)

</div>

## ✨ Features | 功能特性

- 🎯 **Real-time Updates** - 实时更新股票价格
- 📊 **Multi-stock Monitoring** - 同时监控多只股票
- 🎨 **Transparent Widget** - 半透明桌面小组件，不影响工作
- 📌 **Always on Top** - 窗口置顶，随时查看
- 🖱️ **Draggable** - 可拖拽移动到屏幕任意位置
- ⚙️ **Configurable** - 支持自定义配置（股票列表、刷新频率等）
- 🌐 **Multiple Markets** - 支持A股、美股等多个市场
- 💾 **Auto Save** - 自动保存窗口位置和配置

## 📸 Screenshots | 截图

_Desktop widget displaying real-time stock information with price changes and percentages_

## 🚀 Quick Start | 快速开始

### Prerequisites | 前置要求

- Python 3.7 or higher
- PyQt5
- Internet connection for fetching stock data

### Installation | 安装

1. **Clone the repository | 克隆仓库**

```bash
git clone https://github.com/leixq1024/DeskTick.git
cd DeskTick
```

2. **Install dependencies | 安装依赖**

```bash
pip install -r requirements.txt
```

3. **Run the application | 运行应用**

```bash
python main.py
```

## 📖 Usage | 使用说明

### Basic Usage | 基本使用

Simply run the application, and it will display a transparent desktop widget showing real-time stock prices for the configured symbols.

直接运行应用程序，它将显示一个半透明的桌面小组件，展示配置的股票代码的实时价格。

### Configuration | 配置

The first time you run DeskTick, it will create a `config.json` file with default settings. You can edit this file to customize:

首次运行 DeskTick 时，将创建一个 `config.json` 文件。您可以编辑此文件来自定义：

```json
{
  "stocks": ["000001", "600000", "AAPL"],
  "refresh_interval": 5000,
  "window_opacity": 0.9,
  "window_width": 300,
  "window_height": 200,
  "window_x": 100,
  "window_y": 100,
  "always_on_top": true,
  "font_size": 12
}
```

**Configuration Options | 配置选项:**

- `stocks`: List of stock symbols to monitor | 要监控的股票代码列表
- `refresh_interval`: Update interval in milliseconds (default: 5000ms) | 更新间隔（毫秒）
- `window_opacity`: Window transparency (0.0 - 1.0) | 窗口透明度
- `window_width/height`: Widget dimensions | 小组件尺寸
- `window_x/y`: Widget position on screen | 小组件在屏幕上的位置
- `always_on_top`: Keep widget on top of other windows | 保持窗口置顶
- `font_size`: Font size for text display | 文字显示字体大小

### Stock Symbol Format | 股票代码格式

**Chinese A-shares | A股:**
- Shanghai stocks: Use 6-digit code (e.g., `600000` for 浦发银行)
- Shenzhen stocks: Use 6-digit code (e.g., `000001` for 平安银行)

**US stocks | 美股:**
- Use ticker symbol (e.g., `AAPL` for Apple, `MSFT` for Microsoft)

### Controls | 控制

- **Drag to Move** - Click and drag anywhere on the widget to reposition it | 点击并拖拽小组件可移动位置
- **Close** - Click the × button in the top-right corner | 点击右上角的 × 按钮关闭

## 🏗️ Project Structure | 项目结构

```
DeskTick/
├── main.py                 # Application entry point | 应用入口
├── src/
│   ├── __init__.py        # Package initialization | 包初始化
│   ├── config.py          # Configuration management | 配置管理
│   ├── stock_fetcher.py   # Stock data fetcher | 股票数据获取
│   └── widget.py          # Desktop widget UI | 桌面小组件界面
├── requirements.txt       # Python dependencies | Python依赖
├── .gitignore            # Git ignore file | Git忽略文件
├── LICENSE               # MIT License | MIT许可证
└── README.md             # This file | 本文件
```

## 🛠️ Technology Stack | 技术栈

- **Python 3.7+** - Core programming language | 核心编程语言
- **PyQt5** - GUI framework for desktop widget | 桌面小组件GUI框架
- **Requests** - HTTP library for fetching stock data | HTTP库用于获取股票数据
- **Sina Finance API** - Real-time stock data source | 实时股票数据源

## 🔧 Development | 开发

### Running in Development Mode | 开发模式运行

```bash
python main.py
```

### Code Structure | 代码结构

- `main.py`: Application entry point and initialization
- `src/config.py`: Configuration loading and management
- `src/stock_fetcher.py`: Stock data fetching logic
- `src/widget.py`: PyQt5 desktop widget implementation

## 📝 TODO | 待办事项

- [ ] Add support for more stock data sources
- [ ] Implement stock symbol search functionality
- [ ] Add charts and historical data visualization
- [ ] Support for cryptocurrency tracking
- [ ] Multi-language support (i18n)
- [ ] System tray integration
- [ ] Custom alert notifications

## 🤝 Contributing | 贡献

Contributions are welcome! Please feel free to submit a Pull Request.

欢迎贡献！请随时提交 Pull Request。

## 📄 License | 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## ⚠️ Disclaimer | 免责声明

This software is for informational purposes only. Stock data is fetched from public APIs and may have delays. Do not use this as the sole basis for investment decisions. The developers are not responsible for any financial losses.

本软件仅供参考。股票数据来自公共API，可能存在延迟。请勿将其作为投资决策的唯一依据。开发者不对任何金融损失负责。

## 📧 Contact | 联系方式

For questions or suggestions, please open an issue on GitHub.

如有问题或建议，请在 GitHub 上提出 issue。

---

<div align="center">
Made with ❤️ for investors worldwide
</div>
