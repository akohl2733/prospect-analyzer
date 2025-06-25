from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class Prospect:
    name: str
    title: str
    email: str
    owner: str
    meeting: int
    sequence_num: int
    company: str
    last_touch: str
    industry: str
    last_call: str

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
        name=row["name"],
        title=row["title"],
        email=row["email"],
        owner=row["owner"],
        meeting=row["meeting"],
        sequence_num=row["sequence_num"],
        company=row["company"],
        last_touch=row["last_touch"],
        industry=row["industry"],
        last_call=row["last_call"]
    )

def plot_booking_rate(summary_df):
    summary_df = summary_df.sort_values("booking_rate", ascending=False)
    summary_df["booking_rate"].plot(kind="bar", figsize=(10, 6), title="Booking Rate by Role Category")
    plt.ylabel("Booking Rate (%)")
    plt.tight_layout()
    plt.savefig("booking_rate_chart.png")