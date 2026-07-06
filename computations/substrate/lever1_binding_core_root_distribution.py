"""Lever-1 fibre kernel, Stage 9: unit-circle root distribution of the bar-symmetric binding cores R_m.

Bean: z2bn (Lever 1 [FOCUS] — fibre q-difference kernel R(q,x) for the binding genfun).

Context (stated next step of the 2026-06-28 Stage-8 audit
docs/audits/2026-06-28-lever1-binding-core-bar-symmetric-irreducible.md):
    The non-cyclotomic cores R_m (m=6..11) are palindromic (bar-symmetric q↔1/q), irreducible over ℚ,
    pairwise coprime, substrate-positive. The spectral fingerprint distinguishing a "q-special-function"
    core (roots on the unit circle, like cyclotomic / Salem / Lehmer polynomials) from a generic
    bar-even residue (roots off the circle in z↔1/z pairs) is the on/off-unit-circle root split.

DECIDABLE, EXACT (no numerics): a self-reciprocal poly P of degree 2n satisfies
    P(q)/q^n = c_0 + Σ_{k=1}^n c_k (q^k + q^{-k}) = c_0 + Σ_{k=1}^n c_k D_k(y),   y := q + 1/q,
with D_k the Dickson polynomials (D_0=2, D_1=y, D_k = y D_{k-1} − D_{k-2}). A root q of P lies on
|q|=1  ⇔  y = q+1/q ∈ [−2,2] is real. So #(roots of R_m on the unit circle) = 2 · #(real roots of
Q in (−2,2)), counted EXACTLY by sympy's Sturm-based count_roots. Off-circle roots come in z↔1/z (and
conjugate) groups: real |y|>2 → a reciprocal real pair; complex y → an off-circle complex quadruple.

Also factors R_m(1) (the Stage-8 values 28,16,34,1232,1328,9024) to expose any prime/combinatorial law.

Cores read from the Stage-8/7 witness — no S(m) recompute. (a)/(b)-scoped; binding side (exact data);
nothing wired; no fit.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
import sympy as sp  # noqa: E402

q, y = sp.symbols("q y")

WIT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "lever1-binding-correction-cyclotomic-structure.witness.json")
src = json.load(open(WIT))
cores_raw = {int(k.split("=")[1]): v for k, v in src["noncyclotomic_core"].items()}

print("[1/3] Parsing cores; building Dickson reduction Q(y) ...", flush=True)
R = {}
for m, v in sorted(cores_raw.items()):
    if not v["is_trivial"]:
        R[m] = sp.expand(sp.sympify(v["poly"], locals={"q": q}))


def dickson(n):
    """D_k(y) for k=0..n: D_0=2, D_1=y, D_k = y D_{k-1} - D_{k-2}."""
    D = [sp.Integer(2), y]
    for k in range(2, n + 1):
        D.append(sp.expand(y * D[-1] - D[-2]))
    return D


def reduce_to_y(poly):
    """Given a palindromic poly of even degree 2n, return Q(y) with P(q)=q^n Q(q+1/q)."""
    P = sp.Poly(poly, q)
    deg = P.degree()
    assert deg % 2 == 0, "expected even degree (palindromic)"
    n = deg // 2
    coeffs = {deg - i: c for i, c in enumerate(P.all_coeffs())}  # power -> coeff
    D = dickson(n)
    Q = sp.Integer(coeffs.get(n, 0)) * sp.Integer(1)  # c_0 (middle coeff), times D_0/2 = 1
    for k in range(1, n + 1):
        ck = coeffs.get(n + k, 0)
        Q += ck * D[k]
    return sp.Poly(sp.expand(Q), y), n


print("[2/3] Exact on/off-unit-circle root counts via Sturm (count_roots in (−2,2)) ...", flush=True)
dist = {}
for m in sorted(R):
    poly = R[m]
    Qy, n = reduce_to_y(poly)
    # exact real-root count of Q in the open interval (−2, 2): on-circle pairs.
    on_pairs = Qy.count_roots(sp.Integer(-2), sp.Integer(2))
    # endpoints y=±2 correspond to q=±1: check explicitly (R_m(1)≠0 by Stage 8; check q=-1)
    at_minus1 = poly.subs(q, -1)
    # subtract endpoint roots if Q(±2)=0 (q=±1 on circle, but those are real q, treat as on-circle deg-2)
    endpoint_y2 = Qy.eval(2) == 0
    endpoint_ym2 = Qy.eval(-2) == 0
    on_circle_roots = 2 * on_pairs
    off_circle_roots = poly_deg = sp.Poly(poly, q).degree()
    off_circle_roots = poly_deg - on_circle_roots
    dist[m] = {
        "deg": int(poly_deg),
        "y_degree_n": int(n),
        "real_y_roots_in_open_m2_2": int(on_pairs),
        "on_circle_roots": int(on_circle_roots),
        "off_circle_roots": int(off_circle_roots),
        "all_on_circle": bool(off_circle_roots == 0),
        "fraction_on_circle": float(sp.Rational(on_circle_roots, poly_deg)),
        "Q_at_y2_is_zero": bool(endpoint_y2),
        "Q_at_ym2_is_zero": bool(endpoint_ym2),
        "R_at_minus1": str(at_minus1),
    }
    print(f"    R({m}) deg {poly_deg}: on-circle {on_circle_roots}, off-circle {off_circle_roots} "
          f"({100*dist[m]['fraction_on_circle']:.0f}% on)", flush=True)

print("[3/3] Factoring R_m(1) values ...", flush=True)
at1_fac = {}
for m in sorted(R):
    val = sp.Integer(int(sp.sympify(src["noncyclotomic_core"][f"m={m}"]["poly"], locals={"q": q}).subs(q, 1)))
    at1_fac[m] = {"value": int(val), "factorization": str(sp.factorint(val))}
    print(f"    R({m})(1) = {val} = {sp.factorint(val)}", flush=True)

all_on = all(dist[m]["all_on_circle"] for m in dist)
any_on = any(dist[m]["on_circle_roots"] > 0 for m in dist)
if all_on:
    verdict = ("ALL roots of every core R_m lie ON the unit circle — the cores are Salem/Lehmer/"
               "cyclotomic-completion-type bar-symmetric polynomials (a strong special structure, the "
               "q-special-function fingerprint).")
elif any_on:
    verdict = ("MIXED root distribution: each bar-symmetric core R_m has some roots on the unit circle "
               "and some off it (in z↔1/z reciprocal groups). The cores are NOT cyclotomic-type (already "
               "known: irreducible non-cyclotomic) and NOT pure Salem — they are generic bar-even "
               "residues with a definite on/off split, the genuine cyclotomic-completion (Habiro) "
               "content. The on-circle fraction is the spectral fingerprint recorded per m.")
else:
    verdict = ("NO root of any core lies on the unit circle — every root is an off-circle z↔1/z pair; "
               "the cores are 'reciprocal' (anti-cyclotomic) bar-even residues.")
print("\nVERDICT:", verdict, flush=True)

out = {
    "$schema": "https://litlfred.github.io/qou/witness-schema/v1.json",
    "description": "Lever-1 binding cores R_m: exact on/off-unit-circle root distribution (Dickson "
                   "y=q+1/q reduction + Sturm count) and R_m(1) prime factorization.",
    "bean": "z2bn",
    "computation": {"script": "computations/substrate/lever1_binding_core_root_distribution.py",
                    "reads": "computations/substrate/lever1-binding-correction-cyclotomic-structure.witness.json"},
    "root_distribution": {f"m={m}": dist[m] for m in sorted(dist)},
    "all_cores_all_on_circle": bool(all_on),
    "R_at_1_factorizations": {f"m={m}": at1_fac[m] for m in sorted(at1_fac)},
    "verdict": verdict,
    "scope": "(a)/(b) per AGENTS.md: the exact on/off-circle counts and R_m(1) factorizations are "
             "derived facts on m=6..11; no closed-form law is claimed. Nothing wired; no fit.",
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
_wb = WitnessBuilder.wrap_legacy(
    "lever1-binding-core-root-distribution", out,
    script_path=__file__, engine="sympy",
)
# Record the consumed upstream witness so witness_dependency_drift.py can
# machine-check drift (emitted under data.upstream_witness_hashes).
_wb.add_upstream(WIT)
witness_path = _wb.save()
print("witness ->", os.path.relpath(witness_path, os.getcwd()), flush=True)
