#!/usr/bin/env python3
"""Search for a q-independent own-sector quantum trace on the proton weight space.

Pre-registered (this docstring, committed before the run): under the own-sector premise
(NeutronSectorQTraceConstant.lean) the proton constant is kappa * T_p(w), T_p(w) = q tr_{W_p}(w).
The -12 audit requires the proton constant to be q-independent. Question: is there a signed
word w in sigma_1^{+-1}, sigma_2^{+-1} (length <= 6) with q*tr_{W_p}(w) independent of q, so that
kappa would be a pure number? Prediction: none, except possibly words whose W_p trace is
c/q by accident; if one exists its value is reported, not selected. Exact sympy over Q(q).
"""
import itertools, json, sys
from pathlib import Path
import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
# Jimbo matrices on W_p = (uud, udu, duu), as in NucleonWeightSpaceTraces (A1, A2)
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
gens = {"s1": A1, "s2": A2, "S1": A1 - h * sp.eye(3), "S2": A2 - h * sp.eye(3)}
assert sp.simplify(A1 * gens["S1"] - sp.eye(3)) == sp.zeros(3)
assert sp.simplify(A2 * gens["S2"] - sp.eye(3)) == sp.zeros(3)
hits, n = [], 0
for L in range(0, 7):
    for w in itertools.product(gens, repeat=L):
        if any(a[1] == b[1] and a[0] != b[0] for a, b in zip(w, w[1:])):
            continue  # skip s1 S1 cancellations
        M = sp.eye(3)
        for g in w:
            M = M * gens[g]
        val = sp.simplify(q * M.trace())
        n += 1
        if sp.diff(val, q).simplify() == 0:
            hits.append((" ".join(w) or "1", str(val)))
print("words tested:", n)
print("q-independent own-sector quantum traces:", hits)
Path(__file__).with_suffix(".out.json").write_text(json.dumps({"words_tested": n, "hits": hits}, indent=1) + "\n")
