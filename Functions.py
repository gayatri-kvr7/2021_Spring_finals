import numpy as np
import pandas as pd


def EDA_dataframe(df):
    """
    Given a data frame this function does a basic exploration on the data which gives an idea on how to proceed with
    working with the particular data

    :param df: Data frame for which we want to do exploratory Data Analysis
    :return:Prints the basic details like First few rows of that dataframe to see the content of that data frame.
    The number of rows and columns in that complete data frame
    The number of null values in each column - This helps us decide if we can drop these rows or do we need to perform
    certain process on that particular data to include these rows.
    Datatype of each column to figure out how to process the values in that column.

    >>> df=pd.read_csv("DocTest1.csv")
    >>> EDA_dataframe(df)
    Top 5 rows:    Name Place
    0   Joe    US
    1  Lara    UK
    The number of rows are:2. the number of columns are: 2
    The number of null values in each column: Name     0
    Place    0
    dtype: int64
    The datatype of each column is Name     object
    Place    object
    dtype: object

    """
    print("Top 5 rows: {}".format(df.head()))
    print("The number of rows are:{}. the number of columns are: {}".format(df.shape[0], df.shape[1]))
    print("The number of null values in each column: {}".format(df.isnull().sum()))
    print("The datatype of each column is {}".format(df.dtypes))


def extract_year(some_data):
    """
    This function is extracting the year value from a DataTime type column from a DataFrame

    :param some_data: Input Dataframe for which we want to get an year column
    :return: Returning the same dataframe with an Output Year Column added to it. This Column contains the Year
    information which is extracted from the DataTime Column
    >>> df=pd.read_csv("DocTest2.csv")
    >>> extract_year(df)
       ID          Date  FiscalYear
    0   1  6/28/14 0:00        2014
    1   2  3/21/13 0:00        2013
    2   3  3/13/16 0:00        2016
    3   4  3/31/16 0:00        2016
    4   5  2/13/13 0:00        2013

    """
    some_data['FiscalYear'] = pd.DatetimeIndex(some_data['Date']).year
    some_data['FiscalYear'] = some_data['FiscalYear'].fillna(0).astype(np.int64)
    return some_data


def range_year(some_data):
    """
    The Function is used to print the unique year from any dataframe

    :param some_data: Input dataframe for which we need unique year
    :return: printing the Unique Year from the dataframe
    """
    print("Unique Year is {} ".format(some_data.FiscalYear.unique()))


def death_summary(some_data):
    """
    This function prints the number of deaths due to each drug present in the file

    :param some_data: Dataframe for which we need to calculate deaths
    :return: printing the number of deaths due to each drug
    """
    Drug_names = ["Heroin", "Cocaine", "Fentanyl", "FentanylAnalogue", "Oxycodone", "Oxymorphone", "Ethanol",
                  "Hydrocodone", "Benzodiazepine", "Methadone", "Amphet", "Tramad", "Morphine_NotHeroin",
                  "Hydromorphone", "Other"]
    for drug in Drug_names:
        print("Number of deaths due to: {} is {}".format(drug, some_data[drug].notnull().sum()))


def accidental_ethanol_death(some_data):
    """
    This function is filtering Accidental Deaths due to Ethanol from the dataframe

    :param some_data: Dataframe from where we want to filter the Manner of Death as Accidental
    :return: Dataframe with Manner of Death as Accident for Ethanol

    """
    some_data.loc[some_data.MannerofDeath == "accident", "MannerofDeath"] = "Accident"
    some_data.loc[some_data.MannerofDeath == "ACCIDENT", "MannerofDeath"] = "Accident"
    some_data.dropna(subset=["MannerofDeath"])  # dropping missing data rows
    return some_data


def grouped_drugs(some_data):
    """
    This function is grouping data for two different drugs- Ethanol and Morphine_Not_Heroin and calculating the count of
    deaths for the same. The grouping is done on basis of Sex and Year of death.

    :param some_data: Input Dataframe from which we want to extract information for these particular drugs
    :return: returning the grouped data with details of deaths from two drugs grouped up to Manner of Death, sex and
    Fiscal Year
    >>> df4=pd.read_csv("Doc_Test4.csv")
    >>> grouped_drugs(df4)
           MannerofDeath Sex FiscalYear  Morphine_NotHeroin  Ethanol
    0           Hospital   A       2014                   1        1
    1  Social Distancing   B       2015                   1        1
    """
    some_data1 = some_data.groupby(["MannerofDeath", "Sex", "FiscalYear"]).agg(
        {"Morphine_NotHeroin": "count", "Ethanol": "count" })
    some_data1.reset_index(inplace=True)
    #some_data1.drop([6, 7], inplace=True)
    some_data1["FiscalYear"] = some_data1["FiscalYear"].astype(str)
    return some_data1


def per_location_analysis(location, Drugs_Grouped_InjuryPlace):
    """
    This function is filtering and grouping the dataframe by location for Heroin by Fiscal Year

    :param location: This variable specifies the location for which we want to group the data. For e.g Residence
    :param Drugs_Grouped_InjuryPlace: The dataframe for which we want to group the data containing the injury
    information
    :return: returning the dataframe with grouped up data based on drug and Injury

    >>> df5=pd.read_csv("Doc_Test5.csv")
    >>> per_location_analysis("Residence",df5)
       FiscalYear  Heroin
    0        2014       1
     """
    deaths_residence = Drugs_Grouped_InjuryPlace.loc[(Drugs_Grouped_InjuryPlace["InjuryPlace"] == location)]
    df = pd.DataFrame(deaths_residence.groupby("FiscalYear")["Heroin"].count())
    df.reset_index(inplace=True)
    return df
