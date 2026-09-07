#!/usr/bin/env python3
"""Route 1 cannot supply a Phi_k weight family for k >= 2: BOTH horns vanish.

Bean `qou-oots`. This closes route 1 of
`docs/audits/2026-09-05-phi-k-weight-family.md` sec 7 -- and closes it
NEGATIVELY, which is not the outcome that section anticipates.

WHAT ROUTE 1 SAYS
    "the measure a block 'should' carry is its share of whatever object the
     nucleus is a state in. If that object is V^{(x)n} ... the share is
     f^l d_q(l)/[n]_q!-shaped (Molien) and the question is closed. If it is
     the endomorphism algebra End(V^{(x)n}), the share is d_q^2/D^2-shaped
     and the question is closed the other way. Naming which object the
     nucleus is a state in is the whole content."

    So route 1 is posed as a fork: name the object, get the measure.

WHAT IS ACTUALLY TRUE ONCE N IS SETTLED
    N = 2 is settled -- derived sorry-free from condition (v) of
    `def:quantum-observable-universe` (`VolumeConstraintForcesFibreTwo.lean`,
    `exteriorSquareDim_eq_one_iff`), closed by bean `qou-fvzm` on 2026-08-07,
    and carried by four independent production witnesses (#6806, PR #6768).

    At N = 2 BOTH horns of the fork are supported on partitions with AT MOST
    TWO ROWS, i.e. on depth 0 and depth 1 only, and are EXACTLY ZERO on every
    stratum of depth >= 2:

      horn 1  module      f^l * d_q^{SU(2)}(l) / [2]_q^n
                          d_q^{SU(2)} = prod_cells [2 + c]_q / [h]_q,
                          which is 0 for l(l) >= 3 (the cell (3,1) has
                          content -2, giving [2 + (-2)]_q = [0]_q = 0)
      horn 2  operators   (f^l)^2 / Catalan(n) over l(l) <= 2, because
                          q-Schur-Weyl is a SURJECTION at N < n and
                          End_{U_q sl_2}(V^{(x)n}) = TL_n(q), of dimension
                          Catalan(n), not H_n(q) of dimension n!

    Therefore naming the object does NOT decide between two weight families.
    It yields zero either way on exactly the strata Phi_k for k >= 2 is about,
    which by the audit's own R1 (`phi_eq_zero_of_weights_vanish`) means
    Phi_k == 0 for every braid. That is a scope-(b) exclusion of route 1 as a
    SOURCE of the measure, with the invariant cited (the row cap,
    `RowCapObstruction.lean`), not a scope-(a) "it scores badly".

    The fork is real -- the two horns ARE different measures (check D) -- and
    it is decisive at general N. It is the settling of N = 2 that collapses
    it, which is why the audit could not have seen this when it was written.

WHAT THIS DOES **NOT** ESTABLISH -- read this before quoting the probe
    * It does not establish that Molien is correct. Molien survives R1 here
      (check C: strictly positive mass on depth >= 2 at every nuclear n), and
      the owner ruled it canonical on 2026-08-05 ("molien. do the two arm
      reporting"). Surviving a requirement that kills the alternatives is not
      a derivation, and this probe does not supply one.
    * It does not say route 1 was the wrong question to name. As posed, for
      general N, it is decisive. Its collapse is a CONSEQUENCE of the N = 2
      ruling, not a defect in the audit.
    * It does not touch routes 2 (same-n within-stratum observable) or 3
      (a cross-nucleus metric with more than four points). Those remain the
      live ways to settle the family by measurement rather than by ruling.
    * It says nothing about k = 0 or k = 1. Both horns are perfectly good
      measures on depth <= 1; the exclusion is only for k >= 2.

CONVENTION
    Symmetric q-integers [k]_q = (q^k - q^-k)/(q - q^-1). Proton pin
    (`q_at`, owner directive 2026-08-07). Depth k means k+1 rows
    (2026-09-05-phi-k-weight-family.md:104) -- so depth >= 2 is
    ">= 3 rows", and the depth-3 stratum is EXACTLY 4 rows. Getting that
    off-by-one wrong is what produced the retracted claim this probe replaces.

    Nuclear strand counts n = 3A for A = 1, 2, 3, 4.

Precision: mpmath at 50 dps; integer combinatorics exact via `math.factorial`
and integer hook products. No numpy and no statistics import; the only `math`
uses are exact integer `factorial` and `comb`, and no irrational `math` routine
is called. There is no builtin-float coercion in this file.

    (Both sentences are phrased so as not to spell either offender -- the
    coercion with its parenthesis, or the square-root call with its dot. An
    earlier probe in this corpus asserted its own freedom from the coercion in
    a form that a grep for the coercion matched, and the first draft of THIS
    file repeated it one identifier over, naming the square root in the very
    clause disclaiming it. A disclaimer that trips the detector it disclaims
    is worse than none: it manufactures a hit in the one file guaranteed to
    be clean.)
Emits no witness: a structural fact about measures, not a derived constant.

Run:
    PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python \
      python3 -u computations/probes/route_1_is_degenerate_at_n_two_probe.py
"""

