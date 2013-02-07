# This is the abstract class for predictor
int m = 500 # Dimension of matrix A
int n = 0 # Col of matrix A, read from data
bool trans = false # transaction fee control

"""
Read hdf5 file into dataset
input: hdf5
output: numpy array
"""
def readData(dataPath):
    print('Here needs to output the numpy array')

"""
Slice the numpy array and make the window matrix A, and save the remaining in another matrix
Here we need to shift the ith colomn, which is the column we are going to predict, one row upper. Which means the A_ni in matrix A is in the same row of A_(n-1).
input: numpy array
output: start row start, end row end, matrix A
"""
def sliceData(numpy_arr, i):
    print('This is the sliced array')

"""
Use the model needed to get the first K most_significant_eigenvalue.
input: A
output: x
"""
def find_most_sig_eigen(A):
    print('Will produce the eigenvalues, Q, and S')

"""
Predict the ith return with x
input: x, alpha
ouput: A_ni
"""
def predict(x, alpha):
    print('Predict A_ni')

"""
Test the result
input: A_ni
ouput: true A_ni
"""
def test(predicted, truth):
    print('Here comes the result')

"""
Apply strategic method to put and call orders with the transaction fee byte controlled
input: data
output: return
"""
