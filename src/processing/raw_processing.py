import pandas as pd

COLUMN_RENAMES = {
    "month_year_of_transaction_date": "date",
    "transaction_price": "price",
}


def clean_column_names(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize column names of a DataFrame.

    This function removes extra spaces, converts to lowercase, replaces spaces
    with underscores, removes commas, and replaces forward slashes with `_or_`.

    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame with original column names.

    Returns
    -------
    pd.DataFrame
        A new DataFrame with cleaned column names.
    """
    processed_data = data.copy()
    clean_columns = (
        data.columns.str.strip()
        .str.replace(" ", "_", regex=False)
        .str.lower()
        .str.replace(",", "", regex=False)
        .str.replace("/", "_or_", regex=False)
    )
    processed_data.columns = clean_columns
    return processed_data


def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Rename specific columns in the DataFrame for consistency.

    Renames:
    - 'month_year_of_transaction_date' → 'date'
    - 'transaction_price' → 'price'

    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame with cleaned column names.

    Returns
    -------
    pd.DataFrame
        DataFrame with renamed columns.
    """
    return data.rename(columns=COLUMN_RENAMES)


def format_price_column(data: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the 'price' column from string format to numeric.

    The function removes the 'RM' prefix and commas, then converts
    the values to floats.

    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame containing a 'price' column in string format.

    Returns
    -------
    pd.DataFrame
        DataFrame with 'price' column converted to float.
    """
    processed = data.copy()
    processed["price"] = (
        processed["price"]
        .str.replace("RM", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )
    return processed


def format_raw_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Format raw property transaction data for analysis.

    This function applies the following steps:
    1. Clean column names.
    2. Rename specific columns for consistency.
    3. Convert 'price' column to numeric.

    Parameters
    ----------
    data : pd.DataFrame
        Raw input DataFrame containing transaction data.

    Returns
    -------
    pd.DataFrame
        Cleaned and formatted DataFrame ready for analysis.
    """
    return data.pipe(clean_column_names).pipe(rename_columns).pipe(format_price_column)
