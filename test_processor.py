import pytest
from sssm import SimpleStockDataSimulator, SimpleStockProcessor
from sssm.processor import compute_pe_ratio

COLUMNS = [
    "time",
    "ticker",
    "type",
    "last_price",
    "dividend",
    "fixed_dividend",
    "par_value",
    "transaction_type",
    "quantity",
]


class TestProcessorClass:
    def test_init(self):
        simulator = SimpleStockDataSimulator(COLUMNS)
        df = simulator.generate_data(15)
        processor = SimpleStockProcessor(df)
        assert len(processor.data) == len(
            simulator.data
        ), "Dataframe is not the same length as the simulator"

    def test_headers(self):
        simulator = SimpleStockDataSimulator(COLUMNS)
        df = simulator.generate_data(15)
        processor = SimpleStockProcessor(df)
        assert all(
            processor.data.columns == COLUMNS[1:]
        ), "Columns in the processor are not correct"

    def test_pe_ratio(self):
        ratio = compute_pe_ratio(10, 100)
        assert ratio == 10.0, "P/E ratio incorrect"
