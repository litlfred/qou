#!/usr/bin/env python3
"""qbeta_silver_pole_subdominant_probe.py — the silver/Q_A pole of
F = Q_β/[Q_A·cos α_eff] is GENUINE but SUBDOMINANT (corrects PR #2445).

Context (residue-A kernel / 1ppQ Q_β keystone):
`QOU.QBeta.RationalCoeffRecurrence` grounds "find the kernel R ≡ find the
minimal denominator Q"; the poles of `F` are the reciprocals of the
characteristic roots of the `c_k` C-finite recurrence. PR #2445
(`QOU.QBeta.SilverAnchorGrounding`) proved the substrate-branch `Q_A`
numerator `2q+1−q²` vanishes on the silver locus `q = 1+√2`, and CLAIMED
this is "the F-pole fixing the DOMINANT `1/u_substrate ≈ 117.4`
characteristic root". This probe checks that claim and finds it is
**half wrong**:

  1. The pole is GENUINE. The true Q_β = |Δ(net)|·E₀ uses the GB-reduced
     trefoil coefficient Δ(net)(q), NOT the cheat-sheet leading term
     (≈ Q_A). Δ(net)(silver) = 82216 + 58136·√2 ≠ 0 (exact, via the
     canonical free-neutron-decay producer), while Q_A(silver) = 0 — so
     F = |Δ(net)|·E₀/[Q_A·cos α_eff] genuinely blows up at silver.
     (An earlier check that used the cheat-sheet closed-form Q_β ≈ Q_A
     was CIRCULAR: it gave F = 1/cos, trivially regular — do not repeat.)

  2. But the silver pole is SUBDOMINANT, not the dominant root. In the
     substrate variable u = b·ℏ_q², the silver pole sits at
     u_silver = u(1+√2) ≈ 0.321, giving characteristic root
     1/u_silver ≈ 3.12 — far from the established dominant tail ratio
     1/u_substrate ≈ 117.4 (u_substrate = u(q₀) ≈ 0.00852,
     conj:q-beta-radius-of-convergence-gate / PR #1727). Since
     u_substrate < u_silver, the dominant (nearest-to-0) pole is at
     u_substrate and comes from a NON-Q_A source; the Q_A/silver zero
     contributes only the subdominant root 3.12.

Net: pins ONE subdominant root of the kernel's minimal denominator Q
(the silver/Q_A one, now categorically grounded), and prunes the search
for the dominant root (it is NOT the Q_A zero). Corrects the dominance
claim in PR #2445.

NO FLOAT: exact sympy for the algebra, mpmath (50 dps) for the numeric
roots. Exploratory; no fit; promotes nothing.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401,E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This held the RETIRED
# self-certified pin A as a literal -- retired 2026-08-22 for the CODATA-2022
# derivation, so the value was stale AND could not follow the anchor.
#
# MIGRATED TO PROTON on the owner ruling of 2026-08-30: proton is the default,
# and the burden is on the exception. Neither exception applies here -- this
# probe makes no explicit proton-vs-muon comparison (E1), and it is not about
# the CAL-1/2/3 triple as mathematics (E2). "It has always been muon" is
# expressly not a reason. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR`
# resolves to the proton pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

q = sp.Symbol("q", positive=True)
SILVER = 1 + sp.sqrt(2)  # silver ratio, root of q²−2q−1


def _delta_net_numerator() -> sp.Expr:
    """Δ(net)(q) numerator from the canonical free-neutron-decay witness
    (sum of GB-reduced neutron NF coeffs − proton NF coeffs)."""
    import json
    d = json.loads((HERE.parent / "free-neutron-decay.witness.json").read_text())

    def net_sym(part: str) -> sp.Expr:
        tot = sp.Integer(0)
        for t in d[part]["nf_terms"]:
            # bind to the module-level symbol (positive=True) so later subs works
            tot += sp.sympify(str(t["coefficient_symbolic"]), locals={"q": q})
        return sp.simplify(tot)

    dn = sp.simplify(net_sym("neutron") - net_sym("proton"))
    return sp.numer(sp.together(dn))


def main() -> int:
    set_compute_dps()

    # --- exact algebra (sympy) ---
    qA_num = 2 * q + 1 - q**2                      # substrate-branch Q_A numerator
    qA_at_silver = sp.radsimp(sp.expand(qA_num.subs(q, SILVER)))
    dnum = sp.expand(_delta_net_numerator())       # explicit polynomial in q
    dnum_at_silver = sp.radsimp(sp.expand(dnum.subs(q, SILVER)))
    # divisibility is the reliable test (subs+simplify can leave radicals unreduced)
    _, rem = sp.div(sp.Poly(dnum, q), sp.Poly(q**2 - 2 * q - 1, q))
    silver_divides_delta = rem.as_expr() == 0

    pole_genuine = (qA_at_silver == 0) and (not silver_divides_delta)

    # --- numeric roots (mpmath, NO FLOAT) ---
    q0 = Q_MP
    qs = 1 + mp.sqrt(2)

    def hbar(x): return (x - 1) / x

    def b(x): return mp.sqrt(x**4 + x**2 + 1) / (x**2 + 1)

    def u(x): return b(x) * hbar(x) ** 2

    u_sub, u_silver = u(q0), u(qs)
    root_sub, root_silver = 1 / u_sub, 1 / u_silver
    subdominant = u_silver > u_sub          # farther from 0 ⇒ subdominant

    print(f"\n  Q_A numerator (2q+1−q²) at silver      = {qA_at_silver}  (=0 ⇒ Q_A zero)")
    print(f"  Δ(net) numerator at silver             = {dnum_at_silver}")
    print(f"  (q²−2q−1) | Δ(net)?                     = {silver_divides_delta}")
    print(f"  ⇒ F-pole at silver GENUINE?            = {pole_genuine}\n")
    print(f"  u_substrate = u(q₀)     = {mp.nstr(u_sub,10)}   char root 1/u = {mp.nstr(root_sub,8)}  (dominant, PR #1727)")
    print(f"  u_silver    = u(1+√2)   = {mp.nstr(u_silver,10)}   char root 1/u = {mp.nstr(root_silver,8)}  (silver/Q_A)")
    print(f"  ⇒ silver pole SUBDOMINANT (u_silver > u_substrate)? = {subdominant}")
    print(f"\n  VERDICT: silver/Q_A pole is {'GENUINE but SUBDOMINANT' if pole_genuine and subdominant else 'NOT as described'} — "
          f"char root {mp.nstr(root_silver,6)} ≠ dominant {mp.nstr(root_sub,6)}. "
          f"#2445 dominance claim corrected.")

    w = (WitnessBuilder("qbeta-silver-pole-subdominant", engine="sympy+mpmath")
         .set_content_block("prop:qbeta-silver-anchor-grounding")
         .set_description(
             "Corrects PR #2445's dominance claim: the silver/Q_A zero IS a "
             "genuine pole of F=Q_β/[Q_A·cos α_eff] (Δ(net)(silver)=82216+"
             "58136√2≠0 while Q_A(silver)=0; the true Q_β uses GB-reduced "
             "Δ(net), not the cheat-sheet leading term≈Q_A — that check was "
             "circular). But it is SUBDOMINANT: u_silver≈0.321 → char root "
             "≈3.12, not the dominant 1/u_substrate≈117.4 (PR #1727). The "
             "dominant pole is from a non-Q_A source. NO FLOAT. Exploratory."))
    w.add_data("qA_numerator_at_silver", str(qA_at_silver))
    w.add_data("delta_net_numerator_at_silver", str(dnum_at_silver))
    w.add_data("silver_factor_divides_delta_net", bool(silver_divides_delta))
    w.add_data("u_substrate", str(u_sub))
    w.add_data("u_silver", str(u_silver))
    w.add_data("char_root_dominant_1_over_u_substrate", str(root_sub))
    w.add_data("char_root_silver_1_over_u_silver", str(root_silver))
    w.add_assertion(
        "silver_pole_genuine_and_subdominant",
        computed=1.0 if (pole_genuine and subdominant) else 0.0,
        expected=1.0, tolerance=0.0,
        source="Q_A(silver)=0 ∧ Δ(net)(silver)≠0 (genuine pole); "
               "u_silver>u_substrate (subdominant char root 3.12 vs 117.4)")
    print(f"\n  witness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
