import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_level = pd.read_csv("epa-sea-level.csv", float_precision="legacy")
    # Defining values
    x = sea_level["Year"]
    y = sea_level["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))

    # Scatter plot
    ax = plt.scatter(x, y, s=20, c="darkblue")


    # Create first line of best fit
    first_line = linregress(x, y)
    # Plotting the first line fit
    x_fit_one = np.arange(1880, 2050)
    y_fit_one = (first_line.intercept) + (first_line.slope * x_fit_one)
    ax = plt.plot(x_fit_one, y_fit_one, "r--", label="Fitted line with data 1880-2013")


    # Create second line of best fit
    new_dataset = sea_level[sea_level["Year"] >= 2000]
    x_new = new_dataset["Year"]
    y_new = new_dataset["CSIRO Adjusted Sea Level"]
    second_line = linregress(x_new, y_new)
    # Plotting the second line fit
    x_fit_two = np.arange(2000, 2050)
    y_fit_two = (second_line.intercept) + (second_line.slope * x_fit_two)
    ax = plt.plot(x_fit_two, y_fit_two, label="Fitted line with data 2000-2013", c="darkorange")


    # Add labels and title
    ax = plt.title("Rise in Sea Level")
    ax = plt.xlabel("Year")
    ax = plt.ylabel("Sea Level (inches)")
    ax = plt.legend()
    ax = plt.grid(linestyle="--")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()