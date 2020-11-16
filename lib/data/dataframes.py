import pandas as pd

##### TRANSACTIONS CARD INSTALLMENTS #####
df_ci = pd.read_csv(
    "E:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/transaction_card_installments.csv"
)

df_ci

df_t = pd.read_csv(
    "E:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/transaction_description.csv"
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
