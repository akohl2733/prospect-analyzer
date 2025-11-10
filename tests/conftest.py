import pytest
import pandas as pd


@pytest.fixture
def sample_df():
    data = {
        "Name": ["Andrew Kohl", "Apple Kohl", "Banana Kohl"],
        "Currently In Sequence": [True, False, False],
        "Job Title": ["VP of Corporate Real estate", "Director of Facilities", "Manager of Space Management"],
        "Company": ["Lambent", "Apple", "University of Connecticut"],
        "State": ["North Carolina", "San Francisco", "Connecticut"],
        "Number of Sequences Enrolled": [5, 10, 2],
        "Number of Sales Activities": [40, 57, 17],
        "Create Date": ['6/7/2024', '10/5/2023', '2/17/2025'],
        "Last Sequence Enrolled": [283746581, 827361089, 876543876],
        "Last Sequence Ended Date": ['10/10/2025', '9/10/2025', '8/22/2025'],
        "Last Contacted": ['10/10/2025', '9/10/2025', '8/22/2025'],
        "Last Engagement Date": ['7/24/2025', '9/10/2025', '5/22/2025'],
        "Meeting Booked": [1, 0, 1]}
    return pd.DataFrame(data)