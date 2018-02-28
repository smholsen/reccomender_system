from sklearn.model_selection import cross_validate as cv
from sklearn.decomposition.truncated_svd import TruncatedSVD
import pandas as pd

keywords_data_filename = 'keywords_data.txt'
active_data_filename = 'active_time_data.txt'

header = ['user_id', 'item_id', 'rating']
keywords_data = pd.read_csv(keywords_data_filename, sep='*', names=header, engine='python')
active_time_data = pd.read_csv(active_data_filename, sep='*', names=header, engine='python')


# Number of users in current set
print('Number of unique users in current data-set', active_time_data.user_id.unique().shape[0])
print('Number of unique articles in current data-set', active_time_data.item_id.unique().shape[0])

# SVD allows us to look at our input matrix as a product of three smaller matrices; U, Z and V.
# In short this will help us discover concepts from the original input matrix,
# (subsets of users that like subsets of items)
# Note that use of SVD is not strictly restricted to user-item matrices
# https://www.youtube.com/watch?v=P5mlg91as1c

algorithm = TruncatedSVD()

# Finally we run our cross validation in n folds, where n is denoted by the cv parameter.
# Verbose can be adjusted by an integer to determine level of verbosity.
# We pass in our SVD algorithm as the estimator used to fit the data.
# X is our data set that we want to fit.
# Since our estimator (The SVD algorithm), We must either define our own estimator, or we can simply define how it
# score the fitting.
# Since we currently evaluate the enjoyment of our users per article highly binary, (Please see the rate_article fn in
# the filter script), we can easily decide our precision and recall based on whether or not our prediction exactly
# matches the binary rating field in the test set.
# This, the F1 scoring metric seems an intuitive choice for measuring our success, as it provides a balanced score
# based on the two.

cv(estimator=algorithm, X=active_time_data, scoring='f1', cv=5, verbose=True)

