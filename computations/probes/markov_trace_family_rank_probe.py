#!/usr/bin/env python3
"""markov_trace_family_rank_probe — the Markov/Ocneanu trace family has rank
EXACTLY n on a p(n)-dimensional space of trace functionals, so no subtraction
scheme over that family isolates any block of dimension > 1.

This answers, negatively, the question `block_transposition_lift_probe` left
open: whether the trace-blind sector -- where that probe located an *unbounded*
channel asymmetry -- is recoverable by subtraction.  It is not, and the reason
is stronger and less specific than expected: **the recoverability boundary is
not the row cap.**  Even trace-VISIBLE blocks are not individually isolable.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.

## THE QUESTION

Convention D is the `N = 2` member of the Ocneanu family `z_N = q^N/[N]_q`, and
its weights vanish on every partition with more than two rows.  Higher `N`
lifts the cap: `z_3` sees three rows, `z_4` four.  So the natural hope -- and
the one the owner's "computable rather than directly observable" framing
suggests -- is that a blind block's character is a finite linear combination of
traces at several `N`, observable at order 0 only by subtraction:

    sum_N c_N * tr^(N)(x)  =  chi_mu(x)     for all x

Any `N`-dependent normalisation of the trace is absorbed into `c_N`, so this is
a question about the **weights** alone.

## WHAT THE CORPUS ALREADY SUPPLIES — cited, not re-derived

The weight itself is `main`'s, derived and validated there, and this probe
imports the closed form rather than rebuilding it:

  * `computations/schurweyl/ocneanu_weight_general_n.py` — DERIVES the general-n
    Markov weight from the defining conditions `tr(1) = 1`, `tr(sigma) = z`
    (no recall, no fit):

        W_lam(q,z) = prod_cells [ q^(2i) (q^2 - 1 - q z) + q^(2j+1) z ]
                     / prod_cells [ q^(2 h(i,j)) - 1 ]

  * `QOU.QBeta.WenzlWeight.schurPrincipal_eq_zero_iff` (sorry-free) — the row
    cap `s_lam = 0 <=> ell(lam) > r`, every n, every lam, every r.
  * `QOU.QBeta.WenzlWeight.wenzlLevel_conventionD` — convention D **is** level
    `r = 2`.
  * `QOU.BraidsAndKnots.ocneanu_param_eq_of_fibre_qdim` (sorry-free) —
    `z*[N]_q = q^N`, division-free, general N.
  * `docs/audits/2026-08-16-wenzl-level-family.md` §2 — the family `z_r`,
    r = 1..8, with row caps, quotients and coranks tabulated.

**Caveat carried forward, not resolved here.**  `IsOcneanuWeightSystem` is
class-carried with **no instance anywhere** in the corpus
(`docs/audits/2026-08-21-all-n-corank-catalan.md` §"Epistemic tiering";
`WedderburnTraceDecomposition.lean:31`), so the Lean row cap is *conditional*
per "conditional-proved != premise-established".  This probe does not rely on
that: it asserts the row cap **directly from the closed form** below.

## THE RESULT — derived symbolically, then corroborated numerically

### 1. The degree, exactly (sympy over Q(q), no floats anywhere)

Reading `W_lam(q,z)` as a polynomial in `z`: each cell contributes a factor
affine in `z` whose `z`-coefficient is

    q^(2j+1) - q^(2i+1)      -- ZERO exactly on the diagonal i = j

so a monomial of degree `m` in the expanded product needs `m` cells off the
diagonal.  With `d(lam)` = Durfee square size = number of diagonal cells,

    **deg_z W_lam  =  n - d(lam)**

verified for **every** partition at `n = 2..6`.  Since every non-empty
partition has the cell `(0,0)`, `d >= 1` always and the top-degree term `z^n`
**always** dies -- which is why the naive bound `n+1` (from `n` affine factors)
is never attained.

### 2. The rank bound follows

`max_lam deg_z W_lam = n - 1`, so

    W(z)  =  sum_{k=0}^{n-1} z^k c_k

for `n` fixed coefficient vectors `c_k`, giving `dim span{W(z) : z} <= n`
**for structural reasons, not numerical ones**.  The coefficient system is then
computed to have full rank `n` -- exact `Matrix.rank()` over `Q(q)`, `n = 2..6`
-- so the bound is attained:

    n            2   3   4   5   6   7
    p(n) blocks  2   3   5   7  11  15
    rank         2   3   4   5   6   7        -> rank = n EXACTLY

The character space grows like `p(n)`; the family of ALL Markov traces at ALL
`N` spans only `n` dimensions of it, so the accessible fraction `n/p(n)`
collapses to zero.

### 3. Which blocks are individually recoverable

At `n = 6`, only the two **one-dimensional** blocks -- trivial `(6)` and sign
`(1^6)`.  Every other block is outside the span, **including `(4,2)`, which
convention D SEES** and which carries the largest finite channel asymmetry
found by `block_transposition_lift_probe` (ratio 5).  Hence the headline: the
boundary is not the row cap.

## Why the n = 3 case does NOT generalise

At `n = 3`, `p(3) = 3 = rank`, so the family is **complete** and every block is
individually recoverable there; likewise `n = 2`.  From `n = 4` on, `p(n) > n`
and it fails.  Asserted at both ends below, so the boundary is measured from
both sides rather than extrapolated from one.

This matters because a three-trace combination at `H_3` (coefficients
`6.22044128, -33.41778449, 28.19734321`) does isolate a blind block there.
**PROVENANCE, CORRECTED:** an earlier version of this docstring attributed that
combination to "the corpus".  That was wrong.  `git log --all -S"33.41778"` and
`-S"28.19734"` are **empty** -- the coefficients have never appeared in any
commit reachable from `main`.  They are this session's own earlier working, and
citing them as corpus fact would have manufactured a provenance.  The corpus
does, independently, carry a documented instance of exactly the
over-generalisation this section guards against:
`computations/qbeta/qbeta_rank_one_identity_is_n3_only_probe.py` -- *"a low-rank
accident of H_3, not a structural fact ... do not generalise the n=3
coincidence"*.

## Not claimed to be new

No published source for `rank = n` was found in `library/` (searched INDEX,
`sections/`, and the `ocr/` tier).  That is **not** evidence of novelty:
**Wenzl 1988** (*Hecke algebras of type A_n and subfactors*, Invent. Math. 92)
is cited in `folio/schema/references.ts` but is **NOT ingested into
`library/`**, and it is the most likely classical home for this statement --
the polynomiality of the weights in `z` is exactly the route taken above.
22 further PDFs sit un-ingested in `uploads/`, invisible to the corpus grep.
Treat this as "not found in the held sources", never as "original".

## Name collision — say which "rank" you mean

Three distinct quantities in this corpus are called "rank":

  * `markov_z_fibre_rank_bar_covariance_probe.py` — the **SU(N) index N**
    (convention D => 2).
  * `pyhecke_n_generic.gram_inverse_n` — the **Gram rank at a fixed z**, whose
    radical is the TL ideal (bean `qou-8iru`).
  * **this probe** — the **dimension of the span of trace functionals over all
    N**.

A grep for "rank" + "Markov" returns the first two and misses this one.

## What is NOT claimed

  * **NOT** that the trace-blind sector is unreachable by any means.  Scope
    **(a)**, narrowly: this excludes the **Ocneanu/Markov trace family
    parameterised by N** and nothing else.  A non-trace functional -- the
    triple linking number `mu-bar_123` among them -- is untouched, and is where
    a closure would now have to come from.
  * **NOT** a general-n theorem.  `deg_z = n - d` and `rank = n` are verified
    exactly (symbolically) at `n = 2..6` and numerically to `n = 7`; neither is
    proved for all `n`.  The degree argument above is the proof sketch and the
    formalize-first target; proving it upgrades this to a scope-(b) structural
    exclusion.
  * **NOT** a claim that the row cap is unimportant.  It is real and asserted
    here.  The finding is that recoverability is a *strictly stronger*
    constraint, so the cap is not the binding one.
  * **NOT** in tension with `QOU/QBeta/TraceBlindSector.lean`, which says the
    >2-row blocks are the Temperley-Lieb kernel and *"carry no states at
    N = 2"*.  That is about `omega_lam = 0` at ONE `N`.  This is about the span
    over ALL `N`, says nothing about states, and applies to `(4,2)`, which is
    visible.  Strictly stronger, and not implied by it.
  * Nothing wired, nothing fitted.

NO FLOAT64: the primary result is **exact symbolic** (sympy over `Q(q)`); the
numerical corroboration is mpmath at 120 dps on the 50-digit proton pin.

## Three measurement traps recorded, all hit here

1. **`mp.lu_solve` does not raise on a singular system.**  Solving for the
   isolating coefficients at 60 dps returned a vector of magnitude `1e57` with
   **residual 1.0** -- garbage shaped like an answer, and publishing it would
   have been a laundered number.  **Precision scaling** settled it: `1e119` at
   120 dps with residual 31, and `matrix is numerically singular` raised at 240
   dps.  GROWING with precision is the signature of singular; shrinking would
   have meant merely ill-conditioned.  The corpus already warns about this
   function (`qbeta_braid_nf_sdp_offset_probe` refuses to run for it).

2. **Column normalisation changes the row space.**  A first pass normalised
   columns before an SVD and read off residual distances, which answer a
   different question.  Rank and membership survive (`e_b D = c_b e_b`, a
   scalar multiple), so the verdict held -- but the distances were wrong.  The
   conjugation symmetry exposed it: the normalised run gave `0.449` against
   `0.169` for a conjugate pair that must agree.

3. **An ABSOLUTE Gram-Schmidt drop test invents rank.**  `qdim` grows like
   `N^n`, so over a wide `N` range the row norms span many orders and an
   absolute floor admits round-off as a new direction.  Measured at `n = 6`:
   the absolute test reports rank **17** over `N = 2..300` and **28** over
   `2..1000` -- against `p(6) = 11`, i.e. **more directions than the space has
   dimensions**, which is impossible and is the tell.  A *relative* test
   (normalise each row before the drop test) returns 6 at every range out to
   `N = 1000`.  Both the relative test and the assertion `rank <= p(n)` are
   below; the assertion is the cheap invariant that catches this whole class.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from partition_utils import hook_lengths  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 120
ZERO = mp.mpf(10) ** -60          # a qdim below this is structurally zero
GS_REL = mp.mpf(10) ** -60        # Gram-Schmidt drop test, RELATIVE (trap 3)
IN_SPAN = mp.mpf(10) ** -30       # residual below this: character is in span

_q, _z = sp.symbols("q z")


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


def cells(s):
    return [(i, j) for i, r in enumerate(s) for j in range(r)]


def durfee(s):
    """Durfee square size = number of diagonal cells (i, i) in lambda."""
    return sum(1 for i, r in enumerate(s) if r > i)


def sym_hooks(s):
    rows = list(s)
    cols = [sum(1 for r in s if r > j) for j in range(s[0])]
    return [(rows[i] - j - 1) + (cols[j] - i - 1) + 1 for (i, j) in cells(s)]


def W(s):
    """main's DERIVED general-n Markov weight — computations/schurweyl/
    ocneanu_weight_general_n.py.  Imported as a formula, not re-derived."""
    num = sp.Integer(1)
    for (i, j) in cells(s):
        num *= _q ** (2 * i) * (_q ** 2 - 1 - _q * _z) + _q ** (2 * j + 1) * _z
    den = sp.Integer(1)
    for h in sym_hooks(s):
        den *= _q ** (2 * h) - 1
    return sp.cancel(sp.together(num / den))


def main() -> int:
    q = Q_MP

    def qint(m):
        return (q ** m - q ** (-m)) / (q - q ** (-1))

    def qdim(lam, N):
        """SU(N) quantum dimension = the Ocneanu weight at z_N, up to a
        lambda-INDEPENDENT normalisation (which cannot change a span)."""
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

    print("\n[1] THE DEGREE, EXACTLY — symbolic over Q(q), no floats")
    print("-" * 78)
    print("    W_lam(q,z) is main's DERIVED weight (schurweyl/")
    print("    ocneanu_weight_general_n.py), imported here as a formula.")
    print("    Each cell's z-coefficient is q^(2j+1) - q^(2i+1), ZERO on the")
    print("    diagonal i == j, so a degree-m monomial needs m off-diagonal")
    print("    cells.  With d(lam) = Durfee square size:")
    print()
    print("        deg_z W_lam  =  n - d(lam)          <- asserted below")
    print()
    print(f"    {'n':>3} {'partitions':>11} {'max deg':>8} {'== n-1?':>8}")
    degs = {}
    for n in range(2, 7):
        mx = 0
        for s in partitions(n):
            d = sp.Poly(sp.expand(W(s)), _z).degree()
            assert d == n - durfee(s), (
                f"deg_z W_{s} = {d}, expected n - Durfee = {n - durfee(s)}")
            mx = max(mx, d)
        degs[n] = mx
        print(f"    {n:>3} {len(list(partitions(n))):>11} {mx:>8} "
              f"{str(mx == n - 1):>8}")
        assert mx == n - 1, "every partition has (0,0), so z^n always dies"
    print()
    print("    Every non-empty partition has the cell (0,0), so d >= 1 and the")
    print("    z^n term ALWAYS dies — which is why the naive bound n+1, from n")
    print("    affine factors, is never attained.")

    print("\n[2] THE RANK — bound is structural, equality is exact")
    print("-" * 78)
    print("    deg <= n-1  =>  W(z) = sum_{k=0}^{n-1} z^k c_k  =>  rank <= n.")
    print("    The coefficient system's rank is then EXACT over Q(q).")
    print()
    print(f"    {'n':>3} {'p(n)':>5} {'coeff vecs':>11} {'rank(exact)':>12} "
          f"{'== n?':>6} {'<= p(n)?':>9}")
    for n in range(2, 7):
        L = list(partitions(n))
        polys = [sp.Poly(sp.expand(W(s)), _z) for s in L]
        deg = max(p.degree() for p in polys)
        M = sp.Matrix([[p.coeff_monomial(_z ** k) for k in range(deg + 1)]
                       for p in polys])
        r = M.rank()
        print(f"    {n:>3} {len(L):>5} {deg + 1:>11} {r:>12} "
              f"{str(r == n):>6} {str(r <= len(L)):>9}")
        assert r == n, f"n={n}: exact rank {r} != n"
        assert r <= len(L), "rank cannot exceed the number of blocks"

    print("\n[3] NUMERICAL CORROBORATION at the proton pin, and saturation")
    print("-" * 78)
    print("    Independent route: the SU(N) quantum dimensions, which differ")
    print("    from W by a lambda-INDEPENDENT scalar and so span the same")
    print("    space.  Gram-Schmidt with a RELATIVE drop test (trap 3).")
    checked = 0
    for n in range(2, 8):
        for lam in partitions(n):
            for N in range(2, n + 3):
                assert (abs(qdim(lam, N)) < ZERO) == (len(lam) > N), (
                    f"row cap violated at {lam}, N={N}")
                checked += 1
    print(f"    row cap 'qdim == 0 iff rows > N' asserted on {checked} "
          f"(lambda, N) pairs, n = 2..7")

    def gs_basis(L, NS):
        basis = []
        for N in NS:
            v = [qdim(lam, N) for lam in L]
            n0 = mp.sqrt(sum(x ** 2 for x in v))
            if n0 == 0:
                continue
            v = [x / n0 for x in v]          # RELATIVE: normalise first
            for bb in basis:
                d = sum(v[i] * bb[i] for i in range(len(L)))
                for i in range(len(L)):
                    v[i] -= d * bb[i]
            nrm = mp.sqrt(sum(x ** 2 for x in v))
            if nrm > GS_REL:
                basis.append([x / nrm for x in v])
        return basis

    print()
    print(f"    {'n':>3} {'p(n)':>5} " +
          " ".join(f"{'N=2..' + str(h):>10}" for h in (12, 60, 300, 1000)))
    bases = {}
    for n in range(2, 8):
        L = list(partitions(n))
        rr = []
        for hi in (12, 60, 300, 1000):
            b = gs_basis(L, list(range(2, hi + 1)))
            rr.append(len(b))
            assert len(b) <= len(L), (
                f"n={n}, N<={hi}: rank {len(b)} > p(n)={len(L)} is impossible "
                f"— the drop test is admitting round-off (trap 3)")
            assert len(b) == n, f"n={n}, N<={hi}: rank {len(b)} != n"
            if hi == 60:
                bases[n] = (L, b)
        print(f"    {n:>3} {len(L):>5} " + " ".join(f"{x:>10}" for x in rr))
    print()
    print("    Stable across four nested ranges out to N = 1000, and asserted")
    print("    <= p(n) throughout — the invariant that catches trap 3.")

    print("\n[4] WHICH BLOCKS ARE INDIVIDUALLY RECOVERABLE")
    print("-" * 78)
    for n in (3, 6):
        L, basis = bases[n]
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
                "at n=3 the family is COMPLETE (p(3)=3=rank)")
            print("      => n=3 is COMPLETE: p(3) = 3 = rank, every block")
            print("         recoverable.  This is why an H_3 three-trace")
            print("         combination works — and why it does NOT")
            print("         generalise: from n=4 on, p(n) > n.")
        if n == 6:
            good = [lam for lam, r in resid.items() if r < IN_SPAN]
            assert good == [(6,), (1,) * 6], (
                f"expected only the two 1-dim blocks, got {good}")
            print(f"      => only {good} — the two ONE-DIMENSIONAL blocks.")
            print("         (4,2) is NOT recoverable and convention D SEES it,")
            print("         so the boundary is NOT the row cap.")
            for lam in L:
                dual = tuple(sorted((sum(1 for p in lam if p > j)
                                     for j in range(lam[0])), reverse=True))
                assert abs(resid[lam] - resid[dual]) < mp.mpf(10) ** -20, (
                    f"conjugate pair {lam}/{dual} must have equal residuals")
            print(f"      conjugation symmetry resid(lam') == resid(lam) "
                  f"asserted on all {len(L)} blocks.")

    print("\n[5] THE VERDICT")
    print("-" * 78)
    print("    block_transposition_lift_probe left open whether the")
    print("    trace-BLIND sector — where it located an UNBOUNDED channel")
    print("    asymmetry — is recoverable by subtraction.")
    print()
    print("    NO, and the reason is stronger than the question assumed.")
    print("    The weight is a polynomial of degree n - d(lam) in z, so the")
    print("    whole family spans rank n of a p(n)-dimensional character")
    print("    space, and only the two 1-dimensional blocks are individually")
    print("    recoverable.  (4,2) is trace-VISIBLE, carries the largest")
    print("    finite asymmetry found (ratio 5), and is still not isolable.")
    print()
    print("    So 'computable but not directly observable' does NOT hold via")
    print("    this family: the blind sector is not merely unseen, it is")
    print("    outside the span of every subtraction scheme built from Markov")
    print("    traces at any N.  Scope (a), narrowly scoped to that family —")
    print("    a non-trace functional (mu-bar_123 among them) is untouched,")
    print("    and that is where a closure would now have to come from.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
