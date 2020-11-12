import pandas as pd
import numpy as np
import re
import io
from sqlalchemy import create_engine

host = "place-to-pay-team-67.cnhuuzu3g5us.us-east-1.rds.amazonaws.com"
port = 5432
user = "postgres"
passc = "ds4ateam67"
db = "postgres"

# connDB = create_engine(f"postgresql://{user}:{passc}@{host}:{port}/{db}")
# conn = connDB.raw_connection()
# cur = conn.cursor()

# df_x = pd.read_sql("SELECT * FROM payer_merchant ", connDB)
# df_x.rename(columns={"payer": "user", "merchant": "item"}, inplace=True)
# df_x
