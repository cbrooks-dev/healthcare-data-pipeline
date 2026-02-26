import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


def extract() -> bool:
    """Extract and load healthcare csv data into a raw Postgres table."""

    # Connect to db
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Ingest csv data
    path = Path(r"data\raw\healthcare_dataset.csv")
    df = pd.read_csv(filepath_or_buffer=path, sep=",")

    # Rename columns to match table
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Load raw data
    df.to_sql(name="patient", con=engine, if_exists="replace", index=False)
