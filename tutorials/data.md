# Managing Data

A simple tutorial on how to import data into python.

## Pandas

The `pandas` package is the go-to method for loading data into
python. If you successfully installed the `tepper_stats` package,
`pandas` should already be installed in your python environment.

You can check to see if `pandas` is properly installed by running this
command in your commandline:

```shell
python -c "import pandas as pd; print(pd.__version__)"
```

## Loading Data

You will be able to load most types of data files using pandas including:
`.csv`, `tsv`, `xls`, and `.xlsx`

NOTE: for `xls` and `xlsx` files you may need to install an additional
dependency:
```shell
pip install openpyxl
```

You can load data from a specific file using the following python command:

```python
import pandas as pd


# Command to load a csv file
df = pd.read_csv("/path/to/my_csv.csv")

# Command to load an xlsx file
# May require `pip install openpyxl` to have been run prior to this
df = pd.read_excel("/path/to/my_excel.xlsx")
```

Loading data from a file means that python will read the file and load the
data into a `DataFrame`. This is what the variable `df` seen above will be
after the command has been run. You will be able to interact with the
`DataFrame` once the data has been properly loaded.

NOTE: for larger datasets, the loading process could take some time.

## Working with Pandas DataFrames

This is not an all-inclusive tutorial. If you want to get more in-depth
knowledge about how to use `pandas` please refer to the official
[pandas documentation](https://pandas.pydata.org/docs/)

With `pandas` you can do a few different things:

### Summary Information and Statistics

```python
# Shows the top 5 rows of the DataFrame
df.head()

# Displays columns and their types and the number of rows
# this can be useful to see if there are any missing values in your data
df.info()

# Displays simple statistics for each column
# Ex. mean, standard deviation, min, and max.
df.describe()
```

### Selecting Subsets of a DataFrame

`pandas` is slightly different to R. In order to access a specific
subset of the data, you will want to use the following methodology:

```python
import pandas as pd


# Create a really simple DataFrame
df = pd.DataFrame(
    [
        [1, "a", True],
        [2, "b", False],
        [3, "c", False],
        [4, "e", True]
    ],
    columns=["number", "letter", "is_vowel"]
)

# Creates a new variable of only the last column
df_is_vowel = df["is_vowel"]

# Creates a second DataFrame of only the first 2 columns
df_2 = df[["number", "letter"]]
```

### Creating New Columns

`pandas` allows you to create new columns by doing the following:

```python
df["new_column"] = ["dog", "cat", "bird", "mouse"]
```

NOTE: The number of items in the list on the right must be the
same as the number of rows already in the DataFrame

If you want to create a new column by changing values in a pre-existing
column you can do something like this:

```python
# Takes the column `number` and multiplys it by 2,
# and creates a new column named `multiply_by_2`
df["multiply_by_2"] = df["number"].apply(lambda x: x * 2)
```

NOTE: the `lambda` structre seen in the above command can be translated as:

For every row in the column "number", assign the value for that row to `x`
and then multiply `x` by 2, and store that value in the same row under a 
new column "multiply_by_2".
