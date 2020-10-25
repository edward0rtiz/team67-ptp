import pandas as pd
import numpy as np
import re
import io
from sqlalchemy import create_engine

host = "place-to-pay-team-67.cnhuuzu3g5us.us-east-1.rds.amazonaws.com"
port = 5432
user = "postgres"
password = "ds4ateam67"
database = "postgres"

connDB = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
conn = connDB.raw_connection()
cur = conn.cursor()

test = pd.read_sql("SELECT transaction_description FROM transactions ", connDB)
test = (
    test.groupby("transaction_description")
    .size()
    .reset_index()
    .sort_values(by=[0], ascending=False)
)
test = test.reset_index(drop=True)
test = test.rename(columns={0: "amount"})
test
