#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic structural exploration.
"""Q_β heat-route — SYMBOLIC f-map exploration (is the lift forced?).

Follows the a_1-gate probe (docs/audits/2026-06-13-qbeta-heat-kernel-a1-gate-probe.md).
Symbolic (sympy) tests of how the heat-kernel bar-odd structure could lift to
a_1 = -c_3, and whether the f-map (heat-time t ↔ ladder u) is constrained:

  1. κ_λ(q) = (q-1)·μ_λ(q) closed forms for λ ⊢ 3; exact bar-parity.
  2. e_1 = Σ_λ κ_λ bar-parity (the unweighted assembly).
  3. Mode-selectivity: can a bar-EVEN scalar S(q) turn e_1 into a bar-ODD a_1?
     (If e_1 is bar-neither, NO scalar fixes parity ⇒ f-map must select modes.)
  4. The c_3 factorisation: a_1 = κ_(2,1)·S  ⇒  is S a pure-q function or does
     it carry the anchor (the single archimedean scalar of the synthesis)?

STRUCTURAL only — no c_3 value claimed/wired; flip-flop guard respected.
"""
from __future__ import annotations
import sympy as sp

from qbeta_symbolic_utils import (  # shared sympy helpers (single source of truth)
    q, kappa, bar, parity,
)


def main():
    print("=" * 74)
    print("  Q_β heat-route — symbolic f-map exploration  (λ ⊢ 3)")
    print("=" * 74)
    parts3 = [(3,), (2, 1), (1, 1, 1)]
    kappas = {}
    for p in parts3:
        k = kappa(p)
        kappas[p] = k
        print(f"\n  λ={p}")
        print(f"    κ_λ = (q-1)μ_λ = {k}")
        print(f"    bar(κ_λ)        = {bar(k)}")
        print(f"    parity          = {parity(k)}")

    e1 = sp.simplify(sum(kappas.values()))
    print(f"\n  e_1 = Σ_λ κ_λ = {e1}")
    print(f"    parity(e_1) = {parity(e1)}")

    print("\n  ── Mode-selectivity test ──")
    print("  A bar-EVEN scalar S(q) preserves parity: S·(even)=even, S·(odd)=odd,")
    print("  S·(—)=— (bar-neither). So if e_1 is bar-neither ('—'), NO bar-even")
    print(f"  scalar f-map can produce a bar-ODD a_1 from the full sum.  e_1 parity = {parity(e1)}.")
    print("  ⇒ the f-map must SELECT the bar-odd modes (κ_(2,1), the c=1-dominated")
    print("    standard rep), not act as a global scalar.")

    print("\n  ── c_3 factorisation a_1 = κ_(2,1)·S ──")
    k21 = kappas[(2, 1)]
    print(f"  κ_(2,1) = {k21}  [parity {parity(k21)}, pure-q, fibre-level]")
    # numeric: S = a_1_target / κ_(2,1)(q0) at both anchors
    q0 = sp.Rational(110997858275, 100000000000)  # q_0 ≈ 1.10997859556
    k21_q0 = float(k21.subs(q, q0))
    a1_p = float(sp.sqrt(2) * sp.Rational(146324616887618, 100000000000000))
    a1_mu = float(sp.sqrt(2) * sp.Rational(142849728553818, 100000000000000))
    print(f"  κ_(2,1)(q_0) = {k21_q0:.8e}")
    print(f"  S_proton = a_1(p)/κ_(2,1) = {a1_p / k21_q0:.4f}")
    print(f"  S_muon   = a_1(μ)/κ_(2,1) = {a1_mu / k21_q0:.4f}")
    print(f"  S_p / S_μ = {(a1_p/k21_q0)/(a1_mu/k21_q0):.6f}  (≠1 ⇒ S is ANCHOR-dependent,")
    print("    i.e. NOT a pure-q function — it is the single archimedean scalar S=Q_β/E₀")
    print("    of the synthesis; the fibre part κ_(2,1) is pure-q & bar-odd.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
