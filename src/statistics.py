import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from src import row_to_prospect


def amount_by_sequence(df):
    """Group contacts by number of sequences enrolled and calculate booking rate."""
    amt_of_sequences = (
        df.groupby("Number of Sequences Enrolled")["Meeting Booked"]
            .agg(["count", "sum"])
            .reset_index()
        )
    amt_of_sequences["Rate"] = amt_of_sequences["sum"] / amt_of_sequences["count"]
    return amt_of_sequences


def amount_by_activities(df):
    """Group contacts by number of sales activities and calculate booking rate."""
    amt_of_activities = (
        df.groupby("Number of Sales Activities")["Meeting Booked"]
            .agg(["count", "sum"])
            .reset_index()
    )
    amt_of_activities["Rate"] = amt_of_activities["sum"] / amt_of_activities["count"]
    return amt_of_activities


def overall_booking_rate(df):
    """Print String of overall booking rate of a DataFrame"""
    total_success = (df["Meeting Booked"] != 0).sum()
    total_contacts = len(df)
    overall_rate = total_success / total_contacts * 100
    return f"Overall booking rate: {overall_rate:.3f}%"


def significant_num_of_seq(df):
    """Return DataFrame to check for significance by received sequences."""
    new_df = amount_by_sequence(df)
    results = []
    for _, row in new_df.iterrows():
        n = row["count"]
        x = row["sum"]
        if n < 15:
            continue
        stat, pval = proportions_ztest([x, (df["Meeting Booked"] != 0).sum()], [n, len(df)])
        results.append({
            "Sequences": row["Number of Sequences Enrolled"],
            "Rate": row["Rate"],
            "Sample Size": n,
            "p-value": pval,
            "Significant": pval < 0.05
        })
    sig_df = pd.DataFrame(results)
    return sig_df


def significant_num_of_activities(df):
    """Return DataFrame that highlights significance by total sales activities."""
    new_df = amount_by_activities(df)
    results = []
    for _, row in new_df.iterrows():
        n = row["count"]
        x = row["sum"]
        if n < 15:
            continue
        stat, pval = proportions_ztest([x, (df["Meeting Booked"] != 0).sum()], [n, len(df)])
        results.append({
            "Sales Activities": row["Number of Sales Activities"],
            "Rate": row["Rate"],
            "Sample Size": n,
            "p-value": pval,
            "Significant": pval < 0.05
        })
    sig_df = pd.DataFrame(results)
    return sig_df


def significant_by_role(df):
    """Return DataFrame highlighting significance by role category."""
    df["role_category"] = df.apply(lambda row: row_to_prospect(row).get_role_category(), axis=1)
    summary = (
        df.groupby('role_category')["Meeting Booked"]
        .agg(["count", 'sum'])
        .reset_index()
    )

    summary["Rate"] = summary["sum"] / summary["count"]

    summary = summary[summary["count"] >= 20]

    total_success = (df["Meeting Booked"] != 0).sum()
    total_contacts = len(df)
    overall_rate = total_success / total_contacts

    results = []
    for _, row in summary.iterrows():
        n = row["count"]
        x = row["sum"]

        stat, pval = proportions_ztest([x, total_success], [n, total_contacts])
        results.append({
            "Role Category": row["role_category"],        
            "Rate": row["Rate"],
            "Sample Size": n,
            "p-value": pval,
            "Significant": pval < 0.05
        })
    sig_df = pd.DataFrame(results)
    return sig_df


def significant_by_functional_group(df):
    """Return DataFrame highlighting significance by functional group."""
    df["func_group"] = df.apply(lambda row: row_to_prospect(row).get_functional_group(), axis=1)
    df["role_category"] = df.apply(lambda row: row_to_prospect(row).get_role_category(), axis=1)
    summary = (
        df.groupby(['role_category', "func_group"])["Meeting Booked"]
        .agg(["count", 'sum'])
        .reset_index()
    )

    summary["Rate"] = summary["sum"] / summary["count"]

    summary = summary[summary["count"] >= 20]

    total_success = (df["Meeting Booked"] != 0).sum()
    total_contacts = len(df)
    overall_rate = total_success / total_contacts

    results = []
    for _, row in summary.iterrows():
        n = row["count"]
        x = row["sum"]

        stat, pval = proportions_ztest([x, total_success], [n, total_contacts])
        results.append({
            "Functional Group": row["func_group"],        
            "Rate": row["Rate"],
            "Sample Size": n,
            "p-value": pval,
            "Significant": pval < 0.05
        })
    sig_df = pd.DataFrame(results)
    return sig_df


def significant_by_func_and_role(df):
    """Return DataFrame highlighting significance by role category and functional group."""
    df["role_category"] = df.apply(lambda row: row_to_prospect(row).get_role_category(), axis=1)
    df["func_group"] = df.apply(lambda row: row_to_prospect(row).get_functional_group(), axis=1)
    summary = (
        df.groupby(['role_category', "func_group"])["Meeting Booked"]
        .agg(["count", 'sum'])
        .reset_index()
    )

    summary["Rate"] = summary["sum"] / summary["count"]

    summary = summary[summary["count"] >= 20]

    total_success = (df["Meeting Booked"] != 0).sum()
    total_contacts = len(df)
    overall_rate = total_success / total_contacts

    results = []
    for _, row in summary.iterrows():
        n = row["count"]
        x = row["sum"]

        stat, pval = proportions_ztest([x, total_success], [n, total_contacts])
        results.append({
            "Role Category": row["role_category"],
            "Functional Group": row["func_group"],        
            "Rate": row["Rate"],
            "Sample Size": n,
            "p-value": pval,
            "Significant": pval < 0.05
        })
    sig_df = pd.DataFrame(results)
    return sig_df


def sequence_significance(df):
    """Return DataFrame highlighting significance by sequence."""
    summary = (
        df.groupby("Last Sequence Enrolled")["Meeting Booked"]
        .agg(["count", 'sum'])
        .reset_index()
    )

    summary["Rate"] = summary["sum"] / summary["count"]

    summary = summary[summary["count"] >= 20]

    total_success = (df["Meeting Booked"] != 0).sum()
    total_contacts = len(df)
    overall_rate = total_success / total_contacts

    results = []
    for _, row in summary.iterrows():
        n = row["count"]
        x = row["sum"]

        stat, pval = proportions_ztest([x, total_success], [n, total_contacts])
        results.append({
            "Last Sequence Enrolled": row["Last Sequence Enrolled"],        
            "Rate": row["Rate"],
            "Sample Size": n,
            "p-value": pval,
            "Significant": pval < 0.05
        })
    sig_df = pd.DataFrame(results)
    return sig_df