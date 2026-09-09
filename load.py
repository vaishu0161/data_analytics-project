import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

try:
    from google.colab import files
    uploaded = files.upload()
    filename = list(uploaded.keys())[0]
except ImportError:
    filename = '/content/seasonal_agriculture_performance_dataset (1).csv'

df = pd.read_csv(filename)
season_order = ['Kharif', 'Rabi', 'Zaid']
df.head()
