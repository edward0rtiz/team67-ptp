
# coding: utf-8

# # Data Base Adjustment, Cleaning, Transformation, Feature Engineering and saving
# 
# This script takes a CSV file form the company provider (Placetopay) and returns a dataframe useful for next steps. It also saves a copy of the DataFrame as a CSV file, and as a Feather (.ftr) File. 
# 
# Some of the most important features of this process are:
# 
# * Check for and deal with erroneous values in the dataset:
#   * typos, misspelling, upper/lowecase, spaces.\
# * Generate unique IDs to replace hashes
# 
# 
# 
# 
# 

# In[9]:


FileName = 'Reto MinTIC - Inferencia-y-Recomendacion Teams 90-67-89.csv'
# You have to check if the CSV  File is already in the same directory

#if you run this notebook from Google Colab:
#FilePath = '/content/drive/My Drive/DS4A-3/Place to pay - DS4A - Databases and Notebooks/'

# Sample size, The size of the file you want to work with and then save. 
# If the file is bigger than Sample Size, it will make a sample. 
# in this case, we start with: 1000 000 rows. 
Rows = 1000000


# In[5]:


# First import the required libraries.
import pandas as pd
import numpy as np
import io
import os
from csv import reader
from datetime import datetime

import random
import re

# $ pip install feather-format
import feather


# In[6]:


# Making lists of columns for further use:

HashedCols = ['transaction_payer_id', 'transaction_payer_email', 'IP', 'card_id']

DateCols = ['transaction_processing_date_', 'merchant_created']

IntCols = ['transaction_processing_hour', 'transaction_card_installments']

FloatCols = ['transaction_processing_amount']

CategoricalCols = ['transaction_request_language', 'transaction_response_code',
                   'transaction_card_issuer_name', 'transaction_card_type', 
                   'transaction_payer_document_type', 
                   'paymentmethod_franchise',  'paymentmethod_name', 'paymentmethod_type',
                   'ip_location_region_name', 'ip_location_city', 
                   'card_class', 'card_country', 'card_issuer_country',
                   'merchant_id', 'merchant_enabled', 
                   'merchant_address_city', 'merchant_classification', 
                   'isic_division_name', 'isic_section_name',
                   'site_category', 'site_id', 'site_channel']
                   
chosen_cols = HashedCols + FloatCols + DateCols + IntCols + CategoricalCols + [
                'transaction_user_agent', 'transaction_id', 'transaction_description'] + [
                'transaction_processing_currency', 'isic_section_id','isic_division_id', 'ip_location_country']

Cols_to_Drop = ['transaction_country', 'transaction_dispersion',
                'transaction_business_model', 
                'reason_code_iso','reason_description', 'reason_clasiffication', 
                'merchant_country', 'merchant_address_country', 
                'site_classification', 
                'transaction_processing_currency',
                'isic_section_id', 'isic_division_id',
                'ip_location_country']


# # Load Database

# In[7]:


pwd


# In[8]:


ls


# In[10]:


# if it fails it might be necessary to add encoding = "utf-8"
opened_file = open(FileName)   # or Filepath if colab
read_file = reader(opened_file,delimiter=',')
read_file


# In[11]:


# Importing re package for using regular expressions 
import re 
  
