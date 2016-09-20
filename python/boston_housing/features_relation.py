# Import libraries necessary for this project
import numpy as np
import pandas as pd
import visuals as vs # Supplementary code
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_validation import ShuffleSplit

# Load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis = 1)
    
# Success
print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)

for var in ['LSTAT', 'RM', 'PTRATIO']:
    sns.regplot(data[var], prices)
    plt.show()