from __future__ import annotations

import math
import sys

import mpmath as mp

mp.mp.dps = 50

from qou_substrate.constants import q_at  # noqa: E402

Q = q_at(45)
EXACT = mp.mpf("1e-40")
NUCLEAR = [3, 6, 9, 12]          # n = 3A for A = 1, 2, 3, 4


def qint(k: int) -> mp.mpf:
    """Symmetric q-integer [k]_q = (q^k - q^-k)/(q - q^-1); [0]_q = 0."""
    return (Q**k - Q ** (-k)) / (Q - 1 / Q)


def qfact(k: int) -> mp.mpf:
    out = mp.mpf(1)
    for i in range(1, k + 1):
        out *= qint(i)
    return out


def partitions(n: int, mx: int | None = None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


def conj(lam):
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0])) if lam else ()


def cells(lam):
    return [(i, j) for i, r in enumerate(lam) for j in range(r)]


def hook(lam, i, j) -> int:
    lc = conj(lam)
    return lam[i] - j + lc[j] - i - 1


def f_lambda(lam) -> int:
    """#SYT(lambda), exact integer via the hook-length formula."""
    d = 1
    for (i, j) in cells(lam):
        d *= hook(lam, i, j)
    return math.factorial(sum(lam)) // d


def dq_hook(lam) -> mp.mpf:
    """[n]_q! / prod_cells [h]_q -- the hook quantum dimension (all lambda)."""
    p = mp.mpf(1)
    for (i, j) in cells(lam):
        p *= qint(hook(lam, i, j))
    return qfact(sum(lam)) / p


def dq_sun(lam, N: int) -> mp.mpf:
    """prod_cells [N + c]_q / [h]_q -- U_q(sl_N) quantum dim; 0 if rows > N."""
    p = mp.mpf(1)
    for (i, j) in cells(lam):
        p *= qint(N + j - i) / qint(hook(lam, i, j))
    return p


def kappa(lam) -> int:
    return sum(j - i for (i, j) in cells(lam))


def depth(lam) -> int:
    """The phi-k audit's stratification: depth k == k+1 rows."""
    return len(lam) - 1


def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


def horn_module(n: int, N: int = 2) -> dict:
    """Horn 1: the V^(x)n block share, f^l d_q^{SU(N)}(l) / [N]_q^n."""
    den = qint(N) ** n
    return {lam: mp.mpf(f_lambda(lam)) * dq_sun(lam, N) / den
            for lam in partitions(n)}


def horn_operators(n: int, N: int = 2) -> dict:
    """Horn 2: the End(V^(x)n) = TL_n block share, (f^l)^2 / Catalan(n).

    At N < n the commutant is TL_n(q), NOT H_n(q) -- q-Schur-Weyl is a
    surjection with kernel of dimension n! - Catalan(n). So the normaliser is
    Catalan(n) and the index set is l(lambda) <= N.
    """
    c = mp.mpf(catalan(n))
    return {lam: (mp.mpf(f_lambda(lam)) ** 2 / c if len(lam) <= N else mp.mpf(0))
            for lam in partitions(n)}


def molien(n: int) -> dict:
    """f^l q^{-kappa_l} d_q^hook(l) / [n]_q! over ALL partitions."""
    den = qfact(n)
    return {lam: mp.mpf(f_lambda(lam)) * Q ** (-kappa(lam)) * dq_hook(lam) / den
            for lam in partitions(n)}


