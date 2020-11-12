import pandas as pd
import numpy as np
import feather

filepath1 = "data/similarities.feather"
ds_x = feather.read_dataframe(filepath1)
ds_x
