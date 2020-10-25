import pandas as pd
import numpy as np
import feather

filepath = "E:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/isic_section_name_transaction_processing_amount.ftr"

df_x = feather.read_dataframe(filepath)

# print(df_x.info())

df_x["logarithm"] = np.log(df_x["transaction_processing_amount"])
df_x


# Transaction description
df_t = feather.read_dataframe(
    "E:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/transaction_description.ftr"
)
df_t = (
    df_t.groupby("transaction_description")
    .size()
    .reset_index()
    .sort_values(by=[0], ascending=False)
)
df_t = df_t.reset_index(drop=True)
df_t = df_t.rename(columns={0: "amount"})
df_t = df_t.iloc[0:21]
