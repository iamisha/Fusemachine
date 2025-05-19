# 1. Data Wrangling

A proces of transforming raw, messy data into a strucutred, clean format that can be easily analyzed.

#### 1.1 Common Data Wrangling Task
* Identifying and removing duplicate records
* Handling missing values
* Filtering and sampling data
* Fixing structural errors like misspelled column names
* Standardizing data fromats like dates
* Adding derived columns based on calculations
* Converting data types
* Anonymizing private data
* Joining together data from vairous sources

#### 1.2 Why Data Wrangling
1. Improves Data Quality

    Removes errors, duplicates, and inconsistencies.

    Ensures the data is accurate and reliable.

2.  Unifies Different Formats

    Data from different sources comes in different structures:

        Social media: JSON or API responses

        MongoDB: NoSQL documents

        Applications: Databases or logs

        CSV files: Tabular format

    Wrangling transforms all of them into a common format (e.g., DataFrame or structured table) so they can be analyzed together.

3.  ETL = Extract, Transform, Load

        Extract: Get data from different sources (APIs, databases, files)

        Transform: Here’s where data wrangling happens! Clean, format, and restructure the data

        Load: Save the cleaned data into a data warehouse or database

    dbt (Data Build Tool) is a modern tool that helps with the T (Transform) part of ETL

# 2. Introduction to Pandas

### 2.1 Pandas in Python
* NumPy
* Pandas
Installing pandas
```bash
pip install pandas
```
Importing pandas
```bash
import pandas as pd
```

### 2.2 Pandas DataStructures
* Series: pandas series is a one-dimensional labeled array.
* DataFrame: pandas dataframe is a 2-D data strcuture.

###  2.3 Creating pandas Series 
📂 View implementation in `create_pandas_series_df.py`

* pandas.Series(List) -> pandas series
* pandas.Series(array) -> pandas Series
* pandas.Series(dict) -> pandas Series

### 2.3 Accessing element of Pandas Seris
📂 View implementation in `create_pandas_series_df.py`

eg:
   s2[:2]
Accessing first two elements

###  2.4 Creating pandas dataframe 
📂 View implementation in `create_pandas_df.py`

* pandas.DataFrame(List) -> pandas DataFrame
* pandas.DataFrame(dict) -> pandas DataFrame
* series.to_frame() -> pandas DataFrame

### 2.5 Reading CSV, EXCEL and TSV file into dataframe
csv file:
```python
pd.read_csv("csv_file_path")
```
excel file:
```python
pd.read_excel("excel_file_path")
```
tsv file:
```python
pd.read_tsv("tsv_file_path", sep='\t')
```

### 2.6 Pandas some useful methods
📂 View implementation in `pandas_common_methods.py`

* head()
* tail()
* describe()
* nunique()
* unique()
* value_counts()

### 2.7 Label Bases Selection: loc[]
📂 View implementation in `label_select.py`

### 2.7 Label Bases Selection: iloc[]
📂 View implementation in `index_select.py`

# 3. Data Manipulation
📂 View implementation in `data_manipulate.py`