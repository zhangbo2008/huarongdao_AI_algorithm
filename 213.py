import numpy as np

a=[np.array([[1,2,3]])
,np.array([[4,2,4]]),
np.array([[5,2,7]])
]

b=np.array([[1,2,3]])
print(b==a)
print(np.any(np.all(b==a,axis=1)))
