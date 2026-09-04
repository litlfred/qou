#!/usr/bin/env python3
"""magnus_hook_majorant_closed_form_probe.py — a DERIVED reduced-Burau closed form for the
positive majorant tr_λ(X*X) on the hook column (qou-o6ov).

WHERE THIS SITS. The majorant ladder showed the b-decay survives to ‖M_λ‖_F, and the
anti-involution check showed ‖M_λ‖_F² = tr_λ(X*X) with X = ρ·Ω₂^P — a POSITIVE trace of a genuine
Hecke ALGEBRA element. The point of that was: the arc's reductions (#6464 hooks → reduced Burau,
#6525 two-rows → R-matrix sectors) are CHARACTER identities, so they apply to any algebra element,
X*X included. This probe cashes that in for the hook column — turning "the handles apply" from
applicability into an actual closed form.

THE DERIVATION. With c = 4/[2]_q², Ω₂^P = c·Σ_a[σ_a,σ_(a+1)], X = ρ·Ω₂^P, and * the word-reversal
anti-involution (X* = -c·Σ_a[σ_a,σ_(a+1)]·ρ*):

    X* X = -c² · Σ_{a,b} [σ_a,σ_(a+1)] · (ρ* ρ) · [σ_b,σ_(b+1)]

Expanding both commutators gives 4(ngen-1)² WORDS, and — the fact that makes this work — they ALL
have the same length T = 2 + 2L + 2 = 2L+4 (ρ* has the same length L as ρ). So #6464's word-length
twist q^{len·(1-j)} is COMMON to every term and factors out. On a hook (k,1^{n-k}) = Λ^j(V),
j = n-k:

    tr_hook(X* X) = -c² · q^{(2L+4)(1-j)} · Σ_{a,b} [ e_j(μ(A⁺YB⁺)) - e_j(μ(A⁺YB⁻))
                                                     - e_j(μ(A⁻YB⁺)) + e_j(μ(A⁻YB⁻)) ]

where Y = ρ*ρ, A⁺ = σ_aσ_(a+1), A⁻ = σ_(a+1)σ_a (likewise B at index b), and μ(·) are the
eigenvalues of that word in the (n-1)-dim reduced Burau rep V.

WHY IT IS WORTH HAVING. The right-hand side needs only (n-1)×(n-1) matrices — 5×5 at A=2, 8×8 at
A=3 — against dim_λ×dim_λ (up to 216) for the direct computation, and it is uniform in the hook
index j. It is the first DERIVED closed form for the majorant rather than for the quantity.

This probe checks the identity against the direct tr_λ(X*X) on every hook, and confirms the result
is positive (it must be: X*X ⇒ Σσ² ≥ 0). A mismatch would mean the common-twist step is wrong —
report it, do not patch the twist to fit.

scope-(a); NO-FLOAT64 (mpf, dps 140). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_hook_exterior_power_probe import elem_sym_from_eigs  # noqa: E402
from magnus_gauge_hook_closed_form_probe import reflection_generators  # noqa: E402
from magnus_frobenius_is_positive_trace_probe import build  # noqa: E402


def direct_hook_majorant(lam, gens, q, ngen):
    """tr_λ(X* X) computed directly in the seminormal irrep (the reference)."""
    X, Xstar, dim, _asym = build(lam, gens, q, ngen)
    P = Xstar * X
    return mp.re(sum(P[i, i] for i in range(dim))), dim


def burau_closed_form(j, gens, q, ngen, sV, L):
    """-c²·q^{(2L+4)(1-j)}·Σ_{a,b} Σ_± ± e_j(eig of the word), all in the reduced Burau."""
    c = 4 / (q + 1 / q) ** 2
    # Y = ρ* ρ in the reduced Burau
    rho = sV[gens[0]]
    for g in gens[1:]:
        rho = rho * sV[g]
    rho_star = sV[gens[-1]]
    for g in reversed(gens[:-1]):
        rho_star = rho_star * sV[g]
    Y = rho_star * rho

    total = mp.mpf(0)
    for a in range(ngen - 1):
        Ap = sV[a] * sV[a + 1]
        Am = sV[a + 1] * sV[a]
        for b in range(ngen - 1):
            Bp = sV[b] * sV[b + 1]
            Bm = sV[b + 1] * sV[b]
            for (Amat, sa) in ((Ap, 1), (Am, -1)):
                for (Bmat, sb) in ((Bp, 1), (Bm, -1)):
                    E, _ = mp.eig(Amat * Y * Bmat)
                    total += sa * sb * elem_sym_from_eigs(list(E))[j]
    twist = q ** ((2 * L + 4) * (1 - j))
    return -c ** 2 * twist * mp.re(total)


def analyze(A):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    L = len(gens)
    sV, dimV = reflection_generators(n, ngen, q)

    print(f"[hookmaj] A={A} (n={n}); L={L}, all words have length T=2L+4={2*L+4} ⇒ ONE common twist")
    print(f"[hookmaj] tr_hook(X*X) =?= -c²·q^{{T(1-j)}}·Σ_(a,b) Σ_± ± e_j(eig in reduced Burau, dim {dimV})")
    print(f"[hookmaj] {4*(ngen-1)**2} words per hook, each a {dimV}x{dimV} eig — vs dim_λ×dim_λ direct\n")
    print("   k  hook              j   dim   direct tr(X*X)     Burau closed form     |Δ_rel|   positive?")
    worst = mp.mpf(0)
    all_pos = True
    for k in range(n, 0, -1):
        hook = tuple([k] + [1] * (n - k))
        j = n - k
        direct, dim = direct_hook_majorant(hook, gens, q, ngen)
        cf = burau_closed_form(j, gens, q, ngen, sV, L)
        den = abs(direct) if abs(direct) > mp.mpf(10) ** -100 else mp.mpf(1)
        rel = abs(direct - cf) / den
        worst = max(worst, rel)
        if direct < 0:
            all_pos = False
        print(f"  {k:>2}  {str(hook):<16}  {j:>1}  {dim:>4}   {mp.nstr(direct,10):>15}   "
              f"{mp.nstr(cf,10):>17}   {mp.nstr(rel,3):>9}   {'yes' if direct >= 0 else 'NO'}")
    print()
    ok = worst < mp.mpf(10) ** -100
    print(f"  closed form verified on every hook?  {'YES ✓' if ok else 'NO ✗'}  "
          f"(worst |Δ_rel| = {mp.nstr(worst,3)})")
    print(f"  majorant positive on every hook?     {'YES ✓' if all_pos else 'NO ✗'}")
    if ok and all_pos:
        print("\n  ⇒ DERIVED: the positive majorant tr_hook(X*X) = ‖M_hook‖_F² has a reduced-Burau")
        print("    closed form, all orders — the same handle #6464 gave the QUANTITY now gives the")
        print("    BOUND. It needs only (n-1)×(n-1) matrices and one common twist q^{(2L+4)(1-j)},")
        print("    because every one of the expanded words has the same length 2L+4.")
    elif not ok:
        print("\n  ⇒ MISMATCH — the common-twist step is wrong somewhere. Report it; do NOT fit the")
        print("    twist to the data (that is exactly the trap the L+2 twist set in #6464).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2])
    args = ap.parse_args()
    for A in args.A:
        analyze(A)
        print()


if __name__ == "__main__":
    main()
