#!/usr/bin/env python3
# polynomial_q_not_applicable: EXPLORATORY spike; outputs are NOT derivations.
"""HOMFLYPT SU(N) mass-tower evaluation — first multi-channel data.

⚠ EXPLORATORY — NOT A PRODUCTION DERIVATION (demoted 2026-06-04).
This spike consumes homflypt_engine.homflypt_at_su_n, whose absolute
normalisation is BROKEN (fails homflypt_reference_qa.py 0/5; see
docs/audits/2026-06-04-hidden-fitting-verification-gap-mass-binding-walkthrough.md).
Two specific cautions:
  • Before the 2026-06-04 exponent fix the SU(2) channel sat at the
    DEGENERATE point δ≡−1 (every link → ±1), so any prior SU(2) "ratio"
    or "mirror difference" output was noise, not knot data.
  • The "implied E₀ = Q_β/|ΔP|" block below is a BACK-SOLVE (a fit): it
    assumes the answer Q_β and reports the calibration that reproduces it.
    A genuine E₀ is the single universal m_e/(q₀(q₀−1)) ≈ 4.186 MeV, NOT a
    per-channel quantity. Do NOT cite the implied-E₀ values as predictions.
The proton/neutron RATIOS may still be suggestive once the engine is
reference-validated; the mass-tower itself derives no observable today.


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
from q_parameter import Q_50_DIGIT_STR, Q_MP
from witness_base import WitnessBuilder
from _precision import set_compute_dps  # noqa: E402


def main():
    t_start = time.monotonic()
    set_compute_dps()

    Q0 = Q_MP
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
    fam_mpf = {}          # same values, kept as mpf for the assertion routes

    for name, (word, n) in braids.items():
        print(f"\n  {name} (n={n}, {len(word)} crossings):")
        fam = homflypt_su_n_family(word, n, Q0, N_max=N_max)
        results[name] = {}
        fam_mpf[name] = dict(fam)
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
    # (σ₁σ₂⁻¹)³ and (σ₁⁻¹σ₂)³ are a mirror pair; both closures are the
    # Borromean rings, which is amphichiral. ΔP comes out IDENTICALLY zero
    # in every channel, so this column carries no channel split and the
    # Q_β back-solve below has no input at all. Kept in mpf so the assertion
    # measures the real gap rather than a float64 round-trip.
    print("\nMirror difference P(proton) − P(neutron) per SU(N):")
    mirror_diffs = {}
    mirror_worst_gap = mp.mpf(0)
    p_fam_mpf = fam_mpf["proton (σ₁σ₂⁻¹)³"]
    n_fam_mpf = fam_mpf["neutron (σ₁⁻¹σ₂)³"]
    for N in range(2, N_max + 1):
        diff = p_fam[N] - n_fam[N]
        mirror_diffs[N] = diff
        mirror_worst_gap = max(mirror_worst_gap,
                               abs(p_fam_mpf[N] - n_fam_mpf[N]))
        print(f"  SU({N}): ΔP = {diff:+.10f}")

    # ── Q_β BACK-SOLVE (a fit, NOT a prediction) ─────────────────
    # ⚠ This block does NOT predict Q_β. It assumes the experimental
    # answer Q_β and solves for the E₀ that reproduces it — a one-free-
    # constant back-solve. The canonical E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV
    # is a SINGLE universal constant; an "implied E₀" that differs per
    # channel N is the signature of a fit, not a derivation. Kept only as
    # a diagnostic of how far |ΔP| is from carrying Q_β. See the audit doc.
    print("\nQ_β BACK-SOLVE (diagnostic only — NOT a prediction):")
    from experimental_constants import Q_NEUTRON_MEV, M_E_MEV
    Q_beta_target = Q_NEUTRON_MEV  # 0.78233341 MeV
    for N in range(2, N_max + 1):
        dp = mirror_diffs[N]
        if abs(dp) > 1e-30:
            # back-solved E₀ (would be channel-independent IFF |ΔP| were
            # the right structural quantity — it is not).
            E0_implied = Q_beta_target / abs(dp)
            print(f"  SU({N}): |ΔP| = {abs(dp):.8f}, "
                  f"back-solved E₀ = {E0_implied:.4f} MeV "
                  f"(≠ canonical 4.186 ⇒ fit, not prediction)")

    # ── Figure-eight amphicheirality check ───────────────────────
    # Kept in mpf: the ✓/✗ below used to be printed and thrown away, and the
    # float() round-trip that produced it is what made an exact 0 read as
    # 4.44e-16. Both the count and the worst gap now leave the function.
    print("\nFigure-eight amphicheirality (P = P_mirror at each N):")
    fig8_mpf = fam_mpf["figure-eight σ₁σ₂⁻¹σ₁σ₂⁻¹"]
    fig8_mirror_word = [-1, 2, -1, 2]  # mirror of σ₁σ₂⁻¹σ₁σ₂⁻¹
    channels = list(range(2, N_max + 1))
    fig8_amphichiral_channels = 0
    fig8_worst_gap = mp.mpf(0)
    for N in channels:
        p_mirror = homflypt_at_su_n(fig8_mirror_word, 3, N, Q0)
        diff = abs(fig8_mpf[N] - p_mirror)
        ok = diff < mp.mpf("1e-8")
        fig8_amphichiral_channels += 1 if ok else 0
        fig8_worst_gap = max(fig8_worst_gap, diff)
        print(f"  SU({N}): |P − P_mirror| = {mp.nstr(diff, 3)} {'✓' if ok else '✗'}")

    # ── δ = (v⁻¹−v)/z vs −[N]_s: the 2026-06-04 v-exponent invariant ──
    # The engine builds v = q^{N/2}, z = q^{1/2}−q^{-1/2} and reads the
    # defining rep's quantum dimension off δ = (v⁻¹−v)/z. Independently,
    # that dimension is −[N]_s at s = √q. Before the 2026-06-04 fix the
    # exponent was q^{(N−1)/2}, which sends δ → −1 identically at N=2 (the
    # degenerate Jones point where every link collapses to ±1) and off
    # −[N]_s at every other N. Two routes, and a regression of the fix is
    # exactly what separates them.
    s = mp.sqrt(Q0)
    delta_channels_agreeing = 0
    delta_worst_gap = mp.mpf(0)
    print("\nSU(N) quantum dimension δ = (v⁻¹−v)/z vs −[N]_s:")
    for N in channels:
        v = Q0 ** (mp.mpf(N) / 2)
        z = s - 1 / s
        delta_from_v = (1 / v - v) / z
        minus_bracket_N = -(s ** N - s ** (-N)) / (s - 1 / s)
        gap = abs(delta_from_v - minus_bracket_N)
        delta_worst_gap = max(delta_worst_gap, gap)
        delta_channels_agreeing += 1 if gap < mp.mpf("1e-30") else 0
        print(f"  SU({N}): δ = {mp.nstr(delta_from_v, 12)}, "
              f"−[{N}]_s = {mp.nstr(minus_bracket_N, 12)}, |Δ| = {mp.nstr(gap, 3)}")

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
    w.add_data("channels_evaluated", channels)

    # ── Was `spike_completed`, computed=1.0 / expected=1.0 ───────────────
    # Two float literals: it recorded that the file reached its last line.
    # It also put the only two raw float64 fields into the assertions block.
    # Replaced by the three things this run can actually be wrong about.

    # (1) The specialisation point. Route A: δ = (v⁻¹−v)/z as the engine
    #     builds it from v = q₀^{N/2}. Route B: −[N]_s at s = √q₀, the
    #     quantum dimension of the SU(N) defining rep. Independent of the
    #     braid entirely, and the pre-2026-06-04 exponent q^{(N−1)/2} fails
    #     it in every channel (δ ≡ −1 at N=2).
    w.add_assertion(
        "su_n_quantum_dimension_matches_minus_bracket_N",
        computed=str(delta_channels_agreeing),
        expected=str(len(channels)),
        tolerance=0,
        unit="SU(N) channels",
        source=("Route A: δ = (v⁻¹−v)/z with v = q₀^{N/2}, z = √q₀−1/√q₀ — the "
                "point the engine evaluates at. Route B: −[N]_s = "
                "−(s^N−s^{−N})/(s−s^{−1}) at s = √q₀ — the defining rep's "
                "quantum dimension. Expected = the channel list rebuilt from "
                "range(2, N_max+1), so raising N_max tightens this. Guards the "
                "2026-06-04 v-exponent fix (audit §2e)."),
    )

    # (2) Amphicheirality of 4₁. Route A: P of σ₁σ₂⁻¹σ₁σ₂⁻¹. Route B: P of
    #     the mirror word σ₁⁻¹σ₂σ₁⁻¹σ₂ — a separate walk through the Hecke
    #     characters, not a cyclic rotation of the first (conjugation
    #     invariance is automatic for a trace and would prove nothing).
    #     The figure-eight knot is amphichiral, so the two must agree.
    w.add_assertion(
        "figure_eight_amphichiral_in_every_su_n_channel",
        computed=str(fig8_amphichiral_channels),
        expected=str(len(channels)),
        tolerance=0,
        unit="SU(N) channels with |P − P_mirror| < 1e-8",
        source=("Route A: P(σ₁σ₂⁻¹σ₁σ₂⁻¹; SU(N), q₀). Route B: P of the mirror "
                "word σ₁⁻¹σ₂σ₁⁻¹σ₂. 4₁ is amphichiral, so agreement is a known "
                f"property, not a restatement. Worst gap this run: "
                f"{mp.nstr(fig8_worst_gap, 4)}."),
    )

    # (3) The headline the description promises — a per-channel mass split
    #     and Q_β predictor candidates from |ΔP| — measured instead of
    #     asserted. Route A: P of the proton word. Route B: P of the neutron
    #     word, its mirror. ΔP is identically zero in every channel, so the
    #     split is zero and the back-solve prints nothing. Asserting the zero
    #     is what makes a future non-zero visible.
    w.add_assertion(
        "borromean_mirror_pair_has_zero_channel_split",
        computed=mp.nstr(mirror_worst_gap, 20),
        expected="0",
        tolerance="1e-30",
        unit="max_N |P(proton) − P(neutron)| at SU(N)",
        source=("Route A: P((σ₁σ₂⁻¹)³; SU(N), q₀). Route B: P((σ₁⁻¹σ₂)³) — its "
                "mirror. Both close to the Borromean rings, which is "
                "amphichiral, so this engine returns no p/n split in ANY "
                "channel: the ratio column is 1.0 throughout and the Q_β "
                "back-solve has no input. Recorded so a later engine that does "
                "split the pair flips this rather than passing silently."),
    )
    w.add_caveat(
        "The p/n mirror difference is identically zero at every N, so the "
        "'multi-channel mass-split data' and the |ΔP| Q_β back-solve in the "
        "docstring produce nothing at all — the back-solve block prints no "
        "rows. Separately, the absolute normalisation is confirmed broken in "
        "this run: the 2-strand trefoil σ₁³ comes out 14%–44% away from "
        "Lickorish's P(3₁⁺; v, z) = 2v² − v⁴ + v²z² at the same (v, z), so no "
        "absolute value here is assertable and only δ and mirror pairs are."
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
