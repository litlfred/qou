import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0

q = Q0
def qint(m, q=Q0):
    return (q ** m - q ** (-m)) / (q - q ** (-1))

# For S3, the dimensions are 1, 2, 1.
# What if D^2 = [1]^2 + [2]^2 + [1]^2 ?
D2_1 = qint(1)**2 + qint(2)**2 + qint(1)**2
F_21_1 = qint(2)**2 / D2_1

# What if it's the full McKay nodes for a different group?
# For n=3, maybe it's just the dimensions of S3?
# The deuteron is a 2-dimensional representation.

print("f_req:", mp.exp(-mp.mpf("2.224566") / E0))
print("F_21_1 ([2]^2 / ([1]^2+[2]^2+[1]^2)):", F_21_1)

# What if D^2 = [1]^2 + [2]^2 + [3]^2? (SU(2) spins 0, 1/2, 1)
D2_2 = qint(1)**2 + qint(2)**2 + qint(3)**2
F_21_2 = qint(2)**2 / D2_2
print("F_21_2 ([2]^2 / ([1]^2+[2]^2+[3]^2)):", F_21_2)

# What if it uses the full affine E8 McKay data?
# marks: 1,2,3,4,5,6,4,2,3
D2_E8 = mp.fsum(qint(m)**2 for m in [1,2,3,4,5,6,4,2,3])
F_E8_mark2 = qint(2)**2 / D2_E8
print("F_E8_mark2 ([2]^2 / D_E8^2):", F_E8_mark2)

# What if it's the 2/D_E8 like in the script?
print("2/D_E8:", 2/mp.sqrt(D2_E8))

# What about Borromean (Sigma(2,3,3) or something)?
