{% if cookiecutter.include_data_science == 'y' -%}
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
from tqdm import tqdm

logger = logging.getLogger(__name__)


def load_csv(file_path: str | Path, **kwargs) -> pd.DataFrame:
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    logger.info(f"Loading CSV file: {file_path}")
    df = pd.read_csv(file_path, **kwargs)
    logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df


def save_csv(df: pd.DataFrame, file_path: str | Path, **kwargs) -> None:
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Saving CSV file: {file_path}")
    df.to_csv(file_path, index=False, **kwargs)
    logger.info(f"Saved {len(df)} rows to {file_path}")


def clean_dataframe(df: pd.DataFrame, 
                   drop_duplicates: bool = True,
                   drop_na_columns: Optional[List[str]] = None,
                   fill_na_values: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
    logger.info("Starting data cleaning")
    original_shape = df.shape
    
    cleaned_df = df.copy()
    
    if drop_duplicates:
        cleaned_df = cleaned_df.drop_duplicates()
        logger.info(f"Removed {original_shape[0] - len(cleaned_df)} duplicate rows")
    
    if drop_na_columns:
        cleaned_df = cleaned_df.dropna(subset=drop_na_columns)
        logger.info(f"Removed rows with NA in columns: {drop_na_columns}")
    
    if fill_na_values:
        cleaned_df = cleaned_df.fillna(fill_na_values)
        logger.info(f"Filled NA values: {fill_na_values}")
    
    logger.info(f"Data cleaning complete: {original_shape} -> {cleaned_df.shape}")
    return cleaned_df


def process_in_chunks(df: pd.DataFrame, 
                     chunk_size: int = 1000,
                     process_func: callable = None) -> pd.DataFrame:
    if process_func is None:
        return df
    
    logger.info(f"Processing dataframe in chunks of {chunk_size}")
    
    chunks = []
    for i in tqdm(range(0, len(df), chunk_size), desc="Processing chunks"):
        chunk = df.iloc[i:i + chunk_size]
        processed_chunk = process_func(chunk)
        chunks.append(processed_chunk)
    
    result = pd.concat(chunks, ignore_index=True)
    logger.info(f"Processed {len(chunks)} chunks")
    return result


def get_data_summary(df: pd.DataFrame) -> Dict[str, Any]:
    summary = {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "memory_usage": df.memory_usage(deep=True).sum(),
    }
    
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 0:
        summary["numeric_summary"] = df[numeric_columns].describe().to_dict()
    
    return summary
{% endif %}
