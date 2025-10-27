from analyzer.logic import load_contacts, row_to_prospect, plot_booking_rate
from analyzer.search import ProspectSearcher

emails_per_person = 4.76    # constant emails sent per person (on average) -- 17500 / 3677 -- (Total Emails Sent / Total Contacts)
sequences_seen = 1.49       # rough estimate of amount of sequences contacts have been enrolled in based on HubSpot data

if __name__ == "__main__":
    df = load_contacts("cleaned-data-main-seq-25.csv")
    df['role_category'] = df.apply(lambda row: row_to_prospect(row).get_role_category(), axis=1)
    df['func_group'] = df.apply(lambda row: row_to_prospect(row).get_functional_group(), axis=1)


    summary = df.groupby(["role_category", "func_group"])["Meeting Booked"].agg(["count", "sum"])
    summary['booking_rate'] = (summary["sum"] / summary["count"]) * 100
    print(summary.sort_values("booking_rate", ascending=False).round(2))
    # plot_booking_rate(summary)

    # for _, row in df.iterrows():
    #     person = row_to_prospect(row)
    #     if person.meeting == 1:
    #         print(person.name + " -- " + person.title)
