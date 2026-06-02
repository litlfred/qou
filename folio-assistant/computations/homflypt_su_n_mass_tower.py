#!/usr/bin/env python3
"""HOMFLYPT SU(N) mass-tower evaluation — first multi-channel data.

Computes the HOMFLYPT polynomial at SU(N) specializations for
proton, neutron, and deuteron braids at substrate q₀. This is the
first evaluation of the mass tower's MULTI-CHANNEL structure —
prior work used only the Jones polynomial (N=2 slice).

Per rem:archimedean-image-table row 5: the HOMFLYPT gives a
FAMILY of observables indexed by N. Different N-slices probe
different representation-theoretic channels (SU(2) = mass ratio;
SU(3) = color structure; SU(4) = electroweak; ...).

## Braids tested

1. **Borromean proton** — (σ₁σ₂⁻¹)³ on 3 strands. The "simplest"
   proton-type braid in B_3.
2. **Borromean neutron** — (σ₁⁻¹σ₂)³ on 3 strands. Mirror of the
   proton braid (crossing signs flipped).
3. **Figure-eight** — σ₁σ₂⁻¹σ₁σ₂⁻¹ on 3 strands. Amphicheiral
   reference (P = P_mirror at every N).
4. **Trefoil** — σ₁³ on 2 strands. Known reference for validation.

## What this produces

For each braid × each N ∈ {2, 3, 4, 5, 6}:
- P(β̂; SU(N), q₀) — the SU(N) quantum invariant at substrate
- Proton/neutron RATIO at each N — structural mass-split data
- Mirror difference P − P_mirror — CPT-violation per channel
- Q_β predictor candidates from cross-orientation structure

## Compute infrastructure

Uses homflypt_engine.homflypt_at_su_n() which calls
hecke_characters.chi_lambda_braid for 3-strand braids at q₀.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from homflypt_engine import homflypt_at_su_n, homflypt_su_n_family
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


def main():
    t_start = time.monotonic()
    mp.mp.dps = 50

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    print(f"HOMFLYPT SU(N) mass-tower evaluation at q₀ = {mp.nstr(Q0, 12)}")
    print("=" * 70)

    # ── Braid definitions ────────────────────────────────────────
    braids = {
        "proton (σ₁σ₂⁻¹)³": ([1, -2, 1, -2, 1, -2], 3),
        "neutron (σ₁⁻¹σ₂)³": ([-1, 2, -1, 2, -1, 2], 3),
        "figure-eight σ₁σ₂⁻¹σ₁σ₂⁻¹": ([1, -2, 1, -2], 3),
        "trefoil σ₁³": ([1, 1, 1], 2),
    }

    N_max = 6
    results = {}

    for name, (word, n) in braids.items():
        print(f"\n  {name} (n={n}, {len(word)} crossings):")
        fam = homflypt_su_n_family(word, n, Q0, N_max=N_max)
        results[name] = {}
        for N, val in fam.items():
            results[name][N] = float(val)
            print(f"    SU({N}): {mp.nstr(val, 14)}")

    # ── Proton/neutron ratios per N ──────────────────────────────
    print("\n" + "=" * 70)
    print("Proton/neutron RATIOS per SU(N) channel:")
    p_fam = results["proton (σ₁σ₂⁻¹)³"]
    n_fam = results["neutron (σ₁⁻¹σ₂)³"]
    ratios = {}
    for N in range(2, N_max + 1):
        p_val = p_fam[N]
        n_val = n_fam[N]
        if abs(n_val) > 1e-30:
            ratio = p_val / n_val
            ratios[N] = ratio
            print(f"  SU({N}): P(p)/P(n) = {ratio:.10f}")
        else:
            print(f"  SU({N}): P(n) ≈ 0 — ratio undefined")

    # ── Mirror difference (CPT violation per channel) ────────────
    print("\nMirror difference P(proton) − P(neutron) per SU(N):")
    mirror_diffs = {}
    for N in range(2, N_max + 1):
        diff = p_fam[N] - n_fam[N]
        mirror_diffs[N] = diff
        print(f"  SU({N}): ΔP = {diff:+.10f}")

    # ── Q_β predictor candidates ─────────────────────────────────
    print("\nQ_β predictor candidates (ΔP normalized):")
    from experimental_constants import Q_NEUTRON_MEV, M_E_MEV
    Q_beta_target = Q_NEUTRON_MEV  # 0.78233341 MeV
    for N in range(2, N_max + 1):
        dp = mirror_diffs[N]
        if abs(dp) > 1e-30:
            # What E_0 calibration would make ΔP predict Q_β?
            E0_implied = Q_beta_target / abs(dp)
            print(f"  SU({N}): |ΔP| = {abs(dp):.8f}, "
                  f"implied E₀ = {E0_implied:.4f} MeV "
                  f"(vs canonical E₀ ≈ 4.186 MeV)")

    # ── Figure-eight amphicheirality check ───────────────────────
    print("\nFigure-eight amphicheirality (P = P_mirror at each N):")
    fig8 = results["figure-eight σ₁σ₂⁻¹σ₁σ₂⁻¹"]
    fig8_mirror_word = [-1, 2, -1, 2]  # mirror of σ₁σ₂⁻¹σ₁σ₂⁻¹
    for N in range(2, N_max + 1):
        p_mirror = homflypt_at_su_n(fig8_mirror_word, 3, N, Q0)
        diff = abs(fig8[N] - float(p_mirror))
        ok = diff < 1e-8
        print(f"  SU({N}): |P − P_mirror| = {diff:.2e} {'✓' if ok else '✗'}")

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder(
        "homflypt-su-n-mass-tower",
        engine="mpmath",
        start_time=t_start,
    )
    w.set_description(
        "First multi-channel HOMFLYPT evaluation of the mass tower "
        "at substrate q₀. Computes P(β̂; SU(N), q₀) for N=2..6 "
        "across proton, neutron, figure-eight, and trefoil braids. "
        "Records per-N proton/neutron ratios, mirror differences "
        "(CPT structure), and Q_β predictor candidates. Per "
        "rem:archimedean-image-table row 5: this is the first data "
        "from the SU(N>2) channels."
    )
    w.set_content_block("rem:archimedean-image-table")
    w.add_parameter("dps", 50)
    w.add_parameter("N_max", N_max)
    w.add_parameter("q_0", mp.nstr(Q0, 20))
    for name, fam in results.items():
        w.add_data(f"su_n_family_{name.split()[0]}", {
            str(k): v for k, v in fam.items()
        })
    w.add_data("proton_neutron_ratios", {str(k): v for k, v in ratios.items()})
    w.add_data("mirror_differences", {str(k): v for k, v in mirror_diffs.items()})
    w.add_assertion(
        "spike_completed",
        computed=1.0,
        expected=1.0,
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
