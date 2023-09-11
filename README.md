# Descriptive Statistics with Pandas and Matplotlib   [![GitHub Actions](https://github.com/nogibjj/mjh140---MiniProject2/workflows/CI/badge.svg)](https://github.com/nogibjj/mjh140---MiniProject2/actions)


## Summary:

This project introduces the Pandas package for generating descriptive statistics on the Iris Species dataset. Matplotlib and Seaborn packages were used to create a boxplot visualization of Sepal Length by Species. For more info on the Iris Species dataset, visit the following link:

https://www.kaggle.com/datasets/uciml/iris?resource=download

## Structure

```text
├── .devcontainer
│   ├── Dockerfile
│   └── devcontainer.json
├── data
│   └── iris_data.csv
├── .github/workflows
│   └── actions.yml
├── .gitignore
├── Makefile
├── PetalLength_by_Species.png
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   └── descriptive_statistic
└── tests
    ├── __init__.py
    └── test_descriptivestats.py

```

## Results:

The following table of descriptive statistics was outputed from the `describe_iris` function within `src/descriptive_statistic.py`:

|          | PetalLengthCm | PetalWidthCm | SepalWidthCm | SepalLengthCm |
| -------- | ------------- | ------------ | ------------ | ------------- |
|count     |    150.00     |   150.00    |   150.00     |    150.00 |
|mean      |      3.76     |     1.20    |     3.05     |      5.84 |
|std       |      1.76     |     0.76    |     0.43     |      0.83 |
|min       |      1.00     |     0.10    |     2.00     |      4.30 |
|25%       |      1.60     |     0.30    |     2.80     |      5.10 |
|median    |      4.06     |     1.25    |     3.03     |      5.82 |
|75%       |      5.10     |     1.80    |     3.30     |      6.40 |
|max       |      6.90     |     2.50    |     4.40     |      7.90 |


The following boxplot visualization for Sepal Length distribution by Species was created from the `visualize_iris` function within `src/descriptive_statistic.py`:

<p align = "center"><img src = "https://github.com/nogibjj/mjh140---MiniProject2/blob/main/SepalLength_by_Species.png" width = 500px></p>
