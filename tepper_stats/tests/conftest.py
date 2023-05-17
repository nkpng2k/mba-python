import pytest
from pathlib import Path

import pandas as pd


@pytest.fixture
def refrigerator_data():
    test_data_dir = Path(__file__).parent / "data"
    data_file = test_data_dir / "Refrigerator_Data.xlsx"
    yield pd.read_excel(data_file)
