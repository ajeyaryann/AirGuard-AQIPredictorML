import pandas as pd

df = pd.read_csv('sampled_file.csv')

df_sampled = df.sample(frac = 0.1, random_state=42)

df_sampled.to_csv('air_quality_dataset.csv', index = False)