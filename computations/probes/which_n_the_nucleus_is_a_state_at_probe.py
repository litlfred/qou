#!/usr/bin/env python3
"""SETTLED: the nucleus is a state at N = 2, and the question does not decide Phi_3.

Bean `qou-oots`. Answers the one item left open by
`docs/audits/2026-09-05-schur-weyl-share-is-a-third-measure.md` sec 8 --
"which N the nucleus is a state at" -- and RETRACTS that framing, which was
mine and was wrong.

THE ANSWER: N = 2.
    Not newly derived here. It follows from the convention-D owner ruling of
    2026-08-15, and the corpus records it four independent ways:

    (1) `wedderburn_jones_markov.y_lambda_at` calls `y_lambda_su_n(n, q, 2)`.
        The third argument IS N.
    (2) That function's docstring: "D's weights are the SU(2) quantum
        dimensions ... The defining difference is the row cap: y_lambda = 0
        for l(lambda) > 2".
    (3) `wedderburn_jones_markov.py:386-391`: the vanishing blocks "span
        ker(H_n -> TL_n), of dimension n! - Catalan(n) (1, 10, 78, 588, 4611,
        38890 at n = 3..8)", citing the sorry-free
        `QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`.
    (4) `docs/audits/2026-09-05-phi-k-weight-family.md:105` states it outright:
        "Production is N = 2 (convention D)."

    Check A verifies the arithmetic behind (3) independently: it confirms
    `sum_{l(lambda)<=2} (f^lambda)^2 == Catalan(n) == dim TL_n` at n = 3..8 and
    reproduces all six kernel dimensions. That closes the chain

        H_n(q)  --(dim n!)-->  TL_n(q)  ==  End_{U_q sl_2}(V^(x)n)

    so the corpus's canonical trace ALREADY lives on the N=2 module's
    endomorphism algebra. In sec 7's vocabulary, horn 1 is the corpus's actual
    position, and it is not merely asserted in prose -- the row cap is what
    makes the trace factor through it.

RETRACTION -- two errors, both mine, both merged in PR #6768.

    (R1) DEPTH IS OFF BY ONE. `2026-09-05-phi-k-weight-family.md:104` defines
         "Depth k means k+1 rows", so the depth-3 stratum is EXACTLY 4 ROWS.
         `schur_weyl_share_is_a_third_measure_probe.py:200` measures partitions
         with >= 3 rows and labels that "the depth-3 stratum". It is depth >= 2.
         The NUMBERS in that probe are right for what they measure; only the
         stratum name is wrong.

    (R2) THE CONCLUSION DRAWN FROM IT IS FALSE. That audit's sec 8 says route 1
         "turns on ONE thing: which N the nucleus is a state at", because the
         N=2 column was 0.0 and the N=3 column was nonzero. Measured on the
         REAL depth-3 stratum (check B), N=3 gives 0.0 as well -- both readings
         kill it, because depth 3 needs 4 rows and BOTH caps sit below 4. So
         "which N" does not decide Phi_3 at all.

         And the phi-k audit had already said so, at lines 107-108: "at N = 3
         the cap still lands on depth >= 3, so k = 3 is vacuous under y_lambda
         at both the mass (N = 2) and colour (N = 3) readings." I quoted the
         paragraph above it and did not carry the sentence that answered my own
         question.

WHAT SURVIVES from that audit, unaffected by either error:
    F1  Molien == Feray-Meliot q-Plancherel (independently re-derived in exact
        rationals by PR #6771, which is the stronger derivation).
    F2  The V^(x)n share is a THIRD measure, distinct from Molien -- the
        distinctness is per-lambda at N=3, n=6 and does not depend on depth
        labelling at all.
    F4  Horn 2 names the operator algebra, whose share is classical Plancherel.
        Check C sharpens this: at N=2 that share is the TL one,
        (f^lambda)^2 / Catalan(n) over l(lambda) <= 2 -- a FIFTH measure, and
        the correctly-scoped version of the candidate sec 7 omitted.

WHAT IS STILL OPEN, stated without the wrong narrowing:
    Which weight family Phi_k should use. Route 1 does not settle it. What
    route 1 DOES establish is a constraint neither survivor meets: any measure
    consistent with the corpus's canonical trace must vanish on
    ker(H_n -> TL_n), i.e. on every lambda with >= 3 rows. Molien (check B,
    0.074..0.44 on depth 3) and classical Plancherel unrestricted
    (0.042..0.46) both put mass there; `d_q^2/D^2` does too unless D^2 is
    restricted to <= 2 rows. So route 1 CONSTRAINS the family without
    selecting one, and Phi_3 is vacuous under every N=2-consistent choice.

    That is a scope-(b) structural exclusion of Phi_3 as an observable -- not
    "Phi_3 performs badly" but "the stratum it integrates over is in the
    kernel of the map to the state space" -- resting on a sorry-free Lean
    theorem, not on these numbers.

    NOT established: that Phi_1 or Phi_2 are vacuous. Depth 0 and 1 are 1- and
    2-row, inside the cap, and check D shows they carry essentially all the
    N=2 mass. The exclusion is specific to k >= 2.

Precision: mpmath at 50 dps; exact integer combinatorics via math.factorial and
integer hook products; Catalan by math.comb. No builtin-float coercion, no
numpy, no statistics. Emits no witness (a structural fact about the corpus's
own convention, not a derived physical number).

Run:
    PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python \
      python3 -u computations/probes/which_n_the_nucleus_is_a_state_at_probe.py
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


def dq_sun(lam, N: int) -> mp.mpf:
    """prod [N + c]_q / [h]_q -- U_q(sl_N) quantum dim; 0 when rows > N."""
    p = mp.mpf(1)
    for (i, j) in cells(lam):
        p *= qint(N + j - i) / qint(hook(lam, i, j))
    return p


def kappa(lam) -> int:
    return sum(j - i for (i, j) in cells(lam))


def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


def depth(lam) -> int:
    """The phi-k audit's stratification: depth k == k+1 rows."""
    return len(lam) - 1


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # ---- A. the TL chain that pins N = 2 --------------------------------
    print("[A] N=2 <-> TL_n:  sum_{l(lam)<=2} (f^lam)^2 == Catalan(n) == dim TL_n")
    print("    and  n! - Catalan(n)  ==  dim ker(H_n -> TL_n)  (the corpus's own figures)")
    KERNEL_PER_CORPUS = {3: 1, 4: 10, 5: 78, 6: 588, 7: 4611, 8: 38890}
    okA1 = okA2 = True
    for n in range(3, 9):
        s = sum(f_lambda(l) ** 2 for l in partitions(n) if len(l) <= 2)
        c = catalan(n)
        ker = math.factorial(n) - c
        okA1 &= s == c
        okA2 &= ker == KERNEL_PER_CORPUS[n]
        print(f"    n={n}  sum={s:<6} Catalan={c:<6} {'OK' if s == c else 'FAIL'}"
              f"   n!-C={ker:<6} corpus={KERNEL_PER_CORPUS[n]:<6}"
              f" {'OK' if ker == KERNEL_PER_CORPUS[n] else 'FAIL'}")
    checks.append(("2-row blocks ARE TL_n (dim = Catalan)", okA1, "n=3..8"))
    checks.append(("kernel dims match the corpus's own figures", okA2,
                   "1,10,78,588,4611,38890"))

    # ---- B. THE RETRACTION: depth 3 is 4 rows, and N=3 kills it too -----
    print("[B] the REAL depth-3 stratum (depth k == k+1 rows, so EXACTLY 4 rows)")
    print(f"    {'n':>2} {'#d3':>4} {'SW N=2':>8} {'SW N=3':>8} {'SW N=4':>11}"
          f" {'Molien':>11} {'Planch':>11}")
    d3_n2: list[mp.mpf] = []
    d3_n3: list[mp.mpf] = []
    d3_n4: list[mp.mpf] = []
    d3_mol: list[mp.mpf] = []
    for n in range(4, 10):
        L = list(partitions(n))
        D3 = [l for l in L if depth(l) == 3]
        sw = {N: mp.fsum(f_lambda(l) * dq_sun(l, N) for l in D3) / qint(N) ** n
              for N in (2, 3, 4)}
        mo = mp.fsum(f_lambda(l) * Q ** (-kappa(l)) * dq_hook(l) for l in D3) / qfact(n)
        pl = mp.fsum(mp.mpf(f_lambda(l)) ** 2 for l in D3) / mp.mpf(math.factorial(n))
        d3_n2.append(sw[2]); d3_n3.append(sw[3]); d3_n4.append(sw[4]); d3_mol.append(mo)
        print(f"    {n:>2} {len(D3):>4} {mp.nstr(sw[2],4):>8} {mp.nstr(sw[3],4):>8}"
              f" {mp.nstr(sw[4],7):>11} {mp.nstr(mo,7):>11} {mp.nstr(pl,7):>11}")
    okB1 = all(v < EXACT for v in d3_n2)
    okB2 = all(v < EXACT for v in d3_n3)
    okB3 = all(v > EXACT for v in d3_n4)
    okB4 = all(v > EXACT for v in d3_mol)
    print(f"    -> N=2 zero on depth 3:            {okB1}")
    print(f"    -> N=3 zero on depth 3 TOO:        {okB2}   <-- retracts 'which N decides it'")
    print(f"    -> N=4 nonzero (the cap is at 4):  {okB3}")
    checks.append(("depth-3 is zero at N=2", okB1, "exactly 4 rows"))
    checks.append(("depth-3 is zero at N=3 AS WELL", okB2,
                   "so which-N does NOT decide Phi_3"))
    checks.append(("depth-3 is nonzero at N=4", okB3, "cap sits at 4 rows"))
    checks.append(("Molien puts mass on depth 3", okB4,
                   "so it violates the TL constraint"))

    # n=3 has NO depth-3 stratum at all
    n3_d3 = [l for l in partitions(3) if depth(l) == 3]
    print(f"    note: at n=3 (proton, A=1) the depth-3 stratum is EMPTY: {n3_d3}")
    checks.append(("depth-3 stratum is empty at n=3", len(n3_d3) == 0,
                   "no 4-row partition of 3"))

    # ---- C. the correctly-scoped horn-2 share ---------------------------
    print("[C] horn 2, scoped: block share of End_{U_q sl_2}(V^(x)n) == TL_n")
    okC = True
    for n in (4, 6, 8):
        L2 = [l for l in partitions(n) if len(l) <= 2]
        tot = mp.fsum(mp.mpf(f_lambda(l)) ** 2 for l in L2) / mp.mpf(catalan(n))
        ok = abs(tot - 1) < EXACT
        okC &= ok
        print(f"    n={n}  sum (f^lam)^2/Catalan over <=2 rows = {mp.nstr(tot,20)} {'OK' if ok else 'FAIL'}")
    checks.append(("TL share is a normalised measure", okC,
                   "(f^lam)^2/Catalan(n), <=2 rows"))

    # ---- D. the exclusion is specific to k >= 2 -------------------------
    print("[D] where the N=2 mass actually lives (depth 0 and 1 only)")
    okD = True
    for n in (3, 6, 9):
        L = list(partitions(n))
        low = mp.fsum(f_lambda(l) * dq_sun(l, 2) for l in L if depth(l) <= 1) / qint(2) ** n
        ok = abs(low - 1) < EXACT
        okD &= ok
        print(f"    n={n}  N=2 mass on depth<=1 = {mp.nstr(low,20)} {'OK' if ok else 'FAIL'}")
    checks.append(("N=2 mass is entirely on depth 0-1", okD,
                   "so Phi_1/Phi_2 are NOT excluded"))

    print()
    n_ok = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  ({detail})")
    print(f"\n{n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
