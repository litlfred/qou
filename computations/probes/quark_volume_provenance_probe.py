#!/usr/bin/env python3
"""
quark_volume_provenance_probe.py — DERIVES the neutron/proton quark
"quantum-dilogarithm volumes" Φ(uud) ≈ -0.878526, Φ(udd) ≈ -1.226119 from the
canonical Hecke traced-volume construction (level1-qvalues.py / traced_volume),
and prints their exact symbolic closed form.

Φ(K) = Σᵢ log|V̂ᵢ(K)|,  V̂ᵢ = z·M₁₀ + M₁₁,  M = ∏_{j>i} T(cᵢⱼ,dᵢⱼ),
       T(c,d) = [[c·h+d, c],[c,d]],  h = q − q⁻¹,  z = 4993/10000.
proton = uud = [1,1,0],  neutron = udd = [1,0,0].

Companion audit: docs/audits/2026-07-11-quark-volume-provenance.md.
Run from repo root: `python3 computations/probes/quark_volume_provenance_probe.py`
"""
from __future__ import annotations

import math

Z = 4993 / 10000  # NF-basis constant (≈ 1/2)


def _mat_mul(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def _crossing(ti, tj, h):
    if ti == 1 and tj == 1:
        return 1.0, 0.0            # uu
    if ti == 0 and tj == 0:
        return 1.0, -h             # dd
    return 1.0, -h / 2             # ud / du


def traced_volume(i, ordering, h, z=Z):
    M = [[1.0, 0.0], [0.0, 1.0]]
    for j in range(i + 1, len(ordering)):
        c, d = _crossing(ordering[i], ordering[j], h)
        M = _mat_mul(M, [[c * h + d, c], [c, d]])
    return z * M[1][0] + M[1][1]


def phi(ordering, q):
    h = q - 1.0 / q
    return sum(math.log(abs(traced_volume(i, ordering, h)))
               for i in range(len(ordering) - 1))


def main() -> None:
    q0 = 1.1099786  # engine rational q₀ (matches level1-qvalues.py)
    uud, udd = [1, 1, 0], [1, 0, 0]
    print(f"q₀ = {q0},  z = {Z},  h = q−1/q = {q0 - 1/q0:.6f}\n")
    for name, ordv, lit in [("uud (proton)", uud, -0.878526),
                            ("udd (neutron)", udd, -1.226119)]:
        v = phi(ordv, q0)
        print(f"  Φ({name:>14s}) = Σ log|V̂ᵢ| = {v:+.6f}   literal {lit:+.6f}   Δ={abs(v-lit):.1e}")
    print(f"\n  |ΔΦ| = {abs(phi(udd, q0) - phi(uud, q0)):.6f}   (literal 0.347593)")

    try:
        import sympy as sp
    except ImportError:
        print("\n(install sympy for the exact symbolic closed form)")
        return
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    z = sp.Rational(4993, 10000)

    def T(c, d):
        return sp.Matrix([[c * h + d, c], [c, d]])

    def vhat(mats):
        M = sp.eye(2)
        for t in mats:
            M = M * t
        return z * M[1, 0] + M[1, 1]

    Tuu, Tud, Tdd = T(1, 0), T(1, -h / 2), T(1, -h)
    prod_uud = sp.factor(sp.together(vhat([Tuu, Tud]) * vhat([Tud])))
    prod_udd = sp.factor(sp.together(vhat([Tud, Tud]) * vhat([Tdd])))
    print("\n  exact symbolic  Φ(K) = log|∏ᵢ V̂ᵢ(K)|:")
    print(f"    ∏V̂(uud) = {prod_uud}")
    print(f"    ∏V̂(udd) = {prod_udd}")


if __name__ == "__main__":
    main()
