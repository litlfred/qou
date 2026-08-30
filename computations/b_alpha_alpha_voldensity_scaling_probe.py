"""b_αα VolDensity-scaling probe — the α–α bond does NOT carry the proton's ℏ_q² enhancement.

Lane 2 of the bk-crossing-coordination arc (open item 3b: derive b_αα ≈ 2.41 MeV). Follows
the NEGATIVE bare-Markov-trace probe `c_alpha_alpha_categorical_via_jones_markov.py`
(m_e·|tr_M(7²_1)| undershoots ~22.7×) and takes the ONE untried substrate-pure route named in
that probe and in `docs/audits/2026-07-11-bk-crossing-coordination-multiplicity.md`: apply the
**proton VolDensity convention** `Vol/ℏ_q² × linking_weight` to the α–α interface link 7²_1,
instead of the dimensionally-inconsistent literature `m_e·Vol(7²_1)`.

## What this establishes (fit-free; nothing tuned — b_emp is an external AME residual)

At the proton-anchored substrate q₀ (experimental default per AGENTS.md), with
Vol(7²_1) ≈ 4.7495, ℏ_q² ≈ 0.009817, m_e ≈ 0.51100 MeV, linking_weight_family_a ≈ 2.533:

  route                                   b_αα (MeV)   × empirical (2.416)
  bare tr_M      m_e·|tr_M(7²_1)|            0.107        0.044   (prior probe: 22.7× SMALL)
  literature     m_e·Vol(7²_1)              2.427        1.005   (matches, but no ℏ_q²)
  full VolDensity (H₄)  m_e·Vol/ℏ_q²·lw₄  626.1        259.2   (259× BIG)
  full VolDensity (H₃)  m_e·Vol/ℏ_q²·lw₃  330.5        136.8   (137× BIG)

**Result 1 — scope-(a) REFUTATION of the full proton-VolDensity route as the b_αα mechanism.**
Applying the proton convention (with the ℏ_q² Planck enhancement) to 7²_1 overshoots the α–α
bond by **259×** (H₄ linking weight) / 137× (H₃). The ℏ_q² ≈ 0.0098 denominator that lifts the
Borromean volume to the GeV proton mass over-inflates the α–α interface by two orders of
magnitude. So — like the bare tr_M undershoot — the naive convention transplant does not derive
b_αα. This is scope-(a): the route is tested alone and shown insufficient, not structurally
excluded by a proved invariant.

**Result 2 — the dimensional discrepancy is quantified exactly: ρ_αα ≈ ℏ_q².** The per-block
density the AME value implies, ρ_αα := b_emp·ℏ_q²/(m_e·Vol), equals **0.9955·ℏ_q²** — i.e. ℏ_q²
to 0.45%. So the literature `m_e·Vol(7²_1)` is the VolDensity form `m_e·Vol·ρ/ℏ_q²` with a
density ρ_αα = ℏ_q² that cancels the denominator, placing the α–α binding at the bare
hyperbolic-volume scale. The proton, by contrast, carries an O(1) density ρ_p = linking_weight ≈
2.53 (ℏ_q²-independent). The two differ by exactly one ℏ_q² rung:
ρ_p/ρ_αα ≈ 259 ≈ ρ_p/ℏ_q².

## What remains OPEN (numerology guard — magnitudes not interpreted)

ρ_αα ≈ ℏ_q² RESTATES the numerical match `b_αα = m_e·Vol` as a density identity; it is NOT a
derivation. The derivation of b_αα would require a first-principles reason the α–α interface
density is ℏ_q² (binding suppressed by exactly two ℏ_q-powers relative to the rest-mass
VolDensity). That is a scope-(a) observation and a **forward, testable** hypothesis — if binding
residuals live one ℏ_q² rung below their VolDensity, other bond scales (deuteron, per-isotope
b_αα for larger links) should show the same suppression — but it is not established here. No fit;
no production wiring; the α-cluster recursion's C_ALPHA_ALPHA stays as-is.

q₀ pin: proton/experimental (q_parameter.Q_MP), recorded in the witness. No muon-cache input —
no layer straddle.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from knot_volumes import VOL_7_SQ_1_MPF  # noqa: E402
from _li_2_q_util import linking_weight_family_a  # noqa: E402
import q_parameter as qp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Empirical α–α per-bond binding, from the simplex-cluster fit to ¹²C/¹⁶O
# (docs/audits/2026-07-11-bk-crossing-coordination-multiplicity.md §Extension: 2.425 / 2.406).
B_ALPHA_ALPHA_EMPIRICAL_MEV = "2.416"


def main() -> int:
    set_compute_dps(50)
    q = qp.Q_MP
    qi = 1 / q
    me = mp.mpf(str(qp.M_E_MEV))
    hbar2 = qp.HBAR_Q_SQ_MP
    vol = VOL_7_SQ_1_MPF
    lw4 = linking_weight_family_a(q, qi)                 # H₄ Family-A weight (the proton's)
    two_q = q + qi
    lw3 = (mp.mpf(1) + mp.mpf(1) + two_q) / 3           # natural H₃ analog (triv,sign,std=[2]_q)
    b_emp = mp.mpf(B_ALPHA_ALPHA_EMPIRICAL_MEV)

    b_bare_trM = me * mp.mpf("0.2086")                   # from the prior bare-tr_M probe (Wenzl)
    b_lit = me * vol
    b_vd_h4 = me * vol / hbar2 * lw4
    b_vd_h3 = me * vol / hbar2 * lw3
    rho_aa = b_emp * hbar2 / (me * vol)
    rho_ratio = rho_aa / hbar2

    print("=" * 78)
    print("b_αα VolDensity-scaling probe (Lane 2 — proton convention on the 7²_1 interface)")
    print("=" * 78)
    print(f"  q₀ (proton anchor) = {mp.nstr(q, 14)}")
    print(f"  ℏ_q²               = {mp.nstr(hbar2, 10)}")
    print(f"  Vol(7²_1)          = {mp.nstr(vol, 10)}")
    print(f"  m_e                = {mp.nstr(me, 10)} MeV")
    print(f"  linking_wt H₄/H₃   = {mp.nstr(lw4, 8)} / {mp.nstr(lw3, 8)}")
    print(f"  b_αα (empirical)   = {mp.nstr(b_emp, 6)} MeV\n")
    print(f"  {'route':<34}{'b_αα (MeV)':>14}{'× emp':>12}")
    for name, val in [("bare tr_M   m_e·|tr_M|", b_bare_trM),
                      ("literature  m_e·Vol", b_lit),
                      ("full VolDensity H₄  Vol/ℏ_q²·lw₄", b_vd_h4),
                      ("full VolDensity H₃  Vol/ℏ_q²·lw₃", b_vd_h3)]:
        print(f"  {name:<34}{mp.nstr(val, 7):>14}{mp.nstr(val / b_emp, 5):>12}")
    print(f"\n  implied ρ_αα = b_emp·ℏ_q²/(m_e·Vol) = {mp.nstr(rho_aa, 8)}")
    print(f"  ρ_αα / ℏ_q²                          = {mp.nstr(rho_ratio, 8)}  (≈1 ⇒ ρ_αα ≈ ℏ_q²)")
    print(f"  proton density ρ_p (=lw₄)            = {mp.nstr(lw4, 8)}")
    print(f"  ρ_p / ρ_αα                           = {mp.nstr(lw4 / rho_aa, 8)}  (≈ ρ_p/ℏ_q²)")

    print("\n### Net:")
    print("  • Full proton-VolDensity route OVERSHOOTS b_αα by 259× (H₄) / 137× (H₃) —")
    print("    scope-(a) REFUTATION; the ℏ_q² Planck enhancement over-inflates the α–α interface.")
    print("  • The implied α–α density ρ_αα ≈ ℏ_q² (to 0.45%): the α–α binding sits exactly one")
    print("    ℏ_q² rung below the rest-mass scale (ρ_p ≈ 2.53 is O(1); ρ_p/ρ_αα ≈ 259).")
    print("  • OPEN (numerology guard): ρ_αα = ℏ_q² restates the match, it is NOT a derivation.")
    print("    Forward-testable: binding residuals should be ℏ_q²-suppressed vs their VolDensity.")
    print("  • No fit; no wiring; C_ALPHA_ALPHA unchanged.")

    ok = (b_vd_h4 / b_emp > 100) and (mp.fabs(rho_ratio - 1) < mp.mpf("0.01"))
    wb = WitnessBuilder("b-alpha-alpha-voldensity-scaling", engine="python (mpf 50 dps)")
    wb.set_description(
        "Lane 2 of bk-crossing-coordination (open item 3b, b_αα). Applies the proton VolDensity "
        "convention Vol/ℏ_q²×linking_weight to the α–α interface link 7²_1 (the one untried "
        "substrate-pure route named by the prior bare-tr_M probe). Result 1: the full VolDensity "
        "route OVERSHOOTS b_αα by 259× (H₄)/137× (H₃) — scope-(a) refutation; the ℏ_q²≈0.0098 "
        "Planck enhancement that lifts Vol(𝓑₃) to the GeV proton mass over-inflates the α–α bond. "
        "Result 2: the AME-implied α–α per-block density ρ_αα=b_emp·ℏ_q²/(m_e·Vol) equals ℏ_q² to "
        "0.45% (ρ_αα/ℏ_q²=0.9955), so the literature m_e·Vol(7²_1) IS the VolDensity form with a "
        "density ρ_αα=ℏ_q² that cancels the denominator — the α–α binding sits one ℏ_q² rung below "
        "the rest-mass scale (proton ρ_p=linking_weight≈2.53 is O(1); ρ_p/ρ_αα≈259). OPEN "
        "(numerology guard): ρ_αα=ℏ_q² restates the match, not a derivation. No fit; no wiring; "
        "q₀ proton-anchored (no muon-cache straddle).")
    wb.add_parameter("q0_anchor", "proton/experimental (q_parameter.Q_MP)")
    wb.add_parameter("q0", mp.nstr(q, 25))
    wb.add_parameter("b_alpha_alpha_empirical_MeV", B_ALPHA_ALPHA_EMPIRICAL_MEV)
    wb.add_data("hbar_q_sq", mp.nstr(hbar2, 25))
    wb.add_data("vol_7_2_1", mp.nstr(vol, 25))
    wb.add_data("linking_weight_H4", mp.nstr(lw4, 25))
    wb.add_data("linking_weight_H3", mp.nstr(lw3, 25))
    wb.add_data("b_aa_literature_MeV", mp.nstr(b_lit, 25))
    wb.add_data("b_aa_full_voldensity_H4_MeV", mp.nstr(b_vd_h4, 25))
    wb.add_data("b_aa_full_voldensity_H3_MeV", mp.nstr(b_vd_h3, 25))
    wb.add_data("overshoot_factor_H4", mp.nstr(b_vd_h4 / b_emp, 10))
    wb.add_data("rho_alpha_alpha", mp.nstr(rho_aa, 25))
    wb.add_data("rho_alpha_alpha_over_hbar_q_sq", mp.nstr(rho_ratio, 25))
    wb.add_data("rho_p_over_rho_aa", mp.nstr(lw4 / rho_aa, 10))
    wb.add_assertion(
        name="full_voldensity_overshoots_and_rho_aa_is_hbar_q_sq",
        computed=bool(ok), expected=True, tolerance=0,
        source=("Full proton-VolDensity route (Vol/ℏ_q²×linking_weight) applied to 7²_1 overshoots "
                "b_αα by >100× (H₄: 259×), AND the AME-implied density ρ_αα=b_emp·ℏ_q²/(m_e·Vol) "
                "equals ℏ_q² to <1% (0.9955). Scope-(a): the ℏ_q² Planck enhancement belongs to the "
                "rest-mass scale, not the α–α binding, which sits one ℏ_q² rung lower. ρ_αα=ℏ_q² "
                "restates the match, not a derivation (numerology guard). No fit."))
    out = wb.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