# Function to clean the document types 
def Clean_names(Name): 
    Name = str(Name)
    # Search for opening bracket in the name followed by 
    # any characters repeated any number of times 
    if re.search(r'\d.*', Name):
        # Extract the position of beginning of pattern 
        pos = re.search(r'\d.*', Name).start() 
        if re.search(r'\d{8,11}', Name):  # we assume any string of digits from 8 to 11 long is a cedula
            return 'CC'
        elif pos == 0:
            return 'Otro'
        else:
            Name = Name[:pos]
            return Clean_names(Name)
            #return the cleaned name 
    elif re.search(r'PP', Name):  # We assume pp is a type of passport
        return 'PP'
    elif re.search(r'null|NONE|nan'  ,Name):
        return 'nan'
    elif re.search(r'RUT|RUC|NIT', Name): # we assume any of these is a company tax ID
        return 'NIT'
    elif re.search(r'.*CPF.*', Name): #CPF is the ID document for physical persons in Brazil
        return 'CPF'
    elif re.search(r'.*CPJ.*', Name): #CPJ/CNPJ is the ID document for business persons in Brazil
        return 'CPJ'
    elif re.search(r'Citizenship', Name):
        return 'Otro'
    elif re.search(r'.*CC.*', Name):  # We assume this is always a cedula
        return 'CC'
    elif re.search(r'.*CE.*', Name):  # We assume this is cedula of alien individual
        return 'CE'
    elif re.search(r'.*CI.*', Name): # it can be 'Cartao de identidade' in brazil
        return 'CIP'
    #elif re.search(r'\bC\b', Name):  #This is no longuer necessary
        #return 'CC'
    elif re.search(r'TI', Name):  # We assume this is 'Tarjeta de Identidad' for colombian underage individuals
        return 'TI'
    elif re.search(r'LIC|SSN|TAX', Name): # We assume this is Drivers Licence, Social Security Number or Tax ID, in USA.
        return Name                         # If is TaxID, we can say that this is a business, but with no certainty.
    # if clean up needed return the same name 
    else:
        return 'Otro'


# In[12]:


# WARNING: This is a test function.
# The function has to correct upper/lowercases and different spellings or synonims. This has to be improved
#
# Even then, there is an informed decition to make, for example:
# are all the 'GOLD' cards the same type?
# or there is a significant difference when they are issued by 'Studio-F' or 'Lan' as E-Cards?

# Function to clean the document types 

def Clean_cards(Name): 
    Name = str(Name)
    if re.search(r'DEBIT|Debito|Débito|Debit', Name):  # 
        return 'DEBIT'
    elif re.search(r'CLASSIC|Clásica|Clasic|Clásico|CLASICA|Clasica'  ,Name):
        return 'CLASSIC'
    elif re.search(r'STANDARD|Standard|estandar|ESTANDAR', Name): #
        return 'STANDARD'
    elif re.search(r'CORPORATE|Corporativa|Empresarial', Name):  # 
        return 'CORPORATE'
    elif re.search(r'PREPAID|E-CARD E-PREPAGO|Visa Prepago', Name): #
        return 'E-CARD E-PREPAGO'                       # 
    elif re.search(r'GOLD|gold|Gold|Oro|ORO', Name):  # 
        return 'GOLD'
    elif re.search(r'PLATINUM|Platinum', Name): #
        return 'PLATINUM'
    elif re.search(r'BLACK|Black', Name):  #
        return 'BLACK'
    elif re.search(r'BLUE', Name):
        return 'BLUE'
    elif re.search(r'GREEN', Name):  # 
        return 'GREEN'
    elif re.search(r'INFINITE', Name):  #
        return 'INFINITE'
    elif re.search(r'SIGNATURE', Name): #
        return 'SIGNATURE'
    elif re.search(r'GREEN', Name):  # 
        return 'GREEN'
    elif re.search(r'INFINITE|Infinite', Name):  #
        return 'INFINITE'
    elif re.search(r'PREMIER|PREMIUM', Name):  #
        return 'PREMIER'
    elif re.search(r'SIGNATURE|Signature', Name): #
        return 'SIGNATURE'
    #elif re.search(r'BUSINESS', Name):  # 
    #    return 'BUSINESS'
    #elif re.search(r'ELECTRON|Electron', Name):  #
    #    return 'ELECTRON'
    #elif re.search(r'MASTER DEBIT', Name):  # 
        #return 'MASTER'
    #elif re.search(r'DEBIT STANDARD', Name):  # 
        #return 'DEBIT STANDARD'
    
    # if clean up finished and there was no match, return the same name 
    else:
        #return Name 
        return 'Other'


# In[13]:


