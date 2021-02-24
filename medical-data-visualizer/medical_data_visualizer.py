import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
# Dropping rows with non values

# BMI calculations
BMI = df["weight"] / ((df["height"] / 100) ** 2)

# Add 'overweight' column
df["overweight"] = (BMI > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(["cardio" , "variable" , "value"])["value"].count())
    df_cat.rename(columns={"value": "total"}, inplace=True)
    df_cat.reset_index(inplace=True)

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar").fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data

    # Filters: 
    # - Removing data with diastolic pressure (ap_lo) higher than systolic (ap_hi)
    # - Removing data with height less than the 2.5th percentile and height higher than the 97.5th percentile
    # - Removing data with weight less than the 2.5th percentile and weight higher than the 97.5th percentile

    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) & 
        (df["height"] >= df["height"].quantile(0.025)) & 
        (df["height"] <= df["height"].quantile(0.975)) & 
        (df["weight"] >= df["weight"].quantile(0.025)) & 
        (df["weight"] <= df["weight"].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, cmap="vlag", fmt=".1f", linewidth=0.3, cbar_kws={"shrink": .6, "format": "%.2f"})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
