import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df.to_csv(r'C:\ml-ci-cd-pipeline\data\iris.csv', index=False)