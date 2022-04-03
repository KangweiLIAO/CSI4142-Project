import phase_2
import traceback
from phase_2 import db_utils as db
from sqlalchemy import types as sql_types


if __name__ == '__main__':
    # phase_2.dim_country.get_csv()
    try:
        db.connect()
        # Push to database:
        # phase_2.dim_date.get_df().to_sql("dim_date", con=db.sql_engine, if_exists='replace', index_label="date_id")
        # phase_2.dim_country.get_df().to_sql("dim_country", con=db.sql_engine, if_exists='replace', index=False)
        # phase_2.dim_event.get_df().to_sql("dim_event", con=db.sql_engine,
        #                                   if_exists='replace', index_label="event_id")
        phase_2.dim_country_record.get_df().to_sql(
            "dim_country_record", con=db.sql_engine, dtype={"Decades": sql_types.BIGINT()},
            if_exists='replace', method='multi', index=True, index_label="record_id")
        # tables = phase_2.dim_yearly.get_dfs()
        # for i in range(len(tables)):
        #     tables[i].to_sql(f"dim_{csv.yearly_data[i]}", con=db.sql_engine, dtype={"Year": sql_types.BIGINT(
        #     )}, if_exists='replace', method='multi', index=True, index_label=f"{csv.yearly_data[i]}_id")

        # Obtain csv files
        # phase_2.dim_date.get_csv()
        # phase_2.dim_country.get_csv()
        # phase_2.dim_country_record.get_csv()
        # phase_2.dim_yearly.get_csv()
        phase_2.dim_event.get_csv()

        db.grant_permit(["dim_country", "dim_country_record", "dim_date", "dim_event", "dim_education",
                        "dim_health", "dim_life_quality", "dim_population"], "lzou041")
    except Exception as e:
        print(traceback.format_exc())
    finally:
        db.disconnect()
