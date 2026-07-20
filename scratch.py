import mpmath as mp
mp.mp.dps = 50

q = mp.mpf("1.10997859556")
E0 = mp.mpf("4.1859808")
f_req = mp.mpf("0.587762432663460228319559")
W_alg = mp.mpf("0.66067377")
f_std = mp.mpf("0.39479017")
z = mp.sqrt(q)/(q+1)
z0 = mp.sqrt(q) - 1/mp.sqrt(q)

trM = mp.mpf("1.006730454652734")
kappa = mp.mpf(3)/16

print("f_req:", f_req)
print("W_alg:", W_alg)
print("z0:", z0)
print("z:", z)
print("trM:", trM)
print("kappa:", kappa)
print("W_alg * trM:", W_alg * trM)
print("W_alg / trM:", W_alg / trM)
print("trM / W_alg:", trM / W_alg)
print("W_alg * z0:", W_alg * z0)
print("f_req * 1.0", f_req)
print("sqrt(f_req):", mp.sqrt(f_req))
print("W_alg - z0:", W_alg - z0)
print("W_alg * (1 - z0):", W_alg * (1 - z0))
print("W_alg * (1 - z0^2):", W_alg * (1 - z0**2))
print("1 - z0^2:", 1 - z0**2)
print("W_alg * z:", W_alg * z)
print("z0 * E0:", z0 * E0)
print("1 / (trM^something) ...")
