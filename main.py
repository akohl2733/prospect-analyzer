import pandas as pd
from analyzer.logic import load_contacts
from analyzer.search import ProspectSearcher

emails_per_person = 4.76    # constant emails sent per person (on average) -- 17500 / 3677 -- (Total Emails Sent / Total Contacts)
sequences_seen = 1.49       # rough estimate of amount of sequences contacts have been enrolled in based on HubSpot data

if __name__ == "__main__":
    df = load_contacts("contacts.csv")

    kw = ['space']

    search = ProspectSearcher(df)
    peeps = search.filter_by_keywords(kw)
    

    search.percent_booked(peeps, sequences_seen)