#!/usr/bin/env python3
"""Can the labelled-closure weight q^{c-n} be derived from the Ocneanu/Markov trace?

Pre-registration (this docstring, committed with the first run). Hypothesis: the weight is
1/tau_z(T_{w_C}), the Ocneanu trace of the minimal-length element of sigma's conjugacy class
(Geck-Pfeiffer), which is z^{n-c(sigma)}. Test at the canonical z_D = q^3/(q^2+1) and at the
other admissible point z = q. Prediction (from algebra done before running): z_D gives
6 + 3/q^2 (not constant); z = q gives 6. Also test the full trace tau_z(T_sigma) itself as the
weight. Exact sympy; no measured values.
"""
import json
from pathlib import Path
import sympy as sp

q, z = sp.symbols("q z", positive=True)
h = q - 1 / q
# Ocneanu trace on H_3, T^2 = h T + 1, tau(x T_{n-1}) = z tau(x) for x in H_{n-1}
tau = {"e": sp.Integer(1), "s1": z, "s2": z, "s1s2": z**2, "s2s1": z**2, "s1s2s1": z * (h * z + 1)}
ncomp = {"e": 3, "s1": 2, "s2": 2, "s1s2": 1, "s2s1": 1, "s1s2s1": 2}
wmin = {"e": "e", "s1": "s1", "s2": "s1", "s1s2": "s1s2", "s2s1": "s1s2", "s1s2s1": "s1"}  # min-length rep of class
# labelled diagonal entries on the proton sector (mn_labelled_closure_probe / Lean labelled_count_proton)
lab_p = {"e": 3, "s1": q, "s2": q, "s1s2": 0, "s2s1": 0, "s1s2s1": q}
checks = []
checks.append(("tau(T_{w_C}) = z^{n - c} for every class", all(sp.simplify(tau[wmin[k]] - z**(3 - ncomp[k])) == 0 for k in tau)))
zD = q**3 / (q**2 + 1)
out = {}
for name, zz in (("z_D = q^3/(q^2+1)", zD), ("z = q", q)):
    cls = sp.simplify(sum(lab_p[k] / tau[wmin[k]].subs(z, zz) for k in tau))
    full = sp.simplify(sum(lab_p[k] / tau[k].subs(z, zz) for k in tau))
    out[name] = {"weight 1/tau(T_wC)": str(sp.factor(cls)), "weight 1/tau(T_sigma)": str(sp.factor(full))}
checks.append(("z_D: class weight gives 6 + 3/q^2", sp.simplify(sp.sympify(0) + sum(lab_p[k] / tau[wmin[k]].subs(z, zD) for k in tau) - (6 + 3 / q**2)) == 0))
checks.append(("z = q: class weight gives 6", sp.simplify(sum(lab_p[k] / tau[wmin[k]].subs(z, q) for k in tau) - 6) == 0))
# family z_D^{-(n-c)} q^{k(n-c)}: never constant
fam = {kk: sp.simplify(3 + 3 * q * (q**kk / zD)) for kk in range(-6, 7)}
checks.append(("z_D times any q^{k(n-c)}: never q-independent (k = -6..6)",
               all(sp.diff(v, q).simplify() != 0 for v in fam.values())))
ok = all(c for _, c in checks)
for n, c in checks:
    print(("PASS " if c else "FAIL ") + n)
print(json.dumps(out, indent=1))
Path(__file__).with_suffix(".out.json").write_text(json.dumps(
    {"probe": "mn_closure_weight_ocneanu_probe", "checks": dict(checks), "all_pass": ok, "counts": out,
     "reading": "The weight q^{c-n} is 1/tau_z(T_{w_C}) at z = q; at the canonical z_D the count is 6 + 3/q^2."},
    indent=1) + "\n")
raise SystemExit(0 if ok else 1)
