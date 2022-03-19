set schema 'public';

CREATE TABLE "country_china"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);

CREATE TABLE "country_canada"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);

CREATE TABLE "country_india"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);

CREATE TABLE "country_liberia"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);

CREATE TABLE "country_mexico"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);


CREATE TABLE "country_mozambique"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);

CREATE TABLE "country_south_africa"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);

CREATE TABLE "country_usa"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);

CREATE TABLE "country_vietnam"
(
    "year" numeric,
    "total_population" numeric,
    "total_population_rank" numeric,
    "urban_population" numeric,
    "rural_population" numeric,
    "birth_rate" numeric,
	"death_rate" numeric,
	"growth_rate" numeric,
	"density" numeric
);

CREATE TABLE "country_dim"
(
	"country_id" serial,
    "name" varchar(255),
    "region" varchar(255),
    "continent" varchar(255),
    "currency" varchar(255),
    "capital" varchar(255)
);

CREATE TABLE "date_dim"
(
	"date_id" serial,
    "year" numeric,
    "month" numeric,
    "day" numeric
);

CREATE TABLE "health_dim"
(
	"health_id" serial,
    "series_name" varchar(255),
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

CREATE TABLE "education_dim"
(
	"edu_id" serial,
    "series_name" varchar(255),
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

CREATE TABLE "population_dim"
(
	"pop_id" serial,
    "series_name" varchar(255),
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

CREATE TABLE "life_quality_dim"
(
	"life_id" serial,
    "series_name" varchar(255),
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
