# README

**Individual Flask project.**

URL Information:
- To see the growth rate in literacy rate over time in Mexico, enter http://127.0.0.1:PORT/growth/Mexico
- To see the data corresponding to the average years of schooling between 2010 and 2020 in France, enter http://127.0.0.1:PORT/schooling/France/2010/2020

**Individual Database Project.**

Copy Commands: 

`\copy literacy_rates_vs_avg_years_of_schooling FROM 'Data/literacy-rates-vs-average-years-of-schooling.csv' DELIMITER ',' CSV`

`\copy women_in_gov FROM 'Data/share-of-women-in-local-government.csv' DELIMITER ',' CSV`




My group and I had two csv files containing data. I decided to keep all of the columns from the data tables because none of the columns were irrelevant. Initially, I had to delete the top row of headers so that the data was formatted correctly. Then, I assigned datatypes to the different columns. I used the text datatype for entity (country) because it makes sense to compare a string input to a country name. I also used the text datatype for code because the code is a series of letters that represent the country. For the date, I used an integer because the year is the only part of the date provided and using an integer allows me to compare date values. For example, I can write a query that retrieves all dates greater than 2000. I used a float for literacy rate because literacy rates are percentages that include decimals. For average years of schooling I also used a float because the average is calculated to the second decimal place. I used bigint for population because the population can potentially be billions. I used the text datatype for the world region because the region is described in words. Finally, I used a float for government seats held by women because those values are also percentages calculated to the second decimal.

I used the primary key: (entity, date_year) for both tables because no single column uniquely identifies every row. Instead, each country-year pair corresponds to a unique record in the dataset. 


My first query, ‘get_avg_years_of_schooling’ represents the user story “As a student interested in global education trends, I want to look up the average years of schooling in my country for any five years in the dataset, and compare it with other countries, so that I can understand how well my country's education system is performing globally during that time period.” This query retrieves the average years of schooling in a given country between the start and end dates. A student could input the name of their country along with a date range they are interested in, such as 2015-2020, and get a list of the country’s average years of schooling each year between those dates. This allows users to observe educational trends over time and compare results across countries. 

My second query, ‘get_countries_literacy_rate’ represents the user story: “As an educational researcher, I want to see how literacy rates have changed over time in different countries of the world so that I can identify which geographic areas are staying the same versus improving.” This query retrieves literacy data points from a selected country over time. A user can input a country and the query will retrieve every literacy rate that has been recorded over time for that country. An educational researcher would be able to see exactly how the rates have changed over time. 
