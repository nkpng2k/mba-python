# Creating Models

This will provide a short tutorial on how to make models that
can be used by the `tepper_stats` module.

## Statsmodels

In order to create a model that the `tepper_stats` module can use
you can use the `statsmodels` package. If you have successfully
installed the `tepper_stats` package, then `statsmodels` should
already be installed in your python environment

You can check to see if `statsmodels` is properly installed by running
this command in your commandline:

```shell
python -c "import statsmodels.api as sm; print(sm.__version__)"
```

## Training a Model

This is not a comprehensive tutorial on how to use the `statsmodels`
package. For more information on the complete package, please look
[here](https://www.statsmodels.org/stable/index.html) for the complete
documentation of the package.

To train a simple model, you can do the following:
```python
import pandas as pd
import statsmodels.api as sm


df = pd.read_csv("/my/data/file.csv")
# This line adds a linear intercept
exog = sm.add_constant(df[["column_1", "column_2", "column_3"]])
# Trains a linear regression using Ordinary Least Squares method
linear_regression = sm.OLS(df["target"], exog).fit()

# If there is no need for a linear intercept, the regression can be
# trained as:
linear_regression = sm.OLS(df["target"], df[["column_1", "column_2", "column_3"]]).fit()

# To include a linear intercept, make sure to wrap any input columns in
# the following manner:
exog = sm.add_constant(df[["column_1", "column_2", "column_3"]])
linear_regression = sm.OLS(df["target"], exog).fit()
```

## Future

In the future, the plan is to improve the package to allow
usage of scikit learn models, but for now we are limited to
using statsmodels models because of their similarity to R.
