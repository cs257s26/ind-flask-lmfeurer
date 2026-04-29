from flask import Flask
import csv

from ProductionCode.command_line import *


app = Flask(__name__)


@app.route('/')
def homepage():
    return "hello, this is the homepage" 

@app.route('/growth/<string:country>')
def growth(country:str):
    """calls the literacy growth function
    Args: 
        country (str): the name of the country to look at. Retrieved from the route
    Returns: 
        the result of the call to function get_country_literacy_growth
    """

    return get_country_literacy_growth (country)

@app.route('/schooling/<string:country>/<int:start>/<int:end>')
def avg_schooling(country:str, start:int, end:int):
    """calls the get_country_average_year_schooling function
    Args: 
        country (str): the name of the country to look at. Retrieved from first part of the route
        start (int): the start year (second part of route)
        end (int): the end date (the final part of route)
    Returns: 
        the result of the call to function get_country_literacy_growth
    """
    return get_country_average_year_schooling(country, start, end)

if __name__ == '__main__':
    load_data()
    app.run(debug=True)