# Function to clear strange characters from names:

def Clean_chars(Name): 
    #print(type(Name), Name)
    Name = str(Name)
    Name = re.sub('[^a-zA-Z0-9?]','',Name)
    #Name = Name.replace(' ','_').lstrip().rstrip()
    return Name


# In[15]:


def ProcessingColumns(df):
    
    # Convert to integers, # np.float64 uses too much memory:
    df['transaction_processing_hour'] = pd.to_numeric(df['transaction_processing_hour'], downcast='integer')
    df['transaction_card_installments'] = pd.to_numeric(df['transaction_card_installments'], downcast='integer')
    # Convert dates to datetime:
    df.transaction_processing_date_ = pd.to_datetime(df.transaction_processing_date_)
    df.merchant_created = pd.to_datetime(df.merchant_created)
    # Convert Transaction ammount to  Float:
    df['transaction_processing_amount'] = df['transaction_processing_amount'].str.replace(',','.').astype(float) # replace decimal sign
    #df['transaction_processing_amount'] = pd.to_numeric(df['transaction_processing_amount']) # errors='coerce' / errors='ignore'
    df.loc[df['transaction_processing_currency']=='CRC', 'transaction_processing_amount'] = df[df['transaction_processing_currency']=='CRC'][['transaction_processing_amount']].apply(lambda num : num*6.345)
    df.loc[df['transaction_processing_currency']=='USD', 'transaction_processing_amount'] = df[df['transaction_processing_currency']=='USD'][['transaction_processing_amount']].apply(lambda num : num*3821.7)
    df['isic_section_name'] = df['isic_section_id'] + '-' + df['isic_section_name']
    df['isic_division_name'] = df['isic_division_id'].astype(str) + '-' + df['isic_division_name']
    df['ip_location_region_name'] = df['ip_location_country'].astype(str) + '-' + df['ip_location_region_name']
    # Convert to categorical This is not working while loading in chunks, because the function needs all possible categorical values: 
    #for column in CategoricalCols:
    #    df[column] = df[column].astype('category')
        
    df = df.drop(['transaction_processing_currency', 'isic_section_id','isic_division_id','ip_location_country'], axis=1)
    
    # Replace Null Coded values
    df = df.replace(["NI<!H%G$DCY?<.=_`KMG)X6XVZ5M(>,_+*7L6U4B(DS"],np.NaN)
    df['transaction_user_agent'] = df['transaction_user_agent'].replace(["0"],np.NaN)
    
    # Drop test transactions
    PruebasDF = df[((df['transaction_description'].str.contains(r'^(?!.*saber).*prueba.*$',case=False).fillna(False)))]
    df.drop(PruebasDF.index, axis = 0, inplace =True)
    df.drop(df[df['transaction_description'].str.contains('Test',case=False).fillna(False)].index, axis = 0, inplace =True)
    df.drop(df[df['transaction_card_issuer_name']=='Banco De Pruebas'].index, axis = 0, inplace =True)
    df.drop(df[df['transaction_card_issuer_name'].str.contains(r'prueba',case=False, na=False)].index, axis = 0, inplace =True)

    # Update Document Types: 
    df['transaction_payer_document_type'] = df['transaction_payer_document_type'].apply(Clean_names)
    df['transaction_payer_document_type'] = df['transaction_payer_document_type'].replace("nan",np.NaN)
    
    # Update Card Classes:
    #df['card_class'] = df['card_class'].apply(Clean_cards)
    
    # Shortening payer_ids:
    df['transaction_payer_id'] = df['transaction_payer_id'].apply(Clean_chars).str.slice(start=0, stop=10, step=None)
    df['transaction_payer_id'] = df['transaction_payer_id'].replace("nan",np.NaN)
    
    return (df)


# # Full Data Loading
# Now we load the full database in batches
# 

# In[16]:


# Count the lines
num_lines = sum(1 for l in open(FileName))

# Sample size - it is defined at the beginning of this notebook:
# Rows = 1000000

