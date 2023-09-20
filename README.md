## Elon Musk - Tweet-Driven Dogecoin Trading Bot: Data-Driven Insights with Python

## Overview

This project is a sophisticated Dogecoin trading bot that is designed to capitalize on Elon Musk's tweets,
which often have a significant impact on Dogecoin prices. The bot utilizes various Python libraries, 
including Pandas, Numpy, Regex, NLTK, Matplotlib, and SciPy, to perform data filtering, cleaning, manipulation, sentiment analysis, 
visualization, and advanced data analysis. The goal is to provide data-driven insights into how Elon Musk's tweets influence Dogecoin prices 
and develop a rudimentary trade bot, offering valuable information to cryptocurrency traders and enthusiasts.

## Features

- **Data Preprocessing**: Data fetched from Kaggle is cleaned and filtered using Pandas, Numpy, and Regex to extract relevant information.

- **Sentiment Analysis**: The NLTK Sentiment Intensity Analyzer is employed to assess the sentiment of Elon Musk's tweets towards Dogecoin.

- **Price Data**: Historical Dogecoin price data is collected from Kaggle.

- **Statistical Analysis**: SciPy's stats module is used to perform advanced statistical analysis on the relationship between Elon Musk's tweets and Dogecoin price movements.

- **Visualization**: Matplotlib is utilized to create visualizations, such as time series charts, volatility charts, and histograms to help traders understand the data.

## Prerequisites

Before you can run this trading bot, you will need to:

- Install Python and the required libraries.
  - Pandas
  - Matplotlib (PyPlot)
  - Numpy
  - Scipy (Stats)
  - NTLK
    - Vader lexicon
    - NLTK.Sentiment (SentimentIntensityAnalyzer) 
  - Re

## Usage

1. Clone this repository to your local machine:
     ```bash
    git clone https://github.com/PranayN23/Elon_Musk_Tweet_NLP_Project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd dogecoin-trading-bot
    ```
3. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

5. Install the required packages:
    ```bash
    pip install <package_name>
    ```
6. Run the trading bot:
   ```bash
    python main.py
    ```

## Contributing

Pranay Nandkeolyar - Lead Developer

Arav Popli - Lead Developer

## How to Contribute

We welcome contributions to the trading bot! If you'd like to contribute, please follow these guidelines:

Fork the repository on GitHub.

Create a new branch with a descriptive name for your feature or bug fix.

Make your changes and ensure they are well-documented.

Test your changes thoroughly.

Submit a pull request to the main repository's master branch.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Special thanks to the creators of the Python libraries and tools used in this project.
- This project was inspired by the interest in understanding the influence of Elon Musk's tweets on the cryptocurrency market.

---

**Disclaimer**: This trading bot is for educational and research purposes only. 
It does not constitute financial advice, and its performance in live trading scenarios may vary. Use it at your own risk.
