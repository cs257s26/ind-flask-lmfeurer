import sys
import csv
import argparse

datasets = {
    "literacy": [],
    "women": []
}

FILENAME_LITERACY = "ProductionCode/literacy-rates-vs-average-years-of-schooling.csv"
FILENAME_WOMEN = "ProductionCode/share-of-women-in-local-government.csv"

def load_data():
    with open(FILENAME_LITERACY, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            datasets["literacy"].append(row)

    with open(FILENAME_WOMEN, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            datasets["women"].append(row)

def recent_high_low_cats(category):
    if category == "literacy rate":
        data_source = datasets["literacy"]
        val_idx = 3  
    
    elif category == "years of schooling":
        data_source = datasets["literacy"]
        val_idx = 4

    elif category == "women in gov":
        data_source = datasets["women"]
        val_idx = 3
    else:
        return "Please enter valid category"
    
    latest_data = {}
    for row in data_source:
        if not row[val_idx]:
            #check if the index is empty (some are)
            continue
            
        country = row[0]
        year = int(row[2])
        value = float(row[val_idx])

        #Compiles a dictionary of the latest available data for every country
        if country not in latest_data or year > latest_data[country]['year']:
            latest_data[country] = {
                'country': country,
                'year': year,
                'value': value
            }

    results = list(latest_data.values())
    results.sort(key=lambda item: item['value'], reverse=True)    
    return {
    "Countries with highest": f"{category} in recent years",
    "highest": results[:5],
    "lowest": results[-5:][::-1] #Gemini hlped here bc i couldn't reverse a dict without resorting it.
}

def get_country_average_year_schooling(country, start_year=None, end_year=None):
    """Returns average years of schooling for a country for any 5 years.

    Args:
        country (str): The country name to look up (case-insensitive).
        start_year (int): Start of year range (inclusive). Defaults None.
        end_year (int): End of year range (inclusive). Defaults None.

    Returns:
        list[dict]: Each dict keys 'year' (int) and 'avg_schooling' (float).
                    Returns empty list if country not found or no data.
    """
    result = []
    for row in datasets["literacy"]:
        if row[0].strip().lower() == country.strip().lower() and row[4].strip():
            year = int(row[2])
            if (start_year is None or year >= start_year) and (end_year is None or year <= end_year):
                result.append({
                    'year': year,
                    'avg_schooling': float(row[4]),
                })

    result.sort(key=lambda r: r['year'])
    return result

def get_country_literacy_growth (country: str) ->str:
    """Calculates change in literacy rate over time in a given country
     Args:
        country (str): The name of the country to retrieve
    Returns:
        str: A string explaining the results.
    """
    data = datasets.get('literacy')
    if not data:
        return "No data available" 
    
    year_index = 2
    lit_index = 3
    country_index = 0

    valid_data = []
    for row in data[1:]:
        if row[country_index] == country and row[lit_index] != "":
            try:
                valid_data.append({"year": int(row[year_index]), "rate": float(row[lit_index])})
            except ValueError:
                continue

    if not valid_data:
        return "No literacy data for this country"
    if len(valid_data) < 2:
        return "Not enough literacy data found for this country" 
    
    valid_data.sort(key=lambda x: x["year"])
    first = valid_data[0]
    last = valid_data[-1]

    percent_increase = (((last["rate"] - first["rate"]) / first["rate"])*100)

    return (f"In {country}, the first recorded literacy rate was {first['rate']}% "
            f"in {first['year']}.<br>Most recently, in {last['year']}, "
            f"the literacy rate was {last['rate']}%.<br>"
            f"That's a {percent_increase:.2f}% increase.")

def main():
    """Parses command line arguments and calls the corresponding function."""
    parser = argparse.ArgumentParser(
        description="Literacy rate, schooling, and women-in-government data."
    )
    parser.add_argument('--country', type=str,
                        help='Country name to look up (e.g. "France")')
    parser.add_argument('--start', type=int, default=None,
                        help='Start year for filtering (e.g. 2015)')
    parser.add_argument('--end', type=int, default=None,
                        help='End year for filtering (e.g. 2020)')
    
    parser.add_argument('--growth', action='store_true',
                        help='Show the literacy growth report for the specified country')
    
    args = parser.parse_args()

    load_data()

    if args.growth and args.country:
        print(get_country_literacy_growth(args.country))
    elif args.country:
        data = get_country_average_year_schooling(args.country, args.start, args.end)
        print(f"No schooling data found for '{args.country}'." if not data else '\n'.join(f"{row['year']}: {row['avg_schooling']} years" for row in data))
    else:
        parser.print_help()


if __name__=='__main__':
    main()