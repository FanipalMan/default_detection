from typing import Dict

import pandas as pd

from utilities.constants import (
    CATEGORICAL_COLUMNS_TO_ONE_HOT_ENCODE,
    BINARY_CATEGORICAL_COLUMNS,
    CONTINUOUS_COLUMNS_TO_FILLNA,
    CATEGORICAL_COLUMNS_TO_FILLNA,
    COLUMNS_RENAME_MAPPING,
    GENDER_MAPPING,
    BINARY_CATEGORICAL_MAPPING,
    EDUCATION_MAPPING,
    DEPENDANTS_MAPPING
)

def remove_top_percentile(dataset, columns, percentile=0.999):
    mask = pd.Series(True, index=dataset.index)

    for column in columns:
        threshold = dataset[column].quantile(percentile)
        mask = mask & ((dataset[column] < threshold) | (dataset[column].isna()))
    
    dataset = dataset.loc[mask].copy()

    return dataset

def preprocess_data(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset.rename(columns=COLUMNS_RENAME_MAPPING, inplace=True)
    dataset.drop(columns=['ID'], inplace=True)

    dataset["gender"] = dataset["gender"].str.strip().str.lower()
    dataset["gender"] = dataset["gender"].map(GENDER_MAPPING)

    for column in BINARY_CATEGORICAL_COLUMNS:
        dataset[column] = dataset[column].map(BINARY_CATEGORICAL_MAPPING)

    dataset['education'] = dataset['education'].map(EDUCATION_MAPPING)

    dataset['dependent_count'] = dataset['dependent_count'].map(DEPENDANTS_MAPPING)

    return dataset

def add_new_features(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset['has_dependents'] = dataset['dependent_count'].apply(lambda x: 1 if x > 0 else 0)
    dataset['H_bigger_than_zero'] = dataset['H'] > 0
    dataset['is_single'] = dataset['marital_status'].isin(['Single/unmarried', 'Divorced/widow'])

    return dataset

def fillna(datasets: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    
    continuous_columns_fill_value = datasets['train'][CONTINUOUS_COLUMNS_TO_FILLNA].median()
    categorical_columns_fill_value = datasets['train'][CATEGORICAL_COLUMNS_TO_FILLNA].mode().iloc[0]

    filled_datasets = {}

    for data_type, data in datasets.items():
        dataset = data.copy()

        dataset[CONTINUOUS_COLUMNS_TO_FILLNA] = dataset[CONTINUOUS_COLUMNS_TO_FILLNA].fillna(
            continuous_columns_fill_value
        )

        dataset[CATEGORICAL_COLUMNS_TO_FILLNA] = dataset[CATEGORICAL_COLUMNS_TO_FILLNA].fillna(
            categorical_columns_fill_value
        )

        filled_datasets[data_type] = dataset

    return filled_datasets

def one_hot_encode(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset = pd.get_dummies(
        dataset,
        columns=CATEGORICAL_COLUMNS_TO_ONE_HOT_ENCODE,
        drop_first=True,
        dtype=int
    )
    return dataset