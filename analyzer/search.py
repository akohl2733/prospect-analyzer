import pandas as pd

class ProspectSearcher:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    # filter by president
    def filter_president(self):
        clean = self.df["title"].str.strip().str.lower()
        return self.df[clean.isin({"president", "chancellor"}) & 
                    (self.df["industry"].str.contains('higher education', case=False, na=False))]
        
    # filter by provosts
    def filter_provost(self):
        prov = self.df[
            (self.df["title"].str.contains('provost|academic affairs', case=False, na=False))
        ]
        return prov

    # filter by keywords and industry if wanted
    def filter_by_keywords(self, keywords = list[str], industry = str):
        pattern = "|".join(keywords)
        res = self.df[
            (self.df["title"].str.contains(pattern, case=False, na=False))
        ]
        if industry:
            res = res[self.df["industry"].str.contains(industry, case=False, na=False)]
        return res
    
    # filter by industry alone
    def filter_by_industry(self, industy_substring = str):      # search by industry
        return self.df[self.df['industry'].str.contains(industy_substring, case=False, na=False)]
    
    # determime percentage booked out of total enrollments (total sequences)
    def percent_booked(self, df: pd.DataFrame, sequences: float):
        if df.empty:
            print("No data to analyze.")
            return
        total_contacts = len(df)
        total_meetings = df["meeting"].sum()
        rate = total_meetings / (total_contacts * sequences)
        print(f'\nYou targeted {total_contacts} over the past 6 months and enrolled ~{round(sequences * total_contacts)}')
        print(f"Booking rate per sequence: {rate:.4%} and the total meetings were {total_meetings}")