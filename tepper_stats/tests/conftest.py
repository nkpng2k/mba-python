import pytest
from pathlib import Path

import pandas as pd


@pytest.fixture
def data_dir():
    return Path(__file__).parent / "data"


@pytest.fixture
def refrigerator_data(data_dir):
    data_file = data_dir / "Refrigerator_Data.xlsx"
    yield pd.read_excel(data_file)


@pytest.fixture
def beer_data(data_dir):
    data_file = data_dir / "Beer_Data.xlsx"
    yield pd.read_excel(data_file)
