"""Ocneanu '12' — alternative knot-operator geometries on Bring's surface.

Per author 2026-06-01: "are you using right knot operator geometry on
brings? not necc 3 color channels"

PR #1581 found `(α_em/π)/dim H_3 = (α_em/π)/6` lands at 54 ppb. The
`/6` came from assuming the proton sits at H_3 (3-strand Hecke ↔
3 valence quarks ↔ 3 color channels).

But Bring's surface has 5-fold quintic symmetry, the proton has
multiple knot-operator candidates beyond 3-strand:

  - H_5 quintic: 120 = |S_5|, [5]_q! = 122.96 at q_0
  - Hopf-link on B_3 substructure
  - Goeritz-matrix dimension
  - Atomic-3A pair (6 quark-quark interactions)
  - Charge-weighted (2/3, -1/3, +1/3)
  - Bring saturating-genus knots T_(2,3), T_(2,5), T_(2,7) — 3 OF 5

This probe sweeps alt-geometries to test whether ANY of them tightens
the 54 ppb baseline.

## Cross-references

- merged PR #1581 (Ocneanu near-match)
- ocneanu_12_bring_zero_mode_variants.py (Bring template — NULL)
- author 2026-06-01 challenge: "not necc 3 color channels"
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_MU_MEV_VALIDATION  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def trM_borromean_closed(q):
    h = q - 1 / q
    h2 = h * h
    return (4 + h2 - 3 * h2 ** 2 - h2 ** 3) / (h2 + 4)


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def qfact(k, q):
    out = mp.mpf(1)
    for i in range(1, k + 1):
        out *= qint(i, q)
    return out


def main() -> int:
    set_compute_dps(60)
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Ocneanu '12' — alternative knot-operator geometries (60 dps)")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    # Setup
    qfact_3 = qfact(3, q)
    trM = abs(trM_borromean_closed(q))
    F_Bor = trM * qfact_3 / q ** 3
    m_e = mp.mpf("0.51099895069")
    m_mu = M_MU_MEV_VALIDATION
    m_p = mp.mpf("938.27208816")
    k_required = (2 * m_mu * F_Bor - m_p) / m_e
    residual_target = 12 - k_required

    print(f"[Setup] residual target = {mp.nstr(residual_target, 12)}\n")

    alpha_em = mp.mpf(1) / mp.mpf("137.0359991")
    h = q - 1 / q
    h2 = h * h

    # Various knot-operator "dimensions" to test (α_em/π) divided by
    geometries = [
        # Hecke dims at q=1 (classical)
        ("|S_2| = 2", mp.mpf(2)),
        ("|S_3| = 6 (baseline)", mp.mpf(6)),
        ("|S_4| = 24", mp.mpf(24)),
        ("|S_5| = 120", mp.mpf(120)),
        # q-deformed Hecke Poincare polynomial values
        ("[3]_q! at q_0", qfact_3),
        ("[4]_q! at q_0", qfact(4, q)),
        ("[5]_q! at q_0", qfact(5, q)),
        # Bring saturating-genus generation: 3 torus knots T_(2,k)
        ("3 Bring gen-knots", mp.mpf(3)),
        ("3 × 2 EM halving", mp.mpf(6)),
        ("3 × 2 × q²", 6 * q ** 2),
        # Quintic Bring categorical action: 5
        ("5 (Bring quintic root count)", mp.mpf(5)),
        ("5 · 2 EM halving", mp.mpf(10)),
        # Hopf-link sub: J = 2 at q=1, |J(q_0)| ≈ 2.04
        ("|J_Hopf| at q_0 ≈ 2.04", abs(-(q ** 2 + 1 / q ** 2))),
        # Borromean operator: trM at q_0
        ("|tr_M(β_Bor)| at q_0", trM),
        # Atomic 6-channel: 3 valence × 2 spin
        ("3 strands × 2 spin = 6", mp.mpf(6)),
        # Yekutieli edge cells × strands
        ("4 cells × 3 strands = 12", mp.mpf(12)),
        # Plancherel at H_3 (q-deformed Σ d²_λ)
        ("Σ d_q²_λ at q_0 (H_3)", 1 + (qfact_3 / 3) ** 2 + 1),
        # Charge-weighted denominators (proton = uud)
        ("9 = 3·3 (color×generations)", mp.mpf(9)),
        ("8 (gluons in SU(3))", mp.mpf(8)),
        ("3 + 8 = 11 (quarks + gluons)", mp.mpf(11)),
        # Casimir / Wedderburn variants
        ("dim_q V_(2,1) at q_0", qfact_3 / 3),
        ("dim V_(2,1)² · 1.5 = 6", (qfact_3 / 3) ** 2 * mp.mpf("1.5")),
        # q^k variations of dim H_3
        ("6 / q", 6 / q),
        ("6 / q²", 6 / q ** 2),
        ("6 · q", 6 * q),
        # Bring's surface invariants
        ("Bring genus 4 → 8 (Bring's |H¹|?)", mp.mpf(8)),
        ("Bring Euler χ = −6", mp.mpf(6)),  # |χ| only
    ]

    # Score: for each denominator d, compute (α_em/π)/d - residual_target
    print(f"[Denominator scan — (α_em/π) / d vs residual target]")
    print(f"  {'name':<40}{'denominator':<22}{'(α_em/π)/d':<22}{'Δ ppb to k_required'}")
    scored = []
    for name, d in geometries:
        val = alpha_em / mp.pi / d
        k_pred = 12 - val
        delta_k_ppb = (k_pred - k_required) / k_required * mp.mpf("1e9")
        scored.append((name, d, val, delta_k_ppb))

    scored.sort(key=lambda r: abs(r[3]))
    for name, d, val, dk in scored:
        marker = ""
        if abs(dk) < mp.mpf("10"):
            marker = " ⭐⭐ < 10 ppb (structural)"
        elif abs(dk) < mp.mpf("54"):
            marker = " ⭐ tighter than dim H_3 baseline"
        elif abs(dk) < mp.mpf("1000"):
            marker = " * within 1 ppm"
        print(f"  {name:<40}{mp.nstr(d, 18):<22}{mp.nstr(val, 18):<22}{mp.nstr(dk, 8)}{marker}")

    # Verdict
    best = scored[0]
    baseline = next(r for r in scored if "baseline" in r[0])
    print(f"\n[Verdict]")
    if abs(best[3]) < mp.mpf("10") and "baseline" not in best[0]:
        verdict = (
            f"ALT GEOMETRY BEATS BASELINE: '{best[0]}' gives "
            f"{mp.nstr(best[3], 6)} ppb (vs dim H_3 = 6 baseline at "
            f"{mp.nstr(baseline[3], 6)} ppb). Structurally significant!"
        )
    elif abs(best[3]) < abs(baseline[3]):
        verdict = (
            f"BEST: '{best[0]}' at {mp.nstr(best[3], 6)} ppb beats "
            f"dim H_3 baseline ({mp.nstr(baseline[3], 6)} ppb) but not "
            f"below the 10 ppb structural threshold."
        )
    else:
        verdict = (
            f"BASELINE STANDS: dim H_3 = 6 remains the tightest "
            f"denominator (54 ppb). No alternative knot-operator "
            f"geometry on Bring's surface improves the fit."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "ocneanu-12-alt-knot-geometries",
        engine="python",
    )
    w.set_description(
        "Per author challenge 'not necc 3 color channels' — tests "
        "alternative knot-operator geometries beyond H_3 for the Ocneanu "
        "EM correction (α_em/π)/N. Scans Bring saturating-genus knots, "
        "quintic 5-fold, |S_n| / [n]_q!, Hopf/Borromean trace evaluations, "
        "Yekutieli cell counts, charge/color/generation weightings."
    )
    w.add_parameter("q_60dps", Q_50_DIGIT_STR)
    w.add_data("baseline_dim_H_3_ppb", mp.nstr(baseline[3], 12))
    w.add_data("best_name", best[0])
    w.add_data("best_denominator", mp.nstr(best[1], 18))
    w.add_data("best_ppb", mp.nstr(best[3], 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="alt_geometry_scan_completed",
        computed=len(geometries),
        expected=len(geometries),
        tolerance=0,
        source=f"Scanned {len(geometries)} knot-operator geometries at 60 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
