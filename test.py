"""
Pranay Nandkeolyar and Arav Popli
Period 3
Intermediate Data Programming 

Tests the functions in main.py
using a smaller CSV file from which we can manually 
compute the correct values and test them against the code 
computed values 
"""
from main import get_data
from main import clean_data_plot_1
from main import make_daily
from main import add_allocation
from main import calculate_profit
import pandas as pd
import nltk
# Found vader_lexicon off of ChatGPT
nltk.download('vader_lexicon')
from cse163_utils import assert_equals


def test_filter_tweet():
    """
    Tests the tweet filteration function of main.py
    which is get_data() 
    """
    stock_data, tweet_data = get_data('test_stock.csv', 'test_tweet.csv')
    answer = pd.read_csv('first_tweet_filter.csv',
                         index_col="Timestamp",
                         parse_dates=True)
    assert_equals(tweet_data, answer)
    print("Tweet filter passed")
    return stock_data, tweet_data


def test_allocation(stock_data, tweet_data, isPositive):
    """
    This method tests the add_allocation method in main.py
    """
    trade_data = add_allocation(stock_data, tweet_data, isPositive)
    trade_data.to_csv('trade_result.csv')
    result = pd.read_csv('trade_result.csv')
    answer = pd.read_csv('test_trade.csv')
    assert_equals(result, answer)
    print("Trade Data Test Passed")
    return result


def test_make_daily(tweet_data):
    """
    This method tests the make_daily method in main.py
    """
    tweet_data = make_daily(tweet_data)
    tweet_data.to_csv('daily_result.csv')
    result = pd.read_csv('daily_result.csv')
    answer = pd.read_csv('daily.csv')
    # Compares the the test file daily_result to actual in order to determine
    # that they're identical
    assert_equals(result, answer)
    print("Convert to Daily passed")


def test_plot_1(stock_data, tweet_data):
    """
    This method tests the clean_data_plot_1 method in main.py
    """
    merged = clean_data_plot_1(stock_data, tweet_data)
    merged.to_csv('plot_result.csv')
    result = pd.read_csv('plot_result.csv')
    # answer is a dataframe of our test file for clean_data_plot_1()
    answer = pd.read_csv('test_plot_1.csv')
    assert_equals(result, answer)
    print("Plot 1 filtering passed")


def main():
    """
    Runs the test functions of main.py 
    """
    stock_data, tweet_data = test_filter_tweet()
    test_make_daily(tweet_data)
    test_plot_1(stock_data, tweet_data)
    trade = test_allocation(stock_data, tweet_data, False)
    print("All Tests passed")


if __name__ == '__main__':
    main()
