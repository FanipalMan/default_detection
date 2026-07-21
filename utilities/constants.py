CONTINUOUS_COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'L', 'Y', 'Z', 'age']
CONTINUOUS_COLUMNS_TO_FILLNA = ['A', 'E', 'H', 'L', 'Z']
CONTINUOUS_TO_REMOVE_OUTLIERS = ['A', 'C', 'D', 'E', 'F', 'H', 'Z']

CATEGORICAL_COLUMNS_TO_LABEL_ENCODE = ['education', 'dependent_count']
CATEGORICAL_COLUMNS_TO_ONE_HOT_ENCODE = ['G', 'proffessional_status', 'marital_status', 
'housing_status', 'working_status', 'region', 'V']
BINARY_CATEGORICAL_COLUMNS = ['R', 'T', 'U', 'W', 'X']
CATEGORICAL_COLUMNS = (CATEGORICAL_COLUMNS_TO_LABEL_ENCODE + 
                       CATEGORICAL_COLUMNS_TO_ONE_HOT_ENCODE + 
                       BINARY_CATEGORICAL_COLUMNS + ['gender'])
CATEGORICAL_COLUMNS_TO_FILLNA = ['region', 'working_status', 'U', 'W']

COLUMNS_RENAME_MAPPING = {
    'I':'gender', 
    'S':'working_status', 
    'K': 'region',
    'J': 'age',
    'M': 'proffessional_status',
    'N': 'education',
    'O': 'marital_status',
    'P': 'dependent_count',
    'Q': 'housing_status',
    'MARKER': 'target',
}

GENDER_MAPPING = {
    "woman": 0,
    "man": 1
}

BINARY_CATEGORICAL_MAPPING = {
    "Yes": 1,
    "No": 0
}

EDUCATION_MAPPING = {
    'Primary or lower secondary education': 0,
    'Secondary education (plus special education)': 1,
    'Incomplete higher education': 1,
    'Higher education (one or more)': 2
}

DEPENDANTS_MAPPING = {
    '0 Zero': 0,
    '1 One': 1,
    '2 Two': 2,
    '3 Three': 3,
    'More than 3': 4
}

IMPORTANT_FEATURES = [
    'region_Gomel region',
    'V_No',
    'housing_status_property',
    'marital_status_Single/unmarried',
    'region_Vitebsk region',
    'G_5',
    'W',
    'region_Minsk region',
    'T',
    'A',
    'G_4',
    'G_6',
    'gender',
    'H_bigger_than_zero',
    'G_13',
    'region_Grodno region',
    'U',
    'B',
    'X',
    'proffessional_status_NE employee',
    'proffessional_status_Head/Deputy head (organiz.)',
    'F',
    'has_dependents',
    'working_status_Pensioner',
    'G_24',
    'G_9',
    'marital_status_Married',
    'C',
    'L',
    'marital_status_Divorced/widow',
    'region_Minsk',
    'R',
    'E',
    'D',
    'H',
    'education',
    'working_status_Unemployed',
    'G_10',
    'housing_status_rent/hire',
    'working_status_Works',
    'age',
    'is_single',
    'G_3',
    'dependent_count',
    'region_Mogilev region',
    'Y'
 ]