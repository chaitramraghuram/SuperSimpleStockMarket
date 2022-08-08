import numpy as np
import pandas as pd


def preferred_dividend_yield(
    fixed_dividend: float, par_value: int, price: float
) -> float:
    """Calculate the preferred dividend yield.

    Args:
        fixed_dividend (float): Fixed dividend
        par_value (int): Par value of the stock
        price (float): Price of the stock

    Returns:
        float: Preferred dividend yield
    """
    return (fixed_dividend * par_value) / price


def common_dividend_yield(last_dividend: float, price: float) -> float:
    """Calculate the common dividend yield.

    Args:
        last_dividend (float): Last dividend
        price (float): Price of the stock

    Returns:
        float: Common dividend yield
    """
    return last_dividend / price


def compute_pe_ratio(last_dividend: int, price: float) -> float:
    """
    Compute the P/E ratio.

    Args:
        last_dividend (int): Last dividend
        price (float): Price of the stock

    Returns:
        float: P/E ratio
    """
    return price / last_dividend


class SimpleStockProcessor(object):
    def __init__(self, df: pd.DataFrame):
        self.data = df

    def get_ticker_data(self, ticker: str) -> pd.DataFrame:
        """Get data for a given ticker

        Args:
            ticker (str): Ticker symbol

        Returns:
            pd.DataFrame: Data associated with a given ticker
        """
        return self.data[self.data["ticker"] == ticker]

    def calculate_vwsp(self, ticker: str, window_length: int = 900) -> pd.Series:
        """Calculate Volume Weighted Stock Price (VWSP) for a given ticker

        Args:
            ticker (str): Ticker symbol

        Returns:
            float: VWSP for a given ticker
        """
        ticker_data = self.get_ticker_data(ticker)
        window_length_str = str(window_length) + "s"
        vwsp = (
            (ticker_data["quantity"] * ticker_data["last_price"])
            .rolling(window_length_str)
            .sum()
        ) / (ticker_data["quantity"].rolling(window_length_str).sum())
        return vwsp

    def calculate_gbce(self):
        """
        Calculate the GBCE All Share Index using the geometric mean of prices for all stocks.
        """
        gbce = np.exp(
            (np.log(self.data["last_price"].astype(float)).sum()) / len(self.data)
        )
