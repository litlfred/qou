#!/usr/bin/env python3
"""isospin_channel_R_is_one_everywhere_probe — the isospin-channel asymmetry is
EXACTLY 1 in every representation at every dimension, by the minimal polynomial.
This is stronger than the `R <= 1` bound it supersedes, it is dimension-
independent, and it partly undercuts my own conclusion from an hour ago.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.  Follows
`regular_rep_modulus_spread_probe`, whose closing line asks whether the
per-channel `R` is even well-defined in a `d`-dimensional block.  It is, and
the answer is immediate.

## THE ARGUMENT — one line, and it needs no representation theory

Every Hecke generator satisfies the quadratic

    (sigma - q)(sigma + 1/q) = 0

so its **minimal polynomial divides** `(x - q)(x + 1/q)` in ANY representation.
Hence `spec(rho(sigma_i)) subset {q, -1/q}` at every dimension, with only the
multiplicities varying.

The isospin channels are the **spectral projectors of a single crossing**
(`docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`),
and a spectral projector of `sigma` carries exactly one of those two
eigenvalues -- whatever its rank.  So the eigenvalue criterion
`B_T = -alpha*log|lambda_T|` gives

    B(T=1) = -alpha*log q        B(T=0) = +alpha*log q
    R = |B(T=0)/B(T=1)| = 1      EXACTLY, in every block, at every dimension.

Nature requires `R ~ 33.7`.  **The single-crossing isospin criterion is
therefore excluded everywhere -- not merely on the bond-letter family, and not
merely in two dimensions.**

## 🛑 THIS PARTLY UNDERCUTS MY OWN CONCLUSION FROM AN HOUR AGO

`regular_rep_modulus_spread_probe` established, correctly, that the `R <= 1`
bound is a two-dimensional fact that does not extend -- `sum_i log|l_i| =
log|det|` is one equation on `d` unknowns.  I then wrote:

    "which is why the blind sector's high-dimensional blocks are not excluded
     by it"

That sentence is **true about the bound and misleading about the physics.**  A
*different and stronger* argument -- the one above -- excludes the
single-crossing isospin criterion in every block including every blind one, and
it does so without any determinant reasoning at all.  So "not excluded by the
`R <= 1` bound" is not "not excluded".

The optimism the sentence invites is what is being retracted; the statement
about the bound stands.

## AND IT DOES NOT CONTRADICT THE MEASURED SPREAD

`regular_rep_modulus_spread_probe` measured genuine log-modulus ratios up to
**5.0** in the 6-dimensional regular representation.  Both are true, because
they are about different operators:

  * `sigma` alone has spectrum `{q, -1/q}` -- two values, ratio 1.
  * a WORD `w` has a spread spectrum -- `s1^2 s2^2` gives `q^4, q^2, q^2,
    q^-2, q^-2, q^-4`.

**But a word's eigenprojectors are not `sigma`'s spectral projectors**, so the
spread is not available to the isospin channels as those are currently
defined.  Using it would require **re-identifying the channels** against the
word's own decomposition -- a different construction, and an open one.

## THE COMPLETION — every pair at EVERY separation, not just adjacent ones

The argument above covers an adjacent crossing `sigma_i`.  A pair at separation
`s > 1` exchanges via the **band generator**

    a_ij = (s_{j-1} ... s_{i+1}) s_i (s_{i+1}^-1 ... s_{j-1}^-1)

which is a **conjugate of `s_i` by construction**.  Verified two ways: it really
is the `(i,j)` transposition (checked in `S_4` for separations 1, 2 and 3), and
the `H_3` instance `a_02 = s2 s1 s2^-1` satisfies the Hecke quadratic exactly
(residual `5.584e-42`).  Conjugation preserves spectrum, so `a_ij` also has
spectrum `{q, -1/q}` and `R = 1` for that pair.

**So the entire pairwise-exchange picture has `R = 1`: every pair, at every
separation, in every representation.**  The channel asymmetry cannot come from
*any* single exchange.

## WHERE THIS LEAVES THE OPEN PROBLEM

    single crossing, any rep, any dim        R = 1 exactly    EXCLUDED
    pair exchange at ANY separation          R = 1 exactly    EXCLUDED
    sigma_i^k, any power                     R = 1 exactly    EXCLUDED
    far-commuting product sigma_i sigma_j    R = 1 exactly    EXCLUDED
    adjacent 2-crossing sigma_i sigma_j      R = 1            EXCLUDED
    >= 3 crossings, BOTH non-commuting gens  up to 5.0        channels UNDEFINED

**I named "a product `sigma_i sigma_j`" as a surviving candidate last pass.  It
does not survive.**  When `|i-j| >= 2` the generators commute, span
`H_2 (x) H_2`, and the product's spectrum is the PRODUCT SET
`{q,-1/q} x {q,-1/q} = {q^2, -1, -1, 1/q^2}` -- moduli `{q^2, 1, 1, 1/q^2}`,
whose two non-unit log-moduli are BOTH `2 log q`, so `R = 1` exactly.  Verified
on the exact `H_2 (x) H_2` model.  The adjacent 2-crossing product measures 1
too.

Measured minimum for **any** spread: both generators present **and** total
length `>= 3`.  Nothing of length 1 or 2 spreads, and no power of a single
generator spreads at any exponent.

**So the asymmetry requires an ADJACENT, MULTIPLY-BRAIDED object -- three or
more crossings on two non-commuting strands.**  Not a pair, not a product, not
a power: it needs the braid-relation region itself.  Its obstacle is then not a
bound but a definition -- which operator are the two isospin channels the
spectral projectors OF, once the object is not a pair exchange.  That is now
the gate.

Note how this composes with the all-pairs exclusion in
`allpairs_decay_turnover_exclusion_probe`: that ruled out summing pairwise
contributions with distance decay, and this rules out the pairwise
contributions *themselves* carrying the asymmetry.  The pairwise route is
closed from both ends.

## A METHOD NOTE WORTH MORE THAN THE RESULT

My first check of this was numerical: extract eigenvalues, test membership in
`{q, 1/q}` at `1e-25`.  It reported **False** -- and the mathematics is a
one-line proof.  The cause is that `polyroots` resolves a TRIPLE root to only
`~3e-15`, so the tolerance was tighter than the instrument.

The right instrument is the **exact matrix identity** `(M - qI)(M + I/q) = 0`,
which involves no root-finding and verifies to `5.6e-42`.  When a claim is
algebraic, test it algebraically; a numerical eigenvalue check can only ever be
as good as its worst-conditioned root, and a repeated root is the worst case.
This session has now been misled three times by root-finding artefacts
(`mp.eig` non-convergence, a `7.75e9` ratio from a repeated root, and this).

## What is NOT claimed

  * NOT that the framework's binding is wrong -- this excludes ONE criterion,
    the single-crossing eigenvalue reading, and says exactly where it fails.
  * NOT that multi-crossing constructions are excluded.  The opposite: they are
    the surviving row, blocked on a definition rather than a bound.
  * NOT a binding value.  Nothing wired, nothing fitted, no `alpha` needed --
    `R` is a ratio in which it cancels.

Scope **(b)**: the minimal-polynomial argument is a proof, and the exclusion it
gives is structural, not a numerical near-miss.

NO FLOAT64: mpmath `mpf` at 40 dps, 50-digit proton pin.  The central check is
exact matrix arithmetic with no root-finding.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

mp.mp.dps = 40
TOL = mp.mpf(10) ** -30
BASIS = ["e", "1", "2", "12", "21", "121"]


def fmt(x, n=10):
    return mp.nstr(x, n)


def gen(g, h):
    """Left multiplication by s_g on the 6-dim regular rep of H_3."""
    M = mp.zeros(6, 6)

    def add(dst, src, c):
        M[BASIS.index(dst), BASIS.index(src)] += c

    if g == 1:
        add("1", "e", 1); add("1", "1", h); add("e", "1", 1)
        add("12", "2", 1); add("12", "12", h); add("2", "12", 1)
        add("121", "21", 1); add("121", "121", h); add("21", "121", 1)
    else:
        add("2", "e", 1); add("2", "2", h); add("e", "2", 1)
        add("21", "1", 1); add("21", "21", h); add("1", "21", 1)
        add("121", "12", 1); add("121", "121", h); add("12", "121", 1)
    return M


def main() -> int:
    q = Q_MP
    h = q - 1 / q
    L1, L2 = gen(1, h), gen(2, h)
    I = mp.eye(6)

    def nrm(M):
        return max(abs(M[a, b]) for a in range(6) for b in range(6))

    print("=" * 78)
    print(" ISOSPIN-CHANNEL R = 1 EVERYWHERE — by the minimal polynomial")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}   1/q = {fmt(1 / q, 17)}   h = {fmt(h)}")

    print("\n[1] THE ARGUMENT")
    print("-" * 78)
    print("    Every Hecke generator satisfies  (sigma - q)(sigma + 1/q) = 0,")
    print("    so its MINIMAL POLYNOMIAL divides (x - q)(x + 1/q) in ANY")
    print("    representation.  Hence  spec(rho(sigma_i)) subset {q, -1/q}")
    print("    at every dimension -- only the multiplicities vary.")
    print("    The isospin channels are the SPECTRAL PROJECTORS of a single")
    print("    crossing, and each carries exactly one of those two eigenvalues,")
    print("    whatever its rank.  So")
    print("        B(T=1) = -alpha log q,   B(T=0) = +alpha log q,   R = 1")
    print("    EXACTLY, in every block, at every dimension.")

    print("\n[2] VERIFIED BY EXACT MATRIX IDENTITY — no root-finding")
    print("-" * 78)
    cases = [("s1", L1), ("s2", L2),
             ("s1 s2 s1^-1 (a conjugate)", L1 * L2 * (L1 - h * I)),
             ("s2 s1 s2^-1 (a conjugate)", L2 * L1 * (L2 - h * I))]
    for nm, M in cases:
        res = nrm((M - q * I) * (M + I / q))
        print(f"    (M - qI)(M + I/q) residual, {nm:26s} = {fmt(res, 4)}")
        assert res < TOL, f"{nm} must satisfy the Hecke quadratic exactly"
    print("    All conjugates too, since the isospin split is basis-independent.")

    print("\n[3] THE CONSEQUENCE, computed")
    print("-" * 78)
    lp, lm = q, -1 / q
    B1 = -mp.log(abs(lp))
    B0 = -mp.log(abs(lm))
    print(f"    lambda(T=1) = {fmt(lp, 14):>16}   B(T=1)/alpha = {fmt(B1, 14)}")
    print(f"    lambda(T=0) = {fmt(lm, 14):>16}   B(T=0)/alpha = {fmt(B0, 14)}")
    print(f"    B(T=1) + B(T=0) = {fmt(B1 + B0, 4)}   (exact antisymmetry)")
    R = abs(B0 / B1)
    print(f"    R = |B(T=0)/B(T=1)| = {fmt(R, 20)}")
    assert abs(B1 + B0) < TOL, "the two channels must be exactly antisymmetric"
    assert abs(R - 1) < TOL, "R must be exactly 1"
    need = AME_B_DEUTERON_MEV_VALIDATION / mp.mpf("0.066")   # the np 1S0 VIRTUAL STATE, the SAME np pair as the deuteron differing only in isospin.  CORRECTED from 0.1 (= pp/nn, a DIFFERENT PAIR), which conflated pair identity with isospin; see main 1d9d3500f5.
    print(f"    nature requires R ~ {fmt(need, 6)}")
    print(f"    shortfall factor    {fmt(need / R, 6)}")
    print("    => the single-crossing isospin criterion is EXCLUDED at every")
    print("       dimension, in every block, blind sector included.")

    print("\n[4] 🛑 THIS PARTLY UNDERCUTS MY OWN CONCLUSION FROM AN HOUR AGO")
    print("-" * 78)
    print("    regular_rep_modulus_spread_probe correctly showed the R <= 1")
    print("    bound is 2-dimensional and does not extend.  I then wrote:")
    print("      'which is why the blind sector's high-dimensional blocks are")
    print("       not excluded by it'")
    print("    TRUE about the bound, MISLEADING about the physics: the argument")
    print("    above excludes the single-crossing criterion in every block")
    print("    including every blind one, using no determinant reasoning at all.")
    print("    'Not excluded by THAT bound' is not 'not excluded'.")

    print("\n[5] AND IT DOES NOT CONTRADICT THE MEASURED SPREAD")
    print("-" * 78)
    w = L1 * L1 * L2 * L2
    print("    The same probe measured genuine log-modulus ratios up to 5.0.")
    print("    Both hold, because they are about DIFFERENT OPERATORS:")
    res_w = nrm((w - q * I) * (w + I / q))
    print(f"      sigma alone   : (M-qI)(M+I/q) = {fmt(nrm((L1 - q * I) * (L1 + I / q)), 4)}"
          "   -> spectrum {q, -1/q}")
    print(f"      the word s1^2 s2^2 : same product = {fmt(res_w, 6)}")
    print("        -- NOT zero, so the word does NOT satisfy the quadratic and")
    print("           its spectrum is genuinely spread (q^4, q^2, q^-2, q^-4).")
    assert res_w > mp.mpf("1e-3"), (
        "the word must NOT satisfy the generator's quadratic -- that is the point")
    print("    But a word's eigenprojectors are NOT sigma's spectral projectors,")
    print("    so that spread is unavailable to the isospin channels as defined.")

    print("\n[6] WHERE THIS LEAVES THE OPEN PROBLEM")
    print("-" * 78)
    print(f"    {'construction':34s} {'asymmetry':>14s}  {'status':>12s}")
    print(f"    {'single crossing, any dimension':34s} {'R = 1 exactly':>14s}  "
          f"{'EXCLUDED':>12s}")
    print(f"    {'bond-letter family, 2-dim':34s} {'R <= 1':>14s}  "
          f"{'EXCLUDED':>12s}")
    print(f"    {'multi-crossing word, d > 2':34s} {'up to 5.0':>14s}  "
          f"{'OPEN':>12s}")
    print()
    print("    Only the third survives, and its obstacle is NOT a bound: it is")
    print("    that nobody has said which operator the two isospin channels are")
    print("    the spectral projectors OF, once the object is a word rather")
    print("    than a crossing.  A definitional question, and now the gate.")

    print("\n[7] THE COMPLETION — every pair, at EVERY separation, is conjugate")
    print("-" * 78)
    print("    The argument so far covers a single ADJACENT crossing sigma_i.")
    print("    A pair at separation s > 1 exchanges via the BAND GENERATOR")
    print("        a_ij = (s_{j-1}...s_{i+1}) s_i (s_{i+1}^-1...s_{j-1}^-1)")
    print("    which is a CONJUGATE of s_i by construction -- so it carries the")
    print("    same spectrum {q, -1/q}, and R = 1 for that pair too.")
    print()

    def pmul(p, r):
        return [p[r[k]] for k in range(len(p))]

    def pinv(p):
        o = [0] * len(p)
        for i, v in enumerate(p):
            o[v] = i
        return o

    S4 = [[1, 0, 2, 3], [0, 2, 1, 3], [0, 1, 3, 2]]

    def band_perm(i, j):
        left = list(range(4))
        for k in range(j - 1, i, -1):
            left = pmul(left, S4[k])
        return pmul(pmul(left, S4[i]), pinv(left))

    print("    a_ij really is the (i,j) transposition -- checked in S_4:")
    for i, j in ((0, 1), (0, 2), (0, 3), (1, 3)):
        w = band_perm(i, j)
        tgt = list(range(4))
        tgt[i], tgt[j] = tgt[j], tgt[i]
        print(f"      a_{i}{j} -> {w}   transposition ({i},{j})?  {w == tgt}"
              f"   separation {j - i}")
        assert w == tgt, f"a_{i}{j} must be the (i,j) transposition"
    print()
    print("    and the H_3 band generator a_02 = s2 s1 s2^-1 satisfies the")
    print("    Hecke quadratic exactly (section [2], residual 5.584e-42), so")
    print("    its spectrum is {q, -1/q} like every other crossing's.")
    a02 = L2 * L1 * (L2 - h * I)
    assert nrm((a02 - q * I) * (a02 + I / q)) < TOL, (
        "the band generator must satisfy the quadratic")
    print()
    print("    => THE WHOLE PAIRWISE-EXCHANGE PICTURE HAS R = 1: every pair, at")
    print("       every separation, in every representation.  The channel")
    print("       asymmetry cannot come from ANY single exchange.")
    print("       Only a genuinely NON-CONJUGATE multi-crossing object escapes")
    print("       -- a product like sigma_i sigma_j, or the difference")
    print("       Delta_bind -- and those are not exchanges of a pair.")

    print("\n[8] THE FULL CATALOGUE — and it closes two more rows I had left open")
    print("-" * 78)
    print("    Last pass I named 'a product sigma_i sigma_j' as a surviving")
    print("    candidate.  It does NOT survive, and neither do several others.")
    print()
    print("    FAR-COMMUTING PRODUCT.  For |i-j| >= 2 the generators commute, so")
    print("    they span H_2 (x) H_2 and the product's spectrum is the PRODUCT")
    print("    SET {q,-1/q} x {q,-1/q} = {q^2, -1, -1, 1/q^2}.  Moduli")
    print("    {q^2, 1, 1, 1/q^2}: the two non-unit log-moduli are BOTH 2 log q,")
    print("    so R = 1 exactly.  Verified on the exact H_2 (x) H_2 model:")
    A2 = mp.matrix([[h, 1], [1, 0]])

    def kron(X, Y):
        n, m = X.rows, Y.rows
        M = mp.zeros(n * m, n * m)
        for a in range(n):
            for b in range(n):
                for c in range(m):
                    for d in range(m):
                        M[a * m + c, b * m + d] = X[a, b] * Y[c, d]
        return M
    I2 = mp.eye(2)
    Si, Sj = kron(A2, I2), kron(I2, A2)

    def nr4(M):
        return max(abs(M[a, b]) for a in range(M.rows) for b in range(M.cols))
    print(f"      [Si, Sj] commutator      = {fmt(nr4(Si * Sj - Sj * Si), 4)}")
    print(f"      Si quadratic residual    = {fmt(nr4(Si * Si - h * Si - mp.eye(4)), 4)}")
    assert nr4(Si * Sj - Sj * Si) < TOL, "far-commuting generators must commute"
    assert nr4(Si * Si - h * Si - mp.eye(4)) < TOL, "and satisfy the quadratic"
    ev = mp.eig(Si * Sj, left=False, right=False)
    mods = sorted((abs(x) for x in ev), reverse=True)
    print(f"      spectrum moduli of Si*Sj = " + ", ".join(fmt(m, 12) for m in mods))
    print(f"      q^2 = {fmt(q ** 2, 12)}   1/q^2 = {fmt(1 / q ** 2, 12)}")
    lg = [abs(mp.log(m)) for m in mods if abs(mp.log(m)) > mp.mpf("1e-8")]
    print(f"      non-unit log-moduli      = " + ", ".join(fmt(x, 10) for x in lg))
    print(f"      RATIO                    = {fmt(max(lg) / min(lg), 16)}")
    assert abs(max(lg) / min(lg) - 1) < mp.mpf("1e-12"), (
        "a far-commuting product must give R = 1")
    print()
    print("    So nucleons that are FAR APART -- whose generators commute --")
    print("    cannot carry the asymmetry even as a product.  Together with the")
    print("    band-generator result in [7], no separated pair contributes.")
    print()
    print("    THE CATALOGUE (all measured in this PR):")
    print(f"      {'object':44s} {'R':>10s}")
    for nm, val in (
            ("single crossing, any rep, any dimension", "1 exactly"),
            ("pair exchange at ANY separation (band gen)", "1 exactly"),
            ("sigma_i^k, any power k", "1 exactly"),
            ("far-commuting product sigma_i sigma_j", "1 exactly"),
            ("adjacent 2-crossing product sigma_i sigma_j", "1"),
            (">= 3 crossings, BOTH non-commuting gens", "up to 5.0")):
        print(f"      {nm:44s} {val:>10s}")
    print()
    print("    Measured minimum for any spread at all: BOTH generators present")
    print("    AND total length >= 3.  Nothing of length 1 or 2 spreads, and no")
    print("    power of a single generator spreads at any exponent.")
    print()
    print("    => THE ASYMMETRY REQUIRES AN ADJACENT, MULTIPLY-BRAIDED OBJECT:")
    print("       three or more crossings on two NON-COMMUTING strands.  Not a")
    print("       pair, not a product, not a power -- it needs the braid")
    print("       relation region itself.")

    print("\n[9] A METHOD NOTE WORTH MORE THAN THE RESULT")
    print("-" * 78)
    print("    My first check here was numerical -- extract eigenvalues, test")
    print("    membership in {q, 1/q} at 1e-25.  It reported FALSE, against a")
    print("    one-line proof.  Cause: polyroots resolves a TRIPLE root to only")
    print("    ~3e-15, so the tolerance was tighter than the instrument.")
    print("    The exact matrix identity verifies to 5.6e-42 and needs no roots.")
    print("    When a claim is algebraic, test it algebraically.  This session")
    print("    has now been misled three times by root-finding artefacts:")
    print("      mp.eig non-convergence; a 7.75e9 ratio from a repeated root;")
    print("      and this false negative.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
