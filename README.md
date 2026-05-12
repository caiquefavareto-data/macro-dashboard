# Macroeconomic Analytics Dashboard

A real-time data visualization tool built with **Python** and **Streamlit** to monitor global economic indicators, specifically focusing on the energy market and currency trends.

## Overview
This project serves as a bridge between **Economic Theory** and **Data Science**. It automates the extraction of financial data and transforms raw numbers into interactive visual insights. The goal is to provide a clear view of market volatility and asset correlation to support strategic decision-making.

## Tech Stack
* **Language:** Python 3.x
* **Framework:** Streamlit (Web Interface)
* **Data Sources:** Yahoo Finance (yfinance API)
* **Visualization:** Plotly Express
* **Data Manipulation:** Pandas

## Key Features
- **Real-time Data Fetching:** Automated retrieval of Brent Crude Oil futures and USD/BRL Exchange Rates.
- **Interactive UI:** Clean, tab-based navigation separating raw trends from correlation analysis.
- **Statistical Correlation:** Calculates and displays the Pearson Correlation Coefficient between commodity prices and currency fluctuations.
- **Data Caching:** Optimized performance using Streamlit's `@st.cache_data` to minimize API calls.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/macro-dashboard.git](https://github.com/your-username/macro-dashboard.git)