import pandas as pd
import numpy as np
from IPython.display import Image

#### HELPER MODULES #####
import io
import os

#### LOADING MODULES ###
import feather

<<<<<<< HEAD
# filepath = "e:/Users/edwar/Desktop/place_to_pay/team67-ptp/data/placetopayDB4.ftr"  # or 'my_data.feather'
=======
# or 'my_data.feather'


>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
# data = feather.read_dataframe(filepath)

###### PREPROCESOR SINGLE VARIABLE ###########
def preprocess_var(bd, var):
<<<<<<< HEAD
    filepath_sv = (
        f"e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/{var}.csv"
    )
=======
    file_data = f"C:/Users/anemi/OneDrive/Escritorio/dataframes/{var}.csv"
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[var]
    df2 = df2.to_frame()
    if df2[var].dtype is "category":
        df2[var] = df2[var].astype("category").cat.codes
<<<<<<< HEAD
        filename = filepath_sv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    else:
        filename = filepath_sv
=======
        filename = file_data
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    else:
        filename = file_data
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")


# Example: preprocess_var(data, "transaction_payer_id")

###### PREPROCESOR MULTIPLE VARIABLE ###########
def preprocess_mul(bd, var1, var2):
<<<<<<< HEAD
    filepath_mv = (
        f"e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/{var1}_{var2}.csv"
    )
=======
    file_data2 = f"C:/Users/anemi/OneDrive/Escritorio/dataframes/{var1}_{var2}.csv"
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2]]
    # df2 = df2.to_frame()
    if df2[var1].dtype is "category" and df2[var2].dtype is "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
<<<<<<< HEAD
        filename = filepath_mv
=======
        filename = file_data2
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    elif df2[var1].dtype is "category" and df2[var2].dtype is not "category":
        df2[var1] = df2[var1].astype("category").cat.codes
<<<<<<< HEAD
        filename = filepath_mv
=======
        filename = file_data2
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    elif df2[var1].dtype is not "category" and df2[var2].dtype is "category":
        df2[var2] = df2[var2].astype("category").cat.codes
<<<<<<< HEAD
        filename = filepath_mv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    else:
        filename = filepath_mv
=======
        filename = file_data2
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    else:
        filename = file_data2
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")


<<<<<<< HEAD
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
=======
# Example: preprocess_mul(data, "transaction_card_installments", "transaction_payer_id")
###### PREPROCESOR MULTIPLE VARIABLE ###########
def preprocess_mf(bd, var1, var2):
    file_data3 = f"C:/Users/anemi/OneDrive/Escritorio/dataframes/{var1}_{var2}.ftr"
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2]]
    # df2 = df2.to_frame()
    if df2[var1].dtype is "category" and df2[var2].dtype is "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
<<<<<<< HEAD
        filename = filepath_mvf
=======
        filename = file_data3
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif df2[var1].dtype is "category" and df2[var2].dtype is not "category":
        df2[var1] = df2[var1].astype("category").cat.codes
<<<<<<< HEAD
        filename = filepath_mvf
=======
        filename = file_data3
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif df2[var1].dtype is not "category" and df2[var2].dtype is "category":
        df2[var2] = df2[var2].astype("category").cat.codes
<<<<<<< HEAD
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
    else:
        filename = filepath_mvf
=======
        filename = file_data3
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    else:
        filename = file_data3
        df2.to_feather(filename)
        print("Succesfully exported to feather")


def preprocess_mf3(bd, var1, var2, var3):
    file_data4 = (
        f"C:/Users/anemi/OneDrive/Escritorio/dataframes/{var1}_{var2}_{var3}.ftr"
    )
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2, var3]]
    # df2 = df2.to_frame()
    if (
        df2[var1].dtype is "category"
        and df2[var2].dtype is "category"
        and df2[var3].dtype is "category"
    ):
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
        df2[var3] = df2[var3].astype("category").cat.codes
        filename = file_data4
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif (
        df2[var1].dtype is "category"
        and df2[var2].dtype is not "category"
        and df2[var3].dtype is not "category"
    ):
        df2[var1] = df2[var1].astype("category").cat.codes
        filename = file_data4
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif (
        df2[var1].dtype is not "category"
        and df2[var2].dtype is "category"
        and df2[var3].dtype is "category"
    ):
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = file_data4
        df2.to_feather(filename)
        print("Succesfully exported to feather")
    else:
        filename = file_data4
>>>>>>> 966e89db3fc5623bbfd8167ea9afbbd381f06f0b
        df2.to_feather(filename)
        print("Succesfully exported to feather")



def preprocess_mf3(bd, var1, var2, var3):
    filepath_mvf = (
        f"e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/{var1}_{var2}_{var3}.ftr"
    )
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2, var3]]
    # df2 = df2.to_frame()
    if df2[var1].dtype is "category" and df2[var2].dtype is "category" and df2[var3].dtype is "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
        df2[var3] = df2[var3].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif df2[var1].dtype is "category" and df2[var2].dtype is not "category" and df2[var3].dtype is not "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif df2[var1].dtype is not "category" and df2[var2].dtype is "category", and df2[var3].dtype is "category":
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
    else:
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")