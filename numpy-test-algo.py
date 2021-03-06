import numpy as np
print(np.__version__)
'1.12.1'

L = list(range(10))

[str(c) for c in L]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

[type(item) for item in L]
[int, int, int, int, int, int, int, int, int, int]


#creating arrays
np.zeros(10, dtype='int')
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


#creating a 3 row x 5 column matrix
np.ones((3,5), dtype=float)
array([[ 1.,  1.,  1.,  1.,  1.],
      [ 1.,  1.,  1.,  1.,  1.],
      [ 1.,  1.,  1.,  1.,  1.]])


#creating a matrix with a predefined value
np.full((3,5),1.23)
array([[ 1.23,  1.23,  1.23,  1.23,  1.23],
      [ 1.23,  1.23,  1.23,  1.23,  1.23],
      [ 1.23,  1.23,  1.23,  1.23,  1.23]])


#create an array with a set sequence
np.arange(0, 20, 2)
array([0, 2, 4, 6, 8,10,12,14,16,18])


#create an array of even space between the given range of values
np.linspace(0, 1, 5)
array([ 0., 0.25, 0.5 , 0.75, 1.])


#create a 3x3 array with mean 0 and standard deviation 1 in a given dimension
np.random.normal(0, 1, (3,3))
array([[ 0.72432142, -0.90024075,  0.27363808],
      [ 0.88426129,  1.45096856, -1.03547109],
      [-0.42930994, -1.02284441, -1.59753603]])


#create an identity matrix
np.eye(3)
array([[ 1.,  0.,  0.],
      [ 0.,  1.,  0.],
      [ 0.,  0.,  1.]])


#set a random seed
np.random.seed(0)


x1 = np.random.randint(10, size=6) #one dimension
x2 = np.random.randint(10, size=(3,4)) #two dimension
x3 = np.random.randint(10, size=(3,4,5)) #three dimension


print("x3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
('x3 ndim:', 3)
('x3 shape:', (3, 4, 5))
('x3 size: ', 60)