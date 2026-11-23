"""⁴He γγ chain under the conventions that can flip its sign (issue #8960).

Exact Fractions at the proton pin, z_D = q³/(q²+1). Reuses the exact Ocneanu
trace of ../he4_closed_form/hecke_exact.py.

Conventions varied, all others fixed:
  chirality: ruled vertex σ_iσ_{i+1}⁻¹ (owner photon ruling) vs its ι image σ_i⁻¹σ_{i+1}
  side:      bond overlaps the next nucleon's first generator (left entry, the
             production placement) vs the previous nucleon's last generator (right entry)
  labels:    ppnn vs nnpp
Also checks that the trace is invariant under strand reflection σ_i ↦ σ_{n-2-i}.
The chain trace uses the proved chain law (towerTr_ggChain) and its mirror image;
one two-nucleon case is checked against the full word.
"""
import json, os, sys
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "he4_closed_form"))
from hecke_exact import Ring  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
import mpmath as mp  # display only

mp.mp.dps = 40
R = Ring(Fraction(Q_50_DIGIT_STR))
S, I = R.S, R.I
E0_MEV = Fraction("4.22748335562903")  # as recorded in he4-gg-all-pairs.witness.json


def sh(L, k):
    return [(a, b, i + k) for a, b, i in L]


def refl(L, n):
    return [(a, b, n - 2 - i) for a, b, i in L]


N = {"p": R.proton(), "n": R.neutron()}
t = {k: R.tr(3, v) for k, v in N.items()}
V = {"ruled": lambda k: [S(k), I(k + 1)] * 3, "iota": lambda k: [I(k), S(k + 1)] * 3}

checks = {}
bL = {c: {k: R.tr(4, V[c](0) + sh(v, 1)) for k, v in N.items()} for c in V}
bR = {c: {k: R.tr(4, v + V[c](1)) for k, v in N.items()} for c in V}
checks["reflection_invariance"] = all(
    R.tr(4, refl(V[c](0) + sh(v, 1), 4)) == bL[c][k] for c in V for k, v in N.items())
full = R.tr(6, N["p"] + V["ruled"](1) + sh(N["n"], 3))
checks["right_entry_chain_law_2nucleon"] = full == bR["ruled"]["p"] * t["n"]

rows = []
for c in V:
    for side in ("left", "right"):
        for order in ("ppnn", "nnpp"):
            seq = list(order)
            free = Fraction(1)
            for x in seq:
                free *= t[x]
            if side == "left":
                atom = t[seq[0]]
                for x in seq[1:]:
                    atom *= bL[c][x]
            else:
                atom = t[seq[-1]]
                for x in seq[:-1]:
                    atom *= bR[c][x]
            B = E0_MEV * 1000 * (free - atom)
            rows.append({"chirality": c, "side": side, "order": order,
                         "B_chain_keV": mp.nstr(mp.mpf(B.numerator) / B.denominator, 12)})
mu = {f"{c}_{s}_{k}": mp.nstr(mp.mpf((d[k] / t[k] - 1).numerator) / (d[k] / t[k] - 1).denominator, 12)
      for c in V for s, d in (("left", bL[c]), ("right", bR[c])) for k in N}
for r in rows:
    print(r)
print(checks)
assert all(checks.values())
out = {"q0Anchor": "proton", "q0AnchorReason": "exact Fractions at the proton 50-digit pin",
       "issue": 8960, "mu_minus_1": mu, "rows": rows, "checks": checks,
       "note": "Production placement is ruled chirality, left entry: B = -0.862 keV."}
json.dump(out, open(os.path.join(HERE, "he4-sign-conventions.witness.json"), "w"), indent=1)
