"""Eigenvalues of the gamma-gamma vertex V = s0 s1^-1 on the (2,1) block of H_3(q).
Pre-registered in PREREGISTRATION-vertex-eigenvalues.md. Exact sympy; mpmath at 30 dps."""
import json, sympy as sp, mpmath as mp
mp.mp.dps = 30
q = sp.symbols('q', positive=True)
h = q - 1/q
a = h/(1 - q**4); ap = h/(1 - q**-4)
b = sp.sqrt(sp.simplify(1 + a*ap))
s0 = sp.Matrix([[q, 0], [0, -1/q]])
s1 = sp.Matrix([[a, b], [b, ap]])
I2 = sp.eye(2)
hecke = sp.simplify(s1*s1 - h*s1 - I2)
s1i = s1 - h*I2
V = s0*s1i
detV = sp.simplify(V.det())
trV = sp.factor(sp.simplify(V.trace()))
# eigenvalue phase: cos(theta) = tr/2
from qou_substrate.constants import Q_50_DIGIT_STR  # proton pin, not a typed copy
Q0 = mp.mpf(Q_50_DIGIT_STR)
tr0 = mp.mpf(str(sp.N(trV.subs(q, sp.Rational(str(Q0))), 40)))
theta0 = mp.acos(tr0/2)
V3 = V**3
trV3 = sp.factor(sp.simplify(V3.trace()))
out = {
  "preregistration": "34369e6d5df",
  "hecke_check_s1": str(hecke),
  "P1_det_V": str(detV),
  "P1_one_dim_blocks": "(3): q*q^-1 = 1, (1^3): (-1/q)(-q) = 1",
  "tr_V_21": str(trV),
  "tr_V_21_at_q1": str(sp.limit(trV, q, 1)),
  "P2_theta_at_q1_over_2pi": str(sp.nsimplify(sp.acos(sp.limit(trV, q, 1)/2)/(2*sp.pi))),
  "P3_tr_V_at_q0": mp.nstr(tr0, 25),
  "P3_in_open_interval": bool(-2 < tr0 < 2),
  "theta_q0_over_2pi": mp.nstr(theta0/(2*mp.pi), 25),
  "theta_q0_over_2pi_minus_third": mp.nstr(theta0/(2*mp.pi) - mp.mpf(1)/3, 15),
  "R1_charges_q0": [mp.nstr(theta0/(2*mp.pi), 20), mp.nstr(-theta0/(2*mp.pi), 20)],
  "R2_charges_q0": [mp.nstr(theta0/(2*mp.pi), 20), mp.nstr(1-theta0/(2*mp.pi), 20)],
  "P4_tr_V3_21": str(trV3),
  "P4_tr_V3_at_q1": str(sp.limit(trV3, q, 1)),
}
# series of theta/2pi around q=1 in h-like variable
eps = sp.symbols('eps')
ser = sp.series(sp.acos(trV.subs(q, 1+eps)/2)/(2*sp.pi), eps, 0, 3)
out["theta_over_2pi_series_q=1+eps"] = str(sp.simplify(ser))
print(json.dumps(out, indent=1, ensure_ascii=False))
json.dump(out, open(__file__.replace('.py', '.out.json'), 'w'), indent=1, ensure_ascii=False)
