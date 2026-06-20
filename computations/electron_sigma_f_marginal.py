#!/usr/bin/env python3
"""
σ_F vs its marginal — resolving the shell-closure-stability inconsistency.

Cross-ref: consistent with `computations/sigma_f_electron_shell_chain.py` on
main (the canonical 50-dps σ_F chain), which independently finds the categorical
2n² cumulative [2,10,28,60,…] ≠ the noble gases [2,10,18,36,…] and caveats that
σ_F does not support the noble-gas mechanism. This script's distinct point: the
quantity that *does* peak is the marginal Δσ_F, and even it needs the 2n²/Madelung
INPUT to land on the noble gases (case (a) vs the every-2 of the bare T_γe, case (b)).

prop:shell-closure-stability states two things about the SAME σ_F(Z):
  claim 1 — σ_F is monotone NON-DECREASING in Z;
  claim 2 — σ_F attains a STRICT LOCAL MAXIMUM at noble-gas Z.
A non-decreasing function has no strict interior local maximum, so claims 1 and
2 contradict. (The interprets remark switches to "piecewise-monotone", which
contradicts claim 1; the Lean sidesteps both by setting σ_F ≡ 0.)

Resolution (the physically-correct reading): σ_F = n_target·y₀* (the cumulative
dual objective) is monotone — claim 1 is right. The quantity that PEAKS at the
noble gases is the **marginal increment**

    I₁(Z) = σ_F(Z) − σ_F(Z−1)        (the ionisation energy / dressing gap),

NOT σ_F itself. The interprets remark even defines I₁ as a marginal trace-gap,
then mis-attributes it as "∝ σ_F"; it is ∝ Δσ_F.

This script shows (1) σ_F monotone + I₁ = Δσ_F peaking at shell closures, and
(2) that the PEAK LOCATIONS are fixed by the shell CAPACITIES, which are an
INPUT (noble-gas-characterization S_i = 2n²·T_{2,3}), not derived from the
categorical transfer matrix T_γe (which is 2×2 → 2-fold, giving closures every
2, NOT {2,10,18,…}). So a σ_F-peak model that reproduces the periodic table is
CIRCULAR until 2n² is derived — the genuine open categorical problem.

Refs: prop:shell-closure-stability, prop:noble-gas-characterization,
shell-structure-eigenvalues (T_γe is 2×2), shell-closure-stability-interprets.
"""
from __future__ import annotations


def shell_energy(n: int) -> float:
    """Categorical shell energy proxy: deeper (smaller n) binds more.
    Monotone-decreasing-in-n stand-in for the T_γe Chebyshev shell ladder /
    the 1/n² spacing (e-Hartree round 8b). Only the ORDER matters here."""
    return 1.0 / (n * n)


def fill_and_index(capacities):
    """Fill electrons into shells with the given per-shell capacities; return
    σ_F(Z) (cumulative binding, monotone) and I₁(Z)=Δσ_F (the marginal /
    ionisation energy) for Z = 1..Σcap. Closures are at the cumulative sums."""
    energies = []  # energy of the shell each successive electron lands in
    for n, cap in enumerate(capacities, start=1):
        energies += [shell_energy(n)] * cap
    sigma, marg, cum = [], [], 0.0
    for Z, e in enumerate(energies, start=1):
        cum += e
        sigma.append(cum)
        marg.append(e)  # I₁(Z) = σ_F(Z) − σ_F(Z−1) = energy of the Z-th electron
    closures = []
    c = 0
    for cap in capacities:
        c += cap
        closures.append(c)
    return sigma, marg, closures


def peaks(marg):
    """Z where I₁ is a local max (≥ neighbours and strictly > the next) —
    the noble-gas signal."""
    out = []
    for i in range(len(marg)):
        left = marg[i - 1] if i > 0 else -1
        right = marg[i + 1] if i + 1 < len(marg) else -1
        if marg[i] >= left and marg[i] > right:
            out.append(i + 1)  # 1-indexed Z
    return out


def main() -> int:
    print("  σ_F vs MARGINAL Δσ_F — shell-closure-stability claim-1/claim-2 fix\n")

    # (a) INPUT the periodic-table capacities (2n²/Madelung): 2,8,8,18,18,32
    cap_periodic = [2, 8, 8, 18, 18, 32]
    sig_p, marg_p, clo_p = fill_and_index(cap_periodic)
    print("### (a) capacities = INPUT 2n²/Madelung {2,8,8,18,18,32}")
    print(f"  σ_F monotone non-decreasing: {all(sig_p[i] >= sig_p[i-1] for i in range(1, len(sig_p)))}")
    print(f"  closures (cumulative)        : {clo_p}")
    print(f"  I₁=Δσ_F local-max Z (peaks)  : {peaks(marg_p)[:6]}")
    print(f"  noble gases                  : [2, 10, 18, 36, 54, 86]")
    print("  → peaks land on the noble gases — BUT only because the closures")
    print("    {2,10,18,…} were put in as the capacities. Circular.\n")

    # (b) capacities from the categorical T_γe transfer matrix: it is 2×2, so
    #     each shell power gives a 2-fold eigenspace → capacity 2 per shell.
    cap_tgamma = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    sig_t, marg_t, clo_t = fill_and_index(cap_tgamma)
    print("### (b) capacities from the actual T_γe (2×2 ⇒ 2-fold per shell)")
    print(f"  closures (cumulative)        : {clo_t}")
    print(f"  I₁=Δσ_F local-max Z (peaks)  : {peaks(marg_t)[:6]}")
    print("  → the categorical transfer matrix gives closures every 2")
    print("    ({2,4,6,…}), NOT the periodic table. T_γe does not produce 2n².\n")

    print("### Finding")
    print("  • claim 1 (σ_F monotone) is correct; the noble-gas signal is the")
    print("    MARGINAL Δσ_F = I₁ (ionisation energy), which peaks while σ_F")
    print("    rises monotonically. claim 2's 'σ_F local max' + the interprets")
    print("    'piecewise-monotone σ_F' + 'I₁ ∝ σ_F' are the misstatements")
    print("    (should be Δσ_F / μ≥2; I₁ ∝ Δσ_F).")
    print("  • Reproducing the peaks at {2,10,18,…} needs the 2n² capacities,")
    print("    which are an INPUT (noble-gas full-of-curls), not derived from")
    print("    the 2×2 T_γe. Until 2n² is derived, any peak model is circular —")
    print("    the genuine open categorical problem behind the level-6 cut.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
