"""Term 4 two-arm report: which dim_q, on which blocks.

Information only. Writes no witness and changes no production value.

Term 4 is the trace of the co-Casimir C = Σ p_λ / (dim_q(λ) τ(p_λ)), so its value is
Σ_λ 1/dim_q(λ) over the blocks the trace sees. Three readings, all at the production q₀:

* production : Σ_{λ ⊢ 3A} 1/dimQ_hook(λ)  (``probe_term4_conventions``; every block)
* hook arm   : Σ_{λ ⊢ 3A, ℓ(λ) ≤ 2} 1/dimQ_hook(λ)  (convention-D surviving blocks,
               production's dim_q)
* sl₂ arm    : Σ_{λ = (m,k) ⊢ 3A} 1/[m − k + 1]_q  (surviving blocks, dim_q = quantum trace
               of a primitive idempotent under the mass definition's Markov trace;
               Lean ``CoCasimirHecke.quantumDim_primIdem_twoRow``)
* τ₀ arm     : Σ_{λ ⊢ 3A} q^{κ(λ)}/dimQ_hook(λ)  (every block, dim_q = per-simple weight of
               the symmetrising trace τ₀ times [n]!, which is q^{−κ}·dimQ_hook; Lean
               ``CoCasimirHecke.qFact_mul_symTrace_primIdem``)

All values are reported in units of m_e, the unit in which the existing Term-4 shift probe
reports. Which arm is the Term 4 of the mass formula is the open ruling on issue #8109.
"""
import _path_bridge  # noqa: F401
from mpmath import mp

import probe_term4_conventions as P

mp.dps = 60
Q0 = P.Q0


def content_sum(lam):
    return sum(j - i for i, r in enumerate(lam) for j in range(r))


def arms(A: int):
    n = 3 * A
    nf = P.q_factorial(n)
    prod = hook = sl2 = tau0 = mp.mpf(0)
    for lam in P.partitions(n):
        v = P.inv_dim_q(lam, nf)
        prod += v
        tau0 += Q0 ** content_sum(lam) * v
        if len(lam) <= 2:
            hook += v
            m = lam[0]
            k = lam[1] if len(lam) == 2 else 0
            sl2 += 1 / P.q_int_balanced(m - k + 1)
    return n, prod, hook, sl2, tau0


def main() -> None:
    print(f"q0 = {mp.nstr(Q0, 20)}   (units: m_e)")
    hdr = ("A", "n", "production", "hook arm", "sl2 arm", "tau0 arm",
           "sl2-prod", "hook-prod")
    print("{:<2} {:<3} {:>18} {:>18} {:>18} {:>18} {:>12} {:>12}".format(*hdr))
    for A in range(1, 9):
        n, p, h, s, t = arms(A)
        print(f"{A:<2} {n:<3} {mp.nstr(p, 12):>18} {mp.nstr(h, 12):>18} "
              f"{mp.nstr(s, 12):>18} {mp.nstr(t, 12):>18} "
              f"{mp.nstr(s - p, 6):>12} {mp.nstr(h - p, 6):>12}")
    # n = 3 exact checks: production 2 + 1/[2], hook arm 1 + 1/[2], sl2 arm 1/[4] + 1/[2].
    _, p, h, s, _ = arms(1)
    b2, b4 = P.q_int_balanced(2), P.q_int_balanced(4)
    eps = mp.mpf(10) ** -50
    assert abs(p - (2 + 1 / b2)) < eps and abs(h - (1 + 1 / b2)) < eps
    assert abs(s - (1 / b4 + 1 / b2)) < eps


if __name__ == "__main__":
    main()
