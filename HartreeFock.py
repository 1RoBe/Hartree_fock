import numpy as np

def main():
    # return create_Mat_M(vec_nu())
    print(create_Mat_M(vec_nu()))
    # test_create_mat_M()
    a = recursive_func(5)
    print(a)

def vec_v():
    return np.array(range(0, 10, 1))

def vec_nu():
    return np.array(range(1, 6, 1))

def create_Mat_M(vec_1):
    M = np.zeros((len(vec_1), len(vec_1)), dtype=int)

    for j in range(len(vec_1)):
        for i in range(len(vec_1)):
            if j>i:
                M[i][j] = 0
            else: 
                M[i][j] = vec_1[i-j]
                
    return M

def recursive_func(n):
    if n == 1:
        return 1
    else:
        return n * recursive_func(n-1)
    







def test_create_mat_M():
    assert create_Mat_M(np.array([1, 2, 3, 4, 5])).any == np.array([[1, 0, 0, 0, 0], [2, 1, 0, 0, 0], [3, 2, 1, 0, 0], [4, 3, 2, 1, 0], [5, 4, 3, 2, 1]]).any

# print(np.array([[1, 0, 0, 0, 0], [2, 1, 0, 0, 0], [3, 2, 1, 0, 0], [4, 3, 2, 1, 0], [5, 4, 3, 2, 1]]))

if __name__ == "__main__":
    main()