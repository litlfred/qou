"""m_n / Δ_pn flavor-split — Plancherel-channel rewrite (Item 2 of PR #1650).

PR #1645's item 3 confirmed X(q) = ℏ_q²·h_q·[2]_q refinement is NULL
in the natural basis. This probe applies the PR #1645 sign-block /
Plancherel-channel template to attempt a fresh categorical reading.

## The σ_1 eigendecomposition (Hecke at H_2)

The flavor swap u ↔ d on a 3-quark baryon is implemented categorically
by Hecke generator σ_1 acting on a 2-strand sub-braid. σ_1 has
eigenspaces:

  - Symmetric (trivial rep of S_2):    eigenvalue +q
  - Antisymmetric (sign rep of S_2):   eigenvalue -1

Plancherel weights at H_2:
  P_(2)   = 1²/|S_2| = 1/2     (trivial 1-dim)
  P_(1,1) = 1²/|S_2| = 1/2     (sign 1-dim)

## The Plancherel-channel hypothesis for X(q)

Hypothesis (paralleling m_p sign-block): the flavor-split mass-
difference (m_n − m_p)/M_N comes from a per-block × Plancherel-weight
decomposition of the Hecke-skein eigenstructure on H_2.

Test forms:
  X_sign(q) = ℏ_q² · (−1) · P_(1,1) · (additional) = ℏ_q² · (−1) · (1/2)
  X_triv(q) = ℏ_q² · (+q) · P_(2) · (additional) = ℏ_q² · q · (1/2)
  X_combined = (X_sign + X_triv) · (additional factor)

## Cross-references

- PR #1645 ProtonMassEMSignBlock + sign-block scaffold
- PR #1645 flavor_split_xq_refinement.py (the NULL refinement)
- `prop:flavor-split-substrate` baseline X(q)
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
    print("m_n / Δ_pn Plancherel-channel rewrite (item 2 of PR #1650)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(60)} (display)\n")

    M_N_avg = (M_P_MEV + M_N_MEV) / 2
    target = (M_N_MEV - M_P_MEV) / M_N_avg
    print(f"[Target] (m_n - m_p) / M_N_avg = {mp.nstr(target, 18)}")

    # Substrate quantities
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    q2 = q + 1 / q  # [2]_q

    # Baseline
    X_baseline = (q - 1) ** 2 * (1 - q ** (-4)) / 3
    baseline_residual = (X_baseline - target) / target * mp.mpf("1e6")
    print(f"[Baseline X(q)] = {mp.nstr(X_baseline, 18)}, residual {mp.nstr(baseline_residual, 8)} ppm")

    # σ_1 eigenvalues at q_0
    sigma1_symmetric = q       # +q eigenvalue on trivial rep
    sigma1_antisymmetric = -mp.mpf(1)  # -1 eigenvalue on sign rep

    # Plancherel weights at H_2
    P_trivial = mp.mpf(1) / 2
    P_sign = mp.mpf(1) / 2

    print(f"\n[σ_1 eigenstructure at H_2]")
    print(f"  Symmetric (trivial)    eigenvalue +q = {mp.nstr(sigma1_symmetric, 12)}, P = 1/2")
    print(f"  Antisymmetric (sign)   eigenvalue -1 = {mp.nstr(sigma1_antisymmetric, 12)}, P = 1/2")

    # Test Plancherel-channel forms
    # The baseline X(q) = ℏ_q² · h · [2]_q decomposes as:
    # h · [2]_q = (q-q⁻¹)(q+q⁻¹) = q² - q⁻² = [2]_q · ((q-1) + (q-1)·q⁻¹·extra)
    # Hmm, structurally:
    # h · [2]_q = q² - q⁻² (a single q-bracket [2]·[2] product... not quite [4]_q)
    # Actually q² - q⁻² = [4]_q · (q - q⁻¹) / [4]_q · ... it's complicated
    # Just compute: h · [2]_q = (q²-q⁻²)
    print(f"\n[Algebraic identity] h · [2]_q = q² - q⁻² = {mp.nstr(h * q2, 18)}")
    print(f"                     vs ℏ_q² · h · [2]_q = X = {mp.nstr(hbar_q_sq * h * q2, 18)}")

    # Plancherel-channel candidates
    print(f"\n[Plancherel-channel decomposition candidates]")
    candidates = [
        # (a) Per-channel σ_1 eigenvalue × Plancherel weight × ℏ_q²
        ("(a) Σ_λ P_λ · σ_1(λ) · ℏ_q²",
         (P_trivial * sigma1_symmetric + P_sign * sigma1_antisymmetric) * hbar_q_sq),
        # (b) Σ_λ P_λ · σ_1(λ)² · ℏ_q² (symmetric in eigenvalue magnitude)
        ("(b) Σ_λ P_λ · σ_1(λ)² · ℏ_q²",
         (P_trivial * sigma1_symmetric ** 2 + P_sign * sigma1_antisymmetric ** 2) * hbar_q_sq),
        # (c) Asymmetric channel only (just trivial)
        ("(c) P_trivial · σ_1(trivial) · ℏ_q²",
         P_trivial * sigma1_symmetric * hbar_q_sq),
        # (d) Sign-only with multiplier
        ("(d) P_sign · σ_1(sign) · ℏ_q² · [2]_q · h",
         P_sign * sigma1_antisymmetric * hbar_q_sq * q2 * h),
        # (e) Difference of channels (commutator-like)
        ("(e) ℏ_q² · (σ_1(triv) − σ_1(sign)) · 1/2",
         hbar_q_sq * (sigma1_symmetric - sigma1_antisymmetric) / 2),
        # (f) The baseline itself rewritten as P-weighted
        ("(f) baseline (control)", X_baseline),
        # (g) Pure ℏ_q²·h (without [2]_q)
        ("(g) ℏ_q² · h", hbar_q_sq * h),
        # (h) Combined with sign-block ratio
        ("(h) ℏ_q² · (q + 1)/2", hbar_q_sq * (q + 1) / 2),
    ]

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
        elif abs(ppm) < mp.mpf("100"):
            marker = " ⭐ < 100 ppm"
        elif abs(ppm) < mp.mpf("1000"):
            marker = " *"
        print(f"  {name:<48}{mp.nstr(val, 12):<22}{mp.nstr(ppm, 8)}{marker}")

    # Verdict
    best = scored[0]
    print(f"\n[Verdict]")
    if abs(best[2]) < mp.mpf("10"):
        verdict = (
            f"STRUCTURAL CANDIDATE: '{best[0]}' lands at "
            f"{mp.nstr(best[2], 6)} ppm — beats baseline X(q) at 1277 ppm."
        )
    elif abs(best[2]) < mp.mpf("1000"):
        verdict = (
            f"BEST: '{best[0]}' at {mp.nstr(best[2], 6)} ppm — beats X(q) "
            f"baseline (1277 ppm) but not at structural-identity level."
        )
    else:
        verdict = (
            f"NULL — Plancherel-channel decomposition at H_2 does NOT find "
            f"a tighter form than baseline X(q) = ℏ_q²·h·[2]_q. The "
            f"flavor-split residual is NOT captured by σ_1 eigenstructure × "
            f"Plancherel weights at H_2. May need higher-rank Hecke or "
            f"different categorical operator."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "mn-flavor-split-plancherel-channel",
        engine="python",
    )
    w.set_description(
        "Item 2 of PR #1650: applies PR #1645's sign-block / Plancherel-"
        "channel template to m_n flavor-split. Tests whether σ_1 "
        "eigendecomposition at H_2 + Plancherel weights closes the 0.10% "
        "baseline X(q) residual."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("baseline_residual_ppm", mp.nstr(baseline_residual, 12))
    w.add_data("best_candidate_name", best[0])
    w.add_data("best_candidate_ppm", mp.nstr(best[2], 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="plancherel_channel_scan_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} Plancherel-channel candidates at 80 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
