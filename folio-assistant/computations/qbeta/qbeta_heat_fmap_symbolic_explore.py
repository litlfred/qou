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

q = sp.symbols('q', positive=True)


def jackson(k):
    """[k]_q = (1-q^k)/(1-q); [0]=0 (works for negative k too)."""
    if k == 0:
        return sp.Integer(0)
    return (1 - q ** k) / (1 - q)


def contents(part):
    return [j - i for i, row in enumerate(part) for j in range(row)]


def mu(part):
    hbar2 = ((q - 1) / q) ** 2
    return sp.simplify(hbar2 * sum(jackson(c) * jackson(c + 1) for c in contents(part)))


def kappa(part):
    return sp.simplify((q - 1) * mu(part))


def bar(expr):
    return sp.simplify(expr.subs(q, 1 / q))


def parity(expr):
    b = sp.simplify(bar(expr) + expr)
    if b == 0:
        return "ODD"
    if sp.simplify(bar(expr) - expr) == 0:
        return "EVEN"
    return "neither"


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
    print("  S·(neither)=neither. So if e_1 is 'neither', NO bar-even scalar f-map")
    print(f"  can produce a bar-ODD a_1 from the full sum.  e_1 parity = {parity(e1)}.")
    print("  ⇒ the f-map must SELECT the bar-odd modes (κ_(2,1), the c=1-dominated")
    print("    standard rep), not act as a global scalar.")

    print("\n  ── c_3 factorisation a_1 = κ_(2,1)·S ──")
    k21 = kappas[(2, 1)]
    print(f"  κ_(2,1) = {k21}  [parity {parity(k21)}, pure-q, fibre-level]")
    # numeric: S = a_1_target / κ_(2,1)(q0) at both anchors
    q0 = sp.Rational(110997858275, 100000000000)  # q_0 ≈ 1.10997858275
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
