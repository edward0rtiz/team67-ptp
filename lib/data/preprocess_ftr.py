import pandas as pd
import feather

preprocess_mf = __import__("preprocessor").preprocess_mf

filename = "e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/placetopayDB4.ftr"

preprocess_mf(filename, "isic_section_name", "transaction_processing_amount")
