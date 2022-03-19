set schema 'public';
-- Grant auto increment sequence by user
-- lzou041
GRANT USAGE, SELECT ON SEQUENCE country_dim_country_id_seq TO kliao005;
GRANT USAGE, SELECT ON SEQUENCE education_dim_edu_id_seq TO kliao005;
GRANT USAGE, SELECT ON SEQUENCE health_dim_health_id_seq TO kliao005;
GRANT USAGE, SELECT ON SEQUENCE life_quality_dim_life_id_seq TO kliao005;
GRANT USAGE, SELECT ON SEQUENCE populaton_dim_pop_id_seq TO kliao005;
-- kliao005
GRANT USAGE, SELECT ON SEQUENCE date_dim_date_id_seq TO lzou041;
GRANT USAGE, SELECT ON SEQUENCE event_dim_id_seq TO lzou041;