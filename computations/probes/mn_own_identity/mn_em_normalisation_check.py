"""Pre-registered PREREGISTRATION-em-normalisation.md: exact check that the strand-charge reading
(degreeZero_values, k1 = 0, k2 = alpha) and the weight-block reading give the same insertion;
E_n - E_p = -(alpha/3) M_QCD with M_QCD = m_p + 12 m_e from the canonical facade. mpmath 60 dps."""
import json, itertools, sympy as sp, mpmath as mp, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from qou_substrate import constants as C
import canonical_mass as CM
mp.mp.dps = 60
Qu, Qd = sp.Rational(2, 3), sp.Rational(-1, 3)
pair = lambda t: sum(t[i]*t[j] for i in range(3) for j in range(i+1, 3))
k1, k2 = sp.symbols('k1 k2')
deg0 = lambda t: k1*sum(x**2 for x in t) + k2*pair(t)
strand = {"p": sp.simplify(deg0((Qu, Qu, Qd))), "n": sp.simplify(deg0((Qu, Qd, Qd)))}
# weight-block reading: bit 0 = u; QPair on each basis state, grouped by number of 0-bits
blocks = {}
for b in itertools.product([0, 1], repeat=3):
    blocks.setdefault(b.count(0), set()).add(pair(tuple(Qu if x == 0 else Qd for x in b)))
q = mp.mpf(C.Q_50_DIGIT_STR)
qi = lambda n: (q**n - q**-n)/(q - 1/q)
alpha = (1/q)/(qi(9)*qi(10))
me = mp.mpf(C.M_E_MEV_STR)
mp_mev = mp.mpf(str(CM.proton_mass_mev()))
M_QCD = mp_mev + 12*me
E = -(alpha/3)*M_QCD
out = {"preregistration": "PREREGISTRATION-em-normalisation.md",
  "strand_charge_reading": {k: str(v) for k, v in strand.items()},
  "strand_reading_with_k1=0,k2=alpha": {k: str(v.subs({k1: 0, k2: sp.Symbol('alpha')})) for k, v in strand.items()},
  "weight_block_QPair_values": {f"W{w}": sorted(str(x) for x in s) for w, s in sorted(blocks.items())},
  "P1_same_insertion": bool(blocks[2] == {strand["p"].subs({k1: 0, k2: 1})} and blocks[1] == {strand["n"].subs({k1: 0, k2: 1})}),
  "alpha_q0": mp.nstr(alpha, 25), "canonical_m_p_MeV": mp.nstr(mp_mev, 20),
  "M_QCD_MeV": mp.nstr(M_QCD, 20), "E_n_minus_E_p_MeV": mp.nstr(E, 20),
  "alpha_at_q=1": "1/90", "E_over_M_QCD_at_q=1": "-1/270"}
s_ = json.dumps(out, indent=1); print(s_); open(__file__.replace('.py', '.out.json'), 'w').write(s_ + "\n")
