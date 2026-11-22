"""Symbolic assembly of the n - p matter term under the holonomy connection (section 23).
No test against a target: no pass/fail. Exact sympy; mpmath at the CODATA-2022 muon pin."""
import json, sympy as sp
from mpmath import mp, mpf, mpc, sqrt as msqrt, acos, exp, pi as mpi
mp.dps = 30
q = sp.symbols('q', positive=True); mu = sp.symbols('mu')
h = q - 1/q; br2 = q + 1/q; br3 = q**2 + 1 + q**-2
# rank-one, normalised eigenstate: matter = w*(q^-1 mu + (1-q^-1) xi), xi = +1/2 (p), -1/2 (n)
Mp = q*(mu/q + (1 - 1/q)*sp.Rational(1, 2))
Mn = (1/q)*(mu/q - (1 - 1/q)*sp.Rational(1, 2))
d1 = sp.simplify(Mn - Mp)
check1 = sp.simplify(d1 - ((q**-2 - 1)*mu - (1 - 1/q)*br2/2)) == 0
# block: trace over the 3-dim weight space; sum of mu = -h^4 [3]_q, xi scalar
Smu = -h**4*br3
Bp = q*(Smu/q + (1 - 1/q)*sp.Rational(3, 2))
Bn = (1/q)*(Smu/q - (1 - 1/q)*sp.Rational(3, 2))
d2 = sp.factor(sp.simplify(Bn - Bp))
check2 = sp.simplify(d2 - ((q**-2 - 1)*Smu - 3*(1 - 1/q)*br2/2)) == 0
q0 = mpf('1.1099785956427390466817951294')
c1 = (q0**12 - 3*q0**10 + 3*q0**8 - 4*q0**6 + 3*q0**4 - 3*q0**2 + 1)/q0**6
th = acos(-c1/2); muc = mpc(-c1/2, msqrt(1 - (c1/2)**2)) - 1
hv = q0 - 1/q0; b2 = q0 + 1/q0; b3 = q0**2 + 1 + q0**-2
r1 = (q0**-2 - 1)*muc - (1 - 1/q0)*b2/2
r2 = (q0**-2 - 1)*(-hv**4*b3) - 3*(1 - 1/q0)*b2/2
res = {"rank_one_n_minus_p": "(q^-2 - 1) mu - (1 - q^-1)[2]_q/2", "rank_one_check": bool(check1),
       "block_n_minus_p": str(d2), "block_form": "(q^-2 - 1)(-h^4[3]_q) - 3(1 - q^-1)[2]_q/2",
       "block_check": bool(check2),
       "pin": {"own_sector_part_complex": mp.nstr((q0**-2 - 1)*muc, 20),
               "isospin_part_rank_one": mp.nstr(-(1 - 1/q0)*b2/2, 20),
               "rank_one_total_complex": mp.nstr(r1, 20),
               "block_own_sector_part": mp.nstr((q0**-2 - 1)*(-hv**4*b3), 20),
               "block_total": mp.nstr(r2, 20),
               "ratio_own_sector_to_isospin_block": mp.nstr(((q0**-2 - 1)*(-hv**4*b3))/(-3*(1 - 1/q0)*b2/2), 20)},
       "q_to_1": {"mu_order": "h^2 (|mu|^2 = h^4 [3]_q)", "own_sector_part_order": "h^3",
                  "isospin_part_order": "h"}}
out = json.dumps(res, indent=2); print(out)
open(__file__.replace('.py', '.out.json'), 'w').write(out + "\n")
