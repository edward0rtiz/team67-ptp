import pandas as pd
import numpy as np
from IPython.display import Image

#### HELPER MODULES #####
import io
import os

#### LOADING MODULES ###
import feather

# filepath = "e:/Users/edwar/Desktop/place_to_pay/team67-ptp/data/placetopayDB4.ftr"  # or 'my_data.feather'
# data = feather.read_dataframe(filepath)

###### PREPROCESOR SINGLE VARIABLE ###########
def preprocess_var(bd, var):
    filepath_sv = (
        f"e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/{var}.csv"
    )
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[var]
    df2 = df2.to_frame()
    if df2[var].dtype is "category":
        df2[var] = df2[var].astype("category").cat.codes
        filename = filepath_sv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    else:
        filename = filepath_sv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")


# Example: preprocess_var(data, "transaction_payer_id")

###### PREPROCESOR MULTIPLE VARIABLE ###########
def preprocess_mul(bd, var1, var2):
    filepath_mv = (
        f"e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/{var1}_{var2}.csv"
    )
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2]]
    # df2 = df2.to_frame()
    if df2[var1].dtype is "category" and df2[var2].dtype is "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    elif df2[var1].dtype is "category" and df2[var2].dtype is not "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        filename = filepath_mv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    elif df2[var1].dtype is not "category" and df2[var2].dtype is "category":
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    else:
        filename = filepath_mv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")


######### PREPROCESSOR FEATHER SINGLE VAR ######################
def preprocess_sf(bd, var):
    filepath_svf = (
        f"e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/{var}.ftr"
    )
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[var]
    df2 = df2.to_frame()
    if df2[var].dtype is "category":
        df2[var] = df2[var].astype("category").cat.codes
        filename = filepath_svf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
    else:
        filename = filepath_svf
        df2.to_feather(filename)
        print("Succesfully exported to feather")


###### PREPROCESOR MULTIPLE VARIABLE ###########
def preprocess_mf(bd, var1, var2):
    filepath_mvf = (
        f"e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/{var1}_{var2}.ftr"
    )
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2]]
    # df2 = df2.to_frame()
    if df2[var1].dtype is "category" and df2[var2].dtype is "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif df2[var1].dtype is "category" and df2[var2].dtype is not "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif df2[var1].dtype is not "category" and df2[var2].dtype is "category":
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
    else:
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
