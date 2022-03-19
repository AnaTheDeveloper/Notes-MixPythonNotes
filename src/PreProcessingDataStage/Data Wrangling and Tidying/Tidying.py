# LINK: https://www.jeannicholashould.com/tidy-data-in-python.html

# Tidying with Pandas

# Rules of Tidy Data
# Tabular datasets are made up of rows and columns. In data analysis, tidy datasets are standard practice because they
# allow for the most efficient use for data analysis. All tidy datasets follow a common syntax that allows for
# convenient and powerful procedures such as groupby and other aggregation functions to summarize or explain data.

# A tidy dataset follows three fundamental rules:

# Each variable forms a column.
# Each observation forms a row.
# Each type of observational unit forms a table.

# An observational unit is the individual object or instance that we capture information about. For example, in a
# study about trees, the observational unit would be each tree. We can collect different pieces of information about
# each tree, and a table is made up of collected information about all of these trees. Each column of this table would
# describe a specific variable about the trees – such as height, circumference, and the number of branches – and each
# individual row would be the full collection of information about one specific tree.

# [SEE GRAPHIC IN GIT READ ME]

# Cleaning Wide-form Data
# A dataset is considered to be in wide-form when at least one variable is represented across multiple columns as
# column headers rather than in a single column. These datasets are called wide-form because, in this form, the
# dataset has more columns than when it is tidied, thus appearing “wider” despite containing the same amount of
# information.
#
# Suppose we are collecting test scores on three different tests for five different students. The following table is
# in “wide-form” because the single variable Test is expressed as column headers instead of a single column.

# [SEE GRAPHIC IN GIT READ ME]

# Wide-form datasets are common when manually inputting data because this form is generally easier to visualize and
# manage by hand. If this teacher’s grade book had a separate row for each test that each student took, the grade book
# would be pages long and difficult to navigate by hand. However, for data analysis, programs can summarize and analyze
# data better when each row of the dataset represents a single observation. For example, groupby functions separate rows
# of data by the value within one or more columns rather than by the column header.
#
# To convert this dataset into a tidy dataset, we will create a column that holds the test name (“Test 1”, “Test 2”,
# or “Test 3”) and a column for the test score that corresponds to the student and the test. This way, each row will
# represent an individual observation of a student, the test, and their score. Each row will stand as a unique
# and individual observation.

# [SEE GRAPHIC IN GIT READ ME]

# We can see that the dataset went from “wide-form” (4 columns and 5 rows) to “long-form” (3 columns and 15 rows).
# Now with the data in long-form, we can more easily calculate summary values such as the average score for each test
# or the average score for each student. This is a significantly easier task in long-form as compared to wide-form.

import pandas as pd

data = pd.DataFrame({"Name": ["Annie", "John", "Min-ji", "Ravi", "Lucas"],
                     "Test1": [85, 92, 88, 86, 91],
                     "Test2": [78, 86, 79, 90, 93],
                     "Test3": [98, 90, 95, 78, 88]})
print(data)

# We can see that the data in this form matches the initial dataset in wide-form. In this form, the data are correctly
# in an intersection of an individual student and test. However we are limited in that we can only calculate summary
# statistics based on Name but not by test or score.
#
# The .melt() method in the pandas package will allow us to convert a dataset from wide to long-form. The
# parameters for this function are:

# id_vars: name of column(s) of identifier variable (in this example, it is the “Name” column). If there is more than
# one identifier variable, it can be written as id_vars = ["Variable 1","Variable 2",...] for as many variables as needed.

# var_name: the name of the new single column of the names of the columns that are being combined (in this
# example, var_name = "Test" and will hold values “Test 1”, “Test 2”, and “Test 3”).

# value_name: the name of new single column of values (in this example, value_name = "Score")

data_tidy = pd.melt(data, id_vars="Name", var_name="Test", value_name="Score")
print(data_tidy)

data_tidy.groupby(by = "Name").mean()
data_tidy.groupby(by = "Test").mean()
data_tidy[data_tidy["Score"] > 90]

# Cleaning Long-Form Data
# Sometimes datasets can be too long and need to be brought to a wider form. In this case, “too long” is not referring
# to the overall amount of rows of individual observations in the dataset. A dataset is “too long” when a single
# column in the dataset represents more than one variable, thus creating extra rows despite containing the same
# amount of information as compared to the same dataset in tidy form.

# [SEE GRAPHIC IN GIT READ ME]

# This table is in long-form and is considered messy because the column “attribute” represents two variables: age and
# income. This creates a problem in the “value” column because the numbers in this column are not comparable;
# age is in years and income is in thousands of dollars. If we were to perform any summary function or aggregation
# on the “value” column in this current state, the result would not be functional or useful.
#
# Another way to think about it is that all numbers in a single column should have the same unit. In this example,
# the numbers in the column “values” are either in years or thousands of dollars depending on the value of “attribute.”
# Because there is more than one variable represented, the dataset in this current form is messy.
#
# We can clean this by taking the “attribute” column and splitting it into separate “age” and “income” columns.
# By doing so, the values in each column will be of the same unit.

# [SEE GRAPHIC IN GIT READ ME]

# We now have a tidy dataset where each column represents a different attribute with unique units of measurement,
# and each row defines a distinct observation of a participant, their age, and income.

data = pd.DataFrame({"participant": [1,2,3,1,2,3],
                      "attribute": ["age", "age", "age", "income", "income", "income"],
                      "value": [24, 57, 23, 30, 60, 28]})
print(data)

# Though this dataset contains all of the complete information, it would be unnecessarily messy to print the information of one participant.

data[data["participant"] == 1]

# This statement has two lines of information to describe a single participant. We can print this information in a
# more concise form if we tidy the dataset. The pivot method in the pandas package will allow us to reshape the dataset
# based on the values of a column. The parameters for this function are:
#
# index: the name of the column to make the new data frame’s index ( in this scenario, “participant”).
# columns: the name of the column to make the new data frame’s column headers (in this scenario, “attribute”).
# values: the name of the column that will populate the new data frame’s values (in this scenario, “value”)

data_tidy = data.pivot(index="participant",
                         columns="attribute",
                         values="value").reset_index()
data_tidy.columns.name = None

print(data_tidy)

# Using the function .reset_index() and specifying .columns.name = None clears up some of the indexing that was carried
# over from the original form of the data set. Now that the index and column names of data_tidy are releveled
# and cleaned up, we can print this new, tidy dataset.

# This output from this code matches the above visualizations. The transformed tidy dataset has 3 rows and 3 columns,
# where each column represents only a single variable. Now if we wanted to print out the information about an individual
# participant, it would appear much neater.

data_tidy[data_tidy["participant"] == 1]

# Once a dataset is tidy, it can be more easily used to extract useful information, such as summaries or data visualizations.
