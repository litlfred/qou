#!/usr/bin/env python3
"""markov_trace_family_rank_probe — the Markov/Ocneanu trace family has rank
EXACTLY n on a p(n)-dimensional space of trace functionals, so no subtraction
scheme over that family isolates any block of dimension > 1.

This is a **negative** answer to the question `block_transposition_lift_probe`
left open: whether the trace-blind sector -- where that probe located an
*unbounded* channel asymmetry -- is recoverable by subtraction.  It is not, and
the reason is stronger and less specific than expected: **the recoverability
boundary is not the row cap.**  Even trace-VISIBLE blocks are not individually
isolable.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.

## THE QUESTION

Convention D is the `N = 2` member of the Ocneanu family `z_N = q^N/[N]_q`, and
its weights vanish on every partition with more than two rows -- the row cap
that `row_cap_is_one_boundary_probe` measures from the Wedderburn side.  Higher
`N` lifts the cap: `z_3` sees three rows, `z_4` sees four.  So the natural
hope, and the one the owner's "computable rather than directly observable"
framing suggests, is that a blind block's character is recoverable as a finite
linear combination of traces at several `N` -- observable at order 0 only by
subtraction.

Concretely: is there a coefficient vector `c_N` with

    sum_N c_N * tr^(N)(x)  =  chi_mu(x)     for all x

for `mu` one of the blind blocks?  Any `N`-dependent normalisation of the trace
is absorbed into `c_N`, so this is a question about the **weights** alone.

## THE WEIGHTS

The Ocneanu weight on block `lambda` at `z_N` is the SU(N) quantum dimension,
by the quantum hook-content formula

    qdim(lambda, N)  =  prod_cells [N + j - i]_q  /  prod_cells [hook]_q

which vanishes exactly when `ell(lambda) > N`, because then the cell `(N+1, 1)`
contributes `[0]_q = 0`.  That row cap is asserted here directly, for every
partition and every `N` in range, rather than assumed.

## THE RESULT

    n     p(n) blocks     rank of the trace family
    2         2                   2
    3         3                   3
    4         5                   4
    5         7                   5
    6        11                   6
    7        15                   7

**rank = n exactly.**  The character space grows like `p(n)` (superpolynomial);
the family of all Markov traces at all `N` spans only `n` dimensions of it.  So
the accessible fraction `n/p(n)` collapses -- 6/11 at `n = 6`, 7/15 at `n = 7`,
and to zero asymptotically.

Per block at `n = 6`, only the two **one-dimensional** blocks -- the trivial rep
`(6)` and the sign rep `(1^6)` -- have their character in the span.  Every
other block is outside it, **including `(4,2)`, which convention D SEES** and
which carries the largest finite channel asymmetry (ratio 5) found by
`block_transposition_lift_probe`.

## WHY THE H_3 RESULT DOES NOT GENERALISE — read this before citing it

The corpus carries a three-trace combination at `H_3` (coefficients
`6.22044128, -33.41778449, 28.19734321`) that does isolate a blind block.  That
is correct **and it is special to `n = 3`**: `p(3) = 3 = rank`, so at `n = 3`
the family is complete and every block is individually recoverable.  The same
holds at `n = 2`.  From `n = 4` on, `p(n) > n` and it fails.  Asserted below at
both ends, so the boundary is measured rather than asserted from one side.

## Internal consistency

Residual distances come in **conjugate pairs** -- `(5,1)` and `(2,1,1,1,1)`
agree, `(4,2)` and `(2,2,1,1)` agree, `(4,1,1)` and `(3,1,1,1)` agree, `(3,3)`
and `(2,2,2)` agree, and `(3,2,1)` is self-conjugate.  This is forced by
`lambda -> lambda'` being `q -> -1/q`, and is asserted.  It is a real check:
the first version of this measurement column-normalised the matrix, which
BREAKS the symmetry (see below), and the broken symmetry is what exposed it.

## What is NOT claimed

  * **NOT** that the trace-blind sector is unreachable by any means.  This is
    scope **(a)**, and narrowly scoped at that: it excludes the **Ocneanu /
    Markov trace family parameterised by `N`**, and nothing else.  A
    functional that is not a Markov trace -- a different representation, a
    non-trace invariant, a higher-tower operator projected down some other way
    -- is entirely untouched.
  * **NOT** a proof.  `rank = n` is measured at `n = 2..7` by two independent
    methods with a ~110-order-of-magnitude singular-value gap.  That is about
    as decisive as numerics gets, and it is still not a theorem.  Proving it
    would upgrade this to a scope-(b) structural exclusion; formalize-first
    would put the Lean before any wider search built on it.
  * **NOT** a claim that the row cap is unimportant.  It is real and asserted
    here.  The finding is that recoverability is a *strictly stronger*
    constraint, so the cap is not the binding one.
  * Nothing wired, nothing fitted.

NO FLOAT64: mpmath throughout at 120 dps, 50-digit proton pin, exact q-integers.

## Two measurement traps recorded, both hit here

1. **`mp.lu_solve` does not raise on a singular system.**  Solving for the
   isolating coefficients at 60 dps returned a vector of magnitude `1e57` with
   **residual 1.0** -- i.e. garbage that looks like an answer.  Reporting those
   coefficients as "the combination that isolates `(3,2,1)`" would have been a
   laundered number.  What settled it was **precision scaling**: at 120 dps the
   coefficients grew to `1e119` and the residual to 31; by 240 dps mpmath
   raised `matrix is numerically singular`.  Growing with precision is the
   signature of singular; shrinking would have meant merely ill-conditioned.
   The corpus already warns about this exact function
   (`qbeta_braid_nf_sdp_offset_probe` refuses to run for the same reason).

2. **Column normalisation changes the row space.**  A first pass normalised the
   columns before the SVD and read off the residual distances.  Scaling column
   `b` by `1/c_b` maps the row space to a *different* subspace, so those
   distances answer a different question.  Rank is unaffected, and so is
   *membership* (`e_b * D = c_b * e_b`, a scalar multiple), which is why the
   verdict survived -- but the reported distances were wrong, and the
   conjugation symmetry above is what exposed it: the normalised run gave
   `(5,1) = 0.449` against `(2,1,1,1,1) = 0.169` for a conjugate pair that must
   agree.  Both methods are run below and their **rank and verdict** compared;
   the distances quoted are from the un-normalised matrix.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from partition_utils import hook_lengths  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 120
ZERO = mp.mpf(10) ** -60          # a qdim below this is structurally zero
GS_TOL = mp.mpf(10) ** -60        # Gram-Schmidt independence threshold
IN_SPAN = mp.mpf(10) ** -30       # residual below this: character is in span


def fmt(x, n=6):
    return mp.nstr(x, n)


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)

    def qint(m):
        """[m]_q = (q^m - q^-m)/(q - q^-1); exactly 0 at m = 0."""
        return (q ** m - q ** (-m)) / (q - q ** (-1))

    def qdim(lam, N):
        """SU(N) quantum dimension (quantum hook-content formula) = the
        Ocneanu weight at z_N.  Vanishes iff ell(lam) > N."""
        num = mp.mpf(1)
        for i, row in enumerate(lam, start=1):
            for j in range(1, row + 1):
                num *= qint(N + j - i)
        den = mp.mpf(1)
        for h in hook_lengths(lam):
            den *= qint(h)
        return num / den

    print("=" * 78)
    print(" MARKOV-TRACE FAMILY RANK — the blind sector is NOT recoverable")
    print(" by subtraction, and neither is most of the VISIBLE one")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}    dps = {mp.mp.dps}")

    print("\n[1] THE WEIGHTS ARE SU(N) QUANTUM DIMENSIONS; THE ROW CAP IS EXACT")
    print("-" * 78)
    print("    qdim(lam,N) = prod [N+j-i]_q / prod [hook]_q   over cells of lam")
    print("    sanity, SU(2):  qdim((1),2) = [2]_q ;  qdim((1,1),2) = 1 ;")
    print("                    qdim((1,1,1),2) = 0  (three rows, N=2)")
    assert abs(qdim((1,), 2) - qint(2)) < ZERO
    assert abs(qdim((1, 1), 2) - 1) < ZERO
    assert abs(qdim((1, 1, 1), 2)) < ZERO
    checked = 0
    for n in range(2, 8):
        for lam in partitions(n):
            for N in range(2, n + 3):
                vanishes = abs(qdim(lam, N)) < ZERO
                assert vanishes == (len(lam) > N), (
                    f"row cap violated at {lam}, N={N}")
                checked += 1
    print(f"    row cap 'qdim == 0 iff rows > N' asserted on {checked} "
          f"(lambda, N) pairs, n = 2..7")

    print("\n[2] THE RANK OF THE WHOLE FAMILY")
    print("-" * 78)
    print("    Spanning ALL N, not a chosen few.  Two independent methods:")
    print("    SVD on the column-normalised matrix, and modified Gram-Schmidt")
    print("    on the raw rows.  They must agree on the RANK.")
    print()
    print(f"    {'n':>3} {'p(n)':>6} {'traces':>8} {'rank(SVD)':>10} "
          f"{'rank(GS)':>9} {'agree':>6} {'rank==n':>8}")
    data = {}
    for n in range(2, 8):
        L = list(partitions(n))
        NS = list(range(2, 5 * n + 8))
        raw = [[qdim(lam, N) for lam in L] for N in NS]

        M = mp.matrix(len(NS), len(L))
        for a in range(len(NS)):
            for b in range(len(L)):
                M[a, b] = raw[a][b]
        for b in range(len(L)):
            nrm = mp.sqrt(sum(M[a, b] ** 2 for a in range(len(NS))))
            if nrm > 0:
                for a in range(len(NS)):
                    M[a, b] /= nrm
        sv = sorted((abs(x) for x in mp.svd_r(M, compute_uv=False)),
                    reverse=True)
        rank_svd = sum(1 for s in sv if s > sv[0] * mp.mpf(10) ** -40)

        basis = []
        for r0 in raw:
            v = list(r0)
            for bb in basis:
                d = sum(v[i] * bb[i] for i in range(len(L)))
                for i in range(len(L)):
                    v[i] -= d * bb[i]
            nrm = mp.sqrt(sum(x ** 2 for x in v))
            if nrm > GS_TOL:
                basis.append([x / nrm for x in v])
        rank_gs = len(basis)

        data[n] = (L, basis, sv)
        print(f"    {n:>3} {len(L):>6} {len(NS):>8} {rank_svd:>10} "
              f"{rank_gs:>9} {str(rank_svd == rank_gs):>6} "
              f"{str(rank_gs == n):>8}")
        assert rank_svd == rank_gs, (
            f"n={n}: the two methods disagree on rank — neither is trustworthy")
        assert rank_gs == n, f"n={n}: rank {rank_gs} != n"
    L6, _, sv6 = data[6]
    nz = [s for s in sv6 if s > sv6[0] * mp.mpf(10) ** -40]
    zr = [s for s in sv6 if s <= sv6[0] * mp.mpf(10) ** -40]
    print()
    print(f"    the rank cut is not a threshold judgement: at n=6 the smallest")
    print(f"    retained singular value is {fmt(min(nz))} and the largest")
    print(f"    discarded is {fmt(max(zr))} — a gap of ~"
          f"{int(mp.log10(min(nz) / max(zr)))} orders of magnitude.")

    print("\n[3] WHICH BLOCKS ARE INDIVIDUALLY RECOVERABLE")
    print("-" * 78)
    print("    residual = distance from e_lambda to the span of ALL Markov")
    print("    traces.  0 => that block's character IS a finite combination of")
    print("    traces; > 0 => no combination isolates it, at any N.")
    print("    (Distances are from the RAW matrix: column scaling changes them")
    print("     while leaving rank and membership alone — see the docstring.)")
    for n in (3, 6):
        L, basis, _ = data[n]
        print(f"\n    n = {n}   (p({n}) = {len(L)}, rank = {len(basis)})")
        print(f"      {'lambda':>18} {'rows':>4} {'residual':>13} "
              f"{'recoverable':>12}")
        resid = {}
        for b_i, lam in enumerate(L):
            v = [mp.mpf(1) if i == b_i else mp.mpf(0) for i in range(len(L))]
            for bb in basis:
                d = sum(v[i] * bb[i] for i in range(len(L)))
                for i in range(len(L)):
                    v[i] -= d * bb[i]
            r = mp.sqrt(sum(x ** 2 for x in v))
            resid[lam] = r
            print(f"      {str(lam):>18} {len(lam):>4} {fmt(r):>13} "
                  f"{str(r < IN_SPAN):>12}")
        if n == 3:
            assert all(r < IN_SPAN for r in resid.values()), (
                "at n=3 the family is COMPLETE (p(3)=3=rank) — every block "
                "must be recoverable; this is why the H_3 result works")
            print("      => n=3 is COMPLETE: p(3) = 3 = rank, so every block is")
            print("         recoverable.  This is why the corpus's three-trace")
            print("         H_3 combination works, and why it does NOT")
            print("         generalise: from n=4 on, p(n) > n.")
        if n == 6:
            good = [lam for lam, r in resid.items() if r < IN_SPAN]
            assert good == [(6,), (1,) * 6], (
                f"expected only the two 1-dim blocks recoverable, got {good}")
            print(f"      => only {good} — the two ONE-DIMENSIONAL blocks.")
            print("         (4,2) is NOT recoverable and convention D SEES it,")
            print("         so the boundary is NOT the row cap.")
            pairs = 0
            for lam in L:
                dual = tuple(sorted((sum(1 for p in lam if p > j)
                                     for j in range(lam[0])), reverse=True))
                assert abs(resid[lam] - resid[dual]) < mp.mpf(10) ** -20, (
                    f"conjugate pair {lam}/{dual} must have equal residuals")
                pairs += 1
            print(f"      conjugation symmetry resid(lam') == resid(lam) "
                  f"asserted on all {pairs} blocks.")

    print("\n[4] THE VERDICT")
    print("-" * 78)
    print("    The question block_transposition_lift_probe left open was")
    print("    whether the trace-BLIND sector — where it located an UNBOUNDED")
    print("    channel asymmetry — is recoverable by subtraction.")
    print()
    print("    NO, and the reason is stronger than the question assumed.")
    print("    The Markov family spans rank n of a p(n)-dimensional character")
    print("    space, and only the two 1-dimensional blocks are individually")
    print("    recoverable.  (4,2) is trace-VISIBLE, carries the largest finite")
    print("    asymmetry found (ratio 5), and is still not isolable.")
    print()
    print("    So 'computable but not directly observable' does not hold via")
    print("    THIS family: the blind sector is not merely unseen, it is")
    print("    outside the span of every subtraction scheme built from")
    print("    Markov traces at any N.  Scope (a), narrowly scoped to that")
    print("    family — any non-Markov-trace functional is untouched, and")
    print("    that is where a closure would now have to come from.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
