import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df.set_index('Year', inplace=True)

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.scatter(df.index, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    def y(x, slope, y0):
        return (slope * x) + y0

    final_year = 2050

    line1 = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    line1_slope, line1_y0 = line1[0:2]

    df1 = df.copy()

    future_years = np.arange(df.iloc[-1].name+1, final_year+1)
    for year in future_years:
        df1.loc[year] = pd.Series({})

    df1['l1'] = y(df1.index, line1_slope, line1_y0)

    ax.plot(df1.index, df1['l1'], color='red')

    # Create second line of best fit
    df_aux = df.loc[df.index >= 2000]
    line2 = linregress(df_aux.index, df_aux['CSIRO Adjusted Sea Level'])
    line2_slope, line2_y0 = line2[0:2]

    df1['l2'] = y(df1.index, line2_slope, line2_y0)
    df2 = df1.loc[df1.index >= 2000]

    ax.plot(df2.index, df2['l2'], color='pink')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()