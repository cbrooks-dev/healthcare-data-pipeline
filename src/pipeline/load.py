import pandas as pd
from db import connect


def load() -> bool:
    """Load modeled data into tables for analysis."""
    try:
        engine = connect()
        df = pd.read_sql(sql="SELECT * FROM patients_cleaned;", con=engine)
        # TODO: break into fact-dimension model and load into Postgres
    except Exception as e:
        print(e)
        return False

    return True
