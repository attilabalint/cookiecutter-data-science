{{ cookiecutter.project_name }}
==============================
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![code style - Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)
[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/python/mypy)

{{ cookiecutter.description }}

Project Organization
------------

    ├── data
    │   ├── interim             <- Intermediate data that has been transformed.
    │   ├── processed           <- The final, canonical data sets for modeling.
    │   └── raw                 <- The original, immutable data dump.
    │
    ├── docs                    <- A default mkdocs project; see mkdocs.org for details
    │
    ├── models                  <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering)
    │                              and a short `-` delimited description, e.g. `1.0-initial-data-exploration`.
    ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures             <- Generated graphics and figures to be used in reporting
    │
    ├── src                     <- Source code for use in this project.
    │   ├── __init__.py         <- Makes src a Python module
    │   │
    │   ├── data                <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── processing          <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models              <- Scripts to train models and then use trained models to make
    │   │   │                      predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization       <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    ├── tests                   <- Folder for all unit and integration tests.
    │
    ├── .pre-commit-config.yaml <- Pre-commit hooks configuration file for keeping the codebase tidy,
    │                              install it with `pre-commit install` and test with `pre-commit run --all-files`
    ├── LICENSE
    │
    ├── Makefile                <- Makefile with commands like `make data` or `make train`
    │
    ├── pyproject.toml          <- makes project pip installable (pip install -e .) so src can be imported
    │    
    └── README.md               <- The top-level README for developers using this project.
