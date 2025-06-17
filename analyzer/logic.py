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
    