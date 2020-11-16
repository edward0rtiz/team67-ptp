import pandas as pd
import numpy as np
import feather

filepath = "E:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/isic_section_name_transaction_processing_amount.ftr"
df_x = feather.read_dataframe(filepath)
"""
df_x["logarithm"] = np.log(df_x["transaction_processing_amount"])
df_x

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
# print(df_x.info())

np.random.seed(135568109)
ndata = len(df_x)
idx_80 = np.random.choice(range(ndata), int(0.8 * ndata), replace=False)
idx_20 = np.asarray(list(set(range(ndata)) - set(idx_80)))
data_80 = df_x.iloc[idx_80]
data_20 = df_x.iloc[idx_20]
data_20

filepath1 = "C:/Users/anemi/OneDrive/Escritorio/dataframes/isic_section_name_transaction_processing_amount_transaction_processing_date_.ftr"
df_x1 = feather.read_dataframe(filepath1)

df_x1["month"] = df_x1["transaction_processing_date_"].dt.month

np.random.seed(135568109)
ndata_1 = len(df_x1)
idx_80_1 = np.random.choice(range(ndata), int(0.8 * ndata), replace=False)
idx_20_1 = np.asarray(list(set(range(ndata)) - set(idx_80_1)))
data_80_1 = df_x1.iloc[idx_80_1]
data_20_1 = df_x1.iloc[idx_20_1]
data_20_1

df_x1
"""