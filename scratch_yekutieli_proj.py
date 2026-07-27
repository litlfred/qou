import mpmath as mp
mp.mp.dps = 50

Q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
E0 = mp.mpf("0.51099895069") / (Q0 * (Q0 - 1))
AME_D = mp.mpf("2.224566")

f_req = mp.exp(-AME_D / E0)
W_alg = mp.mpf("0.66067377197")
kappa = mp.mpf(3)/16
tr_M_B3 = mp.mpf("1.00673") # wait, exact tr_M_B3:
y_3 = mp.mpf("0.4153957863")
y_21 = mp.mpf("0.2809296340")
y_111 = mp.mpf("0.0227449457")
chi_21 = mp.mpf("1.9941858104")

tr_M_B3 = y_3 * 1 + y_21 * chi_21 + y_111 * 1

print(f"Target f_req = {mp.nstr(f_req, 8)}")

tests = {
    "W_alg * (tr_M_B3 - kappa)": W_alg * (tr_M_B3 - kappa),
    "W_alg - kappa * (1 - y_111)": W_alg - kappa * (1 - y_111),
    "W_alg - kappa * tr_M(B3)": W_alg - kappa * tr_M_B3,
    "W_alg - kappa * tr_M(B3 * (1 - A3))": W_alg - kappa * (tr_M_B3 - y_111),
    "W_alg - kappa * tr_M(B3 * P21)": W_alg - kappa * (y_21 * chi_21),
    "W_alg * (1 - kappa * (tr_M_B3 - y_111))": W_alg * (1 - kappa * (tr_M_B3 - y_111)),
    "(W_alg - y_111) * (1 - kappa)": (W_alg - y_111) * (1 - kappa),
    "W_alg * (1 - kappa * W_alg)": W_alg * (1 - kappa * W_alg),
    "W_alg * exp(-kappa * (tr_M_B3 - y_111))": W_alg * mp.exp(-kappa * (tr_M_B3 - y_111)),
    "W_alg * exp(-kappa * tr_M(P_21))": W_alg * mp.exp(-kappa * (2*y_21)),
}

for name, val in tests.items():
    diff = abs(val - f_req)
    if diff < 0.05:
        print(f"{name:45} = {mp.nstr(val, 8)} (diff: {mp.nstr(diff, 6)})")

