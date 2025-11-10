import pytest
from src import row_to_prospect, load_contacts


def test_row_to_prospect(sample_df):
    row = sample_df.iloc[0]
    prospect = row_to_prospect(row)

    assert prospect.name == "Andrew Kohl"
    assert prospect.company == "Lambent"
    assert prospect.state == "North Carolina"
    assert prospect.last_seq == 283746581
    assert prospect.last_contacted == "10/10/2025"