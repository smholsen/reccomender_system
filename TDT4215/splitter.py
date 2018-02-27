from surprise import Dataset
from surprise import Reader
from surprise import SVD
from sklearn.model_selection import KFold

reader = Reader(line_format='user item rating', sep='**')
data = Dataset.load_from_file('dataset1.txt', reader=reader)
algo = SVD()

kf = KFold(n_splits=2)

for trainset, testset in kf.split(data):
    print(trainset)
    # print(trainset)
    # print(testset)
    # algo.fit(trainset)
    # predictions = algo.test(testset)
