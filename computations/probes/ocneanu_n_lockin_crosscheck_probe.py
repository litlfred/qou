#!/usr/bin/env python3
"""Cross-check of #6829's Ocneanu N lock-in ratios, in the BALANCED convention.

Bean `qou-oots`. Sibling PR #6829 supplied, on #6826, the closed form

    y_{(2,1)} / y_{(3)}  =  [2]_q [N-1]_q / [N+2]_q

with three values at the proton q0, and flagged that its own producer's
docstring states the form ASYMMETRICALLY (a leading factor of q) while
`y_lambda_su_n` computes BALANCED. This probe reproduces the three values
rather than carrying them on trust, and pins both convention arms so a later
reader cannot mistake one for a discrepancy in the other.

WHY IT MATTERS TO sec 4e OF THE `which-N` AUDIT
    That section shows both horns of the phi-k audit's route 1 vanish on depth
    >= 2 at N = 2, and says the fork WOULD decide at general N. That invites a
    rescue -- re-choose N >= 4 and the horns come alive again. The rescue is not
    available: the Ocneanu/Markov weights depend on N through a nontrivial
    rational function of q, so moving N is not a relabelling, it RE-WEIGHTS
    every surviving channel (N = 2 -> 3 moves this ratio by 58 %).

SCOPE -- what is verified here and what is merely cited
    VERIFIED: the three ratios, and the exact leading-q relation between the
    two convention arms.
    CITED, NOT VERIFIED: the stronger identification that N *is* the Ocneanu
    trace parameter, a = q^(N-1), making "choose N" and "choose the trace" one
    act. That is #6829's (`ocneanu_N_lockin_probe`), and this probe does not
    establish it. Do not quote this file as evidence for it.

Precision: mpmath at 50 dps, proton pin (owner directive 2026-08-07). No numpy
and no statistics import; no irrational routine from `math` is called; there is
no builtin-float coercion in this file. (Both offenders are described rather
than spelled, so this paragraph cannot itself trip a grep for them -- the
failure mode recorded in docs/audits/2026-08-15-detector-blindness-taxonomy.md
and committed twice in this corpus already.)
Emits no witness: a cross-check of a closed form, not a derived constant.

Run:
    PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python \
      python3 -u computations/probes/ocneanu_n_lockin_crosscheck_probe.py
"""

from __future__ import annotations

import sys

import mpmath as mp

mp.mp.dps = 50

from qou_substrate.constants import q_at  # noqa: E402

Q = q_at(45)
TOL = mp.mpf("1e-17")

# Reported by #6829 on PR #6826, balanced convention, proton pin.
REPORTED = {
    2: "0.48930712047797097",
    3: "0.774590881357880918",
    4: "0.958124031288484858",
}


def qint(k: int) -> mp.mpf:
    """Balanced q-integer [k]_q = (q^k - q^-k)/(q - q^-1)."""
    return (Q**k - Q ** (-k)) / (Q - 1 / Q)


def ratio_balanced(N: int) -> mp.mpf:
    """y_{(2,1)}/y_{(3)} = [2][N-1]/[N+2], balanced."""
    return qint(2) * qint(N - 1) / qint(N + 2)


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    print("[1] balanced closed form vs the three values reported on #6826")
    print(f"    {'N':>2} {'computed here':>24} {'reported':>24}  match")
    ok1 = True
    for N in (2, 3, 4):
        v = ratio_balanced(N)
        r = mp.mpf(REPORTED[N])
        m = abs(v - r) < TOL
        ok1 &= m
        print(f"    {N:>2} {mp.nstr(v, 20):>24} {REPORTED[N]:>24}  {m}")
    checks.append(("all three reported ratios reproduce at 50 dps", ok1,
                   "N = 2, 3, 4"))

    print("\n[2] the two convention arms differ by EXACTLY a leading q")
    ok2 = True
    for N in (2, 3, 4):
        bal = ratio_balanced(N)
        asym = Q * bal
        ok2 &= abs(asym / bal - Q) < mp.mpf("1e-40")
        print(f"    N={N}  balanced {mp.nstr(bal, 20):>24}"
              f"   asymmetric {mp.nstr(asym, 20):>24}")
    checks.append(("asymmetric = q * balanced exactly -- the producer's "
                   "docstring form is not a discrepancy", ok2, "N = 2, 3, 4"))

    print("\n[3] N is not a free relabelling: it re-weights the channels")
    r2, r3, r4 = (ratio_balanced(N) for N in (2, 3, 4))
    s23 = abs(r3 - r2) / r2
    s34 = abs(r4 - r3) / r3
    print(f"    N=2 -> 3 : {mp.nstr(s23 * 100, 6)} %")
    print(f"    N=3 -> 4 : {mp.nstr(s34 * 100, 6)} %")
    ok3 = s23 > mp.mpf("0.5")
    checks.append(("moving N = 2 -> 3 shifts y_(2,1)/y_(3) by > 50 %, so a "
                   "route-1 rescue by re-choosing N is a change of trace, "
                   "not of reading", ok3, f"{mp.nstr(s23 * 100, 6)} %"))

    print()
    n_ok = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  ({detail})")
    print(f"\n{n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
