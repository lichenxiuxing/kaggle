import pandas as pd
import numpy as np

source_df = pd.read_csv('train.csv')
pred_df = pd.read_csv('test.csv')
full_df=source_df.append(pred_df,ignore_index=True)