dfList = []

if num_lines > Rows:
    # The row indices to skip - make sure 0 is not included to keep the header!
    print('File is more than ', Rows, 'rows, Processing will do a sample of 1M rows')
    skip_idx = random.sample(range(1, num_lines), num_lines - Rows)
    
    # Read a sample of the data, in batches
    print('Starting to read the file')
    DataChunk = pd.read_csv(FileName, skiprows=skip_idx,
                            chunksize=100000, sep=',',
                            encoding='utf-8', usecols = chosen_cols) #latin1 didnt work for accents
    
else:
    # Read entire file
    DataChunk = pd.read_csv(FileName,
                            chunksize=100000, sep=',',
                            encoding='utf-8', usecols = chosen_cols) 

for chunk in DataChunk:
    df = pd.DataFrame(chunk)
    df = ProcessingColumns(df)
    dfList.append(df)
    print('Chunk ', type(chunk), 'of size ', df.memory_usage().sum()/1000000, 'MB has added: ', df.shape' to total: ', bd.shape
    del chunk                       # You have to liberate memory, otherwise, it will crash the kernel
print('concatenating...')
bd = pd.concat(dfList,sort=False)   # You can also convert to dataframe and process inside the for loop.
del DataChunk                       # You have to liberate memory, otherwise, it will crash the kernel
print('dataframe of shape:', bd.shape, 'is loaded and is using ', bd.memory_usage().sum()/1000000, 'MB')


# In[24]:


bd.transaction_processing_date_


# In[25]:


type(bd.transaction_processing_date_[0])


# In[71]:


#len(bd[bd['card_class']=='PRUEBAS'])


# In[ ]:


#bd.drop(bd[bd['card_class']=='PRUEBAS'].index, axis = 0, inplace =True)


# In[ ]:


#bd.card_class.unique()


# In[63]:


len(bd.card_class)


# In[60]:


bd.card_class.isna().sum()


# In[81]:


CardsColumn = pd.DataFrame(bd.card_class.copy())
type(CardsColumn)
#CardsColumn


# In[84]:


#CardsColumn.card_class.unique()


# In[85]:


CardsColumn.value_counts().head(20)


# In[86]:


CardDict = pd.read_csv('card_class.csv', sep = ';')
#CardDict


# In[87]:


CardsColumn = pd.merge(CardsColumn, CardDict, how="left", left_on='card_class',right_on='card_class')
CardsColumn.CardNAME.value_counts().head(30)


# In[88]:


CardsColumn.CardNAME.isna().sum()


# In[89]:


len(CardsColumn)


# In[90]:


bd['card_class'] = CardsColumn.CardNAME


# In[91]:


# Convert to categorical:
for column in CategoricalCols:
    bd[column] = bd[column].astype('category')
    
print('Converting Data Frame ', bd.shape, 'to categorical is finished and is now using ', bd.memory_usage().sum()/1000000, 'MB')


# In[92]:


# Drop Duplicate rows
bd = bd.drop_duplicates(subset=['transaction_id'], keep='first').copy()


# In[93]:


bd.shape


# # Data Enhancement

# In[94]:


# Replacing NULL Payer IDs with another indicator of identity:

CardsDF = bd[['transaction_processing_amount', 'transaction_payer_id', 'card_id']].groupby(['card_id','transaction_payer_id']).count().rename(columns={'transaction_processing_amount':'No_of_transactions'})
CardsDf2 = CardsDF.reset_index().groupby(['card_id']).count()
CardsDf2 = CardsDf2.drop('transaction_payer_id', axis = 1).rename(columns={'No_of_transactions':'No_of_payer_ids'})
HighIDsCards = CardsDf2[CardsDf2['No_of_payer_ids']>=4]
indi_codes = bd[bd['transaction_payer_id'].isna()].copy()
indi_codes.drop(indi_codes[(bd['card_id'].isna()) & (bd['transaction_payer_email'].isna())].index, inplace=True)

emailList=[x for x in list(indi_codes[indi_codes['transaction_payer_email'].notnull()].groupby('transaction_payer_email').count().index)]
ID_DF = bd[bd['transaction_payer_email'].isin(emailList)]
ID_DF = ID_DF.drop(ID_DF[ID_DF['transaction_payer_id'].isna()].index)
no_list = ID_DF.groupby(['transaction_payer_email','transaction_payer_id']).count().reset_index().groupby('transaction_payer_email').count().sort_values(by = 'transaction_payer_id', ascending=False).head(1)#.value_counts()
no_list = (no_list.reset_index())['transaction_payer_email'].values.tolist()
ID_DF.drop(ID_DF[ID_DF['transaction_payer_email'].isin(no_list)].index, inplace=True)
ID_DF.drop_duplicates(subset=['transaction_payer_email', 'transaction_payer_id'], keep='first', inplace=True)
ID_DF_dic = dict(zip(ID_DF['transaction_payer_email'],ID_DF['transaction_payer_id']))

CardList=[x for x in list(indi_codes[indi_codes['card_id'].notnull()].groupby('card_id').count().index) if x not in list(HighIDsCards.index)]
Card_DF = bd[bd['card_id'].isin(CardList)]
Card_DF = Card_DF.drop(Card_DF[Card_DF['transaction_payer_id'].isna()].index)
Card_DF.drop_duplicates(subset='card_id', keep='first', inplace=True)
ID_DF_dic2 = dict(zip(Card_DF['card_id'],Card_DF['transaction_payer_id']))

# Replace Function:
def replace_payerID(row):
    if row[8] in ID_DF_dic:
        return ID_DF_dic[row[8]]
    elif row[25] in ID_DF_dic2:
        return ID_DF_dic2[row[25]]
    else:
        return row[6]

testDF = indi_codes[(indi_codes['transaction_payer_email'].isin(ID_DF_dic) | indi_codes['card_id'].isin(ID_DF_dic2))]
testDF = testDF[testDF['transaction_payer_id'].isna()]
testDF['transaction_payer_id'] = testDF.apply(replace_payerID, axis = 1)

print('Number of ids that can be replaced by crossing with the card_ids, and emails: ', len(testDF['transaction_payer_id'].value_counts()))


# In[95]:


# Replacing values:

bd = pd.concat([bd, testDF])
bd.drop_duplicates(subset=['transaction_id'], keep='last', inplace=True)


# In[96]:


# Using emails as identifiers when nothing else

email_list2 = bd[(bd['transaction_payer_id'].isna())&(bd['transaction_payer_email'].notnull())].index
bd.loc[email_list2,'transaction_payer_id'] = bd.loc[email_list2,'transaction_payer_email']


# In[97]:


# Unidentifiable users:
NullUsers =  bd[(bd['transaction_payer_id'].isna()) & (bd['card_id'].isna()) & (bd['transaction_payer_email'].isna())]
bd.drop(NullUsers.index, axis = 0, inplace =True)


# In[98]:


# Dropping uninformative columns
bd = bd.drop(['transaction_payer_email', 'IP'], axis = 1)
bd = bd.dropna(subset=['transaction_payer_id'])


# In[22]:


#bd['transaction_processing_amount'] = np.log(bd['transaction_processing_amount']+1)


# In[99]:


bd.shape


# In[100]:


bd.isna().sum()


# ## Save the file

# In[104]:


# Save as CSV:
bd.to_csv('placetopayDB3.csv', header=True, index=False)


# Feather files provide compatibility between R and python. the advantage is that the categorical variables spend less memory and the other dtypes are also conserved.

# In[102]:


# Save as a feather file:
feather.write_dataframe(bd, "./placetopayDB3.ftr")
#bd.to_feather(FilePath) # do the same, alternatively


# Another available format is python Pickle:

# In[103]:


# To save as Pickle format:
bd.to_pickle("./placetopayDB3_pickle")


# In[ ]:


del bd

