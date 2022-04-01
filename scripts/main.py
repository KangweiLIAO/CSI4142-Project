import phase_2
import phase_2.db_utils as db
import traceback
from sqlalchemy import types as sql_types


if __name__ == '__main__':
    # phase_2.dim_country.get_csv()
    try:
        db.connect()
        # phase_2.dim_date.get_df().to_sql("dim_date", con=db.sql_engine, if_exists='replace', index_label="date_id")
        phase_2.dim_country.get_df().to_sql("dim_country", con=db.sql_engine, dtype={"Decades": sql_types.BIGINT()},
                                            if_exists='replace', method='multi', index=False)
    except Exception as e:
        print(traceback.format_exc())
    finally:
        db.disconnect()
