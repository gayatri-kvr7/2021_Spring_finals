import numpy as np
import pandas as pd


def EDA_dataframe(df):
    print("Top 5 rows: {}".format(df.head()))
    print("The number of rows are:{}. the number of columns are: {}".format(df.shape[0], df.shape[1]))
    print("The number of null values in each column: {}".format(df.isnull().sum()))
    print("The datatype of each column is {}".format(df.dtypes))


def extract_year(some_data):
    some_data['FiscalYear'] = pd.DatetimeIndex(some_data['Date']).year
    some_data['FiscalYear'] = some_data['FiscalYear'].fillna(0).astype(np.int64)
    return some_data


def range_year(some_data):
    print("Unique Year is {} ".format(some_data.FiscalYear.unique()))


def death_summary(some_data):
    Drug_names = ["Heroin", "Cocaine", "Fentanyl", "FentanylAnalogue", "Oxycodone", "Oxymorphone", "Ethanol",
                  "Hydrocodone", "Benzodiazepine", "Methadone", "Amphet", "Tramad", "Morphine_NotHeroin",
                  "Hydromorphone", "Other"]
    for drug in Drug_names:
        print("Number of deaths due to: {} is {}".format(drug, some_data[drug].notnull().sum()))


def accidental_ethanol_death(some_data):
    some_data.loc[some_data.MannerofDeath == "accident", "MannerofDeath"] = "Accident"
    some_data.loc[some_data.MannerofDeath == "ACCIDENT", "MannerofDeath"] = "Accident"
    some_data.dropna(subset=["MannerofDeath"])  # dropping missing data rows
    return some_data


def grouped_drugs(some_data):
    some_data1 = some_data.groupby(["MannerofDeath", "Sex", "FiscalYear"]).agg(
        { "Morphine_NotHeroin": "count", "Ethanol": "count" })
    some_data1.reset_index(inplace=True)
    some_data1.drop([6, 7], inplace=True)
    some_data1["FiscalYear"] = some_data1["FiscalYear"].astype(str)
    return some_data1



