from computations._deprecated.term6_scaling_heavy import term6
Z, N = 82, 96
A = Z + N
t6 = term6(Z, N)
pred = A * (342.5 * t6 / A**3 + 1.20)
print(f"B_pred for 178Pb: {pred} MeV")
