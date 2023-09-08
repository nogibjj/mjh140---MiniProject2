import pandas as pd
import numpy as np
import os
import sys

def describe_data(file_name: str):
    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    new_path = parent_dir + "\\data"
    file_path = os.path.join(new_path, file_name)

    try:
        df = pd.read_csv(file_path)
        return df.describe()
    except FileNotFoundError:
        return print(f"The file ({file_name}) was not found.")
    except Exception as e:
        return print(f"An exception of type {type(e).__name__} occurred: {e}")
    
if __name__ == "__main__":
    describe_data("testdata.csv")