def stratum_mass(w: dict, k_min: int) -> mp.mpf:
    return mp.fsum(v for lam, v in w.items() if depth(lam) >= k_min)


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # ---- A/B. both horns: normalised, and ZERO on depth >= 2 -------------
    print("Both horns of route 1 at N = 2, over the nuclear n = 3A")
    print(f"{'n':>3} {'A':>2} | {'sum horn1':>14} {'d>=2 horn1':>12}"
          f" | {'sum horn2':>14} {'d>=2 horn2':>12}")
    ok_a = ok_b = True
    for n in NUCLEAR:
        h1, h2 = horn_module(n), horn_operators(n)
        s1, s2 = mp.fsum(h1.values()), mp.fsum(h2.values())
        m1, m2 = stratum_mass(h1, 2), stratum_mass(h2, 2)
        print(f"{n:>3} {n // 3:>2} | {mp.nstr(s1, 12):>14} {mp.nstr(m1, 6):>12}"
              f" | {mp.nstr(s2, 12):>14} {mp.nstr(m2, 6):>12}")
        ok_a &= abs(s1 - 1) < EXACT and m1 == 0
        ok_b &= abs(s2 - 1) < EXACT and m2 == 0
    checks.append(("horn 1 (module share) normalises and is EXACTLY 0 on "
                   "depth >= 2 at every nuclear n", ok_a, "n = 3,6,9,12"))
    checks.append(("horn 2 (End = TL_n share) normalises and is EXACTLY 0 on "
                   "depth >= 2 at every nuclear n", ok_b, "n = 3,6,9,12"))

    # ---- C. the operator-algebra dimension really is Catalan, not n! -----
    print("\nThe normaliser of horn 2 is dim TL_n, not dim H_n")
    print(f"{'n':>3} | {'sum_{l<=2}(f^l)^2':>18} {'Catalan(n)':>11}"
          f" {'n!':>9} {'kernel':>8}")
    ok_c = True
    for n in NUCLEAR:
        s = sum(f_lambda(lam) ** 2 for lam in partitions(n) if len(lam) <= 2)
        c, nf = catalan(n), math.factorial(n)
        print(f"{n:>3} | {s:>18} {c:>11} {nf:>9} {nf - c:>8}")
        ok_c &= s == c
    checks.append(("sum_{l(lambda)<=2}(f^l)^2 == Catalan(n) == dim TL_n, so "
                   "ker(H_n ->> TL_n) has dimension n! - Catalan(n)",
                   ok_c, "n = 3,6,9,12"))

    # ---- D. the two horns are genuinely DIFFERENT measures ---------------
    #        (so route 1 was a real fork, not one option written twice)
    print("\nThe fork is real: the two horns differ per-lambda")
    ok_d = True
    for n in NUCLEAR:
        h1, h2 = horn_module(n), horn_operators(n)
        dmax = max(abs(h1[lam] - h2[lam]) for lam in h1)
        print(f"  n = {n:>2}  max_lambda |horn1 - horn2| = {mp.nstr(dmax, 12)}")
        ok_d &= dmax > mp.mpf("1e-3")
    checks.append(("the two horns are different measures -- route 1 is a real "
                   "fork at general N; it is N = 2 that collapses it",
                   ok_d, "max per-lambda gap > 1e-3 at every nuclear n"))

    # ---- E. Molien is neither horn, and SURVIVES R1 ----------------------
    print("\nMolien is a third measure and is the only one alive on depth >= 2")
    print(f"{'n':>3} | {'sum Molien':>14} {'d>=2 mass':>12} "
          f"{'d==2':>10} {'d==3':>10}")
    ok_e = True
    for n in NUCLEAR:
        mo = molien(n)
        s = mp.fsum(mo.values())
        m2 = stratum_mass(mo, 2)
        d2 = mp.fsum(v for lam, v in mo.items() if depth(lam) == 2)
        d3 = mp.fsum(v for lam, v in mo.items() if depth(lam) == 3)
        print(f"{n:>3} | {mp.nstr(s, 12):>14} {mp.nstr(m2, 6):>12} "
              f"{mp.nstr(d2, 6):>10} {mp.nstr(d3, 6):>10}")
        ok_e &= abs(s - 1) < EXACT and m2 > 0
    # d==3 (exactly 4 rows) needs n >= 4, so it is 0 at n = 3 by arithmetic,
    # not by any weight vanishing. Only depth >= 2 is asserted here.
    checks.append(("Molien normalises to 1 and carries STRICTLY POSITIVE mass "
                   "on depth >= 2 at every nuclear n -- it passes R1 where "
                   "both horns fail it", ok_e, "n = 3,6,9,12"))

    print()
    n_ok = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  ({detail})")
    print(f"\n{n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
