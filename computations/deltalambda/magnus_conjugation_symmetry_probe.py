#!/usr/bin/env python3
"""magnus_conjugation_symmetry_probe.py — is the b-profile of tr(ρ_λ Ω₂) conjugation-symmetric?
(qou-o6ov)

The decay of tr(ρ_λ Ω₂) runs from the b=1 PEAK (reflection rep (n−1,1) = reduced Burau =
Alexander sector, #6392) to the b=n−1 sign-rep ZERO (#6387). The near-endpoint rep
(2,1ⁿ⁻²) (b=n−2, dim n−1) is the CONJUGATE partition of the (n−1,1) peak. Hecke conjugation
λ↦λ' acts by the sign-twist q ↦ −q⁻¹ (contents/axial-distances negate). So the two ENDS of the
b-profile may be structurally related.

This probe MEASURES, for each conjugate pair (λ, λ') at the atom, the ratio
    R(λ) = tr(ρ_{λ'} Ω₂) / tr(ρ_λ Ω₂)
and the same normalised by dim, and reports whether R is a clean function of q (a monomial in
q₀, ±1, or a simple ratio) — which would be a structural symmetry linking the b=1 Burau peak to
the b=n−2 near-endpoint, a real handle on the profile. Self-conjugate λ (λ=λ') are noted (their
value is forced by the symmetry if R=±1).

scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/ (mass_at_3A_proper moved up)

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_extreme_rep_endpoint_probe import omega2_trace  # noqa: E402


def conjugate(shape):
    """Conjugate (transpose) partition."""
    if not shape:
        return ()
    m = shape[0]
    return tuple(sum(1 for p in shape if p > c) for c in range(m))


def analyze(A):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    print(f"[conj] A={A} (n={n}); q₀={mp.nstr(base.Q0,8)}, −1/q₀={mp.nstr(-1/base.Q0,8)}")
    print(f"[conj] R(λ) = tr(ρ_{{λ'}} Ω₂) / tr(ρ_λ Ω₂)   for conjugate pairs (λ, λ')\n")

    seen = set()
    rows = []
    for shape in base.partitions(n):
        _pg, dim = base.block_structure(shape)
        if dim <= 1:
            continue
        lp = conjugate(shape)
        key = frozenset([shape, lp])
        if key in seen:
            continue
        seen.add(key)
        b = n - shape[0]
        bp = n - lp[0]
        tr, _ = omega2_trace(shape, gens)
        if shape == lp:
            rows.append((b, shape, lp, dim, tr, None, None, True))
            continue
        trp, dimp = omega2_trace(lp, gens)
        R = (trp / tr) if tr != 0 else mp.mpf("inf")
        rows.append((b, shape, lp, dim, tr, trp, R, False))

    rows.sort(key=lambda r: r[0])
    print("   b   λ                     b'  λ'                    R=tr(λ')/tr(λ)     |tr(λ)|/dim")
    for b, shape, lp, dim, tr, trp, R, selfc in rows:
        bp = n - lp[0]
        if selfc:
            print(f"  {b:>2}  {str(shape):<20}  —   (self-conjugate)         —              "
                  f"{mp.nstr(abs(tr)/dim,4)}")
        else:
            print(f"  {b:>2}  {str(shape):<20} {bp:>2}  {str(lp):<20}  "
                  f"{mp.nstr(R,6):>14}   {mp.nstr(abs(tr)/dim,4)}")

    # focus: the peak/near-endpoint pair (n-1,1) <-> (2,1^{n-2})
    peak = tuple([n - 1, 1])
    near = conjugate(peak)
    tr_peak, dpk = omega2_trace(peak, gens)
    tr_near, dnr = omega2_trace(near, gens)
    print(f"\n  FOCUS peak↔near-endpoint:  (n−1,1)={peak} [b=1, Burau/Alexander]  ↔  "
          f"{near} [b={n-near[0]}]")
    print(f"    tr(peak)={mp.nstr(tr_peak,6)}  tr(near)={mp.nstr(tr_near,6)}  "
          f"ratio={mp.nstr(tr_near/tr_peak,6) if tr_peak!=0 else 'inf'}")
    # candidate clean values for the ratio
    for name, val in [("−1", mp.mpf(-1)), ("+1", mp.mpf(1)),
                      ("−q₀²", -base.Q0**2), ("−1/q₀²", -1/base.Q0**2),
                      ("q₀²", base.Q0**2), ("1/q₀²", 1/base.Q0**2)]:
        if tr_peak != 0 and abs(tr_near/tr_peak - val) < mp.mpf(10)**-6:
            print(f"    ⇒ ratio ≈ {name}  (clean!)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
