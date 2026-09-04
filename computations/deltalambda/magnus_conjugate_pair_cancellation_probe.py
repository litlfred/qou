#!/usr/bin/env python3
"""magnus_conjugate_pair_cancellation_probe.py — the b(λ)-decay is CANCELLATION, not size: the
controlled conjugate-pair experiment (qou-o6ov).

THE QUESTION. #6534 established (★): tr_λ(ρ·Ω₂^P) = (4/[2]²)·Σ_a tr_λ([ρ,σ_a]·σ_(a+1)), for every
λ. That says WHAT the decay object is. It does not say WHY it decays with b(λ) = n − λ₁. Two
candidates:
  SIZE        — the commutator [ρ,σ_a] is itself smaller in high-b irreps ⇒ a norm bound
                |tr| ≤ Σ_a ‖[ρ,σ_a]‖·‖σ_(a+1)‖ would capture the decay.
  CANCELLATION— [ρ,σ_a] is NOT smaller; the decay comes from signed cancellation when it is
                traced against σ_(a+1) ⇒ NO norm bound can capture it, and a spectral route
                (as the hook bound #6520 took) is forced.

WHY A RAW b-SCAN CANNOT DECIDE IT. dim λ varies wildly with b, and both |tr|/dim and the
normalised norm mix a b-effect with a dim-effect. Worse, the normalised norm is U-SHAPED in b at
both A=2 and A=3 — it falls to a minimum near mid-b and rises again — so a scan truncated before
the tail (as the first A=3 run was, at b ≤ 4) reads as "falls with b" and inverts the answer.

THE CONTROL. dim λ = dim λ' EXACTLY (transpose/conjugate partition), while
b(λ') = n − λ'₁ = n − (number of parts of λ). So a conjugate pair is two irreps of IDENTICAL
dimension at (generally very) different b — the clean A/B test. For each pair this probe reports
    norm ratio   = normalised ‖[ρ,σ_a]‖ at the HIGHER-b partner / at the lower-b partner
    trace ratio  = (|tr|/dim)          at the HIGHER-b partner / at the lower-b partner
SIZE predicts norm ratio < 1 tracking the trace ratio. CANCELLATION predicts norm ratio ≳ 1
(commutators no smaller, or larger) while the trace ratio ≪ 1.

scope-(a); NO-FLOAT64 (mpf, dps 140). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_gauge_invariant_curvature_probe import projector_curvature_trace  # noqa: E402
from magnus_curvature_commutator_identity_probe import sigma_dense, frob  # noqa: E402


def conjugate(lam):
    """Transpose partition λ' — dim λ' = dim λ exactly, while b flips."""
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))


def measure(lam, gens, q, ngen):
    """(|tr(ρΩ₂^P)|/dim, normalised Σ_a‖[ρ,σ_a]‖/(dim·‖ρ‖), dim)."""
    sig, dim = sigma_dense(lam, q, ngen)
    rho = sig[gens[0]]
    for g in gens[1:]:
        rho = rho * sig[g]
    tr, _ = projector_curvature_trace(lam, gens, q)
    cn = mp.mpf(0)
    for a in range(ngen):
        cn += frob(rho * sig[a] - sig[a] * rho, dim)
    return abs(mp.re(tr)) / dim, cn / (dim * frob(rho, dim)), dim


def analyze(A, max_dim):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    print(f"[conj] A={A} (n={n}); conjugate pairs (dim λ = dim λ' EXACTLY), dim ≤ {max_dim}")
    print(f"[conj] SIZE ⇒ norm ratio < 1 tracking trace ratio.  "
          f"CANCELLATION ⇒ norm ratio ≳ 1 while trace ratio ≪ 1.\n")
    print("   low-b λ          b    high-b λ'         b'   dim   |tr|/dim (low)  (high)      "
          "trace ratio   NORM ratio")
    seen = set()
    rows = []
    for lam in base.partitions(n):
        lam = tuple(lam)
        cj = conjugate(lam)
        if lam == cj or lam in seen or cj in seen:
            seen.add(lam)
            continue
        seen.add(lam); seen.add(cj)
        b1, b2 = sum(lam) - lam[0], sum(cj) - cj[0]
        lo, hi = (lam, cj) if b1 < b2 else (cj, lam)
        _pg, d = base.block_structure(lo)
        if d > max_dim:
            continue
        t_lo, nrm_lo, d_lo = measure(lo, gens, q, ngen)
        t_hi, nrm_hi, d_hi = measure(hi, gens, q, ngen)
        assert d_lo == d_hi, f"conjugate dims differ: {d_lo} vs {d_hi} — control is broken"
        if t_lo == 0 or nrm_lo == 0:
            continue                              # trivial/sign pair: both exactly 0, no ratio
        tr_ratio, nrm_ratio = t_hi / t_lo, nrm_hi / nrm_lo
        rows.append((lo, hi, d_lo, tr_ratio, nrm_ratio))
        print(f"  {str(lo):<16} {sum(lo)-lo[0]:>1}    {str(hi):<16} {sum(hi)-hi[0]:>1}  {d_lo:>4}   "
              f"{mp.nstr(t_lo,6):>12}  {mp.nstr(t_hi,6):>10}   {mp.nstr(tr_ratio,4):>10}   "
              f"{mp.nstr(nrm_ratio,4):>9}")

    if not rows:
        print("\n  no pairs under the dim cap — raise --max-dim")
        return
    print()
    n_norm_ge = sum(1 for *_, nr in [(r[0], r[1], r[2], r[3], r[4]) for r in rows] if nr >= 1)
    worst_tr = max(r[3] for r in rows)
    print(f"  pairs measured: {len(rows)};  norm ratio ≥ 1 in {n_norm_ge}/{len(rows)};  "
          f"largest trace ratio = {mp.nstr(worst_tr,4)}")
    if n_norm_ge == len(rows) and worst_tr < 1:
        print("  ⇒ CANCELLATION. At IDENTICAL dimension, the higher-b partner has commutators that")
        print("    are no smaller (indeed larger) yet a strictly smaller trace. The b-decay is NOT")
        print("    a size effect, so NO norm bound |tr| ≤ Σ_a‖[ρ,σ_a]‖·‖σ_(a+1)‖ can produce it —")
        print("    a spectral route (as the hook bound #6520 took) is forced for the general λ.")
    elif worst_tr < 1:
        print("  ⇒ trace falls at higher b in every pair, but the norm ratio is not uniformly ≥ 1;")
        print("    cancellation is indicated but not cleanly separated from size on this sample.")
    else:
        print("  ⇒ NOT a clean b-decay on conjugate pairs — some higher-b partner has the LARGER")
        print("    trace. Report this rather than the headline: the control refutes the simple story.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    ap.add_argument("--max-dim", type=int, default=50,
                    help="skip pairs whose (shared) dim exceeds this; cost is O(dim³) mpf matmul")
    args = ap.parse_args()
    for A in args.A:
        analyze(A, args.max_dim)
        print()


if __name__ == "__main__":
    main()
