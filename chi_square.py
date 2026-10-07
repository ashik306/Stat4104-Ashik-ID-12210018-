#3. Chi-Square Test of Homogeneity
#Example: Treatment preference across three hospitals
import numpy as np
from scipy.stats import chi2_contingency

table = np.array([
    [40, 35, 25],
    [30, 45, 25],
    [20, 30, 50]
])

chi2, p, df, expected = chi2_contingency(table)

print("Chi-square =", chi2)
print("Degrees of freedom =", df)
print("p-value =", p)

print("\nExpected frequencies:")
print(expected)

if p < 0.05:
    print("\nReject H0: The treatment distributions differ among hospitals.")
else:
    print("\nFail to reject H0: The treatment distributions are homogeneous.")
