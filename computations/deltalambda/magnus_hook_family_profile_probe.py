#!/usr/bin/env python3
"""magnus_hook_family_profile_probe.py — the tr-decay along the HOOK family (qou-o6ov).

NEW ANGLE (not one of the 7 dead routes in the 2026-09-02 consolidation). Reframe:
tr(ρ_λ Ω₂)/dim_λ = χ^λ(Z)/dim_λ = the NORMALIZED CHARACTER of the fixed Hecke element
Z = ρ·Ω₂, read across the character table (fixed n, varying λ). The most tractable slice
covering the FULL b-range is the HOOK family
    λ = (k, 1ⁿ⁻ᵏ),   b = n − k,   dim = C(n−1, k−1),   k = 1 … n.
Hooks are the irreducible constituents of the exterior powers of the reflection rep, so if any
family has exploitable structure it is this one. The endpoint k=1 (sign rep (1ⁿ)) is the proved
zero (#6387); k=n (trivial (n)) is the other proved zero. This probe measures the hook profile
τ_k = tr(ρ_{(k,1ⁿ⁻ᵏ)} Ω₂)/dim between them and looks for:
  - a closed form / clean ratio τ_{k}/τ_{k+1},
  - a monotone or single-peak shape,
  - whether |τ_k| is bounded by a simple function of dim = C(n−1,k−1).

If a clean law appears it is a genuine sub-theorem (the decay ALONG the hooks); if not, an
honest negative that narrows the character-row structure. scope-(a); NO-FLOAT64 (mpf).
No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_extreme_rep_endpoint_probe import omega2_trace  # noqa: E402


def hook(n, k):
    """λ = (k, 1^{n-k})."""
    if k == n:
        return (n,)
    return tuple([k] + [1] * (n - k))


def analyze(A):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    print(f"[hook] A={A} (n={n}); the hook family λ=(k,1^(n-k)), b=n-k, dim=C(n-1,k-1)")
    print(f"[hook]  k   λ                    b   dim    tr(ρ_λ Ω₂)        |tr|/dim      τ_k/τ_(k-1)")
    prev = None
    data = []
    for k in range(1, n + 1):
        lam = hook(n, k)
        _pg, dim = base.block_structure(lam)
        b = n - k
        tr, _ = omega2_trace(lam, gens)
        ratio = ""
        if prev is not None and prev[1] != 0:
            ratio = mp.nstr(tr / prev[1], 5)
        tnorm = abs(tr) / dim if dim else mp.mpf(0)
        print(f"      {k:>2}  {str(lam):<20} {b:>2}  {dim:>4}  {mp.nstr(tr,6):>14}   "
              f"{mp.nstr(tnorm,5):>10}   {ratio:>12}")
        data.append((k, b, dim, tr, tnorm))
        prev = (k, tr)

    # analysis of |tr|/dim across the hooks (exclude the two exact zeros k=1, k=n)
    interior = [(k, b, dim, tr, tn) for (k, b, dim, tr, tn) in data if k not in (1, n) and dim > 1]
    if len(interior) >= 2:
        peak = max(interior, key=lambda r: r[4])
        print(f"\n  hook |tr|/dim peaks at k={peak[0]} (λ={hook(n,peak[0])}, b={peak[1]}) = {mp.nstr(peak[4],4)}")
        # is |tr| ~ dim (i.e. |tr|/dim ~ const) or |tr|/dim decaying toward the endpoints?
        lo = interior[0]; hi = interior[-1]
        print(f"  |tr|/dim at smallest-k interior hook (k={lo[0]}, b={lo[1]}): {mp.nstr(lo[4],4)}")
        print(f"  |tr|/dim at largest-k  interior hook (k={hi[0]}, b={hi[1]}): {mp.nstr(hi[4],4)}")
        # test: is |tr| ≤ C·(dim of the b=1 reflection hook)?  the reflection rep is k=n-1.
        refl = next((r for r in data if r[0] == n - 1), None)
        if refl:
            print(f"  reflection hook k={n-1} (b=1): tr={mp.nstr(refl[3],5)}, |tr|/dim={mp.nstr(refl[4],4)} "
                  f"(the Burau/Alexander peak)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
