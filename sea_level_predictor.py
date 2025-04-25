import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (all data)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all = res_all.slope
    intercept_all = res_all.intercept

    # extend years to 2050
    years_all = pd.Series(range(df['Year'].min(), 2051))
    plt.plot(
        years_all,
        intercept_all + slope_all * years_all,
        'r',
        label='Fit: all data'
    )

    # Create second line of best fit (from 2000 on)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    slope_2000 = res_2000.slope
    intercept_2000 = res_2000.intercept
    years_2000 = pd.Series(range(2000, 2051))
    plt.plot(
        years_2000,
        intercept_2000 + slope_2000 * years_2000,
        'b',
        label='Fit: 2000–present'
    )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()