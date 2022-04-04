import phase_2
import traceback
from phase_2 import utils_db as db
from sqlalchemy import types as sql_types


def init_fact():
    pass


if __name__ == '__main__':
    try:
        db.connect()
        # Push to database:
        # phase_2.dim_date.push(db.sql_engine)
        # phase_2.dim_country.push(db.sql_engine)
        # phase_2.dim_country_record.push(db.sql_engine)
        phase_2.dim_yearly.push(db.sql_engine)
        # phase_2.dim_event.push(db.sql_engine)
        # phase_2.staging_hdi.push(db.sql_engine)

        # Obtain csv files
        # phase_2.dim_date.get_csv()
        # phase_2.dim_country.get_csv()
        # phase_2.dim_country_record.export_csv()
        phase_2.dim_yearly.get_csv()
        # phase_2.dim_event.get_csv()
        # phase_2.staging_hdi.get_csv()

        # Permissions
        tables_kw = ["dim_country", "dim_country_record", "dim_date", "dim_event", "dim_education",
                     "dim_health", "dim_life_quality", "dim_population", "staging_hdi"]
        db.grant_permit(tables_kw, "lzou041")
        # table_lq = []
        # db.grant_permit(tables_lq, "kliao005")

    except Exception as e:
        print(traceback.format_exc())
    finally:
        db.disconnect()
