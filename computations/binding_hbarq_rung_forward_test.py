"""Binding vs mass ℏ_q-rung — EXPLORATORY forward test, not wired into production.

Critical-distance re-scope of the b_αα result. The scope marker above is load-bearing,
not decoration: this file compares against the DEPRECATED `Vol(𝓑₃)·ρ` absolute-mass form
(deliberately — that form is its subject), and `canonical_mass_status_guard` reads the
first two docstring lines to decide whether such a comparison is a live status claim.
Verified before asserting it: the only importer is `binding_mass_rung_derivation_probe.py`
(itself a probe), and this module is absent from the no-free-parameter production closure.

Follows Lane 2 (`b_alpha_alpha_voldensity_scaling_probe.py`), which found the AME-implied α–α
density ρ_αα ≈ ℏ_q² and floated "binding residuals are ℏ_q²-suppressed vs their VolDensity" as a
forward-testable rule. This probe RUNS that test across the arc's light isotopes — and the honest
outcome is a **re-scope of my own Lane 2 phrasing** (critical-distance duty, AGENTS.md):

## Test 1 — ρ_implied/ℏ_q² = M_need is DEFINITIONAL (so "ρ ≈ ℏ_q²" ⟺ "M ≈ 1")

Writing the binding in the VolDensity form B = m_e·Vol·ρ/ℏ_q² and solving for the density gives
ρ_implied := B·ℏ_q²/(m_e·Vol), so **ρ_implied/ℏ_q² = B/(m_e·Vol) = M_need identically** — no
content beyond the arc's own multiplicity M_need = B_AME/(m_e·Vol). Across the isotopes:

  iso   B_AME     Vol        M_need = ρ/ℏ_q²
  ³H    8.482    8.2863      2.003
  ³He   7.718    7.3277      2.061
  ⁴He  28.296    7.3277      7.556
  α–α   2.416    4.7495      1.005   (single bond, link 7²_1)

So `ρ_αα ≈ ℏ_q²` is precisely the statement **M_need(single α–α bond) ≈ 1** — NOT a universal
binding law. Multi-bond bindings have M_need = 2.0 (³H, ³He) and 7.6 (⁴He), i.e. ρ = M·ℏ_q² with
M = O(1). **CORRECTION to Lane 2:** "binding residuals are ℏ_q²-suppressed" over-generalised; the
accurate statement is `ρ_binding = M·ℏ_q²`, and only the single α–α bond (M ≈ 1) gives ℏ_q².

## Test 2 — what survives is a genuine two-scale separation (non-circular)

The definitional identity is trivial, but the comparison to the MASS scale is not. At fixed
(m_e·Vol) normalisation:

  mass:     m_p/(m_e·Vol(𝓑₃))   = ρ_p/ℏ_q²  ≈ 258       (ρ_p = linking_weight ≈ 2.53, O(1))
  binding:  B/(m_e·Vol)         = M_need    ≈ 1 … 7.6

So the mass multiplier is O(1/ℏ_q²) while the binding multiplier is O(1) — a **measured two-scale
separation of ~1/ℏ_q²** at fixed volume. Crucially this is a statement about ℏ_q→0 SCALING, not a
magnitude coincidence: the proton density ρ_p = linking_weight_family_a is **finite and O(1) as
ℏ_q→0** (→ 2.5, the classical Wedderburn dimension average), whereas the binding density M·ℏ_q²
**→ 0 as ℏ_q→0**. Rest mass is classical (survives ℏ_q→0); nuclear binding is an O(ℏ_q²) quantum
correction (vanishes classically). That is the defensible, non-circular content — and it is the
real form of the "one rung below" language.

## Test 3 — connection to Lane 1

In the linear-chain regime the multiplicity IS Lane 1's coordination number: M_need(³H)=2.003,
M_need(³He)=2.061 ≈ z = A−1 = 2 (the `coordination_degree` fact). So there
`ρ_binding = z·ℏ_q² = (A−1)·ℏ_q²` — the binding density is the per-nucleon coordination number
times ℏ_q². This ties Lane 2's rung picture to Lane 1's graph fact.

## Open (unchanged, sharpened)

The two-scale separation is *measured*, not *derived*: why the mass multiplier is
`linking_weight/ℏ_q²` (O(1) density, one ℏ_q² enhancement) while the binding multiplier is the
bare coordination count M (no linking_weight, no ℏ_q² enhancement) remains the open question — now
stated as a scaling law rather than a magnitude coincidence. No fit; no wiring; q₀ proton-anchored.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from _li_2_q_util import linking_weight_family_a  # noqa: E402
from knot_volumes import VOL_7_SQ_1_MPF  # noqa: E402
import q_parameter as qp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# AME2020 binding energies (MeV) and the arc's committed 𝓑_K interface volumes
# (docs/audits/2026-07-11-bk-crossing-coordination-multiplicity.md; bk_crossing_coordination.py).
ISO = {
    "3H":  dict(A=3, B="8.481821",  vol="8.286316817806593", link="8_11"),
    "3He": dict(A=3, B="7.718041",  vol="7.327724753417752", link="L6a4"),
    "4He": dict(A=4, B="28.295674", vol="7.327724753417752", link="L6a4-base"),
}
B_ALPHA_ALPHA = "2.416"   # single α–α bond residual (¹²C/¹⁶O simplex fit)


def main() -> int:
    set_compute_dps(50)
    q = qp.Q_MP
    qi = 1 / q
    me = mp.mpf(str(qp.M_E_MEV))
    hbar2 = qp.HBAR_Q_SQ_MP
    lw = linking_weight_family_a(q, qi)              # proton density ρ_p (O(1))
    m_p = mp.mpf(str(qp.M_P_MEV))
    vol_b3 = qp.VOL_BORROMEAN

    print("=" * 78)
    print("Binding vs mass ℏ_q-rung — forward test + critical-distance re-scope")
    print("=" * 78)
    print(f"  q₀(proton)={mp.nstr(q,12)}  ℏ_q²={mp.nstr(hbar2,8)}  m_e={mp.nstr(me,8)} MeV\n")

    print("--- Test 1: ρ_implied/ℏ_q² = M_need (definitional) ---")
    print(f"  {'iso':<5}{'B_AME':>10}{'Vol':>11}{'M_need=ρ/ℏ_q²':>16}{'z=A-1':>7}")
    rows = {}
    for k, d in ISO.items():
        B = mp.mpf(d["B"]); vol = mp.mpf(d["vol"])
        M_need = B / (me * vol)
        rho = M_need * hbar2
        # closed check: rho/hbar2 must equal M_need exactly
        assert mp.fabs(rho / hbar2 - M_need) < mp.mpf("1e-40")
        rows[k] = M_need
        print(f"  {k:<5}{float(B):>10.3f}{float(vol):>11.4f}{float(M_need):>16.3f}{d['A']-1:>7}")
    # single alpha-alpha bond
    B_aa = mp.mpf(B_ALPHA_ALPHA); vol_aa = VOL_7_SQ_1_MPF
    M_aa = B_aa / (me * vol_aa)
    rows["a-a"] = M_aa
    print(f"  {'α–α':<5}{float(B_aa):>10.3f}{float(vol_aa):>11.4f}{float(M_aa):>16.3f}{1:>7}")
    print("  ⇒ ρ/ℏ_q² = M_need identically; ρ_αα≈ℏ_q² is just M(single α–α bond)≈1,")
    print("    NOT a universal law — multi-bond M_need = 2.0 (³H,³He), 7.6 (⁴He).")

    print("\n--- Test 2: mass vs binding two-scale separation (non-circular) ---")
    mass_mult = m_p / (me * vol_b3)          # = ρ_p/ℏ_q² ≈ 258
    print(f"  mass    m_p/(m_e·Vol(𝓑₃))   = {mp.nstr(mass_mult,6)}   (= ρ_p/ℏ_q²; ρ_p=lw={mp.nstr(lw,5)}, O(1))")
    print(f"  binding B/(m_e·Vol) = M_need = {mp.nstr(min(rows.values()),4)} … {mp.nstr(max(rows.values()),4)}   (O(1))")
    print(f"  ⇒ mass multiplier O(1/ℏ_q²)≈{mp.nstr(mass_mult,4)}, binding multiplier O(1): separation ~1/ℏ_q².")
    # classical-limit scaling check: linking_weight is finite & O(1) as ℏ_q→0 (q→1)
    lw_near1 = linking_weight_family_a(mp.mpf("1.000001"), 1 / mp.mpf("1.000001"))
    print(f"  ρ_p(q→1) = {mp.nstr(lw_near1,5)} (finite, O(1) ⇒ mass classical); binding ρ=M·ℏ_q²→0 (quantum).")

    print("\n--- Test 3: linear-chain regime M_need = z = A−1 (Lane 1 tie-in) ---")
    print(f"  M_need(³H)={mp.nstr(rows['3H'],4)}, M_need(³He)={mp.nstr(rows['3He'],4)} ≈ z=2 ⇒ ρ_binding=(A−1)·ℏ_q².")

    print("\n### Net (critical distance on my own Lane 2):")
    print("  • ρ/ℏ_q² = M_need is DEFINITIONAL ⇒ 'binding is ℏ_q²-suppressed' (Lane 2) OVER-CLAIMED;")
    print("    corrected: ρ_binding = M·ℏ_q², only the single α–α bond (M≈1) gives ℏ_q².")
    print("  • Survives (non-circular): mass multiplier O(1/ℏ_q²) vs binding O(1) — a two-scale")
    print("    separation ~1/ℏ_q²; mass is classical (ρ_p O(1) at ℏ_q→0), binding O(ℏ_q²) quantum.")
    print("  • Lane 1 tie: M = z = A−1 in the linear-chain regime ⇒ ρ_binding = (A−1)·ℏ_q².")
    print("  • Lane 2 Result 1 (259× overshoot) stands. No fit; no wiring.")

    multi_bond_not_one = all(rows[k] > mp.mpf("1.5") for k in ("3H", "3He", "4He"))
    aa_is_one = mp.fabs(rows["a-a"] - 1) < mp.mpf("0.05")
    ok = multi_bond_not_one and aa_is_one and (mass_mult > 100)

    wb = WitnessBuilder("binding-hbarq-rung-forward-test", engine="python (mpf 50 dps)")
    wb.set_description(
        "Forward test + critical-distance re-scope of the Lane 2 b_αα result. Test 1: ρ_implied/ℏ_q² "
        "= M_need = B/(m_e·Vol) is a DEFINITIONAL identity, so 'ρ_αα≈ℏ_q²' is just M_need(single α–α "
        "bond)≈1, NOT a universal binding law — multi-bond M_need = 2.00 (³H), 2.06 (³He), 7.56 "
        "(⁴He). Corrects Lane 2's 'binding is ℏ_q²-suppressed' over-claim to ρ_binding = M·ℏ_q². "
        "Test 2 (non-circular survivor): the mass multiplier m_p/(m_e·Vol)=ρ_p/ℏ_q²≈258 is O(1/ℏ_q²) "
        "with ρ_p=linking_weight≈2.53 finite/O(1) as ℏ_q→0 (classical), while the binding multiplier "
        "M_need is O(1) so ρ_binding=M·ℏ_q²→0 (quantum) — a two-scale separation ~1/ℏ_q² that is a "
        "SCALING statement, not a magnitude coincidence. Test 3: M_need=z=A−1 in the linear-chain "
        "regime (Lane 1 tie) ⇒ ρ_binding=(A−1)·ℏ_q². Lane 2 Result 1 (259× overshoot) stands. Open: "
        "why mass carries linking_weight/ℏ_q² and binding the bare coordination count M. No fit; no "
        "wiring; q₀ proton-anchored.")
    wb.add_parameter("q0_anchor", "proton/experimental (q_parameter.Q_MP)")
    for k in ISO:
        wb.add_data(f"M_need_{k}", mp.nstr(rows[k], 12))
    wb.add_data("M_need_alpha_alpha", mp.nstr(rows["a-a"], 12))
    wb.add_data("mass_multiplier_mp_over_meVol", mp.nstr(mass_mult, 12))
    wb.add_data("proton_density_linking_weight", mp.nstr(lw, 12))
    wb.add_data("linking_weight_q_to_1_limit", mp.nstr(lw_near1, 12))
    wb.add_data("hbar_q_sq", mp.nstr(hbar2, 25))
    wb.add_assertion(
        name="rho_over_hbarsq_is_M_need_and_binding_is_M_hbarsq_not_universal_hbarsq",
        computed=bool(ok), expected=True, tolerance=0,
        source=("ρ_implied/ℏ_q² = M_need identically (definitional); multi-bond M_need > 1.5 (³H 2.00, "
                "⁴He 7.56) while single α–α bond M_need ≈ 1 — so ρ_binding = M·ℏ_q², not a universal "
                "ℏ_q² (corrects Lane 2). Non-circular survivor: mass multiplier m_p/(m_e·Vol) > 100 "
                "(O(1/ℏ_q²)) vs binding O(1) — mass classical, binding O(ℏ_q²) quantum. No fit."))
    out = wb.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
