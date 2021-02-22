import math
import pandas as pd
from itertools import product

def x_val(k):
    return pow(10, -1*k)

def empirical(x):
    return (math.exp(x) - 1)/x

def mathematical(x):
    return (math.exp(x) - 1)/math.log(math.exp(x))

values = []
results = []
for i in range(1, 16):
   values.append(x_val(i))
   val = mathematical(x_val(i))
   results.append(val)

df = pd.DataFrame({"x values": values, "results": results})
df['results'] = df['results'].map(lambda x: '%2.16f' % x)
print(df)