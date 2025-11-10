from src import row_to_prospect
import matplotlib.pyplot as plt


def booking_rate_by_func(df):
    df["role_category"] = df.apply(lambda row: row_to_prospect(row).get_role_category(), axis=1)
    df["func_group"] = df.apply(lambda row: row_to_prospect(row).get_functional_group(), axis=1)
    summary = df.groupby(['role_category', "func_group"])["Meeting Booked"].agg(["count", 'sum'])
    summary["booking_rate"] = (summary["sum"] / summary['count']) * 100
    sorted_summary = summary.sort_values("booking_rate", ascending=False).round(2)
    return sorted_summary


def analyze_by_field(df, field, cutoff=None):

    amt_of_sequences = (
        df.groupby(f"{field}")["Meeting Booked"]
            .agg(["count", "sum"])
            .reset_index()
        )
    
    amt_of_sequences["Rate"] = amt_of_sequences['sum'] / amt_of_sequences['count'] * 100
    amt_of_sequences = amt_of_sequences.sort_values(f"{field}")

    if cutoff != None:
        filtered = amt_of_sequences[amt_of_sequences[f"{field}"] <= cutoff]
    else:
        filtered = amt_of_sequences
    
    fig, ax = plt.subplots(figsize=(8,5))
    ax.bar(filtered[f"{field}"], filtered["Rate"], color="steelblue")
    
    ax.set_title(f"Booking Rate By {field}")
    ax.set_xlabel(f"{field}")
    ax.set_ylabel("Booking Rate (%)")
    
    plt.tight_layout()
    plt.show()


def results_by_state(df):
    states = df.groupby("State")["Meeting Booked"].agg(["count", 'sum']).reset_index()
    states["Rate"] = states['sum'] / states['count'] * 100
    states_sorted = states.sort_values("Rate", ascending=False)
    states_sorted[states_sorted["Rate"] > 0]
    return states_sorted