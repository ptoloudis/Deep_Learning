import pandas as pd

test_data = []
with open('neural_collaborative_filtering-master/Data/ml-1m.test.negative', 'r') as fd:
    line = fd.readline()
    while line != None and line != '':
        arr = line.split('\t')
        u = eval(arr[0])[0]
        test_data.append([u, eval(arr[0])[1]])
        for i in arr[1:]:
            test_data.append([u, int(i)])
        line = fd.readline()

test_data = pd.DataFrame(test_data, columns=['user_id', 'item_id'])
test_data.to_csv('test_data.csv', index=False)