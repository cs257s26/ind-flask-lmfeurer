# README

Individual Flask project.

URL Information:
- To see the growth rate in literacy rate over time in Mexico, enter http://127.0.0.1:PORT/growth/Mexico
- To see the data corresponding to the average years of schooling between 2010 and 2020 in France, enter http://127.0.0.1:PORT/schooling/France/2010/2020

Individual Database Project.

Copy Commands: 

`\copy literacy_rates_vs_avg_years_of_schooling FROM 'ProductionCode/literacy-rates-vs-average-years-of-schooling.csv' DELIMITER ',' CSV`

`\copy women_in_gov FROM 'ProductionCode/share-of-women-in-local-government.csv' DELIMITER ',' CSV`




My group and I had two csv files containing data. I decided to keep all of the columns from the data tables because none of the columns were irrelevant. Initially, I had to delete the top row of headers so that the data was formatted correctly. Then, I assigned datatypes to the different columns. I used the text datatype for entity (country) because it makes sense to compare a string input to a country name. I also used the text datatype for code because the code is a series of letters that represent the country. For the date, I used an integer because the year is the only part of the date provided and using an integer allows me to compare date values. For example, I can write a query that retrieves all dates greater than 2000. I used a float for literacy rate because literacy rates are percentages that include decimals. For average years of schooling I also used a float because the average is calculated to the second decimal place. I used bigint for population because the population can potentially be billions. I used the text datatype for the world region because the region is described in words. Finally, I used a float for government seats held by women because those values are also percentages calculated to the second decimal. I used the primary key: (entity, date_year) for both tables because no single column uniquely identifies every row. Instead, each country-year pair corresponds to a unique record in the dataset. 
