"""Pre-registered 7c8ef0b86c3. Series and zero of the section-35 M1 arm. Exact sympy + mpmath 60 dps."""
import json, sympy as sp, mpmath as mp
from qou_substrate import constants as C
q, e = sp.symbols('q epsilon', positive=True)
arms = json.load(open('mn_muon_scale_probe.out.json'))["arms"]
E_over_2mmu = sp.sympify(arms["M1_D2"]["E_over_2m_mu"], locals={"q": q})
# E / (m_e Vol) = 2 * E_over_2mmu / hbar^2
G = sp.together(2*E_over_2mmu/(1 - 1/q)**2)
ser = sp.series(G.subs(q, 1 + e), e, 0, 4).removeO()
coeffs = {k: sp.nsimplify(sp.simplify(ser.coeff(e, k))) for k in range(4)}
mp.mp.dps = 60
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(C.M_E_MEV_STR); vol = 2*mp.clsin(2, mp.pi/3)
f = sp.lambdify(q, G, "mpmath")
num = sp.factor(sp.numer(sp.together(G)))
roots = [r for r in sp.Poly(sp.numer(sp.together(G)), q).nroots(n=50) if r.is_real and 1 < r < 1.2]
qs = mp.findroot(f, (mp.mpf('1.01'), q0), solver='anderson')
val = me*vol*f(q0)
out = {"preregistration": "7c8ef0b86c3",
  "series_E_over_meVol_in_eps": {str(k): str(v) for k, v in coeffs.items()},
  "leading_coeff_MeV": mp.nstr(me*vol*mp.mpf(sp.N(coeffs[1], 60)), 15),
  "zero_q_star": mp.nstr(qs, 25), "real_numerator_roots_in_(1,1.2)": [str(r) for r in roots],
  "value_q0_MeV": mp.nstr(val, 15),
  "comparison_after": {"ratio_to_lattice_quark_mass_2.52": mp.nstr(val/mp.mpf('2.52'), 6),
                       "ratio_to_CODATA_1.29333": mp.nstr(val/mp.mpf('1.29333'), 6)}}
s = json.dumps(out, indent=1); print(s); open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
