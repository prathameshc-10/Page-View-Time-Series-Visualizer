import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_clean_data():
    """Load forum page-view data, index by date, and remove extreme 2.5% tails."""
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    lower_bound = df["value"].quantile(0.025)
    upper_bound = df["value"].quantile(0.975)
    return df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]


def draw_line_plot():
    # Use a copy so this plot cannot modify data used by other charts.
    df = load_and_clean_data().copy()

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.tight_layout()

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Use a copy so this plot cannot modify data used by other charts.
    df = load_and_clean_data().copy()
    df["year"] = df.index.year
    df["month"] = df.index.month

    # Average daily page views for each month, grouped by year.
    df_bar = (
        df.groupby(["year", "month"])["value"]
        .mean()
        .unstack()
    )
    df_bar = df_bar.reindex(columns=range(1, 13))

    fig, ax = plt.subplots(figsize=(10, 7))
    df_bar.plot(kind="bar", ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(
        title="Months",
        labels=[
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
        ],
    )
    fig.tight_layout()

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Use a copy so this plot cannot modify data used by other charts.
    df_box = load_and_clean_data().copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month_num"] = df_box["date"].dt.month
    df_box["month"] = df_box["date"].dt.strftime("%b")

    # Keep months in calendar order (Jan through Dec).
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
    ]
    df_box["month"] = pd.Categorical(
        df_box["month"], categories=month_order, ordered=True
    )

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0], color="lightblue")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[0].tick_params(axis="x", rotation=0)

    sns.boxplot(
        data=df_box, x="month", y="value", order=month_order,
        ax=axes[1], color="lightgreen"
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].tick_params(axis="x", rotation=0)

    fig.tight_layout()
    fig.savefig("box_plot.png")
    return fig
