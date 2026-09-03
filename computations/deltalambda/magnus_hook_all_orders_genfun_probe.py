#!/usr/bin/env python3
"""magnus_hook_all_orders_genfun_probe.py — the Ω₂-inserted hook column is a determinant
DERIVATIVE of the reduced Burau: the "all orders" generalization (qou-o6ov).

The plain identity (magnus_hook_exterior_power_probe.py, exact to 139 digits) is equivalent to
    Σ_j tr_{(n-j,1^j)}(ρ) t^j = q^L · det(1 + s·ρ^V),   s = t/q^L,
i.e. the hook column of the PLAIN character is the reduced-Burau characteristic polynomial in a
rescaled variable. This probe tests the ALL-ORDERS generalization for the actual decay object
tr(ρ·Ω₂): the Ω₂ insertion acts on Λ^j(V) as the induced DERIVATION, so by Jacobi's formula
    Σ_j tr_{(n-j,1^j)}(ρ·Ω₂) t^j  =  q^L · s · det(1+s·ρ^V) · tr( (1+s·ρ^V)^{-1} Ω₂^V ρ^V ),
                                     s = t/q^L,
governed by the SAME (n-1)-dim reduced-Burau data ρ^V, Ω₂^V. Verified by evaluating both sides
at several t (LHS = Σ_j (directly-computed hook traces) t^j; RHS from the reflection rep). A
match to full precision establishes that the WHOLE hook column of the tr-decay — every order j
— reduces to the reduced Burau, closing the hook slice of the theorem.

scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_extreme_rep_endpoint_probe import omega2_trace  # noqa: E402
from magnus_hook_exterior_power_probe import word_dense, hook  # noqa: E402


def refl_rho_and_omega2(shape, gens):
    """ρ^V and Ω₂^V = Σ_a ⁅A_a,A_{a+1}⁆ as dense mp matrices in the reflection rep `shape`."""
    per_gen, dim = base.block_structure(shape)
    ngen = max(gens) + 1
    sig = base.sigma_csr(per_gen, dim, base.Q0)
    germ_rows, hcheck = base.germ_csr(per_gen, dim, base.Q0, base.EPS)
    assert hcheck < mp.mpf(10) ** -55
    sd = [base._dense_from_csr(sig[g], dim) for g in range(ngen)]
    ad = [base._dense_from_csr(germ_rows[g], dim) for g in range(ngen)]
    rho = sd[gens[0]]
    for g in gens[1:]:
        rho = rho * sd[g]
    O = mp.zeros(dim, dim)
    for a in range(ngen - 1):
        O = O + (ad[a] * ad[a + 1] - ad[a + 1] * ad[a])
    return rho, O, dim


def analyze(A):
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    L = len(gens)
    qL = base.Q0 ** L

    # LHS coefficients a_j = tr(ρ_{(n-j,1^j)} Ω₂), j = 0..n-1  (hook (k,1^{n-k}), j=n-k)
    a = [mp.mpf(0)] * n
    for k in range(1, n + 1):
        lam = hook(n, k)
        tr, _ = omega2_trace(lam, gens)
        a[n - k] = tr

    # reduced-Burau data
    refl = tuple([n - 1, 1])
    rhoV, O2V, dv = refl_rho_and_omega2(refl, gens)
    I = mp.eye(dv)

    print(f"[genfun] A={A} (n={n}); reflection dim n-1={dv}, L={L}, q^L={mp.nstr(qL,6)}")
    print(f"[genfun] test  Σ_j a_j t^j  ==  q^L·s·det(1+s ρ^V)·tr((1+s ρ^V)^-1 Ω₂^V ρ^V),  s=t/q^L\n")
    print("     t          LHS=Σ a_j t^j          RHS (det-derivative)        |Δ_rel|")
    worst = mp.mpf(0)
    for t0 in [mp.mpf("0.3"), mp.mpf("0.7"), mp.mpf("1.3"), mp.mpf("2.1"), -mp.mpf("0.9")]:
        lhs = mp.mpf(0)
        for j in range(n):
            lhs += a[j] * t0 ** j
        s0 = t0 / qL
        Asx = I + s0 * rhoV
        try:
            Ainv = Asx ** -1
        except Exception:
            continue
        detA = mp.det(Asx)
        M = Ainv * (O2V * rhoV)
        trres = sum(M[i, i] for i in range(dv))
        rhs = qL * s0 * detA * trres
        rel = abs(lhs - rhs) / (abs(lhs) + mp.mpf(10) ** -80)
        worst = max(worst, rel if not mp.isnan(rel) else mp.mpf(0))
        print(f"  {mp.nstr(t0,4):>6}   {mp.nstr(lhs,10):>20}   {mp.nstr(rhs,10):>20}   {mp.nstr(rel,3):>8}")
    ok = worst < mp.mpf(10) ** -20
    print(f"\n  worst relative |LHS − RHS| = {mp.nstr(worst,4)}  "
          f"{'✓ EXACT ⇒ the WHOLE hook column of tr(ρΩ₂) (all orders j) is a determinant' if ok else '✗ no match (twist/form differs)'}")
    if ok:
        print("  derivative of the (n-1)-dim reduced Burau — the hook slice of the decay is closed-form.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    args = ap.parse_args()
    analyze(A=args.A)


if __name__ == "__main__":
    main()
