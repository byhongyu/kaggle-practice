# -*- coding: utf-8 -*-

from os import path
import pandas as pd

# acquire data
train_df = pd.read_csv(path.join('data','train.csv'))
test_df = pd.read_csv(path.join('data','test.csv'))
combine = [train_df,test_df]

print(train_df.columns.values)
train_df.head()
train_df.tail()
train_df.info()
