import numpy as np
import pandas as pd

from ..references.data_reference import EXPECTED_RAW_COLUMNS


def validate_raw_data(data: pd.DataFrame) -> None:
    """
    Validate the structure and types of the raw property transaction data.

    This function checks that:
      1. The DataFrame has the expected column names, in the correct order.
      2. The column ``"Month, Year of Transaction Date"`` is of datetime type.

    Parameters
    ----------
    data : pandas.DataFrame
        Raw property transaction dataset to validate.

    Raises
    ------
    ValueError
        If the DataFrame columns do not exactly match the expected schema.
    TypeError
        If the `Month, Year of Transaction Date` column is not a datetime type.

    """
    columns = data.columns.str.strip()
    if not np.array_equal(columns, EXPECTED_RAW_COLUMNS):
        raise ValueError(
            "The columns do not match the established column structure"
            f"{list(columns)}. Expected: {EXPECTED_RAW_COLUMNS}"
        )

    if not pd.api.types.is_datetime64_any_dtype(
        data["Month, Year of Transaction Date"]
    ):
        raise TypeError("`Month, Year of Transaction Date` must be datetime type")
