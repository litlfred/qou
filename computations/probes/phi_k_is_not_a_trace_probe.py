#!/usr/bin/env python3
"""RETRACTION: Phi_k is not a trace, so the "TL constraint" I imposed is a scope error.

Bean `qou-oots`. Retracts sec 4 of the MERGED audit
`docs/audits/2026-09-05-which-n-the-nucleus-is-a-state-at.md`, which was mine.

WHAT I CLAIMED (merged, and wrong)
    "Any weight family consistent with the corpus's canonical trace must vanish
     on ker(H_n ->> TL_n), i.e. on every lambda with >= 3 rows. ... no candidate
     currently on the table satisfies the corpus's own consistency requirement."

WHY IT IS WRONG -- three ways, any one sufficient.

  (1) THE AUDIT ALREADY NAMES THIS AS THE ERROR IT EXISTS TO BLOCK.
      `2026-09-05-phi-k-weight-family.md` requirement R3 reads, in its own
      verdict table: "no Markov property is required -- Phi is NOT a trace ...
      it removes the reason to want y_lambda and BLOCKS A SCOPE ERROR."
      My constraint is precisely that scope error: it demands Phi_k's weight
      family be consistent with tr_M's.

  (2) Phi_k IS NOT LINEAR ON THE ALGEBRA. It is
          Phi_k(beta) = sum_{lambda : depth k} w_lambda * log(|chi^lambda(beta)|
                                                              * d_q(lambda))
      -- a log-weighted sum over one depth stratum. tr_M = sum_lambda y_lambda
      chi^lambda is a linear functional on H_n(q). A kernel argument about the
      second says nothing about the first: `ker(H_n ->> TL_n)` is a statement
      about which ALGEBRA ELEMENTS act as zero on V^(x)n, not about which
      PARTITIONS a separate functional may weight.

  (3) THE CONSTRAINT ANNIHILATES ITS OWN SUBJECT -- a reductio, and check A
      measures it. Imposing it forces w_lambda = 0 for every lambda with >= 3
      rows, i.e. on every stratum of depth >= 2 (depth k == k+1 rows), so
      Phi_k == 0 for ALL k >= 2 by the audit's own R1
      (`phi_eq_zero_of_weights_vanish`). A requirement that forbids the object
      being constructed is not a requirement.

AND THE CANDIDATE I OFFERED AS "THE ONE THAT CLEARS THE CONSTRAINT" FAILS R1.
    Sec 4 named the TL share `(f^lambda)^2/Catalan(n)` over `l(lambda) <= 2` as
    "the one candidate that clears the constraint". It clears it by being zero
    off the two-row cap -- which is exactly the property R1 retires `y_lambda`
    for. Check B: it carries ZERO mass on every stratum of depth >= 2, so it
    makes Phi_k == 0 there. My "solution" was the degenerate case, and it fails
    the audit's FIRST requirement.

WHAT SURVIVES from that audit, untouched by this retraction:
    sec 1  N = 2, with its four corpus witnesses -- the answer to the question
           the audit was written to settle.
    sec 2  the TL/Catalan arithmetic: sum_{l<=2}(f^l)^2 = Catalan(n) = dim TL_n,
           and n! - C_n reproducing all six recorded kernel dimensions.
    sec 3  the depth-off-by-one correction and the N=3-is-also-null measurement.
    sec 4c/4d (in the follow-on) the bare-iso defect and the two sourcing errors.
    Only the CONSTRAINT in sec 4, and the "fifth measure" it endorsed, are
    withdrawn.

WHAT THE OWNER RULED (2026-09-05, after that audit merged): "molien. do the two
    arm reporting" -- Molien canonical for Phi_k, `d_q^2/D^2` retained as a
    labelled comparison arm. Check C confirms Molien satisfies R1 on the strata
    my withdrawn constraint would have excluded it for. This probe does not
    re-open the family question; it removes a wrong argument against the
    ruling's answer.

Precision: exact integer combinatorics (math.factorial, integer hook products,
math.comb) and mpmath at 50 dps for the q-dependent family. No builtin-float
coercion, no numpy, no statistics. Emits no witness.

Run:
    PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python \
      python3 -u computations/probes/phi_k_is_not_a_trace_probe.py
"""

from __future__ import annotations

import math
import sys

import mpmath as mp

mp.mp.dps = 50

from qou_substrate.constants import q_at  # noqa: E402

Q = q_at(45)
EXACT = mp.mpf("1e-40")


def qint(k: int) -> mp.mpf:
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
    d = 1
    for (i, j) in cells(lam):
        d *= hook(lam, i, j)
    return math.factorial(sum(lam)) // d


def dq_hook(lam) -> mp.mpf:
    p = mp.mpf(1)
    for (i, j) in cells(lam):
        p *= qint(hook(lam, i, j))
    return qfact(sum(lam)) / p


def kappa(lam) -> int:
    return sum(j - i for (i, j) in cells(lam))


def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


def depth(lam) -> int:
    """The phi-k audit's stratification: depth k == k+1 rows."""
    return len(lam) - 1


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # ---- A. the constraint annihilates every stratum of depth >= 2 --------
    print("[A] the withdrawn constraint forces w_lambda = 0 on depth >= 2,")
    print("    so Phi_k == 0 for every k >= 2 by the audit's own R1.")
    print(f"    {'n':>2} {'strata present':>32}  {'depth>=2 strata killed':>24}")
    okA = True
    for n in (4, 6, 9):
        L = list(partitions(n))
        ds = sorted({depth(l) for l in L})
        killed = sorted({d for d in ds if d >= 2})
        okA &= len(killed) > 0
        print(f"    {n:>2} {str(ds):>32}  {str(killed):>24}")
    checks.append(("the constraint kills every depth>=2 stratum", okA,
                   "so Phi_k == 0 for k >= 2 -- a reductio"))

    # ---- B. the "fifth measure" I endorsed FAILS R1 -----------------------
    print("[B] the TL share (f^l)^2/Catalan(n) over l(lambda) <= 2:")
    print("    mass on each stratum -- it is ZERO exactly where Phi_k needs support")
    okB = True
    for n in (4, 6, 9):
        L = list(partitions(n))
        C = catalan(n)
        row = []
        for d in sorted({depth(l) for l in L}):
            m = mp.fsum(mp.mpf(f_lambda(l)) ** 2 for l in L
                        if depth(l) == d and len(l) <= 2) / mp.mpf(C)
            row.append(f"d{d}={mp.nstr(m, 4)}")
            if d >= 2 and m > EXACT:
                okB = False
        print(f"    n={n}: " + "  ".join(row))
    print("    -> zero on every depth >= 2 stratum: it FAILS R1, the same way y_lambda does")
    checks.append(("my endorsed 'fifth measure' fails R1", okB,
                   "zero on depth>=2, exactly what R1 retires y_lambda for"))

    # ---- C. Molien (the ruling's answer) SATISFIES R1 there ---------------
    print("[C] Molien f^l q^-kappa d_q^hook/[n]_q! -- the canonical family per the ruling")
    okC = True
    for n in (4, 6, 9):
        L = list(partitions(n))
        row = []
        for d in sorted({depth(l) for l in L}):
            m = mp.fsum(f_lambda(l) * Q ** (-kappa(l)) * dq_hook(l)
                        for l in L if depth(l) == d) / qfact(n)
            row.append(f"d{d}={mp.nstr(m, 4)}")
            if d >= 2 and not m > EXACT:
                okC = False
        print(f"    n={n}: " + "  ".join(row))
    print("    -> nonzero on every depth >= 2 stratum: it SATISFIES R1")
    checks.append(("Molien satisfies R1 on the strata I excluded it for", okC,
                   "nonzero on every depth>=2 stratum"))

    # ---- D. and it is a probability measure, so R2 is met too -------------
    print("[D] Molien total mass (R2: n-independent total mass)")
    okD = True
    for n in range(3, 10):
        tot = mp.fsum(f_lambda(l) * Q ** (-kappa(l)) * dq_hook(l)
                      for l in partitions(n)) / qfact(n)
        ok = abs(tot - 1) < EXACT
        okD &= ok
        print(f"    n={n}: {mp.nstr(tot, 20)} {'OK' if ok else 'FAIL'}")
    checks.append(("Molien total mass is exactly 1 at n=3..9", okD, "R2 met"))

    print()
    n_ok = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  ({detail})")
    print(f"\n{n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
