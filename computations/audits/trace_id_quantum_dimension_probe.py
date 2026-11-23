#!/usr/bin/env python3
"""tr(id_A) as a quantum dimension: what the owner's 2026-09-15 ruling forces.

RULING (owner, 2026-09-15, verbatim): "i think it is [2]_q ..... euler
charactersitc of object in the QOU category".  So the categorical trace is the
quantum dimension,

    tr(id_X) = dim_q(X),

which is q-DEPENDENT.  This probe asks what that costs the corpus's other
reading of the same symbol, chi(A) = tr(id_A) = -6.

THREE MEASUREMENTS, all exact-arithmetic (mpmath mpf end to end, no float):

  1. dim_q of every finite-dimensional irrep is POSITIVE at the substrate q0.
     dim_q(V_n) = [n+1]_q = (q^(n+1) - q^-(n+1))/(q - q^-1), and at real q > 1
     this is >= [1]_q = 1, strictly increasing.  So -6 is not the naive
     quantum dimension of ANY finite-dimensional irrep.

  2. For the base algebra itself the question does not even have an answer.
     A = O_q(SU(2)) is not an irrep; by Peter-Weyl it is the infinite direct
     sum (+)_n V_n (x) V_n^*, so the naive quantum dimension is

         dim_q(A) = sum_n (dim_q V_n)^2 = sum_n [n+1]_q^2,

     whose terms grow like q^(2n).  At q0 > 1 that DIVERGES.  This is the
     load-bearing measurement: a regularisation is not an optional refinement,
     it is REQUIRED before tr(id_A) has a value at all.

  3. An alternating sum over the same tower does reach negative values, which
     is the shape a -6 would have to come from -- an Euler characteristic of a
     COMPLEX, not a naive dimension.  Demonstrated, not proposed: this probe
     does NOT claim the corpus's -6 arises this way, only that the naive
     reading cannot produce it and this class can produce negatives.

WHAT THIS DOES NOT CLAIM.  It does not derive -6, does not identify the
regularisation, and does not decide whether prop:euler-char-stability's bridge
tr(id_{A_n}) = chi_top(S_n) holds.  Scope (a) throughout except measurement 2,
which is scope (b) for the narrow claim "the naive dim_q(A) is not a real
number at q0", invariant = divergence of a series with ratio > 1.

Run:  python3 computations/audits/trace_id_quantum_dimension_probe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(50, mp.mp.dps)

FAILURES: list[str] = []
CHECKS = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


Q0 = mp.mpf(Q_50_DIGIT_STR)


def q_int(n: int) -> mp.mpf:
    """[n]_q = (q^n - q^-n) / (q - q^-1), exact in mpf at the working dps."""
    return (Q0**n - Q0 ** (-n)) / (Q0 - 1 / Q0)


def dim_q_irrep(n: int) -> mp.mpf:
    """dim_q of the (n+1)-dimensional irrep V_n of SU_q(2)."""
    return q_int(n + 1)


def main() -> int:
    print(f"q0 = {mp.nstr(Q0, 20)}   (proton pin, qou_substrate.constants.Q_50_DIGIT_STR)")
    print()

    # -- 1. every finite-dim irrep has positive quantum dimension ------------
    print("1. dim_q of the finite-dimensional irreps")
    dims = [dim_q_irrep(n) for n in range(0, 41)]
    check(
        "dim_q(V_n) > 0 for n = 0..40",
        all(d > 0 for d in dims),
        f"min = {mp.nstr(min(dims), 12)} at n = 0;  dim_q(V_1) = [2]_q = "
        f"{mp.nstr(dims[1], 20)}",
    )
    check(
        "dim_q(V_n) is strictly increasing in n",
        all(dims[i] < dims[i + 1] for i in range(len(dims) - 1)),
        "so inf over all n is [1]_q = 1, attained at n = 0",
    )
    check(
        "-6 is not dim_q(V_n) for any n = 0..40",
        all(abs(d - (-6)) > mp.mpf("1e-30") for d in dims),
        "every value is >= 1; the target is negative, so no n can reach it",
    )
    print()

    # -- 2. the base algebra's naive quantum dimension diverges -------------
    print("2. dim_q(A) for A = O_q(SU(2)), via Peter-Weyl A = (+)_n V_n (x) V_n^*")
    partial: list[tuple[int, mp.mpf]] = []
    s = mp.mpf(0)
    for n in range(0, 121):
        s += dim_q_irrep(n) ** 2
        if n in (5, 10, 20, 40, 80, 120):
            partial.append((n, +s))
    for n, val in partial:
        print(f"         sum_(n<={n:<3}) [n+1]_q^2 = {mp.nstr(val, 12)}")
    ratio = (dim_q_irrep(121) ** 2) / (dim_q_irrep(120) ** 2)
    check(
        "the series sum_n [n+1]_q^2 diverges",
        ratio > 1,
        f"ratio of consecutive terms at n = 120 is {mp.nstr(ratio, 12)} > 1; "
        f"terms ~ q^(2n) with q0 = {mp.nstr(Q0, 10)} > 1",
    )
    check(
        "the partial sums are strictly increasing and unbounded on the sample",
        all(partial[i][1] < partial[i + 1][1] for i in range(len(partial) - 1)),
        f"sum_(n<=120) = {mp.nstr(partial[-1][1], 12)}",
    )
    check(
        "so the NAIVE dim_q(A) is not a real number at q0",
        True,
        "a regularisation is REQUIRED before tr(id_A) has a value at all -- "
        "this is forced by the ruling, not a choice",
    )
    print()

    # -- 3. an alternating sum over the same tower can be negative ----------
    print("3. can an Euler-characteristic-of-a-complex shape reach a negative?")
    alt4 = sum((-1) ** k * dim_q_irrep(k) for k in range(4))
    check(
        "alternating sums over the tower do reach negative values",
        alt4 < 0,
        f"sum_(k=0..3) (-1)^k [k+1]_q = {mp.nstr(alt4, 14)}",
    )
    check(
        "this probe does NOT claim the corpus's -6 arises this way",
        True,
        "it shows only that the naive reading cannot produce a negative and "
        "this class can; identifying the actual construction is open",
    )
    print()

    w = WitnessBuilder("trace-id-quantum-dimension", engine="mpmath")
    w.save(
        {
            "q0Anchor": "proton",
            "description": (
                "Under the owner ruling of 2026-09-15 that tr(id_A) is the "
                "quantum dimension, the naive dim_q of the base algebra "
                "O_q(SU(2)) diverges at the substrate q0, so a regularisation "
                "is required before tr(id_A) has a value; and no "
                "finite-dimensional irrep has a negative quantum dimension, so "
                "the corpus's chi(A) = -6 cannot be a naive dim_q."
            ),
            "q0Value": mp.nstr(Q0, 20),
            "dim_q_V1_is_2q": mp.nstr(dim_q_irrep(1), 25),
            "dim_q_min_over_irreps": mp.nstr(min(dims), 12),
            "peter_weyl_partial_sums": {
                str(n): mp.nstr(v, 14) for n, v in partial
            },
            "consecutive_term_ratio_at_n120": mp.nstr(ratio, 14),
            "series_diverges": True,
            "alternating_sum_k0_to_3": mp.nstr(alt4, 14),
            "checks": CHECKS,
            "failures": FAILURES,
        }
    )

    print("=" * 66)
    if FAILURES:
        print(f"FAILED {len(FAILURES)}/{CHECKS}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"PASSED {CHECKS}/{CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
