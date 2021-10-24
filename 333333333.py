import pandas as pd
import numpy as np

arr = np.array([[64, 22,],   [58, 64],   [42, 31]])

# li = ['one','two','three']
df = pd.DataFrame(arr, index=None,columns=None)
kk=[df,df,df]
print(kk)