import mpmath as mp
import itertools
mp.mp.dps = 50

q = mp.mpf("1.10997859556")
E0 = mp.mpf("4.1859808")
f_req = mp.mpf("0.587762432663460228319559")
W_alg = mp.mpf("0.660673770417933908")
h = q - 1/q
z = mp.sqrt(q)/(q+1)
z0 = mp.sqrt(q) - 1/mp.sqrt(q)
kappa = mp.mpf(3)/16

vals = {
    "W": W_alg,
    "z0": z0,
    "z": z,
    "h": h,
    "q": q,
    "kappa": kappa,
    "pi": mp.pi,
    "1": mp.mpf(1),
    "2": mp.mpf(2),
    "3": mp.mpf(3),
    "1/2": mp.mpf("0.5"),
    "E0": E0
}

# Try W * (1 - something)
print("Target:", f_req)
print("W_alg:", W_alg)
print("W_alg - target:", W_alg - f_req)
print("Ratio target/W_alg:", f_req / W_alg)

ratio = f_req / W_alg
print("Ratio:", ratio)
# 0.889640927
# 1 - ratio: 0.110359
print("1 - Ratio:", 1 - ratio)

print("z0:", z0)  # 0.104388

# Check if there is an exact formula
print("Difference from z0:", (1 - ratio) - z0) # 0.00597

print("kappa * z0:", kappa * z0)
print("z0 + z0^2:", z0 + z0**2)
