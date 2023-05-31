# Setting Up Python and `tepper_stats`

A short tutorial on how to setup the `tepper_stats` module in your python
environment.

## Setting Up Tepper Stats Package

For now, the `tepper_stats` package is not hosted on `pypi`, the official
python package index, and does not come prebuilt as an installable file.
Therefore, once a python environment has been created, you can install the 
`tepper_stats` package via the following steps

```shell
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

## Running Python

There are three main ways to interact with python:
1. Python Shell
   * This is the most direct way to work with python, but is less user-friendly.
   * In order to start a python shell, simply type `python` in your commandline.

```shell
# Example:
python
```
```shell
# Which results in something like:
Python 3.8.13 (default, Jul  6 2022, 21:20:18)
[Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import tepper_stats
>>> exit()
```

2. Python Script
   * A pre-written file. Basically a list of things you want python to do.
   * You can find a very simple python script [here](./examples/simple_script.py)
   
```shell
# Example
# From mba-python directory
python tutorials/examples/simple_script.py
```

3. Jupyter Notebooks
   * Probably the most difficult to setup, but is very user-friendly once installed
   * Gives you an interactive python UI to use.
   * Learn more [here](https://jupyter.org/)
   * You can find a very simple notebook [here](examples/simple_notebook.ipynb)

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
