"""Direction 2 Step 1 — empirical baseline for k_{ud} (flavor-displacement exponent).

EXPLORATORY / AUDIT-ONLY: this probe establishes the EMPIRICAL value of
the flavor-displacement exponent `k_{ud}` in the Bring color-tube
weight refinement, scanning small-integer candidates and reporting
which gives the closest match to PDG. **This is NOT a derivation** —
it surfaces the data-side baseline that Direction 2 Step 2 must
explain categorically.

Per the workplan `docs/workplans/2026-05-30-mass-asymmetric-flavor-
split.md` §Direction 2:

  Production X(q) is flavor-blind. The conjectured refinement is:

    1/(1 − h_q · q^{10}) at the substrate base (flavor-blind)
       ──►
    9-pair weighted average over (u,u), (u,d), (d,u), (d,d) with
    each pair carrying its own `k_{quark1,quark2}`:

      w(quark₁, quark₂, q) = 1/(1 − h_q · q^{10 + k_{quark1,quark2}})

  Symmetry constraints from bar-invariance + flavor identity:
    k_{uu} = k_{dd} = 0  (same-type, no flavor cost — reference scale)
    k_{ud} = k_{du}      (bar-symmetry under q ↔ q⁻¹ + flavor swap)

  One free parameter: k_{ud}.

This probe scans k_{ud} ∈ {-3, -2, -1, 0, 1, 2, 3} and reports for
each:
  - the resulting weighted average value
  - the implied m_d/m_u prediction
  - the gap vs PDG 2.16(7)

The k_{ud} value with the smallest residual is the "empirical baseline"
— call it k_{ud}^empirical. Step 2 then has to find a categorical
invariant equal to that value (e.g. a Hecke partition weight ratio,
Catalan / Lobachevsky integral, etc.) WITHOUT fitting.

If no small-integer k_{ud} closes the residual, fractional values
(probably linked to Hecke partition weights like y_{(1,1)}/y_{(2)})
should be tried instead.

References:
- prop:pn-averaging-uniqueness (PR #1445) — ColorFlavorCompatible class
- lambda_scale_refinement_h4_correction_bring.py — current production
  flavor-blind form
- prop:proton-mass-substrate-identity — the m_p anchor identity
- docs/workplans/2026-05-30-mass-asymmetric-flavor-split.md
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path
import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


# PDG 2024 quark mass ratio (light-quark mass-ratio average from
# lattice + chiral perturbation theory). Used only as comparison
# target — NEVER as a fit input.
M_D_OVER_M_U_PDG = mpf("2.16")
M_D_OVER_M_U_PDG_ERR = mpf("0.07")

# Bring genus-class base exponent (current production flavor-blind).
BRING_BASE_EXPONENT = 10


def bring_color_tube_weight(q: mpf, k: int) -> mpf:
    """1/(1 − h_q · q^{base + k}) — Bring color-tube weight at
    exponent shift k from the flavor-blind base.

    k = 0 reproduces the production flavor-blind form
    `1/(1 − h_q · q^{10})`.
    """
    h_q = (q - 1) / q
    exp = BRING_BASE_EXPONENT + k
    return 1 / (1 - h_q * q ** exp)


def nine_pair_weighted_average(q: mpf, k_ud: int) -> mpf:
    """The 9-pair weighted average across the p-n boundary slice:
       2·(u,u) + 4·(u,d) + 1·(d,u) + 2·(d,d) — from p=uud × n=udd.

    With symmetry k_{uu} = k_{dd} = 0 and k_{ud} = k_{du} = k_ud:
      avg = (1/9) · [ 2·w_0 + 4·w_{k_ud} + 1·w_{k_ud} + 2·w_0 ]
          = (1/9) · [ 4·w_0 + 5·w_{k_ud} ]
    """
    w0 = bring_color_tube_weight(q, 0)
    wk = bring_color_tube_weight(q, k_ud)
    return (4 * w0 + 5 * wk) / 9


def implied_md_mu_ratio(q: mpf, k_ud: int) -> mpf:
    """Implied m_d/m_u from the asymmetric weighted average.

    Structural form: m_d / m_u = w_d / w_u = w(d,d) / w(u,u) at the
    quark-only level — but since k_{uu} = k_{dd} = 0 this is unity
    on the diagonal. The off-diagonal asymmetry surfaces in the
    mixed (u,d) terms, so the effective m_d/m_u is read from the
    ratio of (u→d) flip vs (d→u) flip channels — under bar-symmetry
    this collapses to the structural relation

      m_d / m_u = (1 − h_q · q^{10}) / (1 − h_q · q^{10 + k_ud})

    The numerator is the bare (u-anchored) weight inverse; the
    denominator is the (u-to-d transit) weight inverse. This is the
    structural ansatz Direction 2 Step 3 will refine; for the
    empirical baseline we use it as-is.
    """
    h_q = (q - 1) / q
    num = 1 - h_q * q ** BRING_BASE_EXPONENT
    den = 1 - h_q * q ** (BRING_BASE_EXPONENT + k_ud)
    return num / den


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    q = mpf(Q_50_DIGIT_STR)

    print("=" * 76)
    print("  Direction 2 Step 1 — empirical baseline k_{ud} scan")
    print("=" * 76)
    print()
    print(f"  q_0                              = {mp.nstr(q, 20)}")
    print(f"  Bring base exponent (flavor-blind) = {BRING_BASE_EXPONENT}")
    print(f"  PDG m_d/m_u target               = "
          f"{float(M_D_OVER_M_U_PDG):.3f} ± {float(M_D_OVER_M_U_PDG_ERR):.3f}")
    print()
    print(f"  {'k_ud':>5}  {'avg_weight':>14}  "
          f"{'implied_m_d/m_u':>16}  {'PDG_residual_pct':>18}")
    print(f"  {'-'*5}  {'-'*14}  {'-'*16}  {'-'*18}")

    results = []
    best_k = None
    best_residual_abs = None
    for k in range(-3, 4):
        avg = nine_pair_weighted_average(q, k)
        md_mu = implied_md_mu_ratio(q, k)
        residual_pct = float((md_mu - M_D_OVER_M_U_PDG) / M_D_OVER_M_U_PDG * 100)
        results.append({
            "k": k,
            "avg_weight": mp.nstr(avg, 15),
            "implied_md_mu": mp.nstr(md_mu, 10),
            "pdg_residual_pct": residual_pct,
        })
        print(f"  {k:>+5d}  {float(avg):>14.10f}  "
              f"{float(md_mu):>16.6f}  {residual_pct:>+18.3f}%")
        if best_residual_abs is None or abs(residual_pct) < best_residual_abs:
            best_residual_abs = abs(residual_pct)
            best_k = k

    # Recover signed residual for the best k to keep the witness
    # schema consistent with per-row `pdg_residual_pct` convention
    # (Copilot review: don't store absolute value under a field
    # name that implies signed).
    best_pdg_residual_signed = next(
        r["pdg_residual_pct"] for r in results if r["k"] == best_k
    )
    print()
    print(f"  Best integer k_ud = {best_k} "
          f"(PDG residual {best_pdg_residual_signed:+.3f}%)")
    print()
    print("  Step 1 interpretation:")
    print("  - This is the EMPIRICAL baseline; no categorical derivation yet.")
    print("  - If the best k is a small integer with simple structural")
    print("    significance (±2, ±3 for second/third Bring-class shift), it")
    print("    suggests the categorical invariant in Step 2 is a partition")
    print("    weight ratio at small n.")
    print("  - If the best k is large or none close, fractional k values")
    print("    linked to y_{(1,1)}/y_{(2)} Wenzl weights are next.")
    print()
    print("  Direction 2 Step 2 task: find a categorical invariant whose")
    print(f"  value at q_0 equals the empirical k_ud above ({best_k}) —")
    print("  without fitting.")
    print()

    w = WitnessBuilder("probe-k-ud-bring-color-tube-empirical-baseline",
                       engine="mpmath", start_time=_t0)
    w.set_description(
        "EXPLORATORY probe: empirical baseline for the flavor-"
        "displacement exponent k_ud in the Bring color-tube weight "
        f"refinement. Scans k_ud ∈ {{-3..3}} and reports implied "
        f"m_d/m_u vs PDG 2.16(7). Best k_ud = {best_k}. NOT a "
        "categorical derivation — this is the data-side baseline "
        "that Direction 2 Step 2 must explain. Audit-only."
    )
    w.set_audit_only(
        "docs/workplans/2026-05-30-mass-asymmetric-flavor-split.md"
    )
    w.add_data("q_0", mp.nstr(q, 50))
    w.add_data("bring_base_exponent", BRING_BASE_EXPONENT)
    w.add_data("pdg_md_mu_target", str(M_D_OVER_M_U_PDG))
    w.add_data("pdg_md_mu_err", str(M_D_OVER_M_U_PDG_ERR))
    w.add_data("scan_results", results)
    w.add_data("best_integer_k_ud", best_k)
    # Signed value matches per-row schema (Copilot review fix).
    w.add_data("best_pdg_residual_pct", best_pdg_residual_signed)
    w.add_data("best_pdg_residual_pct_abs", best_residual_abs)
    w.add_assertion(
        "scan_produced_results",
        computed=len(results), expected=7, tolerance=0,
        source="k ∈ {-3, -2, -1, 0, 1, 2, 3} all evaluated"
    )
    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
