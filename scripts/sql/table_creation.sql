SET schema 'public';

CREATE TABLE "fact_hiv" (
    date_key integer REFERENCES dim_date(date_id), 
    country_key integer REFERENCES dim_country(country_id), 
    health_key integer REFERENCES dim_health(health_id), 
    edu_key integer REFERENCES dim_education(edu_id), 
    pop_key integer REFERENCES dim_population(pop_id), 
    life_key integer REFERENCES dim_life_quality(life_id), 
    "active_cases" numeric, 
    "death_cases" numeric, 
    "infected_population" numeric, 
    "infected_rate" numeric, 
    CONSTRAINT pk PRIMARY KEY (
        date_key, country_key, health_key, 
        edu_key, pop_key, life_key
    )
);

CREATE TABLE "dim_country" (
    "country_id" serial PRIMARY KEY, 
    "name" varchar(255) NOT NULL, 
    "region" varchar(255), 
    "continent" varchar(255), 
    "currency" varchar(255), 
    "capital" varchar(255)
);

CREATE TABLE "country_china" (
"year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);
CREATE TABLE "country_canada" (
    "year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);

CREATE TABLE "country_india" (
    "year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);

CREATE TABLE "country_liberia" (
    "year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);

CREATE TABLE "country_mexico" (
    "year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);

CREATE TABLE "country_mozambique" (
    "year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);

CREATE TABLE "country_south_africa" (
    "year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);

CREATE TABLE "country_usa" (
    "year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);

CREATE TABLE "country_vietnam" (
    "year" numeric NOT NULL PRIMARY KEY, 
    "total_population" numeric, "total_population_rank" numeric, 
    "urban_population" numeric, "rural_population" numeric, 
    "birth_rate" numeric, "death_rate" numeric, 
    "growth_rate" numeric, "density" numeric
);


CREATE TABLE "dim_date" (
    "date_id" serial PRIMARY KEY, 
    "month_name" varchar(40), 
    "month_num" integer, 
    "year" integer, 
    "date" DATE -- an actual date type 
);

INSERT INTO "dim_date"(month_name, month_num, year, date) 
SELECT 
    to_char(months.d, 'FMMonth'), 
    to_char(months.d, 'MM'):: integer, 
    to_char(months.d, 'YYYY'):: integer, 
    months.d :: DATE 
FROM (
       SELECT generate_series(
              ('2005-01-01'):: date, 
              ('2020-12-01'):: date, 
              interval '1 month'
       )
) AS months(d);

CREATE TABLE "dim_health_china" (
    "Adults (ages 15+) living WITH HIV" numeric, 
    "Children (ages 0-14) newly infected WITH HIV" numeric, 
    "AIDS estimated deaths (UNAIDS estimates)" numeric, 
    "Current health expenditure (% of GDP)" numeric, 
    "Low-birthweight babies (% of births)" numeric, 
    "Hospital beds (per 1, 000 people)" numeric, 
    "Number of people who are undernourished" numeric, 
    "Nurses AND midwives (per 1, 000 people)" numeric, 
    "Physicians (per 1, 000 people)" numeric, 
    "Children (0-14) living WITH HIV" numeric, 
    "Children orphaned by HIV/AIDS" numeric, 
    "Domestic general government health expenditure(% of GDP)" numeric, 
    "Domestic general government health expenditure (% of general government expenditure)" numeric, 
    "Mortality caused by road traffic injury (per 100, 000 people)" numeric, 
    "Capital health expenditure (% of GDP)" numeric, 
    "Prevalence of overweight (% of adults)" numeric, 
    "Prevalence of overweight (modeled estimate, % of children under 5)" numeric
);

CREATE TABLE "dim_education" (
    "edu_id" serial PRIMARY KEY, 
    "series_name" varchar(255) NOT NULL, 
    "series_code" varchar(255), 
    "country_name" varchar(255), 
    "country_code" varchar(255), 
    "yr2005" numeric, 
    "yr2006" numeric, 
    "yr2007" numeric, 
    "yr2008" numeric, 
    "yr2009" numeric, 
    "yr2010" numeric, 
    "yr2011" numeric, 
    "yr2012" numeric, 
    "yr2013" numeric, 
    "yr2014" numeric, 
    "yr2015" numeric, 
    "yr2016" numeric, 
    "yr2017" numeric, 
    "yr2018" numeric, 
    "yr2019" numeric, 
    "yr2020" numeric
);

CREATE TABLE "dim_population" (
    "pop_id" serial PRIMARY KEY, 
    "series_name" varchar(255) NOT NULL, 
    "series_code" varchar(255), 
    "country_name" varchar(255), 
    "country_code" varchar(255), 
    "yr2005" numeric, 
    "yr2006" numeric, 
    "yr2007" numeric, 
    "yr2008" numeric, 
    "yr2009" numeric, 
    "yr2010" numeric, 
    "yr2011" numeric, 
    "yr2012" numeric, 
    "yr2013" numeric, 
    "yr2014" numeric, 
    "yr2015" numeric, 
    "yr2016" numeric, 
    "yr2017" numeric, 
    "yr2018" numeric, 
    "yr2019" numeric, 
    "yr2020" numeric
);

CREATE TABLE "dim_life_quality" (
    "life_id" serial PRIMARY KEY, 
    "series_name" varchar(255) NOT NULL, 
    "series_code" varchar(255), 
    "country_name" varchar(255), 
    "country_code" varchar(255), 
    "yr2005" numeric, 
    "yr2006" numeric, 
    "yr2007" numeric, 
    "yr2008" numeric, 
    "yr2009" numeric, 
    "yr2010" numeric, 
    "yr2011" numeric, 
    "yr2012" numeric, 
    "yr2013" numeric, 
    "yr2014" numeric, 
    "yr2015" numeric, 
    "yr2016" numeric, 
    "yr2017" numeric, 
    "yr2018" numeric, 
    "yr2019" numeric, 
    "yr2020" numeric
);
