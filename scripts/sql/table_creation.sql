SET schema 'public';

CREATE TABLE "fact_hiv" (
	"active_cases" numeric, 
	"death_cases" numeric, 
	"infected_population" numeric, 
	"infected_rate" numeric, 
	date_key integer REFERENCES dim_date(date_id), 
	country_key integer REFERENCES dim_country(country_id), 
	health_key integer REFERENCES dim_health(health_id), 
	edu_key integer REFERENCES dim_education(edu_id), 
	pop_key integer REFERENCES dim_population(pop_id), 
	life_key integer REFERENCES dim_life_quality(life_id), 
	constraint pk primary key (date_key, country_key, health_key, edu_key, pop_key, life_key)
)

CREATE TABLE "country_china" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "country_canada" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "country_india" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "country_liberia" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "country_mexico" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "country_mozambique" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "country_south_africa" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "country_usa" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "country_vietnam" ( "year" numeric NOT NULL PRIMARY KEY, "total_population" numeric, "total_population_rank" numeric, "urban_population" numeric, "rural_population" numeric, "birth_rate" numeric, "death_rate" numeric, "growth_rate" numeric, "density" numeric );

CREATE TABLE "dim_country" ( "country_id" serial PRIMARY KEY, "name" varchar(255) NOT NULL, "region" varchar(255), "continent" varchar(255), "currency" varchar(255), "capital" varchar(255) );

CREATE TABLE "dim_date" ( "date_id" serial PRIMARY KEY, "year" numeric NOT NULL, "month" numeric, "day" numeric );

CREATE TABLE "dim_health" ( "health_id" serial PRIMARY KEY, "series_name" varchar(255) NOT NULL, "series_code" varchar(255), "country_name" varchar(255), "country_code" varchar(255), "yr2005" numeric, "yr2006" numeric, "yr2007" numeric, "yr2008" numeric, "yr2009" numeric, "yr2010" numeric, "yr2011" numeric, "yr2012" numeric, "yr2013" numeric, "yr2014" numeric, "yr2015" numeric, "yr2016" numeric, "yr2017" numeric, "yr2018" numeric, "yr2019" numeric, "yr2020" numeric );

CREATE TABLE "dim_education" ( "edu_id" serial PRIMARY KEY, "series_name" varchar(255) NOT NULL, "series_code" varchar(255), "country_name" varchar(255), "country_code" varchar(255), "yr2005" numeric, "yr2006" numeric, "yr2007" numeric, "yr2008" numeric, "yr2009" numeric, "yr2010" numeric, "yr2011" numeric, "yr2012" numeric, "yr2013" numeric, "yr2014" numeric, "yr2015" numeric, "yr2016" numeric, "yr2017" numeric, "yr2018" numeric, "yr2019" numeric, "yr2020" numeric );

CREATE TABLE "dim_population" ( "pop_id" serial PRIMARY KEY, "series_name" varchar(255) NOT NULL, "series_code" varchar(255), "country_name" varchar(255), "country_code" varchar(255), "yr2005" numeric, "yr2006" numeric, "yr2007" numeric, "yr2008" numeric, "yr2009" numeric, "yr2010" numeric, "yr2011" numeric, "yr2012" numeric, "yr2013" numeric, "yr2014" numeric, "yr2015" numeric, "yr2016" numeric, "yr2017" numeric, "yr2018" numeric, "yr2019" numeric, "yr2020" numeric );

CREATE TABLE "dim_life_quality" ( "life_id" serial PRIMARY KEY, "series_name" varchar(255) NOT NULL, "series_code" varchar(255), "country_name" varchar(255), "country_code" varchar(255), "yr2005" numeric, "yr2006" numeric, "yr2007" numeric, "yr2008" numeric, "yr2009" numeric, "yr2010" numeric, "yr2011" numeric, "yr2012" numeric, "yr2013" numeric, "yr2014" numeric, "yr2015" numeric, "yr2016" numeric, "yr2017" numeric, "yr2018" numeric, "yr2019" numeric, "yr2020" numeric );