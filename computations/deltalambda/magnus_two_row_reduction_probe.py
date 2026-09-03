#!/usr/bin/env python3
"""magnus_two_row_reduction_probe.py — does the exterior-power/determinant handle reach beyond
hooks to TWO-ROW shapes? (qou-o6ov)

The hook column reduced to the (n-1)-dim reduced Burau ρ^V because hooks (k,1^{n-k}) = Λ^{n-k}(V)
are IRREDUCIBLE Schur functors of the reflection rep V (PR #6430). Two-row shapes (n-k,k) are
NOT single Schur functors of V — S^{(n-k,k)}(V) is reducible over S_n — so the naive reduction
should FAIL. Confirming that failure tells us the correct handle is elsewhere (two-rows are
Schur-Weyl dual to U_q(sl₂), i.e. the 2-dim Jones rep, not ρ^V).

TEST 1 (expect FAIL, to confirm hooks are special): is
    tr_{(n-k,k)}(ρ)  ==  q^{twist} · s_{(n-k,k)}(eigenvalues of ρ^V)
where s_{(n-k,k)} = h_{n-k}·h_k − h_{n-k+1}·h_{k-1} (Jacobi–Trudi; h_j = complete homogeneous,
h_j(μ) = [t^j] ∏ 1/(1−t μ_i))? If it held, two-rows would reduce to ρ^V like the hooks.

Reports the two-row plain characters, the Schur candidate, and the ratio, so any residual clean
structure is visible. scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
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
from magnus_hook_exterior_power_probe import word_dense, word_trace  # noqa: E402


def complete_homogeneous(eigs, jmax):
    """h_j(eigs) for j=0..jmax via ∏ 1/(1 − t μ_i) truncated to order jmax (mpf convolution)."""
    h = [mp.mpf(1)] + [mp.mpf(0)] * jmax
    for mu in eigs:
        # multiply current series by 1/(1 − μ t) = Σ (μ t)^m
        new = [mp.mpf(0)] * (jmax + 1)
        for j in range(jmax + 1):
            s = mp.mpf(0)
            muk = mp.mpf(1)
            for m in range(j + 1):
                s += h[j - m] * muk
                muk *= mu
            new[j] = s
        h = new
    return h  # h[j] = h_j


def analyze(A):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    L = len(gens)
    qL = base.Q0 ** L

    # reflection-rep eigenvalues
    refl = tuple([n - 1, 1])
    Mrefl, _ = word_dense(refl, gens)
    E, _ = mp.eig(Mrefl)
    h = complete_homogeneous(E, n)  # h_0..h_n

    print(f"[tworow] A={A} (n={n}); L={L}, q^L={mp.nstr(qL,6)}")
    print(f"[tworow] TEST: tr_(n-k,k)(ρ) =?= q^twist · s_(n-k,k)(eig ρ^V),  "
          f"s = h_(n-k)h_k − h_(n-k+1)h_(k-1)\n")
    print("   k   λ=(n-k,k)     dim    tr_λ(ρ)              s_(n-k,k)(eig)        ratio tr/s")
    ratios = []
    for k in range(1, n // 2 + 1):
        lam = (n - k, k)
        _pg, dim = base.block_structure(lam)
        trl, _ = word_trace(lam, gens)
        # Jacobi–Trudi for a two-row shape (n-k, k):
        s = h[n - k] * h[k] - h[n - k + 1] * h[k - 1]
        s = mp.re(s)
        trl_r = mp.re(trl)
        ratio = (trl_r / s) if abs(s) > mp.mpf(10) ** -60 else mp.mpf("nan")
        ratios.append((k, ratio))
        print(f"  {k:>2}   {str(lam):<12}  {dim:>4}  {mp.nstr(trl_r,10):>16}   "
              f"{mp.nstr(s,10):>16}   {mp.nstr(ratio,6):>12}")

    # verdict: is the ratio a clean q-power (like the hook q^{L(1-j)}) — i.e. does the reduction hold?
    print()
    clean = True
    for k, r in ratios:
        # a clean hook-like ratio would be q^{L·f(k)} for a simple f; check it's at least a pure
        # power of q₀ (real, positive, log_q integer-ish) — the hook case had exactly that.
        if mp.isnan(r) or r <= 0:
            clean = False
            continue
        lg = mp.log(r) / mp.log(base.Q0)   # = exponent if r = q₀^lg
        # hook twist exponents were multiples of L; check if lg/L is near a small rational
        clean = clean and (abs(lg - mp.nint(lg)) < mp.mpf("1e-6"))
    if clean:
        print("  ⇒ ratio is a clean q-power in every row — two-rows DO reduce to ρ^V (Jacobi–Trudi).")
    else:
        print("  ⇒ ratio is NOT a clean q-power — two-rows do NOT reduce to ρ^V (as expected:")
        print("    S^{(n-k,k)}(V) is reducible over S_n; the hook reduction was special to")
        print("    single-column Schur functors). The correct handle for two-rows is the 2-dim")
        print("    U_q(sl₂) fundamental (Schur–Weyl dual), not the (n-1)-dim reduced Burau.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
