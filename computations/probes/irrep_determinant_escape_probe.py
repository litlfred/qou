#!/usr/bin/env python3
"""irrep_determinant_escape_probe — RETRACTS a scope-(b) claim I committed hours
ago in the same PR, and the retraction opens the escape the claim had closed.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Corrects
`channel_asymmetry_letter_family_bound_probe` section [6].

## THE RETRACTION

`channel_asymmetry_letter_family_bound_probe` states, as a scope-(b) SETTLED
result:

    "a bigger irrep does NOT escape it.  det rho(w) = +-1 for every braid word
     in every irrep, forcing R = 1 identically.  Three-strand H_3 is worse, not
     better -- verified on the 2-dim irrep built from the relations."

**The first sentence is FALSE.**  It was verified on exactly one irrep -- the
2-dim irrep of `H_3` -- and generalised from that single case.  In that irrep
the two eigenvalue multiplicities happen to be EQUAL, which is the only reason
`|det| = 1` there.  The check confirmed the claim on the one example that
could not distinguish it from its negation.

**Immediate counterexample, in any `H_n`.**  The two 1-dimensional
representations both satisfy the Hecke quadratic exactly:

    trivial:  sigma -> q       |det| = q     = 1.10998   > 1
    sign:     sigma -> -1/q    |det| = 1/q   = 0.90092   < 1

So `|det| < 1` is available, and `|det| < 1` was the ONE load-bearing condition
my own bound identified as the escape.  The blocking argument was wrong.

## THE CORRECT STATEMENT, and it is a formula rather than a constant

In the seminormal basis of irrep `lambda`, `sigma_i` acts diagonally on SYT
where `i, i+1` share a row (eigenvalue `q`) or share a column (eigenvalue
`-1/q`), and in 2-dim blocks with spectrum `{q, -1/q}` -- which contribute one
of each and cancel.  Writing

    m_plus (lambda,i) = #{SYT : i, i+1 in the same ROW}
    m_minus(lambda,i) = #{SYT : i, i+1 in the same COLUMN}

    ==>   |det rho_lambda(sigma_i)|  =  q^( m_plus - m_minus )

so `|det| = 1` **iff** `m_plus = m_minus`, and the escape condition `|det| < 1`
is exactly `m_minus > m_plus` -- more column-pairs than row-pairs, i.e. a
**column-heavy** partition.

## WHY THIS MATTERS BEYOND THE CORRECTION

Column-heavy means MANY ROWS.  And `main`'s `qou-cds1` Step 27 establishes that
under convention D the observable is the SU(2)/Temperley-Lieb trace, so
`omega_lambda` vanishes on every partition with **more than two rows** -- 588 of
720 dimensions at `3A = 6` are invisible.

So this probe asks whether the two sets coincide -- and **measured over every
partition of n = 2..8 by direct SYT enumeration, they do NOT.**  The relation is
a ONE-WAY implication:

    column-heavy  ==>  TL-blind        1 exception, and it is nameable
    TL-blind      =/=> column-heavy    14 counterexamples

**Every block that can escape the `R <= 1` bound is invisible to the observable;
most invisible blocks cannot escape it.  The escape set is the strictly smaller
one.**  That is weaker than "the same set", which is what I expected going in,
and it is the actual answer.

The single exception is `lambda = (1,1)` at `n = 2`: two rows, so TL-visible
only because "blind" means *more* than two rows, and column-heavy because its
one SYT puts 1 and 2 in a column.  A boundary case, not a structural
counterexample.

At `n = 6` -- the deuteron's own `3A`, where Step 27 measures -- there are
**5 escaping blocks**, `(3,1,1,1)`, `(2,2,2)`, `(2,2,1,1)`, `(2,1,1,1,1)`,
`(1^6)`, totalling 30 dimensions.  The sum of squared dimensions over all
blocks is `720 = 6!`, the same 720 Step 27 reports, reached from the Wedderburn
side -- so the two analyses are demonstrably about one object.

## AND IT DISCRIMINATES STEP 27's TWO BLOCKS

Step 27 reports the arc's first eigenphases *below* the required `0.0447444` in
two blind blocks, `(3,2,1)` and `(2,2,1,1)`, and treats them symmetrically (it
sums them).  On the determinant they are not symmetric:

    (3,2,1)     m+ = 8  m- = 8   |det| = 1          DET-LOCKED
    (2,2,1,1)   m+ = 3  m- = 6   |det| = q^-3       free

All `sigma_i` are conjugate, so a braid word `w` of writhe `e` has
`|det rho_lambda(w)| = |det rho_lambda(sigma)|^e`.  In `(3,2,1)` that is `1` for
**every** braid word at **every** writhe; in `(2,2,1,1)` it is `q^(-3e)`, free
to leave 1.

**🛑 RETRACTED: the clause "so the `R <= 1` argument closes that block
outright".**  The det-lock is real; the closure does not follow.  `R <= 1` was
derived for a 2x2, where `sum_i log|l_i| = log|det|` is one equation on TWO
unknowns and therefore pins their ratio.  In dimension `d` it is one equation
on `d` unknowns, leaving `d - 2` free directions -- and `dim (3,2,1) = 16`.
Demonstrated in the 6-dimensional regular representation of `H_3`: the word
`s1^2 s2^2` has `|det| = 1` and log-modulus ratio **exactly 2** (moduli
`q^4, q^2, q^2, q^-2, q^-2, q^-4`).  See `regular_rep_modulus_spread_probe`.
So `(3,2,1)` is **not** closed, and the det-lock separates the two blocks on a
weaker footing than stated here.

**🛑 Scope, and it is this argument's limit.**  Step 27's object is
`Delta_bind = beta_atom - beta_free`, a **difference** of braid words.  A
difference is not group-like and its determinant is unconstrained in *either*
block, so this does **not** discriminate Step 27's eigenphases directly.  What
it says is narrower: any mechanism built from braid words **alone** cannot break
bar symmetry in `(3,2,1)`, and can in `(2,2,1,1)`.  That is a statement about
which constructions are available, not about `Delta_bind`.

## What is NOT claimed

  * NOT that `R > 1` is achieved in an escaping block.  `|det| < 1` is
    NECESSARY for `R > 1`, not sufficient, and `R` as defined in the bound
    probe is a two-eigenvalue quantity whose extension to a `d`-dimensional
    block is a separate question this probe does not settle.
  * NOT that the blind sector supplies the 33.7:1 asymmetry.  It says the
    bound that EXCLUDED it does not apply there.  Removing an obstruction is
    not producing a mechanism.
  * NOT a binding value.  Nothing wired, nothing fitted.
  * The `R <= 1` bound itself is UNAFFECTED and stands: it is a statement about
    the bond-letter family `d in [-h, 0]` in the regular representation, where
    `|det| = 1 + s(h-s) >= 1` is computed directly and does not go through the
    irrep argument at all. Only the "bigger irrep cannot help" rider is
    retracted.

Scope **(a)** for the measurement; the determinant formula is exact algebra.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin; the combinatorics is
exact integer arithmetic and the only floating quantity is `q^(m+ - m-)`.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50
TOL = mp.mpf(10) ** -40


def fmt(x, n=10):
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


def syt(shape):
    """All standard Young tableaux of `shape`, as dict value -> (row, col)."""
    n = sum(shape)
    out = []

    def rec(pos, filled, rows):
        if pos > n:
            out.append(dict(filled))
            return
        for r in range(len(shape)):
            c = rows[r]
            if c >= shape[r]:
                continue
            if r > 0 and rows[r - 1] <= c:
                continue          # column-strict: cell above must be filled
            rows[r] += 1
            filled[pos] = (r, c)
            rec(pos + 1, filled, rows)
            rows[r] -= 1
            del filled[pos]

    rec(1, {}, [0] * len(shape))
    return out


def mplus_mminus(shape, i):
    """(#SYT with i,i+1 in same row, #SYT with i,i+1 in same column)."""
    mp_, mm_ = 0, 0
    for T in syt(shape):
        (r1, c1), (r2, c2) = T[i], T[i + 1]
        if r1 == r2:
            mp_ += 1
        elif c1 == c2:
            mm_ += 1
    return mp_, mm_


def main() -> int:
    q = Q_MP

    print("=" * 78)
    print(" IRREP DETERMINANT — retracting my own 'no irrep escapes' claim")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}")

    print("\n[1] THE COUNTEREXAMPLE, in any H_n")
    print("-" * 78)
    h = q - 1 / q
    for nm, s in (("trivial  sigma ->  q  ", q), ("sign     sigma -> -1/q", -1 / q)):
        quad = s * s - h * s - 1
        print(f"    {nm}: quadratic residual {fmt(abs(quad), 3):>8}   "
              f"|det| = {fmt(abs(s), 12):>14}   < 1 ?  {abs(s) < 1}")
        assert abs(quad) < TOL, "both 1-dim reps must satisfy the Hecke quadratic"
    assert abs(1 / q) < 1, "the sign rep has |det| < 1 -- the claim is refuted"
    print("    => 'det rho(w) = +-1 in every irrep' is FALSE.  The sign rep of")
    print("       ANY H_n has |det| = 1/q < 1, which is exactly the escape")
    print("       condition my own bound identified.  Retracted.")

    print("\n[2] WHY THE ORIGINAL CHECK PASSED — it could not have failed")
    print("-" * 78)
    mp3, mm3 = mplus_mminus((2, 1), 1)
    print(f"    H_3 2-dim irrep, lambda = (2,1): m+ = {mp3}, m- = {mm3}")
    print(f"    |det| = q^(m+ - m-) = q^{mp3 - mm3} = {fmt(q ** (mp3 - mm3), 12)}")
    assert mp3 == mm3, "the one irrep I checked has EQUAL multiplicities"
    print("    The multiplicities are EQUAL, so |det| = 1 there for a reason")
    print("    special to that block.  Verifying a general claim on the single")
    print("    example that cannot distinguish it from its negation is the")
    print("    whole defect; the arithmetic was never wrong.")

    print("\n[3] THE FORMULA, and the escape/blindness correlation")
    print("-" * 78)
    print("    |det rho_lambda(sigma_i)| = q^(m+ - m-),  so |det| < 1 iff the")
    print("    partition is COLUMN-HEAVY (m- > m+), i.e. has many ROWS.")
    print("    Step 27: convention D's SU(2)/TL trace is BLIND to every")
    print("    partition with MORE THAN TWO ROWS.  Are they the same set?")
    print()
    print(f"    {'n':>2} {'lambda':>16} {'rows':>5} {'dim':>5} {'m+':>4} {'m-':>4} "
          f"{'|det|':>13} {'esc':>4} {'blind':>6}")
    agree = disagree = 0
    esc_and_blind = esc_not_blind = blind_not_esc = 0
    for n in range(2, 9):
        for lam in partitions(n):
            T = syt(lam)
            mp_, mm_ = mplus_mminus(lam, 1)
            d = q ** (mp_ - mm_)
            escapes = mp_ < mm_                 # |det| < 1
            blind = len(lam) > 2                # TL-invisible under convention D
            if escapes == blind:
                agree += 1
            else:
                disagree += 1
            if escapes and blind:
                esc_and_blind += 1
            elif escapes:
                esc_not_blind += 1
            elif blind:
                blind_not_esc += 1
            if n <= 5 or escapes != blind:
                print(f"    {n:>2} {str(lam):>16} {len(lam):>5} {len(T):>5} "
                      f"{mp_:>4} {mm_:>4} {fmt(d, 9):>13} "
                      f"{('YES' if escapes else '-'):>4} "
                      f"{('YES' if blind else '-'):>6}")
    tot = agree + disagree
    print()
    print(f"    partitions of n = 2..8 examined : {tot}")
    print(f"      escape-condition == blindness : {agree}  ({100*agree//tot} %)")
    print(f"      disagree                      : {disagree}")
    print(f"        escaping but VISIBLE        : {esc_not_blind}")
    print(f"        blind but NOT escaping      : {blind_not_esc}")

    print("\n[3a] THE MEASURED ANSWER — they do NOT coincide; the implication")
    print("     runs ONE WAY, and the exception is nameable")
    print("-" * 78)
    exceptions, per_n = [], {}
    for n in range(2, 9):
        esc = []
        for lam in partitions(n):
            mp_, mm_ = mplus_mminus(lam, 1)
            if mp_ < mm_:
                esc.append(lam)
                if len(lam) <= 2:
                    exceptions.append((n, lam, mp_, mm_))
        per_n[n] = esc
    print("    ESCAPING (column-heavy, |det| < 1) partitions per n:")
    for n in range(2, 9):
        names = ", ".join(str(l) for l in per_n[n]) or "(none)"
        print(f"      n = {n}: {len(per_n[n]):>2}   {names}")
    print()
    print(f"    escaping but TL-VISIBLE (<= 2 rows): {len(exceptions)}")
    for n, lam, a, b in exceptions:
        print(f"      n = {n}  lambda = {lam}  m+ = {a}  m- = {b}  "
              f"rows = {len(lam)}")
    assert len(exceptions) == 1 and exceptions[0][1] == (1, 1), (
        "the single visible escaper must be lambda = (1,1)")
    print("    Exactly ONE, and it is lambda = (1,1) -- the 2-row sign")
    print("    partition, TL-visible only because 'blind' means MORE than two")
    print("    rows.  It is the n = 2 boundary case, not a structural")
    print("    counterexample to the pattern.")
    print()
    print("    So the honest statement is the ONE-WAY implication:")
    print("        column-heavy  ==>  TL-blind      (1 exception, n = 2)")
    print(f"        TL-blind      =/=> column-heavy  ({blind_not_esc} counterexamples)")
    print("    NOT 'the same set'.  Every block that can escape the R <= 1")
    print("    bound is invisible to the observable; most invisible blocks")
    print("    cannot escape it.  The escape set is the SMALLER one.")
    assert esc_not_blind == 1, "the one-way implication must have a single exception"
    assert blind_not_esc > 5, "and the converse must fail broadly"

    print("\n[3b] AT n = 6 — the deuteron's own 3A, where Step 27 measures")
    print("-" * 78)
    e6 = per_n[6]
    print(f"    escaping partitions of 6: {len(e6)}")
    for lam in e6:
        mp_, mm_ = mplus_mminus(lam, 1)
        print(f"      {str(lam):>18}  rows = {len(lam)}  dim = {len(syt(lam)):>3}  "
              f"m+ = {mp_:>3}  m- = {mm_:>3}  |det| = {fmt(q ** (mp_ - mm_), 10)}")
    dim_esc = sum(len(syt(l)) for l in e6)
    dim_tot = sum(len(syt(l)) ** 2 for l in partitions(6))
    print(f"    total dim over escaping blocks : {dim_esc}")
    print(f"    sum of squares over all blocks : {dim_tot}   (= 6! = 720 check)")
    assert dim_tot == 720, "Wedderburn: sum of squared dims must be 6! = 720"
    print("    The 720 here is the same 720 Step 27 reports, arrived at from")
    print("    the Wedderburn side -- so the two are talking about one object.")

    print("\n[3c] IT DISCRIMINATES STEP 27's TWO SMALL-EIGENPHASE BLOCKS")
    print("-" * 78)
    print("    Step 27 reports the arc's first eigenphases BELOW the required")
    print("    0.0447444, in two blind blocks, and treats them symmetrically")
    print("    (it sums them).  On the determinant they are NOT symmetric:")
    print()
    for lam in ((3, 2, 1), (2, 2, 1, 1)):
        mp_, mm_ = mplus_mminus(lam, 1)
        dd = q ** (mp_ - mm_)
        locked = abs(dd - 1) < TOL
        print(f"      {str(lam):>14}  rows = {len(lam)}  dim = {len(syt(lam)):>2}  "
              f"m+ = {mp_:>2}  m- = {mm_:>2}  |det| = {fmt(dd, 10):>13}"
              f"   {'DET-LOCKED' if locked else 'free'}")
    mp321, mm321 = mplus_mminus((3, 2, 1), 1)
    mp2211, mm2211 = mplus_mminus((2, 2, 1, 1), 1)
    assert mp321 == mm321, "(3,2,1) must be det-locked at 1"
    assert mp2211 < mm2211, "(2,2,1,1) must be column-heavy"
    print()
    print("    All sigma_i are conjugate in H_n, so every generator has the same")
    print("    determinant in a block, and for a BRAID WORD w of writhe e")
    print("        |det rho_lambda(w)| = |det rho_lambda(sigma)|^e.")
    print("    Hence in (3,2,1) EVERY braid word has |det| = 1 regardless of")
    print("    writhe, while in (2,2,1,1) |det| = q^(-3e), free to leave 1.")
    print()
    print("    🛑 RETRACTED, the clause that used to follow: 'so the R <= 1")
    print("    argument closes (3,2,1) outright'.  The det-lock is real; the")
    print("    CLOSURE does not follow.  R <= 1 was derived for a 2x2, where")
    print("        sum_i log|l_i| = log|det|")
    print("    is ONE equation on TWO unknowns and so pins their ratio.  In")
    print("    dimension d it is one equation on d unknowns, leaving d-2 free")
    print("    directions -- and dim (3,2,1) = 16.  Demonstrated in the 6-dim")
    print("    regular rep of H_3: the word s1^2 s2^2 has |det| = 1 and")
    print("    log-modulus ratio EXACTLY 2 (moduli q^4, q^2, q^2, q^-2, q^-2,")
    print("    q^-4).  See regular_rep_modulus_spread_probe.")
    print("    So (3,2,1) is NOT closed, and the det-lock discriminates the two")
    print("    blocks on a WEAKER footing than this section first claimed.")
    print()
    print("    🛑 SCOPE, and it is the limit of this argument.  Step 27's object")
    print("    is Delta_bind = beta_atom - beta_free, a DIFFERENCE of braid")
    print("    words, not a braid word.  A difference is not group-like and its")
    print("    determinant is unconstrained in EITHER block, so this does NOT")
    print("    discriminate Step 27's eigenphases directly.  What it does say:")
    print("    any mechanism built from braid words ALONE cannot break bar")
    print("    symmetry in (3,2,1), and can in (2,2,1,1).  That is a statement")
    print("    about the constructions available, not about Delta_bind.")

    print("\n[4] WHAT THIS SETTLES")
    print("-" * 78)
    print("  RETRACTED: 'no irrep escapes the R <= 1 bound'.  False; the sign")
    print("    rep of any H_n has |det| = 1/q < 1.  I verified a general claim")
    print("    on one example that could not falsify it.")
    print("  UNAFFECTED: the R <= 1 bound ITSELF stands.  It is about the")
    print("    bond-letter family d in [-h, 0] in the REGULAR representation,")
    print("    where |det| = 1 + s(h-s) >= 1 is computed directly and never")
    print("    goes through the irrep argument.  Only the rider is retracted.")
    print("  ESTABLISHED: |det rho_lambda(sigma_i)| = q^(m+ - m-) exactly, so")
    print("    the escape condition is a COMBINATORIAL property of the")
    print("    partition -- column-heaviness -- not a numerical accident.")
    print("  MEASURED, and weaker than I expected: escape and blindness do NOT")
    print("    coincide.  column-heavy ==> TL-blind (1 exception, lambda=(1,1)")
    print("    at n=2); TL-blind =/=> column-heavy (14 counterexamples).  The")
    print("    escape set is strictly the smaller one.  I went in expecting the")
    print("    two sets to be equal; they are not, and the one-way implication")
    print("    is the result.")
    print("  DISCRIMINATES: of Step 27's two small-eigenphase blocks, (3,2,1) is")
    print("    det-locked at 1 for every braid word at every writhe, while")
    print("    (2,2,1,1) is free at q^(-3e).  Step 27 treats them symmetrically")
    print("    (it sums their phases); on this invariant they are not.")
    print("  NOT CLAIMED: that R > 1 is achieved anywhere.  |det| < 1 is")
    print("    NECESSARY, not sufficient, and extending R to a d-dimensional")
    print("    block is a separate question.  Removing an obstruction is not")
    print("    producing a mechanism.")
    print("  NOT CLAIMED: that this discriminates Delta_bind.  That object is a")
    print("    DIFFERENCE of braid words, not group-like, so its determinant is")
    print("    unconstrained in either block.  The discrimination is over")
    print("    mechanisms built from braid words alone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
