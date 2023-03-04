# importing the Libraries
import pandas as pd
import matplotlib.pyplot as plt

# The csv file is read into a DataFrame

df_europe_gdp = pd.read_csv('GDP_table_europe.csv', index_col=0)

# create the list of column year to be plotted

year = ['2017', '2018', '2019', '2020', '2021']

# Plotting a line plot of the GDP of the European countries

def plot_gdp_line(df_europe_gdp, x_column, y_cols):
    """
    Plots a line plot of GDP trends for each country over the years.

    Parameters:
    df_europe_gdp (pd.DataFrame): A pandas dataframe with columns as years and rows as countries
    x_column: Represents the label on the x-axis
    y_column: Represents the label on the y-axis
    Returns:
    None
    """
    plt.figure()

    # Plotting the lines for each country
    for country in df_europe_gdp:
        plt.plot(year, df_europe_gdp[country], label=country)

    # Adding labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('GDP (in 100 billion US dollars')
    plt.title('GDP Trends of Six European Countries (2017-2021)')
    plt.legend(loc='upper right')

    plt.show()


plot_gdp_line(df_europe_gdp, 'year', list(df_europe_gdp.columns))

# Plotting a stacked bar of the GDP of the European countries

def stacked_gdp_bar(df_europe_gdp):
    """
    Plots a stacked bar chart of the GDPs of different countries for a particular year.

    Parameters:
    df_europe_gdp (pd.DataFrame): A pandas dataframe with columns as years and rows as countries
    year (int): The year for which the GDPs are to be compared

    Returns:
    None
    """

    df_europe_gdp.plot(kind='bar', stacked=True)
    plt.xlabel('Year')
    plt.ylabel('GDP (in 100 billion US dollars)')
    plt.title(f'Comparison of GDPs for Six European Countries')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

    plt.show()


stacked_gdp_bar(df_europe_gdp)

# Plotting a pie chart of the GDP of the European countries

def plot_gdp_pie(year, countries):
    """
    Plots a pie chart of the GDPs of different countries for a particular year.

    Parameters:
    df_europe_gdp (pd.DataFrame): A pandas dataframe with columns as years and rows as countries
    year (int): The year for which the GDPs are to be compared

    Returns:
    None
    """

    gdp_euro = df_europe_gdp.loc[2021]
    
# plot a pie chart for the last row of the dataframe

# define explode values
    explode = [0, 0, 0.1, 0, 0, 0]

    plt.pie(gdp_euro, labels=gdp_euro.index, autopct='%1.1f%%', explode=explode)

    plt.title('Gross Domestic Product by Country in 2021')
    plt.axis('equal')
    plt.legend(loc='best')
    plt.show()


plot_gdp_pie('year', df_europe_gdp.columns)
