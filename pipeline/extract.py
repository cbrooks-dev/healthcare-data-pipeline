import pandas as pd
from pathlib import Path
from db import connect


def extract() -> bool:
    """Extract and load healthcare patient csv data into raw Postgres table."""
    try:
        # Ingest csv data
        path = Path(r"data\raw\healthcare_dataset.csv")
        df = pd.read_csv(filepath_or_buffer=path, sep=",")

        # Rename columns to match table
        df.columns = [col.lower().replace(" ", "_") for col in df.columns]

        # Load raw data
        engine = connect()
        df.to_sql(name="patient_raw", con=engine, if_exists="replace", index=False)
    except Exception as e:
        print(e)
        return False
    
    return True
