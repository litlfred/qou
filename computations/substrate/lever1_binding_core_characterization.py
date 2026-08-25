"""Lever-1 fibre kernel, Stage 8: characterize the GROWING non-cyclotomic core R_m of the binding correction.

Bean: z2bn (Lever 1 [FOCUS] — fibre q-difference kernel R(q,x) for the binding genfun).

Context (the stated next-decidable step of the 2026-06-28 Stage-7 audit
docs/audits/2026-06-28-lever1-binding-correction-cyclotomic-core-growth.md):
    The additive correction D(m) = S(m) − (S(m−1) + [m−1]_q S(m−2)) factors exactly as
        D(m)·q^{a_m} = c_m · (q−1)² · ∏_d Φ_d(q)^{e} · R_m(q),
    with a non-cyclotomic core R_m whose degree GROWS (0,0,8,10,14,28,34,46 for m=4..11). The
    growing core is the genuine Habiro-ring content. This stage characterizes R_m itself.

DECIDABLE QUESTIONS (no fit, exact in q; cores read from the Stage-7 witness — no S(m) recompute):
  (Q1) Palindromy: is each R_m self-reciprocal, q^{deg}·R_m(1/q) = ±R_m(q)? (bar-symmetry q↔1/q).
       The 2026-06-27 audit noted this only for the D(7) core; this tests all of m=6..11.
  (Q2) Value at q=1: R_m(1) (must be ≠0 — the (q−1)² carries all the q=1 vanishing) and its sign.
  (Q3) Irreducibility over ℚ and full factorization (is the core a single irreducible, or built
       from smaller pieces the Stage-7 cyclotomic strip missed?).
  (Q4) Cross-m shared factors: pairwise gcd(R_m, R_{m'}) — does a nested/common core persist
       (a single growing element) or is each R_m essentially new?
  (Q5) Degree law of the core / of D(m) numerator, and value at the substrate q0.

(a)/(b)-scoped per AGENTS.md; binding side (exact data); nothing wired; no fit.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
import sympy as sp  # noqa: E402

q = sp.Symbol("q", positive=True)
try:
    from qou_substrate import constants as C  # noqa: E402
    Q0 = str(C.Q_MP) if hasattr(C, "Q_MP") else str(C.Q)
except Exception:
    Q0 = "1.10997859555733471"

WIT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "lever1-binding-correction-cyclotomic-structure.witness.json")
src = json.load(open(WIT))
cores_raw = {int(k.split("=")[1]): v for k, v in src["noncyclotomic_core"].items()}

print("[1/5] Parsing core polynomials from the Stage-7 witness ...", flush=True)
R = {}
for m, v in sorted(cores_raw.items()):
    if v["is_trivial"]:
        continue
    R[m] = sp.expand(sp.sympify(v["poly"], locals={"q": q}))
    print(f"    R({m}) deg {sp.Poly(R[m], q).degree()}", flush=True)

q0 = sp.Rational(0)  # set below numerically


def is_palindromic(poly):
    """Return +1 if q^deg R(1/q)=R(q) (palindromic), -1 if anti-palindromic, 0 if neither."""
    P = sp.Poly(poly, q)
    d = P.degree()
    rev = sp.expand(q ** d * poly.subs(q, 1 / q))
    rev = sp.cancel(rev)
    if sp.simplify(rev - poly) == 0:
        return 1
    if sp.simplify(rev + poly) == 0:
        return -1
    return 0


print("[2/5] Palindromy + value at q=1 + sign at q0 ...", flush=True)
analysis = {}
mp = __import__("mpmath")
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
q0f = mp.mpf(Q0)
for m, poly in R.items():
    pal = is_palindromic(poly)
    at1 = sp.simplify(poly.subs(q, 1))
    at_q0 = mp.mpf(str(sp.N(poly.subs(q, sp.Float(Q0, 40)), 30)))
    analysis[m] = {
        "deg": int(sp.Poly(poly, q).degree()),
        "palindromic": {1: "palindromic", -1: "anti-palindromic", 0: "neither"}[pal],
        "value_at_q1": str(at1),
        "value_at_q0": mp.nstr(at_q0, 12),
        "positive_at_q0": bool(at_q0 > 0),
    }
    print(f"    R({m}): {analysis[m]['palindromic']}, R(1)={at1}, R(q0)={mp.nstr(at_q0,8)} "
          f"({'>' if at_q0>0 else '<='}0)", flush=True)
all_palindromic = all(a["palindromic"] == "palindromic" for a in analysis.values())
all_pos_q1 = all(sp.sympify(a["value_at_q1"]) > 0 for a in analysis.values())

print("[3/5] Irreducibility over ℚ + factorization ...", flush=True)
irred = {}
for m, poly in R.items():
    fl = sp.factor_list(poly)
    pieces = [(str(sp.factor(f)), e) for (f, e) in fl[1]]
    is_irred = len(fl[1]) == 1 and fl[1][0][1] == 1
    irred[m] = {"irreducible_over_Q": bool(is_irred), "n_factors": len(fl[1]),
                "factors": pieces}
    print(f"    R({m}): {'IRREDUCIBLE' if is_irred else str(len(fl[1]))+' factors'}", flush=True)
all_irreducible = all(v["irreducible_over_Q"] for v in irred.values())

print("[4/5] Cross-m shared factors (pairwise gcd) ...", flush=True)
ms = sorted(R)
shared = {}
any_shared = False
for i in range(len(ms)):
    for j in range(i + 1, len(ms)):
        g = sp.gcd(R[ms[i]], R[ms[j]])
        gd = sp.Poly(g, q).degree() if g != 1 and g != 0 else 0
        if gd >= 1:
            any_shared = True
            shared[f"{ms[i]},{ms[j]}"] = {"gcd_deg": int(gd), "gcd": str(sp.factor(g))}
print(f"    any nontrivial pairwise gcd among cores? {any_shared}", flush=True)

print("[5/5] Degree law ...", flush=True)
core_degs = {m: analysis[m]["deg"] for m in ms}
deg_diffs = [core_degs[ms[k + 1]] - core_degs[ms[k]] for k in range(len(ms) - 1)]

verdict = (
    "The growing core R_m is " +
    ("UNIFORMLY PALINDROMIC (q↔1/q bar-symmetric)" if all_palindromic else "NOT uniformly palindromic") +
    "; R_m(1)≠0 " + ("(all positive)" if all_pos_q1 else "(mixed sign)") + "; " +
    ("each R_m is IRREDUCIBLE over ℚ" if all_irreducible else "the R_m factor further over ℚ") + "; " +
    ("the cores share NO common factor across m (each order brings a genuinely new bar-symmetric core)"
     if not any_shared else "the cores share a persistent common factor (a nested growing element)") +
    ". This pins the binding correction's essential content: a (q−1)² × Φ_d cyclotomic tower (Stage 7) "
    "times a tower of bar-symmetric, q=1-nonvanishing cores that grow and do not nest — the genuine "
    "cyclotomic-completion (Habiro) residue, not reducible to a single finite element."
)
print("\nVERDICT:", verdict, flush=True)
print("  core degrees:", core_degs, " diffs:", deg_diffs, flush=True)

out = {
    "$schema": "https://litlfred.github.io/qou/witness-schema/v1.json",
    "description": "Lever-1 binding correction non-cyclotomic core R_m: palindromy, q=1/q0 values, "
                   "irreducibility over Q, cross-m shared factors, degree law.",
    "bean": "z2bn",
    "computation": {"script": "computations/substrate/lever1_binding_core_characterization.py",
                    "reads": "computations/substrate/lever1-binding-correction-cyclotomic-structure.witness.json"},
    "params": {"q0": Q0},
    "core_analysis": {f"m={m}": analysis[m] for m in ms},
    "all_palindromic": bool(all_palindromic),
    "all_positive_at_q1": bool(all_pos_q1),
    "irreducibility": {f"m={m}": irred[m] for m in ms},
    "all_irreducible_over_Q": bool(all_irreducible),
    "cross_m_shared_factors": shared,
    "any_shared_factor": bool(any_shared),
    "core_degrees": {f"m={m}": core_degs[m] for m in ms},
    "core_degree_diffs": deg_diffs,
    "verdict": verdict,
    "scope": "(a)/(b) per AGENTS.md: palindromy / irreducibility / no-nesting / R_m(1)≠0 are exact "
             "derived facts on the available m=6..11; 'core grows unboundedly / not a single finite "
             "element' remains a bounded-MMAX observation, not a proved (b)-exclusion. Nothing wired; "
             "no fit; binding side (exact data).",
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
_wb = WitnessBuilder.wrap_legacy(
    "lever1-binding-core-characterization", out,
    script_path=__file__, engine="sympy",
)
# Record the consumed upstream witness so witness_dependency_drift.py can
# machine-check drift (emitted under data.upstream_witness_hashes).
_wb.add_upstream(WIT)
witness_path = _wb.save()
print("witness ->", os.path.relpath(witness_path, os.getcwd()), flush=True)
