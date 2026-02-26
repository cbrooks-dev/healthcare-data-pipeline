import pandas as pd
from pathlib import Path
from db import connect


def transform() -> bool:
    """Transform raw healthcare patient table data and load into cleaned Postgres table."""
    try:
        # Load raw table data
        engine = connect()
        df = pd.read_sql(sql="SELECT * FROM patient_raw;", con=engine)
        # TODO: write and call functions for data transformations
    except:
        return False
    
    return True
