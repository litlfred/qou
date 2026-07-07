#!/usr/bin/env python3
"""qbeta_fmap_modular_dual_missing_probe.py — the compact q-dilog omits Φ_b's modular dual.

Quantifies WHAT the corpus compact q-dilogarithm `phi_q(z) = ∏(1−q^{-k}z)^{-1}`
is missing relative to the true Faddeev non-compact `Φ_b`, WITHOUT evaluating
the transcendental Φ_b (which needs the state integral / quantum-Teichmüller
machinery — deferred). It uses only the algebraic modular relation, so it is
safe from summation/contour inaccuracy.

Foundation (corrected 2026-07-07; the earlier 'modular double = bar involution'
framing was retracted):
  * Convention q = e^{2πi b²}.  The Faddeev Φ_b is a RATIO of two products at
    reciprocal scales b and b^{-1}:  Φ_b = (b-product)/(b^{-1}-product), with
    q̃ = e^{2πi b^{-2}} the modular DUAL of q (b↔b^{-1} ⇒ q↦q̃, NOT q↦q^{-1}).
  * The compact phi_q depends on q ALONE — it has NO q̃ (b^{-1}) product. That
    missing dual factor is the modular / quantum-Teichmüller (root-of-unity)
    structure of the Faddeev saddle.

This probe:
  1. computes the modular dual q̃ at the substrate q₀ and shows |q̃| is a wildly
     different scale from q₀ — so a q-only function cannot carry the dual;
  2. computes the two modular periods (b, b^{-1}) and confirms they are distinct
     ⇒ the Φ_b pole set c_b + ib·ℕ + ib^{-1}·ℕ is a genuine 2-generator lattice
     of SIMPLE poles (literature: Faddeev–Kashaev; Andersen–Kashaev).

Honest scope: this does NOT evaluate Φ_b, and does NOT claim to derive the
observed simple pole at u_substrate (PR #1727) — the u↔x (f-map) map is open.
It quantifies the missing structure; it fits nothing.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 50

# Substrate q₀ (documented canonical value; real, > 1 — the Rogers/torus saddle).
Q0 = mp.mpf("1.10997859555733471989976322048322502665620840878015")


def main() -> int:
    print("=" * 76)
    print(" Q_β f-map — the compact q-dilog omits Φ_b's modular dual (convention q=e^{2πib²})")
    print("=" * 76)

    lnq = mp.log(Q0)
    # b² = ln q / (2πi);  b^{-2} = 2πi / ln q;  q̃ = e^{2πi b^{-2}} = e^{-4π²/ln q}.
    b2 = lnq / (2 * mp.pi * mp.mpc(0, 1))
    b = mp.sqrt(b2)
    binv = 1 / b
    q_tilde = mp.e ** (-4 * mp.pi ** 2 / lnq)

    print(f"  q₀            = {mp.nstr(Q0, 20)}   (real, >1)")
    print(f"  b²  = lnq/(2πi) = {mp.nstr(b2, 12)}   (purely imaginary)")
    print(f"  b             = {mp.nstr(b, 12)}")
    print(f"  b^{{-1}}         = {mp.nstr(binv, 12)}")
    print()
    print("  1. Modular dual q̃ = e^{2πi b^{-2}} = e^{-4π²/lnq}:")
    print(f"     |q̃|          = {mp.nstr(mp.fabs(q_tilde), 6)}")
    print(f"     log10|q̃|     = {mp.nstr(mp.log(mp.fabs(q_tilde), 10), 8)}")
    print(f"     |q̃ − q₀|     = {mp.nstr(mp.fabs(q_tilde - Q0), 6)}  (≈ q₀ — utterly different scale)")
    print("     => the compact phi_q(q₀,·) has NO q̃-dependence, so it omits the")
    print("        ENTIRE modular-dual product of Φ_b (not a small correction).")
    print()
    print("  2. Two modular periods (pole lattice generators ib, ib^{-1}):")
    p1, p2 = mp.mpc(0, 1) * b, mp.mpc(0, 1) * binv
    print(f"     ib           = {mp.nstr(p1, 10)}")
    print(f"     ib^{{-1}}       = {mp.nstr(p2, 10)}")
    ratio = p2 / p1
    print(f"     ib^{{-1}} / ib  = {mp.nstr(ratio, 10)}  (non-real ⇒ 2 independent generators)")
    distinct = mp.fabs(mp.im(ratio)) > mp.mpf("1e-30")
    print(f"     independent 2D lattice of SIMPLE poles? {distinct}")
    print()
    print("  HONEST SCOPE: Φ_b itself is NOT evaluated here (state-integral, deferred).")
    print("  The u↔x (f-map) link to the observed u_substrate pole (PR #1727) is OPEN.")
    print("  This quantifies the missing modular-double structure; it fits nothing.")

    ok = mp.fabs(q_tilde) < mp.mpf("1e-50") and distinct
    print(f"\n  structural check (dual scale ≪ q₀ AND 2D pole lattice): {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
