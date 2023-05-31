# Setting Up Python and `tepper_stats`

## Setting Up Tepper Stats Package

For now, the `tepper_stats` package is not hosted on `pypi`, the official
python package index, and does not come prebuilt as an installable file.
Therefore, once a python environment has been created, you can install the 
`tepper_stats` package via the following steps

```commandline
# To check if python is properly installed
python --version
# Output should look like this:
# Python 3.8.13

git clone https://github.com/nkpng2k/mba-python.git
cd mba-python/tepper_stats

# Install Poetry
pip install poetry==1.4.2
# Install tepper_stats package and all necessary dependencies
poetry install

# Test that tepper_stats package has been properly installed
python -c "import tepper_stats; print(tepper_stats.__name__)"
```

NOTE: The `tepper_stats` package uses `poetry` to manage dependencies, making it
slightly easier to build and install all the necessary packages to run the
`tepper_stats` package.

## Future

The goal is to add better documentation on how to install and configure
python for personal use. However, for the time being, the assumption is
that you, the user, are capable of installing python on your own.

### Helpful Links

1. Installing python for **MacOS** -
   * Manual Installation:
     * [Official MacOS Python Documentation](https://docs.python.org/3/using/mac.html)
     * [Installing Python via Python.org](https://www.python.org/downloads/macos/)
     * Using Homebrew:
       * [Install Homebrew](https://brew.sh/)
       * [Installing Python via Homebrew](https://formulae.brew.sh/formula/python@3.8)
2. Installing python for **Windows** -
   * Manual Installation:
     * [Official Windows Python Documentation](https://docs.python.org/3/using/windows.html)
     * [Installing Python via Python.org](https://www.python.org/downloads/windows/)
3. Python Virtual Environments
    * While not required, it is highly recommended that you use virtual environments to 
      manage your python environments.
    * More about python `venv` and `virtualenv`
      * https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
      * https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
