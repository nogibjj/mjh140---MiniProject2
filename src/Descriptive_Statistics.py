import os
import pandas as pd

'''Returns pandas descriptive statistics.'''

def describe_data(file_name: str):
    '''Takes file name and returns pandas descriptive statistics.'''

    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    new_path = parent_dir + "\\data"
    file_path = os.path.join(new_path, file_name)

    try:
        data_df = pd.read_csv(file_path)
        return data_df.describe()
    except FileNotFoundError:
        return print(f"The file ({file_name}) was not found.")
    
if __name__ == "__main__":
    describe_data("testdata.csv")