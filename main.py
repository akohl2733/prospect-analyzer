import pandas as pd
from analyzer.logic import load_contacts, row_to_prospect
from analyzer.search import ProspectSearcher

emails_per_person = 4.76    # constant emails sent per person (on average) -- 17500 / 3677 -- (Total Emails Sent / Total Contacts)
sequences_seen = 1.49       # rough estimate of amount of sequences contacts have been enrolled in based on HubSpot data

if __name__ == "__main__":
    df = load_contacts("contacts.csv")

    kw = ['facilities plan', 'facility plan']
    industry = "education"

    search = ProspectSearcher(df)
    peeps = search.filter_by_keywords(kw, industry)
    for _, row in df.iterrows():
        person = row_to_prospect(row)
        if person.meeting == 1:
            print(person.name + " -- " + person.company + " -- " + person.title + "\n")
    
    search.percent_booked(df, sequences_seen)