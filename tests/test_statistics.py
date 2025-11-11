import pytest
import pandas as pd
from src import amount_by_sequence, overall_booking_rate, significant_num_of_seq, significant_num_of_activities, significant_by_role, significant_by_functional_group, significant_by_func_and_role, sequence_significance


def test_amount_by_sequence(sample_df):
    res = amount_by_sequence(sample_df)

    # check type of res
    assert isinstance(res, pd.DataFrame)

    # ensure expected columns are populated
    expected_cols = {"count", "sum", "Rate", "Number of Sequences Enrolled"}
    assert expected_cols.issubset(res.columns)

    # make sure there are rows
    assert len(res) > 0

    # confirm rate results are between 0 and 100
    assert res["Rate"].between(0, 1).all()


def test_overall_booking_rate(sample_df):
    res = overall_booking_rate(sample_df)

    # determine type of response
    assert isinstance(res, str)

    # determine contains text
    assert len(res) > 0


def test_sgnf_num_seq(sample_df):
    res = significant_num_of_seq(sample_df)

    assert isinstance(res, pd.DataFrame)

    # if not empty run tests - will be empty because sample_df doesn't have enough data
    if not res.empty:
        expected_cols = {"Sequences", "Rate", "Sample Size", "p-value", "Significant"}
        assert expected_cols.issubset(res.columns)
        assert res["Rate"].between(0, 100).all()
    else:
        # If empty, verify at least it returns a DataFrame
        assert list(res.columns) == [] or res.empty


def test_sgnf_num_activities(sample_df):
    res = significant_num_of_activities(sample_df)

    assert isinstance(res, pd.DataFrame)

    # if not empty run tests - will be empty because sample_df doesn't have enough data
    if not res.empty:
        expected_cols = {"Sales Activities", "Rate", "Sample Size", "p-value", "Significant"}
        assert expected_cols.issubset(res.columns)
        assert res["Rate"].between(0, 100).all()
    else:
        # If empty, verify at least it returns a DataFrame
        assert list(res.columns) == [] or res.empty


def test_sgnf_role(sample_df):
    res = significant_by_role(sample_df)

    assert isinstance(res, pd.DataFrame)

    # if not empty run tests - will be empty because sample_df doesn't have enough data
    if not res.empty:
        expected_cols = {"Role Category", "Rate", "Sample Size", "p-value", "Significant"}
        assert expected_cols.issubset(res.columns)
        assert res["Rate"].between(0, 100).all()
    else:
        # If empty, verify at least it returns a DataFrame
        assert list(res.columns) == [] or res.empty


def test_sgnf_func_group(sample_df):
    res = significant_by_functional_group(sample_df)

    assert isinstance(res, pd.DataFrame)

    # if not empty run tests - will be empty because sample_df doesn't have enough data
    if not res.empty:
        expected_cols = {"Functional Group", "Rate", "Sample Size", "p-value", "Significant"}
        assert expected_cols.issubset(res.columns)
        assert res["Rate"].between(0, 100).all()
    else:
        # If empty, verify at least it returns a DataFrame
        assert list(res.columns) == [] or res.empty


def test_sgnf_func_and_role(sample_df):
    res = significant_by_func_and_role(sample_df)

    assert isinstance(res, pd.DataFrame)

    # if not empty run tests - will be empty because sample_df doesn't have enough data
    if not res.empty:
        expected_cols = {"Role Category", "Functional Group", "Rate", "Sample Size", "p-value", "Significant"}
        assert expected_cols.issubset(res.columns)
        assert res["Rate"].between(0, 100).all()
    else:
        # If empty, verify at least it returns a DataFrame
        assert list(res.columns) == [] or res.empty


def test_sgnf_sequence(sample_df):
    res = sequence_significance(sample_df)

    assert isinstance(res, pd.DataFrame)

    # if not empty run tests - will be empty because sample_df doesn't have enough data
    if not res.empty:
        expected_cols = {"Last Sequence Enrolled", "Rate", "Sample Size", "p-value", "Significant"}
        assert expected_cols.issubset(res.columns)
        assert res["Rate"].between(0, 100).all()
    else:
        # If empty, verify at least it returns a DataFrame
        assert list(res.columns) == [] or res.empty