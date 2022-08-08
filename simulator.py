import random
import time
from datetime import datetime

import numpy as np
import pandas as pd

DEFAULT_TICKERS = ["TEA", "POP", "GIN", "ALE", "JOE"]
DEFAULT_MODES = ["Common", "Preferred"]
DEFAULT_PAR_VALUES = [10, 100]
DEFAULT_TRANSACTION_TYPES = ["BUY", "SELL"]


class SimpleStockDataSimulator(object):
    def __init__(
        self,
        fields: list,
        tickers: list = DEFAULT_TICKERS,
        dividend_mode: list = DEFAULT_MODES,
    ):
        """Simulates stock data to mimic a stream but in a dataframe.

        Args:
            fields (list): Fields to be simulated.
            tickers (list, optional): List of ticker symbols to be simulated (Defaults to DEFAULT_TICKERS)
            dividend_mode (list, optional): Dividend mode (Defaults to DEFAULT_MODES)
        """
        self.fields = fields
        self.tickers = tickers
        self.dividend_mode = dividend_mode
        self.data = pd.DataFrame(columns=self.fields)

    def __set_time_as_index(self):
        self.data["time"] = pd.to_datetime(self.data["time"])
        self.data.set_index("time", inplace=True)

    def generate_data(self, duration: int) -> pd.DataFrame:
        """Generate data for a given time duration

        Args:
            duration (int): Time duration in seconds

        Returns:
            pd.DataFrame: Dataframe with simulated data
        """

        tic = time.time()
        index = 0

        while time.time() - tic < duration:
            chosen_mode = np.random.choice(self.dividend_mode, 1)[0]
            last_price = np.random.randint(
                700, 800
            )  # TODO: Price is between 700 and 800. This needs to be input.
            par_val = np.random.choice(DEFAULT_PAR_VALUES, 1)[0]

            self.data.loc[index] = [
                str(datetime.now()),  # Current time as string
                np.random.choice(self.tickers, size=1)[0],  # Pick a ticker at random
                chosen_mode,  # Choose the type of share - Common or Preferred
                last_price,  # Last traded price
                np.random.randint(1, 100),  # Dividend
                (
                    np.random.randint(1, 99) if (chosen_mode == "Preferred") else 0
                ),  # Fixed dividend
                (par_val if (par_val <= last_price) else (last_price - 1)),  # Par value
                np.random.choice(DEFAULT_TRANSACTION_TYPES, size=1)[
                    0
                ],  # Transaction type
                np.random.randint(10, 900),
            ]  # Quantity of shares traded

            index += 1

            time.sleep(random.uniform(0.1, 4))

        self.__set_time_as_index()

        return self.data

    def to_csv(self, filepath_or_buffer: str) -> None:
        """Write the data to a csv file.

        Args:
            filepath_or_buffer (str): Path or the buffer to write the data to.
        """
        self.data.to_csv(filepath_or_buffer)

    def to_parquet(self, filepath_or_buffer: str) -> None:
        """
        Write the data to a parquet file.
        """
        self.data.to_parquet(filepath_or_buffer)
