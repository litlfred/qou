#!/usr/bin/env python3
"""magnus_chain_end_to_end_probe.py — compose the whole arc's chain and check it against the
ACTUAL target quantity, on the complete n=9 census. (qou-o6ov)

WHAT THIS CLOSES. Every link of this arc exists, but they have never been composed and checked
end to end against the quantity the bean is actually about — the signed trace tr_λ(ρ·Ω₂^P). Each
link was verified in isolation, on a different (often dim-capped) sample:

    |tr_λ(ρ·Ω₂^P)|  ≤  Σ_i |eig_i(M_λ)|          triangle inequality on the spectrum
                    ≤  √(dim_λ · tr_λ(X*X))       (B): Cauchy–Schwarz + Schur, #6573, Lean-proved
                    ≤  dim_λ · √(E(b(λ)))         E(b) = max_{b(λ)=b} tr_λ(X*X)/dim_λ, #6729

with E strictly decreasing in b over all seven complete levels (#6729). Composing gives a per-
dimension bound on the ORIGINAL target that falls with b:

    |tr_λ(ρ·Ω₂^P)| / dim_λ  ≤  √(E(b(λ)))                                              (CHAIN)

NO EIGENVALUES NEEDED, which is what makes this affordable at every shape including dim 216:
|tr X| ≤ Σ|eig X| ≤ √(dim·Σ|eig|²) ≤ √(dim·‖X‖_F²), so the middle term can be skipped and both
ends computed from the sparse column-wise kernel — the trace is a diagonal sum, tr(X*X) is the
Frobenius norm. The Σ|eig| step is where the bound gives away the most (#6573 measured 2–6×), and
it is bypassed here rather than evaluated.

WHAT IS BEING TESTED, since the inequalities are theorems and cannot fail. Two things that are
NOT theorems:
  (1) the ARITHMETIC — a failure would mean the kernel or the recorded envelope is wrong, not that
      Cauchy–Schwarz is;
  (2) the TIGHTNESS — how much the composed bound gives away, per shape and per level. A bound
      that holds by a factor of 500 is a true statement and a useless one, and that is the number
      a reader needs in order to judge whether this chain is worth anything.

E(b) is RECOMPUTED here from the same census rather than transcribed from #6729 — a chain check
that quotes its own inputs is checking arithmetic it already did.

scope-(a); NO-FLOAT64 (mpf; dps asserted at every compute entry). Nothing wired.
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

_WANT_DPS = None


def _assert_dps(where):
    if _WANT_DPS is not None and mp.mp.dps != _WANT_DPS:
        raise RuntimeError(f"mp.mp.dps is {mp.mp.dps}, expected {_WANT_DPS}, at {where}")


def trace_and_frob(lam, gens, q, ngen):
    """(tr_λ(ρ·Ω₂^P), tr_λ(X*X) = ‖X‖_F², dim) in one column-wise sweep.

    Both come from the same X e_j: the trace is Σ_j (X e_j)_j, the Frobenius norm is Σ_j ‖X e_j‖².
    Computing them together halves the work and guarantees they describe the same matrix — taking
    them from two passes would let a discrepancy hide as a mismatch between runs.
    """
    _assert_dps(f"trace_and_frob({lam})")
    per_gen, dim = base.block_structure(tuple(lam))
    sig = base.sigma_csr(per_gen, dim, q)
    c = 4 / (q + 1 / q) ** 2
    rev = list(reversed(gens))
    tr = mp.mpf(0)
    frob = mp.mpf(0)
    for j in range(dim):
        e = [mp.mpf(0)] * dim
        e[j] = mp.mpf(1)
        acc = [mp.mpf(0)] * dim
        for a in range(ngen - 1):
            u = base.spmatvec(sig[a], base.spmatvec(sig[a + 1], e))
            w = base.spmatvec(sig[a + 1], base.spmatvec(sig[a], e))
            for r in range(dim):
                acc[r] += u[r] - w[r]
        v = [c * x for x in acc]
        for g in rev:
            v = base.spmatvec(sig[g], v)
        tr += v[j]
        for x in v:
            if x:
                frob += x * x
    return tr, frob, dim


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps

    q = base.Q0
    A = args.A
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    print(f"[chain] n={n}: |tr_λ(ρΩ₂^P)| ≤ √(dim_λ·tr_λ(X*X)) ≤ dim_λ·√(E(b)) on the COMPLETE census")
    print(f"[chain] E(b) is RECOMPUTED here, not quoted from #6729 — a chain check that quotes its")
    print(f"[chain] own inputs is checking arithmetic it already did.  (mp.dps = {args.dps})\n")

    data = {}
    for lam in base.partitions(n):
        lam = tuple(lam)
        tr, frob, dim = trace_and_frob(lam, gens, q, ngen)
        data[lam] = (mp.re(tr), frob, dim)

    # E(b) from this run's own numbers
    E = {}
    for lam, (_tr, frob, dim) in data.items():
        b = sum(lam) - lam[0]
        E[b] = max(E.get(b, mp.mpf(0)), frob / dim)

    print("     b   λ                        dim    |tr|/dim      link1 √(F/dim)   "
          "link2 √(E(b))    slack1   slack2")
    ok1 = ok2 = True
    worst1 = worst2 = mp.mpf(0)
    best1 = best2 = mp.mpf("inf")
    for lam in sorted(data, key=lambda l: (sum(l) - l[0], -data[l][1] / data[l][2])):
        tr, frob, dim = data[lam]
        b = sum(lam) - lam[0]
        lhs = abs(tr) / dim
        l1 = mp.sqrt(frob / dim)          # √(dim·F)/dim
        l2 = mp.sqrt(E[b])
        tol = 1 + mp.mpf(10) ** -40
        h1 = lhs <= l1 * tol
        h2 = l1 <= l2 * tol
        ok1, ok2 = ok1 and h1, ok2 and h2
        if lhs > 0:
            worst1 = max(worst1, l1 / lhs)
            best1 = min(best1, l1 / lhs)
        if l1 > 0:
            worst2 = max(worst2, l2 / l1)
            best2 = min(best2, l2 / l1)
        s1 = (l1 / lhs) if lhs > 0 else mp.mpf("inf")
        s2 = (l2 / l1) if l1 > 0 else mp.mpf("inf")
        print(f"    {b:>2}   {str(lam):<24} {dim:>4}  {mp.nstr(lhs,7):>11}  "
              f"{mp.nstr(l1,7):>14}  {mp.nstr(l2,7):>14}  {mp.nstr(s1,4):>7}  {mp.nstr(s2,4):>7}")

    print(f"\n  link 1  |tr|/dim ≤ √(tr(X*X)/dim)  holds on every shape?  {'YES ✓' if ok1 else 'NO ✗'}")
    print(f"  link 2  √(tr(X*X)/dim) ≤ √(E(b))    holds on every shape?  {'YES ✓' if ok2 else 'NO ✗'}")
    if not (ok1 and ok2):
        print("\n  ⇒ A LINK FAILED. These are theorems, so a failure means the KERNEL or the")
        print("    recomputed envelope is wrong — not Cauchy–Schwarz. Report it as an arithmetic")
        print("    defect and do not adjust the bound.")
        return

    env = [(b, mp.sqrt(E[b])) for b in sorted(E) if E[b] > 0]
    mono = all(env[i + 1][1] < env[i][1] for i in range(len(env) - 1))
    print(f"\n  COMPOSED BOUND  |tr_λ(ρΩ₂^P)|/dim_λ ≤ √(E(b(λ))), strictly decreasing in b?  "
          f"{'YES ✓' if mono else 'NO'}")
    print("      " + " > ".join(f"b={b}:{mp.nstr(v,6)}" for b, v in env))
    print(f"\n  TIGHTNESS — the part a reader needs to judge whether the chain is worth anything:")
    print(f"    link 1 (spectrum → Frobenius) gives away  {mp.nstr(best1,4)}×  to  {mp.nstr(worst1,4)}×")
    print(f"    link 2 (shape → level envelope) gives away {mp.nstr(best2,4)}×  to  {mp.nstr(worst2,4)}×")
    print("    A bound that holds by a factor of 500 is a true statement and a useless one; these")
    print("    figures are what decide which this is, not the ✓ marks above.")


if __name__ == "__main__":
    main()
