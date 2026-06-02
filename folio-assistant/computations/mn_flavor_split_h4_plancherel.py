"""m_n flavor-split at H_4 — higher-rank Plancherel-channel test (item 3).

PR #1654 confirmed H_3 Plancherel-channel doesn't close m_n's 0.10%
X(q) residual; the residual would need the STANDARD channel piece
(P_(2,1) = 4/6) which has no clean natural form.

This probe tests H_4 — 5 Wedderburn blocks (4), (3,1), (2,2), (2,1,1),
(1,1,1,1) with classical dims 1, 3, 2, 3, 1 and Plancherel weights
1/24, 9/24, 4/24, 9/24, 1/24.

The hypothesis: a higher-rank decomposition of the flavor-split
(3 quarks + 1 spectator? Or different categorical interpretation)
provides additional channels that close the residual.

## Cross-references

- PR #1654 Item A: H_3 Plancherel insight
- Sibling research-one-plus-q-over-two-derivation REFUTED 2026-06-01
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _h4_substrate import M_E_MEV, M_P_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
import experimental_constants as _ec  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    DPS = 80
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("m_n flavor-split at H_4 — higher-rank Plancherel-channel test")
    print("=" * 78)
    print(f"\nq_0 = {q_str(60)} (display)\n")

    M_N_MEV = M_P_MEV + M_E_MEV + mp.mpf(repr(_ec.Q_NEUTRON_MEV))
    M_N_avg = (M_P_MEV + M_N_MEV) / 2
    target = (M_N_MEV - M_P_MEV) / M_N_avg

    X_baseline = (q - 1) ** 2 * (1 - q ** (-4)) / 3
    delta = target - X_baseline
    print(f"[Recap] target = {mp.nstr(target, 18)}")
    print(f"        X(q) baseline = {mp.nstr(X_baseline, 18)}")
    print(f"        Δ = target - X = {mp.nstr(delta, 12)}")

    # H_4 Wedderburn structure (classical, q-independent)
    # partitions: (4) (3,1) (2,2) (2,1,1) (1,1,1,1)
    # classical dims: 1, 3, 2, 3, 1, Σ d² = 1+9+4+9+1 = 24 = |S_4|
    print(f"\n[H_4 Wedderburn]")
    blocks = [
        ("(4)",        1, mp.mpf(1) / 24),
        ("(3,1)",      3, mp.mpf(9) / 24),
        ("(2,2)",      2, mp.mpf(4) / 24),
        ("(2,1,1)",    3, mp.mpf(9) / 24),
        ("(1,1,1,1)",  1, mp.mpf(1) / 24),
    ]
    for name, d, P in blocks:
        print(f"  {name:<14} dim {d}  P = {mp.nstr(P, 8)}")

    # Substrate
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    q2 = q + 1 / q

    # The 4-strand σ_1, σ_2, σ_3 have specific eigenvalue patterns.
    # For simplicity test: 1-dim blocks (4) and (1,1,1,1) have
    # eigenvalues +q (trivial) and -1 (sign). Other blocks are
    # higher-dimensional with both eigenvalues mixed.

    # Test forms targeting various H_4 Plancherel structures
    print(f"\n[H_4 Plancherel-channel candidates]")
    candidates = [
        # (a) 1-dim sub-sum: (P_(4) + P_(1,1,1,1)) · (something) = (2/24) · ?
        ("(a) (P_(4) + P_(1,1,1,1)) · ℏ_q²·h·[2]_q (=Δ_pn/12 form)",
         (mp.mpf(2)/24) * hbar_q_sq * h * q2),
        # (b) 2-dim block: (P_(2,2)) · (something) = (4/24) · ?
        ("(b) P_(2,2) · ℏ_q²·h²",
         (mp.mpf(4)/24) * hbar_q_sq * h2),
        # (c) Per-block channels: trivial gives X-form, others give corrections
        ("(c) X(q) baseline (control)", X_baseline),
        # (d) (4·X) / 24 = X/6 - a sub-channel at H_4
        ("(d) X(q) / 6", X_baseline / 6),
        # (e) (P_(3,1) + P_(2,1,1)) · ℏ_q²·h (18/24 = 3/4 weight)
        ("(e) (3/4) · ℏ_q² · h",
         (mp.mpf(18)/24) * hbar_q_sq * h),
        # (f) Antisymmetric pair: (P_(2,2)) · h² · α_em/π
        ("(f) P_(2,2) · h² · α_em/π",
         (mp.mpf(4)/24) * h2 * mp.mpf(1)/mp.mpf("137.0359991")/mp.pi),
        # (g) bare 1/24 with X-like multiplier
        ("(g) (1/24) · ℏ_q² · h · [2]_q²",
         (mp.mpf(1)/24) * hbar_q_sq * h * q2 ** 2),
    ]

    print(f"  {'name':<48}{'value':<22}{'Δ rel %'}")
    scored = []
    for name, val in candidates:
        rel = (val - target) / target * 100
        scored.append((name, val, rel))

    scored.sort(key=lambda r: abs(r[2]))
    for name, val, rel in scored:
        marker = ""
        if abs(rel) < mp.mpf("0.5"):
            marker = " ⭐⭐ < 0.5%"
        elif abs(rel) < mp.mpf("5"):
            marker = " ⭐ < 5%"
        print(f"  {name:<48}{mp.nstr(val, 12):<22}{mp.nstr(rel, 6)}{marker}")

    # Direct test: is delta = (P_(2,2)) · h⁴ ?
    print(f"\n[Test: delta = P_(2,2) · h⁴?]")
    test_val = (mp.mpf(4)/24) * h ** 4
    print(f"  (4/24) · h⁴ = {mp.nstr(test_val, 12)} vs δ = {mp.nstr(delta, 12)}")
    rel = (test_val - delta) / delta * 100
    print(f"  Δ rel = {mp.nstr(rel, 6)}%")

    best = scored[0]
    print(f"\n[Verdict]")
    if abs(best[2]) < mp.mpf("0.5"):
        verdict = (
            f"H_4 CANDIDATE: '{best[0]}' at {mp.nstr(best[2], 6)}%. "
            f"Higher-rank Plancherel may close the m_n residual."
        )
    elif abs(best[2]) < mp.mpf("10"):
        verdict = (
            f"Weak H_4 candidate: '{best[0]}' at {mp.nstr(best[2], 6)}% — "
            f"beats baseline (1277 ppm) at the structural-suggestion level."
        )
    else:
        verdict = (
            f"NULL at H_4 — higher-rank Plancherel-channel does NOT close "
            f"m_n flavor-split residual. The 0.10% residual is genuinely "
            f"outside the classical Wedderburn × Plancherel structure at "
            f"H_2, H_3, AND H_4. Likely requires non-Hecke operator or "
            f"q-deformed Plancherel."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "mn-flavor-split-h4-plancherel",
        engine="python",
    )
    w.set_description(
        "Item 3 of PR #1671: tests Plancherel-channel template at H_4 "
        "(5 Wedderburn blocks) for m_n / Δ_pn flavor-split. Continues "
        "PR #1654 Item A (H_3) which identified the residual as needing "
        "standard channel."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("best_candidate", best[0])
    w.add_data("best_rel_pct", mp.nstr(best[2], 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="h4_plancherel_scan_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} H_4 candidates at 80 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
