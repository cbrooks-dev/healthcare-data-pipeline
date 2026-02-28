import pandas as pd
from db import connect


def table_to_lower(df: pd.DataFrame) -> None:
    """Convert all values to lower case."""
    for col in df.columns:
        if df[col].dtype == "string":
            df[col] = df[col].str.lower()


def table_strip_whitespace(df: pd.DataFrame) -> None:
    """Remove all leading and trailing whitespace."""
    for col in df.columns:
        if df[col].dtype == "string":
            df[col] = df[col].str.strip()


def table_normalize_gender(df: pd.DataFrame) -> None:
    """Normalize all gender fields."""
    df["gender"] = df["gender"].map(
        {
            "male": "m",
            "female": "f",
        }
    )


def transform() -> bool:
    """Transform raw healthcare patient table data and load into cleaned Postgres table."""
    try:
        # Load raw table data
        engine = connect()
        df = pd.read_sql(sql="SELECT * FROM patient_raw;", con=engine)
        table_to_lower(df)
        table_strip_whitespace(df)
        table_normalize_gender(df)
        print(df)
        # TODO: write and call functions for data transformations
    except Exception as e:
        print(e)
        return False

    return True


transform()
