import pandas as pd


class ProspectSearcher:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def filter_president(self):     # search for HE Presidents
        clean = self.df["title"].str.strip().str.lower()
        return self.df[clean.isin({"president", "chancellor"}) & 
                    (self.df["industry"].str.contains('higher education', case=False, na=False))]
        
    def filter_provost(self):     # search for this in academic affairs or provost titles
        prov = self.df[
            (self.df["title"].str.contains('provost|academic affairs', case=False, na=False))
        ]
        return prov

    def filter_by_keywords(self, keywords = list[str]):     # search by keywords
        pattern = "|".join(keywords)
        res = self.df[
            (self.df["title"].str.contains(pattern, case=False, na=False))
        ]
        return res
    
    def filter_by_industry(self, industy_substring = str):      # search by industry
        return self.df[self.df['industry'].str.contains(industy_substring, case=False, na=False)]
    
    def percent_booked(self, df: pd.DataFrame, sequences: float):
        if df.empty:
            print("No data to analyze.")
            return
        total_contacts = len(df)
        total_meetings = df["meeting"].sum()
        rate = total_meetings / (total_contacts * sequences)
        print(f"Booking rate per sequence: {rate:.4%}")