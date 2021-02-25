import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Clean data
# Dropping rows with non values
df = df.replace(to_replace="None", value=np.nan).dropna()

# Filtering data by removing days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    linePlot = df.plot.line(
        figsize=(15, 6),
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
        xlabel="Date",
        ylabel="Page Views",
        color="crimson",
        legend=False)

    fig = linePlot.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Assigning name to the month integers
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    df_bar["month"] = df_bar["month"].apply(lambda x: months[x-1])

    # Setting month column as categorical data to enable proper sorting
    df_bar["month"] = pd.Categorical(df_bar["month"], categories=months, ordered=True)

    # Groupping data by year and month
    df_bar = pd.DataFrame(df_bar.groupby(["year", "month"]).mean().round(2))
    df_bar.rename(columns={"value": "Average Page Views"}, inplace=True)

    # Creating pivot table
    df_bar = df_bar.reset_index()
    df_bar = df_bar.pivot(index="year", columns="month", values="Average Page Views")

    # Draw bar plot
    barPlot = df_bar.plot.bar(
        figsize=(15, 6),
        xlabel="Years",
        ylabel="Average Page Views",
        legend=True,
        cmap="Paired")

    plt.legend(title="Months")

    fig = barPlot.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Setting month column as categorical data to enable proper sorting
    m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box["month"] = pd.Categorical(df_box["month"], categories=m, ordered=True)

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(15,6))
    sns.boxplot(data=df_box, x="year", y="value", orient="v", ax=ax[0])
    sns.boxplot(data=df_box, x="month", y="value", orient="v", ax=ax[1])
    ax[0].set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")
    ax[1].set(title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig