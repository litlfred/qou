#!/usr/bin/env python3
"""Route 1 of the Phi_k weight question: the V^(x)n share is a THIRD measure.

Bean `qou-oots`. Audit `docs/audits/2026-09-05-phi-k-weight-family.md` sec 7
names the decisive route and calls it structural, not numerical:

    "the measure a block 'should' carry is its share of whatever object the
     nucleus is a state in. If that object is V^{tensor n} with V the
     U_q(sl_N) fundamental, the share is f^lambda d_q(lambda)/[n]_q!-shaped
     (Molien) and the question is closed."

This probe measures that share instead of describing it, and the parenthesis
is where it breaks. Three findings, in order of how much they cost the route:

  (F1) The Molien family IS a probability measure -- sum = 1 exactly at
       n = 2..7 (check A). The audit's sec 2 identification of it with
       Feray-Meliot's q-Plancherel M_{n,Q} is CONFIRMED here independently,
       both numerically and by the change of variables below.

  (F2) But the Molien family is NOT the V^(x)n share. Both are
       "f^lambda times one dimension over one normaliser", so both are
       Molien-SHAPED -- and they are different measures:

           V^(x)n share  :  f^l * d_q^{SU(N)}(l) / [N]_q^n,  l with <= N rows
                            d_q^{SU(N)}(l) = prod_cells [N + c]_q / [h]_q
           Molien family :  f^l * q^{-kappa_l} * d_q^{hook}(l) / [n]_q!,  ALL l
                            d_q^{hook}(l)   = [n]_q! / prod_cells [h]_q

       Each sums to 1 on its own index set (checks A and B), so neither is a
       mis-normalisation of the other. Same shape, different object.

  (F3) At N = 2 the V^(x)n share is EXACTLY ZERO on every partition with 3 or
       more rows (check C), because [N + c]_q = [0]_q = 0 at the cell of
       content -N. That measurement stands.

       *** CORRECTED 2026-09-05 -- THE STRATUM NAME AND THE CONCLUSION WERE
       *** BOTH WRONG, AND BOTH WERE MINE. See
       *** computations/probes/which_n_the_nucleus_is_a_state_at_probe.py.
       ***
       *** (a) ">= 3 rows" is NOT the depth-3 stratum. The phi-k audit defines
       ***     "depth k means k+1 rows" (2026-09-05-phi-k-weight-family.md:104),
       ***     so >= 3 rows is depth >= 2, and depth 3 is EXACTLY 4 rows. The
       ***     numbers below are correct for what they measure; only the name
       ***     was wrong.
       *** (b) Because of (a), the claim that route 1 "survives only at N >= 3"
       ***     is FALSE. On the real depth-3 stratum, N = 3 gives 0.0 as well --
       ***     both caps sit below 4 rows. Which N the nucleus is a state at
       ***     does NOT decide Phi_3. The phi-k audit had already said this at
       ***     its lines 107-108; I quoted the paragraph above it and did not
       ***     carry the sentence that answered the question.
       ***
       *** N is settled independently: it is 2, by the convention-D ruling of
       *** 2026-08-15. The >= 3-row blocks are ker(H_n -> TL_n) and
       *** TL_n = End_{U_q sl_2}(V^(x)n), so the corpus's canonical trace
       *** already factors through the N=2 module's endomorphism algebra.

WHY THE ALGEBRA IS THE SAME OBJECT, NOT A COMPETING ONE
    The audit's sec 7 offers `End(V^(x)n)` as the other horn. Under q-Schur-Weyl
    `H_n(q) = End_{U_q sl_N}(V^(x)n)` (Jimbo) that is not a rival state space --
    it is the OPERATOR ALGEBRA of the same pair, and the corpus says so
    (`QOU/MassEndomorphism/MassLeftMulEndomorphism.lean`, `QSchurWeyl.lean`).
    Its block share is dim M_{f^l} / dim H_n(q) = (f^l)^2 / n!, the CLASSICAL
    Plancherel measure -- a candidate the audit does not list.

    *** CORRECTED 2026-09-05: THAT IS THE WRONG ALGEBRA AT N = 2. q-Schur-Weyl
    *** is an isomorphism only for N >= n; at N = 2, n = 3A the map
    *** H_n(q) ->> End_{U_q sl_2}(V^(x)n) = TL_n(q) is SURJECTIVE with kernel of
    *** dimension n! - Catalan(n). So the operator algebra of the pair is TL_n
    *** (dim Catalan(n)), and its block share is (f^l)^2 / Catalan(n) over
    *** l(lambda) <= 2 -- NOT (f^l)^2 / n!. Check D below therefore measures a
    *** real and normalised measure (Burnside), but NOT the share of the object
    *** horn 2 names. The corrected share is check C of
    *** which_n_the_nucleus_is_a_state_at_probe.py. Feray-Meliot
    sec 6.1 (`library/arxiv-1001.2180v2`, the paper the audit already cites for
    sec 2) states exactly this pairing in the literature's own vocabulary:
    the module gives the "Schur-Weyl measure", the regular representation
    gives Plancherel. Check D measures that third candidate's total mass, which
    is 1 at every n by Burnside -- and is q-INDEPENDENT, which is its own
    problem for a substrate observable.

    So `d_q^2/D^2` is the share of NEITHER: it is the Reshetikhin-Turaev /
    Verlinde weight of the S^2 x S^1 Hilbert space, a third object again
    (`docs/audits/2026-06-20-keystone-wlambda-beasley-witten-localization.md`).

SCOPE -- stated tightly
    Establishes: the three measures are distinct and each is normalised on its
    own index set; the N=2 module share is null on depth >= 3; the audit's
    sec 7 horn 1 conflates "Molien-shaped" with "is the Molien family".
    Does NOT establish: which family Phi_k should use. Route 1 is narrowed and
    partly excluded, not completed. In particular this probe does NOT claim
    the corpus's N is 2 for the colour reading -- `schur-weyl-mass-decomposition`
    keeps rows beyond 3, and the depth-3 channel is elsewhere read at N = 3,
    where check C shows the share is nonzero (0.0355 / 0.3068 / 0.6023 at
    n = 3 / 6 / 9). Which N the nucleus is a state at is the remaining
    structural question, and it is now the ONLY thing route 1 turns on.

CONVENTION
    Symmetric q-integers throughout, [k]_q = (q^k - q^-k)/(q - q^-1). The
    corpus's Q = q^2 bridge to Feray-Meliot's non-symmetric [k]_Q =
    (Q^k - 1)/(Q - 1) is [k]_Q = q^{k-1} [k]_q, whence
        M_{n,Q}(l) = Q^{b(l)} f^l / prod [h]_Q
                   = q^{2n(l)} f^l / (q^{n(l)+n(l')} prod [h]_q)
                   = f^l q^{-kappa_l} / prod [h]_q
    using sum_cells h = n(l) + n(l') + n and kappa_l = n(l') - n(l). That is
    the Molien family, which is why check A returns 1.

Precision: mpmath at 50 dps; integer combinatorics exact via `math.factorial`
and integer hook products. No builtin-float coercion anywhere, no numpy, no
statistics. Emits no witness (a structural fact about measures, not a derived
physical constant).

Run:
    PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python \
      python3 -u computations/probes/schur_weyl_share_is_a_third_measure_probe.py
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 50

from qou_substrate.constants import q_at  # noqa: E402

Q = q_at(45)
EXACT = mp.mpf("1e-40")


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


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # ---- A. Molien (hook d_q, all lambda) is a probability measure --------
    print("[A] Molien  f^l q^-kappa d_q^hook / [n]_q!   over ALL partitions")
    okA = True
    for n in range(2, 8):
        L = list(partitions(n))
        tot = mp.fsum(f_lambda(l) * Q ** (-kappa(l)) * dq_hook(l) for l in L) / qfact(n)
        ok = abs(tot - 1) < EXACT
        okA &= ok
        print(f"    n={n}  #lambda={len(L):3d}  sum = {mp.nstr(tot, 22)}  {'OK' if ok else 'NOT 1'}")
    checks.append(("Molien family is normalised (n=2..7)", okA, "sum == 1"))

    # ---- B. the SU(N) module share is ALSO a probability measure ---------
    print("[B] V^(x)n share  f^l d_q^SU(N) / [N]_q^n   over lambda with <= N rows")
    okB = True
    for N in (2, 3):
        for n in (3, 6, 9):
            L = list(partitions(n))
            tot = mp.fsum(f_lambda(l) * dq_sun(l, N) for l in L) / qint(N) ** n
            ok = abs(tot - 1) < EXACT
            okB &= ok
            print(f"    N={N} n={n}  sum = {mp.nstr(tot, 22)}  {'OK' if ok else 'NOT 1'}")
    checks.append(("V^(x)n share is normalised too", okB, "sum == 1"))

    # ---- C. THE ONE THAT BITES: N=2 share is null on depth >= 3 ----------
    print("[C] mass on partitions with >= 3 rows == DEPTH >= 2")
    print("    (NOT the depth-3 stratum -- depth k means k+1 rows, so depth 3 is 4 rows;")
    print("     see which_n_the_nucleus_is_a_state_at_probe.py, which corrects this)")
    rows3 = {}
    for N in (2, 3):
        for n in (3, 6, 9):
            L = list(partitions(n))
            m = mp.fsum(f_lambda(l) * dq_sun(l, N) for l in L if len(l) >= 3) / qint(N) ** n
            rows3[(N, n)] = m
            print(f"    V^(x)n share  N={N} n={n}: {mp.nstr(m, 12)}")
    for n in (3, 6, 9):
        L = list(partitions(n))
        m = mp.fsum(f_lambda(l) * Q ** (-kappa(l)) * dq_hook(l) for l in L if len(l) >= 3) / qfact(n)
        print(f"    Molien             n={n}: {mp.nstr(m, 12)}")
    okC1 = all(rows3[(2, n)] < EXACT for n in (3, 6, 9))
    okC2 = all(rows3[(3, n)] > mp.mpf("0.03") for n in (3, 6, 9))
    print(f"    -> N=2 share is EXACTLY zero on depth>=3: {okC1}")
    print(f"    -> N=3 share is nonzero there:            {okC2}")
    checks.append(("N=2 module share is null on >=3 rows (depth>=2)", okC1,
                   "row cap [N+c]_q = [0]_q = 0"))
    checks.append(("N=3 module share is NOT null on >=3 rows", okC2,
                   f"{mp.nstr(rows3[(3,6)], 8)} at n=6"))

    # ---- D. the audit's missing third candidate: classical Plancherel ----
    print("[D] classical Plancherel (f^l)^2/n! -- the share of H_n, which at N=2")
    print("    is NOT the operator algebra of the pair (that is TL_n, dim Catalan(n));")
    print("    see which_n_the_nucleus_is_a_state_at_probe.py check C for the right one")
    okD = True
    for n in (3, 6, 9):
        L = list(partitions(n))
        # Burnside is an identity in Z: sum_lambda (f^lambda)^2 == n! exactly.
        # `f_lambda` is annotated `-> int` and `math.factorial` returns an int,
        # so BOTH sides are exact integers and the equality can be decided
        # exactly. The previous form pushed them through `mp.fsum`/`mp.mpf` and
        # then compared to 1 within a 1e-40 tolerance -- weaker than the
        # arithmetic allows, and it made an exact statement look approximate.
        num = sum(f_lambda(l) ** 2 for l in L)
        den = math.factorial(n)
        ok = (num == den)
        okD &= ok
        print(f"    n={n}  sum = {num}/{den} = "
              f"{'1 (exact)' if ok else Fraction(num, den)}"
              f"  (Burnside; q-INDEPENDENT)")
    checks.append(("classical Plancherel is normalised, and q-free", okD,
                   "sum == 1 by Burnside"))

    # ---- E. the three are pairwise DIFFERENT measures ---------------------
    print("[E] pairwise distinctness at N=3, n=6 (per-lambda, first mismatch)")
    n, N = 6, 3
    L = [l for l in partitions(n)]
    sw = {l: f_lambda(l) * dq_sun(l, N) / qint(N) ** n for l in L}
    mo = {l: f_lambda(l) * Q ** (-kappa(l)) * dq_hook(l) / qfact(n) for l in L}
    cl = {l: mp.mpf(f_lambda(l)) ** 2 / mp.mpf(math.factorial(n)) for l in L}
    diff_sw_mo = max(abs(sw[l] - mo[l]) for l in L)
    diff_sw_cl = max(abs(sw[l] - cl[l]) for l in L)
    diff_mo_cl = max(abs(mo[l] - cl[l]) for l in L)
    print(f"    max|share - Molien|    = {mp.nstr(diff_sw_mo, 10)}")
    print(f"    max|share - Plancherel|= {mp.nstr(diff_sw_cl, 10)}")
    print(f"    max|Molien - Plancherel|= {mp.nstr(diff_mo_cl, 10)}")
    okE = min(diff_sw_mo, diff_sw_cl, diff_mo_cl) > mp.mpf("1e-6")
    checks.append(("all three are distinct measures", okE,
                   f"min pairwise max-dev {mp.nstr(min(diff_sw_mo, diff_sw_cl, diff_mo_cl), 6)}"))

    print()
    n_ok = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  ({detail})")
    print(f"\n{n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
