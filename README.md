## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) for installation.

Run the following commands:
```bash
pip install pipenv
```
```bash
pipenv install
```
```bash
pipenv shell
```


## Running the tests

Run from inside the pipenv shell

To run all tests:
```
python -m pytest
```

To run specific set - smoke, regression:
```
python -m pytest -m smoke
```

```
python -m pytest -m regression
```


## Bonus solution for the logger task
In the utils.locator_decorator.py you can find a decorator method(monkey patching) for the base methods
that are coming from playwright. 

This way you don't need to wrap every method and action that is used in the page object.