import bs4
import requests
import pandas as pd
from scipy.interpolate._cubic import CubicSpline
from matplotlib import pyplot as plt
import numpy as np

response = requests.get("https://en.wikipedia.org/wiki/United_States_Census")


def get_table():
    """
        Initial function

        We use BeautifulSoup to parse the above Wikipedia page to 
        pull the table off the page

        Also, we remove any unnecessary text we pull from the table,
        like the <sup> page element
    """
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'sortable wikitable'})

    for sup in table.find_all("sup", {'class': 'reference'}):
        sup.decompose()

    return table


def get_census_data(table):
    """
        We use this function to actually get html data from the table
        We then insert the data into a DataFrame, and drop
        any headings we don't need

        (we will use years, populations, and slaves from the table)

        Also, we assert that the values we pull are numeric with regex
        NULL values are replaced with 0

        parameters
        ----------
        :param table - the table we get from get_table()
    """
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])
    df.drop(["Change in population",
             "Most populated state",
             "Most populated city",
             "Ethnic demographics counted",
             "Notes"], axis=1, inplace=True)
    df.replace(['/\D/g'], regex=True, inplace=True)
    df.replace('—', 0, inplace=True)
    return df


data = get_census_data(get_table())


def get_yr_and_pop(df):
    """
        function which returns lists of the column data

        parameters
        ----------
        :param df - dataframe with columns from get_census_data()
    """
    list_of_years = df['Year'].to_list()
    list_of_populations = df['Total population'].to_list()
    list_of_slaves = df['Slaves'].to_list()

    return list_of_years, list_of_populations, list_of_slaves


years, populations, slaves = get_yr_and_pop(data)


def graph_cs(x_input, y_input, y_label, title):
    """
        Graph x values with y values that have had cubic spline applied to them

        parameters
        ----------
        :param x_input - x values
        :param y_input - y values, preferable with cubic applied
        :param y_label - label for the y axis
        :param title - name of the graph 
    """
    plt.title(title)
    plt.plot(x_input, y_input, label='Cubic Spline')
    plt.xlabel("years")
    plt.ylabel(y_label)
    plt.legend(loc='best')

    plt.show()


def graph_errors():
    """
        So, this is where the fun happens

        We take a list of population over the years and a list of slaves over the years
        
        steps
        -----
        :param step 1) As we iterate over the years, we assign temporary lists based
        on the existing Census data
        :param step 2) Remove the year, population, and slave data from one row of the table
        :param step 3) Take the Cubic Spline using the popped off variables
            (aka for year, population and year, slaves)
        :param step 4) Calculate the errors based off of the removed y data points
        :param step 5) Append to a list of all error points to be plotted
        :param step 6) Graph the plotted errors over all the years 

    """
    plot_of_population_errors = []
    plot_of_slave_errors = []

    for i in range(len(years)):
        temp_years, temp_populations, temp_slaves = list(
            years), list(populations), list(slaves)
        temp_years.pop(i)
        temp_populations.pop(i)
        temp_slaves.pop(i)

        cs_pop = CubicSpline(temp_years, temp_populations)
        cs_slav = CubicSpline(temp_years, temp_slaves)

        plot_of_population_errors.append(cs_pop(populations[i]))
        plot_of_slave_errors.append(cs_slav(slaves[i]))

    graph_cs(years, plot_of_population_errors,
             "population", "Plot of Population Errors")
    graph_cs(years, plot_of_slave_errors, "slaves", "Plot of Slaves Errors")


def graph_sub(axs, i, cs_func, x_input, y_input, y_label, title):
    """
        Graph subplots using CubicSpline function passed in

        parameters
        ----------
        :param axs - subplot grouping
        :param i - value of subplot we are using
        :param cs - cubic spline polynomial we are mapping y onto
        :param x_input - x values
        :param y_input - y values, preferable with cubic applied
        :param y_label - label for the y axis
        :param title - name of the graph 
    """
    axs[i].set_title(title)
    axs[i].plot(x_input, cs_func(y_input), label='Cubic Spline')
    axs[i].set_ylabel(y_label)
    plt.xlabel("years")
    axs[i].legend(loc='best')


def graph_original_spline():
    """
        These are the natural cubic splines for the year, population dataset
        and year, slaves dataset

        We take the cubic splines of these individually
        Then generate the subplot which comprises of one figure comparing these both
    """
    cs_pop = CubicSpline(years, populations)
    cs_slav = CubicSpline(years, slaves)

    fig, axs = plt.subplots(2)

    graph_sub(axs, 0, cs_pop, years, populations, "population",
              "Cubic Spline on Populaton over Years")
    graph_sub(axs, 1, cs_slav, years, slaves, "slaves",
              "Cubic Spline on Slaves over Years")

    plt.show()


graph_original_spline()
