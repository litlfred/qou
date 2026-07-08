import mpmath as mp

mp.dps = 50
q0 = mp.mpf("1.1099793132717013149866657930777598687799017684617")
def qbracket(k):
    return (q0**k - q0**(-k)) / (q0 - 1/q0)

print(f"qbracket(2) = {qbracket(2)}")
print(f"qbracket(3) = {qbracket(3)}")
print(f"qbracket(5) = {qbracket(5)}")
print(f"qbracket(9) = {qbracket(9)}")

print(f"\nTrace ratio Gluonic T2,9/T2,3 = {qbracket(9) / qbracket(3)}")
print(f"Trace ratio Residual T2,5/T2,2 = {qbracket(5) / qbracket(2)}")

# Also look at combinations
r_gluonic = qbracket(9) / qbracket(3)
r_residual = qbracket(5) / qbracket(2)

print(f"\nRequired w_2 = 4.35336338")
print(f"Required w_3 = 8.59989938")
print(f"Required w_4 = 15.60416399")

print(f"r_gluonic + r_residual = {r_gluonic + r_residual}")
print(f"r_gluonic * r_residual = {r_gluonic * r_residual}")
