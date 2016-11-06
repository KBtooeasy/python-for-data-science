import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('Datasets/wheat.data')


#
# TODO: Drop the 'id' feature
# 
df.drop(labels='id', axis=1, inplace=True)

#
# TODO: Compute the correlation matrix of your dataframe
# 
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)
plt.show()


#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..


plt.show()


