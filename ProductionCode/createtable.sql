DROP TABLE IF EXISTS literacy_rates_vs_avg_years_of_schooling;
CREATE TABLE literacy_rates_vs_avg_years_of_schooling (
  entity text,
  code text,
  date_year year,
  lit_rate float,
  avg_years_of_schooling float,
  population long int,
  world_region text  
);


DROP TABLE IF EXISTS women_in_gov;
CREATE TABLE women_in_gov (
  entity text,
  code text,
  date_year year,
  seats_held_by_women float,
  world_region text  
);
