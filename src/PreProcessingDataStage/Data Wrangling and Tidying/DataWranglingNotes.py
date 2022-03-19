# We need to clean, transform, and sometimes manipulate the data structure to gain any insights.
# This process is often called data wrangling or data munging.

# At the final stages of the data wrangling process, we will have a dataset that we can easily use for modeling
# purposes or for visualization purposes. This is a tidy dataset where each column is a variable and each row is an
# observation.

# USED DATASET: https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j

import pandas as pd

restaurants = pd.read_csv(r"/DOHMH_New_York_City_Restaurant_Inspection_Results.csv")

print(restaurants.shape)

# Preliminary data cleaning

# Remove any duplicate rows using .drop_duplicates() function.
restaurants = restaurants.drop_duplicates()

# If we look at the first four columns of our data: DBA, BORO, CUISINE DESCRIPTION, and GRADE. These column names are
# all capitalized, while the columns following it use both uppercase and lowercase. To have some consistency across
# column names, we will iterate over the column names of our dataset and convert them all to lowercase using the map()
# and lower() functions. We also need to make sure to include the str function to identify that we are working with
# strings.

# map() applies the str.lower() function to each of the columns in our dataset to convert the column names to all lowercase
restaurants.columns = map(str.lower, restaurants.columns)

# We can use the rename() function and a dictionary to relabel our columns. While we are renaming our columns, we
# might also want to shorten the cuisine description column to just cuisine.

# # axis=1` refers to the columns, `axis=0` would refer to the rows
# # In the dictionary the key refers to the original column name and the value refers to the new column name {'oldname1': 'newname1', 'oldname2': 'newname2'}
restaurants = restaurants.rename({'dba': 'name', 'cuisine description': 'cuisine'}, axis=1)

print(restaurants.head(10))

# Data Types

print("Data Types: \n", restaurants.dtypes)

# We have two types of variables: object and float64. object can consist of both strings or mixed types (both numeric
# and non-numeric), and float64 are numbers with a floating point (ie. numbers with decimals). There are other data
# types such as int64 (integer numbers), bool (True/False values), and datetime64 (date and/or time values).
#
# Since we have both continuous (float64) and categorical (object) variables in our data, it might be informative
# to look at the number of unique values in each column using the nunique() function.

# .nunique() counts the number of unique values in each column
print("No of unique values: \n", restaurants.nunique())

# We see that our data consists of 4 boroughs in New York and 15 cuisine types. We know that we also have missing
# data in url from our initial inspection of the data, so the unique number of values in url might not be super
# informative. Additionally, we have corrected for duplicate restaurants, so the restaurant name, latitude, longitude,
# and url should be unique to each restaurant

# Missing Data

# From our initial inspection of the data, we know we have missing data in grade, url, latitude, and longitude. Let’s
# take a look at how the data is missing, also referred to as missingness. To do this we can use isna() to identify if
# the value is missing. This will give us a boolean and indicate if the observation in that column is missing (True)
# or not (False). We will also use sum() to count the number of missing values, where isna() returns True.

# counts the number of missing values in each column
print("Missing data \n", restaurants.isna().sum())

# We see that there are missing values in grade and url, but no missing values in latitude and longitude. However, we
# cannot have coordinates at (0.000, 0.000) for any of the restaurants in our dataset, and we saw that these exist in
# our initial analysis. Let’s replace the (0.000,0.000) coordinates with NaN values to account for this. We will use
# the where() function to replace the coordinates 0.000 with np.nan.

# here our .where() function replaces latitude values less than 40 with NaN values
restaurants['latitude'] = restaurants['latitude'].where(restaurants['latitude'] < 40, np.nan)

# here our .where() function replaces longitude values greater than -70 with NaN values
restaurants['longitude'] = restaurants['longitude'].where(restaurants['longitude'] > -70, np.nan)

# .sum() counts the number of missing values in each column
print("Missing data \n", restaurants.isna().sum())

# Characterizing missingness with crosstab

# Let’s try to understand the missingness in the url column by counting the missing values across each borough.
# We will use the crosstab() function in pandas to do this.
# The crosstab() computes the frequency of two or more variables. To look at the missingness in the url column we can
# add isna() to the column to identify if there is an NaN in that column. This will return a boolean, True if there is
# a NaN and False if there is not. In our crosstab, we will look at all the boroughs present in our data and whether or
# not they have missing url links.

pd.crosstab(

    # tabulates the boroughs as the index
    restaurants['boro'],

    # tabulates the number of missing values in the url column as columns
    restaurants['url'].isna(),

    # names the rows
    rownames=['boro'],

    # names the columns
    colnames=['url is na'])

# We see that most of the restaurants in Manhattan in our dataset have restaurant links, while most restaurants in Brooklyn do not have url links.

# Removing prefixes
# It might be easier to read what url links are by removing the prefixes of the websites, such as “https://www.".
# We will use str.lstrip() to remove the prefixes. Similar to when we were working with our column names, we need
# to make sure to include the str function to identify that we are working with strings and lstrip to remove parts of
# the string from the left side.

# .str.lstrip('https://') removes the “https://” from the left side of the string
restaurants['url'] = restaurants['url'].str.lstrip('https://')

# .str.lstrip('www.') removes the “www.” from the left side of the string
restaurants['url'] = restaurants['url'].str.lstrip('www.')

# the .head(10) function will show us the first 10 rows in our dataset
print(restaurants.head(10))


# --------------------Error handling Documentation ----------------------------

# Line 12 - Error Received - SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#         - Solution - Put an 'r' before the normal string as it converts it to a raw string.
#         - Result - Fixed and the file can be read.

