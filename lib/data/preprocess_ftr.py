import pandas as pd
import feather

preprocess_mf = __import__("preprocessor").preprocess_mf
preprocess_sf = __import__("preprocessor").preprocess_sf
preprocess_mf3 = __import__("preprocessor").preprocess_mf3

filename = "e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/placetopayDB4.ftr"
preprocess_mf(filename, "isic_section_name", "transaction_processing_amount")

filename = "e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/placetopayDB4.ftr"
preprocess_mf3(
    filename,
    "isic_section_name",
    "transaction_processing_amount",
    "transaction_processing_date_",
)