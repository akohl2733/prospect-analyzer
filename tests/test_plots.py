import matplotlib
matplotlib.use("Agg")

import pytest
import pandas as pd
import matplotlib.pyplot as plt
from src import booking_rate_by_func, analyze_by_field, results_by_state


# testing booking_rate_by_func function in src/plots.py
def test_booking_rate_by_func(sample_df):
    # create df
    res = booking_rate_by_func(sample_df)

    # Check if Pandas DataFrame
    assert isinstance(res, pd.DataFrame)

    # Verify columns exist 
    expected_cols = {"count", 'sum', "booking_rate"}
    assert expected_cols.issubset(res.columns)

    # Ensure at least 1 combination of functional_group / role is present
    assert len(res) > 0

    # check rate is within bounds
    assert res["booking_rate"].between(0, 100).all()

    # check index names are included
    assert list(res.index.names) == ["role_category", 'func_group']


# testing analyze_by_field function in plots.py
def test_analyze_by_field(sample_df):
    # run function to give plot
    analyze_by_field(sample_df, field="Number of Sequences Enrolled")

    # get current figure and axes (gcf/gca)
    fig = plt.gcf()
    ax = plt.gca()

    # ensure there is a figure present
    assert isinstance(fig, matplotlib.figure.Figure)

    # verify there are bars
    bars = ax.patches
    assert len(bars) > 0

    # determine if axes titles are accurate
    assert "Booking Rate By Number of Sequences Enrolled" in ax.get_title()
    assert "Booking Rate (%)" in ax.get_ylabel()

    # confirm bar height is between 0 and 100
    heights = [bar.get_height() for bar in bars]
    assert all(0 <= h <= 100 for h in heights)

    # cleaning
    plt.close(fig)    


# testing results_by_state function in plots.py
def test_results_by_state(sample_df):
    res = results_by_state(sample_df)

    # confirm type is pandas DF
    assert isinstance(res, pd.DataFrame)

    # determine length is above zero
    assert len(res) > 0

    # Verify columns exist 
    expected_cols = {"State", "count", 'sum', "Rate"}
    assert expected_cols.issubset(res.columns)

    # check rate is between 0 and 100
    assert res["Rate"].between(0, 100).all()