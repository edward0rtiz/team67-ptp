import pandas as pd

filename1 = "data/transaction_merchant.csv"
filename2 = "data/similarities.csv"

df_x = pd.read_csv(filename1)
df_x.rename(
    columns={"transaction_payer_id": "user",
             "merchant_id": "item"}, inplace=True
)
df_x

ds_x = pd.read_csv(filename2)
ds_x
