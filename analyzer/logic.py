from dataclasses import dataclass
from datetime import datetime
import matplotlib.pyplot as plt

@dataclass
class Prospect:
    name: str
    curr_in_seq: bool
    title: str
    company: str
    state: str
    num_of_seq: int
    num_of_touches: int
    create_date: datetime
    last_seq: int
    last_seq_end_date: datetime
    last_contacted: datetime
    last_engagement_date: datetime
    meeting_booked: int

    def get_role_category(self) -> str:
        title = str(self.title).lower()
        if "president" == title or "chancellor" in title:
            return "President/Chancellor"
        elif "provost" in title or "academic affairs" in title:
            return "Provost/Academic Affairs"
        elif "vp" in title or "vice president" in title:
            return "Vice President"
        elif "executive director" in title or "exec director" in title:
            return "Executive Director"
        elif "director" in title:
            return "Director"
        elif "dean" in title:
            return "Dean"
        elif "manager" in title:
            return "Manager"
        elif "analyst" in title:
            return "Analyst"
        elif "head" in title:
            return "Head"
        elif "project" in title:
            return "Project Manager"
        elif "coordinator" in title:
            return "Coordinator"
        else:
            return "other"
        
    def get_functional_group(self) -> str:
        title = str(self.title).lower()
        if "space" in title:
            return "Space"
        elif "campus plan" in title or "capital" in title:
            return "Campus/Capital"
        elif "facilit" in title:
            return "Facilities"
        elif "academic" in title or "provost" in title:
            return "Academic Affairs"
        elif "finance" in title or "cfo":
            return "finance"
        elif "president" == title or "chancellor" == title:
            return "President/Chancellor"
        elif "workplace" in title:
            return "Workplace"
        elif "real estate" in title:
            return "Real Estate"
        else:
            return "Other"
        
def load_contacts(file_path):
    import pandas as pd

    df = pd.read_csv(file_path)
    return df
    
def row_to_prospect(row):
    return Prospect(
        name=row["Name"],
        curr_in_seq=row["Currently In Sequence"],
        title=row["Job Title"],
        company=row["Company"],
        state=row["State"],
        num_of_seq=row["Number of Sequences Enrolled"],
        num_of_touches=row["Number of Sales Activities"],
        create_date=row["Create Date"],
        last_seq=row['Last Sequence Enrolled'],
        last_seq_end_date=row["Last Sequence Ended Date"],
        last_contacted=row["Last Contacted"],
        last_engagement_date=row["Last Engagement Date"],
        meeting_booked=row["Meeting Booked"],
    )

def plot_booking_rate(summary_df):
    summary_df = summary_df.sort_values("booking_rate", ascending=False)
    summary_df["booking_rate"].plot(kind="bar", figsize=(10, 6), title="Booking Rate by Role Category")
    plt.ylabel("Booking Rate (%)")
    plt.tight_layout()
    plt.savefig("booking_rate_chart.png")