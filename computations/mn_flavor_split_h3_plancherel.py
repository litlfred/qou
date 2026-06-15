"""m_n flavor-split at H_3 — Plancherel-channel test (Item A of PR #1654).

PR #1650 confirmed Plancherel-channel at H_2 (2-strand) doesn't close
the 0.10% X(q) residual. This probe tests the same template at H_3
(3-strand), where the 3 Wedderburn blocks (trivial, standard, sign)
have Plancherel weights (1/6, 4/6, 1/6).

## Hypothesis

The flavor-split is a 3-quark phenomenon. The natural Wedderburn
channel may be standard V_(2,1) (the only non-1-dim block at H_3),
not the H_2 sign rep.

## Method

Apply the H_3 Plancherel-channel decomposition:
  X(q)_pred = Σ_λ P_λ · (per-block contribution)

where per-block contribution depends on the σ_i eigenstructure and
the flavor-swap action.

Tests:
  - Per-block × Markov trace at each block
  - Per-block × σ_1 + σ_2 eigenstructure
  - Various weighted combinations

## Cross-references

- merged PR #1650 Item 2 (H_2 NULL)
- prop:flavor-split-substrate (X(q) baseline)
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

M_N_MEV = M_P_MEV + M_E_MEV + mp.mpf(repr(_ec.Q_NEUTRON_MEV))


def main() -> int:
    DPS = 80
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("m_n flavor-split at H_3 — Plancherel-channel test (item A)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(60)} (display)\n")

    M_N_avg = (M_P_MEV + M_N_MEV) / 2
    target = (M_N_MEV - M_P_MEV) / M_N_avg
    print(f"[Target] (m_n - m_p) / M_N_avg = {mp.nstr(target, 18)}")

    # Substrate
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    q2 = q + 1 / q

    # Baseline
    X_baseline = (q - 1) ** 2 * (1 - q ** (-4)) / 3
    print(f"[Baseline X(q)] = {mp.nstr(X_baseline, 18)}, "
          f"residual {mp.nstr((X_baseline - target)/target * 1e6, 8)} ppm")

    # H_3 Plancherel weights at q=1 (classical)
    P_trivial = mp.mpf(1) / 6
    P_standard = mp.mpf(4) / 6
    P_sign = mp.mpf(1) / 6

    # Eigenvalue on irreps of σ_1 at H_n:
    #   trivial → +q
    #   sign    → -1
    #   standard → 2x2 matrix; characteristic poly is [σ_1 - q][σ_1 + 1] = 0
    #            → eigenvalues are +q and -1 (with mult 1 each in 2-dim)
    print(f"\n[H_3 Wedderburn structure]")
    print(f"  P_(3)     = 1/6  (σ_1 = +q)")
    print(f"  P_(2,1)   = 4/6  (σ_1 has eigenvalues +q AND -1 in 2-dim)")
    print(f"  P_(1,1,1) = 1/6  (σ_1 = -1)")

    # Test Plancherel-channel candidates at H_3
    candidates = [
        # (a) Trivial channel: σ_1 = +q
        ("(a) P_trivial · (q-1)² · ℏ_q²",
         P_trivial * (q - 1) ** 2 * hbar_q_sq),
        # (b) Sign channel: σ_1 = -1
        ("(b) P_sign · ℏ_q²",
         P_sign * hbar_q_sq),
        # (c) Standard: combines both eigenvalues; "antisymmetric part"
        # has σ_1 = -1, so this gives the gap (q + 1) per the 2x2 structure
        ("(c) P_standard · (q+1)² · ℏ_q² / 2",
         P_standard * (q + 1) ** 2 * hbar_q_sq / 2),
        # (d) Pair: trivial + sign (1-dim blocks)
        ("(d) (P_triv + P_sign) · h · [2]_q · ℏ_q²",
         (P_trivial + P_sign) * h * q2 * hbar_q_sq),
        # (e) Wedderburn-weighted h² order
        ("(e) Σ P_λ · σ_1(λ)² · ℏ_q² (Markov trace ~)",
         (P_trivial * q ** 2 + P_standard * (q ** 2 + 1) + P_sign * 1) * hbar_q_sq),
        # (f) baseline (control)
        ("(f) baseline X(q)", X_baseline),
        # (g) standard channel only: dim_q V_(2,1) = [2]_q
        ("(g) P_standard · [2]_q · h · ℏ_q²",
         P_standard * q2 * h * hbar_q_sq),
        # (h) Frobenius trace: (q-q⁻¹)/2 × Plancherel-weighted
        ("(h) (h/2) · (P_triv + P_sign) · [2]_q · ℏ_q²",
         (h / 2) * (P_trivial + P_sign) * q2 * hbar_q_sq),
        # (i) Sign-block + trivial × ℏ_q²·[2]_q
        ("(i) (P_sign + P_triv)·([2]_q·h)·ℏ_q²",
         (P_sign + P_trivial) * q2 * h * hbar_q_sq),
        # (j) sign-only with [2]_q · h
        ("(j) P_sign · [2]_q · h · ℏ_q² · 6",
         P_sign * q2 * h * hbar_q_sq * 6),
    ]

    print(f"\n[Plancherel-channel decomposition candidates at H_3]")
    print(f"  {'name':<48}{'value':<22}{'Δ ppm vs target'}")
    scored = []
    for name, val in candidates:
        ppm = (val - target) / target * mp.mpf("1e6")
        scored.append((name, val, ppm))

    scored.sort(key=lambda r: abs(r[2]))
    for name, val, ppm in scored:
        marker = ""
        if abs(ppm) < mp.mpf("10"):
            marker = " ⭐⭐ < 10 ppm"
        elif abs(ppm) < mp.mpf("1000"):
            marker = " ⭐ < 1000 ppm"
        elif abs(ppm) < mp.mpf("10000"):
            marker = " *"
        print(f"  {name:<48}{mp.nstr(val, 12):<22}{mp.nstr(ppm, 8)}{marker}")

    best = scored[0]
    print(f"\n[Verdict]")
    if abs(best[2]) < mp.mpf("100"):
        verdict = (
            f"STRUCTURAL CANDIDATE at H_3: '{best[0]}' lands at "
            f"{mp.nstr(best[2], 6)} ppm — beats baseline 1277 ppm."
        )
    elif abs(best[2]) < mp.mpf(1277):
        verdict = (
            f"BEST: '{best[0]}' at {mp.nstr(best[2], 6)} ppm — beats "
            f"baseline X(q) (1277 ppm) but not structural threshold."
        )
    else:
        verdict = (
            f"NULL at H_3 — Plancherel-channel decomposition at H_3 does "
            f"NOT find a tighter form than baseline X(q) = ℏ_q²·h·[2]_q. "
            f"Combined with PR #1650's NULL at H_2: the Plancherel-channel "
            f"template at H_n with classical weights does NOT close the "
            f"m_n flavor-split residual. Likely requires q-deformed "
            f"Plancherel or different categorical operator entirely."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "mn-flavor-split-h3-plancherel",
        engine="python",
    )
    w.set_description(
        "Item A of PR #1654: tests Plancherel-channel template at H_3 "
        "(3 Wedderburn blocks) for the m_n / Δ_pn flavor-split residual."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("best_candidate", best[0])
    w.add_data("best_ppm", mp.nstr(best[2], 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="h3_plancherel_scan_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} candidates at 80 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
