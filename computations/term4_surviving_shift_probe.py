"""Term 4 on the surviving blocks: shift against the production all-partition sum.

Information only. Production (``probe_term4_conventions``) sums 1/dim_q(λ) over
every λ ⊢ 3A. Under convention D, τ(p_λ) = 0 for λ with three or more rows, so the
co-Casimir element is only defined on the surviving blocks; its trace is the sum
over λ with at most two rows (Lean:
``QOU.MassTheory.CoCasimirSurviving.tr_coCasimirSurv_conventionD``).

This probe prints, for A = 1..8, both sums at the production q₀ and their
difference in units of m_e. It writes no witness and changes no production value.
Uses the producer's own partitions / hook-length dim_q, so only the support differs.
"""
import _path_bridge  # noqa: F401
from mpmath import mp

import probe_term4_conventions as P

mp.dps = 60


def surviving_shift(A: int):
    n = 3 * A
    nf = P.q_factorial(n)
    total = mp.mpf(0)
    surv = mp.mpf(0)
    n_surv = n_dead = 0
    for lam in P.partitions(n):
        v = P.inv_dim_q(lam, nf)
        total += v
        if len(lam) <= 2:
            surv += v
            n_surv += 1
        else:
            n_dead += 1
    return n, n_surv, n_dead, total, surv, surv - total


def main() -> None:
    print("A  n   surv dead  Σ_all (production)   Σ_≤2rows (C°)       shift / m_e")
    for A in range(1, 9):
        n, ns, nd, tot, surv, d = surviving_shift(A)
        print(f"{A}  {n:<3} {ns:<4} {nd:<5} {mp.nstr(tot, 15):<20} "
              f"{mp.nstr(surv, 15):<19} {mp.nstr(d, 15)}")
    # A = 1 check: the only dead block at n = 3 is (1,1,1), and 1/dim_q(1³) = 1.
    _, _, _, _, _, d1 = surviving_shift(1)
    assert abs(d1 + 1) < mp.mpf(10) ** -50, d1


if __name__ == "__main__":
    main()
