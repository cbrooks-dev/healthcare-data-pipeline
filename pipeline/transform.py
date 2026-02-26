import pandas as pd
from db import connect


def table_to_lower(df: pd.DataFrame) -> None:
    """Convert all values to lower case."""
    for col in df.columns:
        if df[col].dtype == "string":
            df[col] = df[col].str.lower()


def transform() -> bool:
    """Transform raw healthcare patient table data and load into cleaned Postgres table."""
    try:
        # Load raw table data
        engine = connect()
        df = pd.read_sql(sql="SELECT * FROM patient_raw;", con=engine)
        table_to_lower(df)
        print(df)
        # TODO: write and call functions for data transformations
    except Exception as e:
        print(e)
        return False
    
    return True

transform()
