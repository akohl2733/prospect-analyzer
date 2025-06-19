from dataclasses import dataclass

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