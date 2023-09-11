'''Returns pandas descriptive statistics.'''

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def import_iris(file_name: str):
    '''Converts csv file to dataframe'''

    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    new_path = parent_dir + "/data"
    file_path = os.path.join(new_path, file_name)

    try:
        iris_df = pd.read_csv(file_path)
        cols = set(iris_df.columns) - {'Id'}
        reduced_iris = iris_df[list(cols)]
        return reduced_iris
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"The file ({file_name}) was not found.") from exc

def describe_iris(iris_df):
    '''Returns pandas descriptive statistics on dataframe.'''

    if not isinstance(iris_df, pd.DataFrame):
        raise TypeError("Iris data must be in pandas dataframe form")
    
    return iris_df.describe()

def visualize_iris(iris_df):
    '''Plots Petal Length by Species'''
    plt.figure(figsize=(10, 6))
    sns.violinplot(x="Species", y="PetalLengthCm", data=iris_df)
    plt.title("Violin Plot of Petal Length by Species")
    plt.show()

    plt.savefig("PetalLength_by_Species.png")

    
if __name__ == "__main__":
    iris_data = import_iris("iris_data.csv")
    print(describe_iris(iris_data))
    visualize_iris(iris_data)