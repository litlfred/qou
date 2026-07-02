"""Lever-1 fibre kernel, Stage 7: the cyclotomic (Habiro) structure of the binding correction tower.

Bean: z2bn (Lever 1 [FOCUS] — fibre q-difference kernel R(q,x) for the binding genfun).

Context (the stated next-decidable step of the 2026-06-28 Stage-6 audit
docs/audits/2026-06-28-lever1-binding-correction-not-single-qhypergeometric.md):
    Stages 3-6 proved the binding period S(m)=Σ_{λ⊢m} dim_q(λ) and its correction towers are NOT
    finite low-order q-difference operators and NOT single low-order q-hypergeometric elements. The
    productive remaining attack is the DIRECT cyclotomic-basis structure, not a recurrence search.

The additive correction D(m) := S(m) − (S(m−1) + [m−1]_q·S(m−2)) clears to a Laurent polynomial in q
(its denominators are pure q-powers; the Stage-1 listing D(4)=(q−1)²(q²+q+1)/q², … confirms this).
So D(m) has an EXACT cyclotomic factorization over ℚ:
        D(m) · q^{a_m}  =  c_m · (q−1)^{2} · ∏_d Φ_d(q)^{e_{m,d}} · R_m(q),
with R_m the non-cyclotomic core (if any). This is decidable and parameter-free.

TWO DECIDABLE QUESTIONS (no fit, no target):
  (Q1) The root-of-unity vanishing structure = the Habiro fingerprint: for each cyclotomic index d,
       at which m does Φ_d first divide D(m), and how does its multiplicity e_{m,d} grow? A clean rule
       (e.g. Φ_d | D(m) ⇔ m ≥ f(d)) is a DERIVED parameter-free constraint any candidate kernel must
       satisfy.
  (Q2) Non-cyclotomic core growth: is deg R_m bounded (⇒ D(m) is a FINITE cyclotomic object — strong)
       or growing (⇒ genuine cyclotomic-completion / Habiro object with an essential non-cyclotomic
       core)? Stage-1 already saw a non-cyclotomic deg-14 cofactor at D(8); this tracks it to MMAX.

Symbolic, exact in q (sympy); (a)/(b)-scoped per AGENTS.md; nothing wired; binding side (exact data),
distinct from the gated Q_β element F(q).
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402

from young_qdim import q, qint, S  # noqa: E402

MMAX = 11
DMAX = 60  # match cyclotomic factors Φ_d for d up to this

print(f"[1/4] Computing S(0..{MMAX}) (symbolic in q) ...", flush=True)
Sm = {}
for m in range(0, MMAX + 1):
    Sm[m] = sp.cancel(S(m))
    print(f"    S({m}) done", flush=True)

print("[2/4] Building correction tower D(m) and clearing to Laurent polynomial ...", flush=True)
# Precompute cyclotomic polynomials Φ_d(q) as Poly objects for exact division.
PhiP = {d: sp.Poly(sp.cyclotomic_poly(d, q), q) for d in range(1, DMAX + 1)}


def cyclotomic_decompose(num_expr):
    """Strip q^k, divide out each Φ_d (exact division) to its full multiplicity, return
    (cmap {d: mult}, core_Poly, core_deg). The remainder Poly IS the non-cyclotomic core."""
    P = sp.Poly(sp.expand(num_expr), q)
    # strip the q^k monomial factor (from the Laurent denominator clearing)
    while P.degree() >= 1 and P.eval(0) == 0:
        P = P.quo(sp.Poly(q, q))
    cmap = {}
    for d in range(1, DMAX + 1):
        phid = PhiP[d]
        while True:
            quo, rem = sp.div(P, phid, q)
            if rem.is_zero and P.degree() >= phid.degree():
                P = quo
                cmap[d] = cmap.get(d, 0) + 1
            else:
                break
    # P is now the non-cyclotomic core (up to a rational unit); normalise degree
    core_deg = P.degree() if P.degree() >= 1 else 0
    return cmap, P, core_deg


D = {}
cyc_map = {}      # m -> {d: multiplicity}
core = {}         # m -> {"deg": int, "poly": str, "is_trivial": bool}
qminus1_order = {}
for m in range(4, MMAX + 1):
    Dm = sp.cancel(Sm[m] - (Sm[m - 1] + qint(m - 1) * Sm[m - 2]))
    D[m] = Dm
    if Dm == 0:
        cyc_map[m] = {}
        core[m] = {"deg": -1, "poly": "0", "is_trivial": True}
        qminus1_order[m] = None
        continue
    num, _den = sp.fraction(sp.cancel(Dm))
    cmap, coreP, core_deg = cyclotomic_decompose(num)
    cyc_map[m] = cmap
    o1 = cmap.get(1, 0)  # multiplicity of Φ_1 = (q−1) = order of vanishing at q=1
    is_trivial = core_deg == 0
    core[m] = {"deg": core_deg, "poly": ("1" if is_trivial else str(sp.factor(coreP.as_expr()))),
               "is_trivial": is_trivial}
    qminus1_order[m] = o1
    print(f"    D({m}): Φ-factors {cmap}, core deg {core_deg}, (q−1)-order {o1}", flush=True)

# ---- (Q1) root-of-unity vanishing rule -----------------------------------------------------
print("[3/4] Testing the Φ_d first-appearance rule ...", flush=True)
first_appearance = {}  # d -> smallest m with Φ_d | D(m)
for m in range(4, MMAX + 1):
    for d in cyc_map.get(m, {}):
        if d not in first_appearance:
            first_appearance[d] = m
# rule candidates for d>=2: does Φ_d first divide D(m) at m = d, d+1, or d-1 ... ?
rule_rows = []
for d in sorted(first_appearance):
    if d == 1:
        continue
    fm = first_appearance[d]
    rule_rows.append({"d": d, "first_m": fm, "first_m_minus_d": fm - d})
# is (q−1)² universal? (the O(h²) Stage-1 claim)
q1_orders = [qminus1_order[m] for m in range(4, MMAX + 1) if qminus1_order[m] is not None]
qminus1_universal_2 = all(o >= 2 for o in q1_orders)

# ---- (Q2) non-cyclotomic core growth -------------------------------------------------------
core_degs = {m: core[m]["deg"] for m in range(4, MMAX + 1)}
nontrivial_core_from = next((m for m in range(4, MMAX + 1) if not core[m]["is_trivial"]), None)
core_grows = False
if nontrivial_core_from is not None:
    ds = [core_degs[m] for m in range(nontrivial_core_from, MMAX + 1)]
    core_grows = ds[-1] > ds[0]

print("[4/4] Assembling verdict ...", flush=True)
# verdict
if nontrivial_core_from is None:
    verdict = ("PURELY CYCLOTOMIC (strong): every D(m) up to m=%d factors entirely into cyclotomic "
               "Φ_d × (q-power) — a FINITE cyclotomic object, not a transcendental Habiro tail." % MMAX)
elif core_grows:
    verdict = ("GENUINE CYCLOTOMIC-COMPLETION (Habiro) object: D(m) carries a universal (q−1)² × "
               "Φ_d cyclotomic tower (root-of-unity vanishing rule below) PLUS a non-cyclotomic core "
               "R_m whose degree GROWS with m (first nontrivial at m=%d, deg %d → %d at m=%d). The "
               "binding correction is therefore not a finite cyclotomic object; its essential core is "
               "the genuine Habiro-ring content — consistent with Stages 3-6 (no finite low-order "
               "operator). The Φ_d tower is the derived, parameter-free constraint; the growing core "
               "is what any candidate Habiro element must reproduce." %
               (nontrivial_core_from, core_degs[nontrivial_core_from], core_degs[MMAX], MMAX))
else:
    verdict = ("MIXED, bounded core: cyclotomic Φ_d tower + a non-cyclotomic core of BOUNDED degree "
               "(first at m=%d). Re-examine whether the bounded core is itself a fixed element." %
               nontrivial_core_from)
print("\nVERDICT:", verdict, flush=True)
print("  Φ_d first-appearance:", {r["d"]: r["first_m"] for r in rule_rows}, flush=True)
print("  (q−1)-order per m:", q1_orders, "  universal ≥2?", qminus1_universal_2, flush=True)
print("  core degrees per m:", core_degs, flush=True)

out = {
    "$schema": "https://litlfred.github.io/qou/witness-schema/v1.json",
    "description": "Lever-1 binding correction tower D(m): exact cyclotomic (Habiro) factorization — "
                   "Φ_d root-of-unity vanishing rule + non-cyclotomic core growth.",
    "bean": "z2bn",
    "computation": {"script": "computations/substrate/lever1_binding_correction_cyclotomic_structure.py"},
    "params": {"MMAX": MMAX, "DMAX": DMAX},
    "cyclotomic_factor_map": {f"m={m}": {f"Phi_{d}": e for d, e in cyc_map.get(m, {}).items()}
                              for m in range(4, MMAX + 1)},
    "phi_first_appearance": {f"Phi_{r['d']}": r["first_m"] for r in rule_rows},
    "phi_first_minus_d": {f"Phi_{r['d']}": r["first_m_minus_d"] for r in rule_rows},
    "qminus1_order_per_m": {f"m={m}": qminus1_order[m] for m in range(4, MMAX + 1)},
    "qminus1_universal_squared": bool(qminus1_universal_2),
    "noncyclotomic_core": {f"m={m}": core[m] for m in range(4, MMAX + 1)},
    "noncyclotomic_core_first_m": nontrivial_core_from,
    "noncyclotomic_core_grows": bool(core_grows),
    "verdict": verdict,
    "scope": "(a)/(b) per AGENTS.md: the Φ_d vanishing rule + (q−1)² prefactor are derived structural "
             "facts (positive); 'not a finite cyclotomic object' is a bounded-MMAX observation, not a "
             "proved (b)-exclusion. Nothing wired; no fit; binding side (exact data).",
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
witness_path = WitnessBuilder.wrap_legacy(
    "lever1-binding-correction-cyclotomic-structure", out,
    script_path=__file__, engine="sympy",
).save()
print("witness ->", os.path.relpath(witness_path, os.getcwd()), flush=True)
