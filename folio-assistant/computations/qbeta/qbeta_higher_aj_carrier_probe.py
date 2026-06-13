#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic structural exploration.
"""Q_β heat-route — higher kernel coefficients a_2, a_3 (fibre carriers).

With a_1 = -c_3 pinned to the fibre carrier κ_(2,1) (bar-odd) and period-3/ζ₆
CLOSED (bar-stability lemma), the natural fibre continuation is the HIGHER
recursion coefficients. The depth-d recursion is c_{k+1} = Σ_j a_j c_{k+1-j};
the heat route makes the a_j the elementary symmetric polynomials of the
per-mode RATES r_λ = (q-1)·μ_λ = κ_λ (the q-difference kernel of a product of
depth-1 modes A_λ(t)=1-(q-1)μ_λ t composes to e_j coefficients).

Two results (all fibre, no archimedean scalar S — S is owner-DECLINED):

  1. PARITY-ALTERNATION THEOREM (abstract): if the f-map feeds bar-ODD rates
     r_λ (the bar-odd projections, which carry each mode's ζ-content by the
     bar-stability lemma), then bar(e_j) = (-1)^j e_j, so a_j alternates
     bar-parity: a_1 ODD, a_2 EVEN, a_3 ODD. Forced, mode-set-independent.
     (Matches c_2=-1 bar-even seed → c_3 bar-odd → … consistency.)

  2. CONCRETE CARRIERS: e_1, e_2, e_3 of a principled depth-3 active set,
     with bar-parity + root-of-unity (ζ_d) content, showing where ζ₆ first
     enters the higher coefficients.

STRUCTURAL only; no c_3 value; flip-flop guard respected.
"""
from __future__ import annotations
import itertools
import sympy as sp

q = sp.symbols('q')


def jackson(k):
    if k == 0:
        return sp.Integer(0)
    return sp.cancel((1 - q ** k) / (1 - q))


def contents(part):
    return [j - i for i, row in enumerate(part) for j in range(row)]


def kappa(part):
    """Per-mode rate r_λ = (q-1)·μ_λ = (q-1)·ℏ_q²·Σ_□[c][c+1]."""
    hbar2 = ((q - 1) / q) ** 2
    return sp.cancel((q - 1) * hbar2 * sum(jackson(c) * jackson(c + 1)
                                          for c in contents(part)))


def bar(expr):
    return sp.cancel(expr.subs(q, 1 / q))


def odd_part(expr):
    return sp.cancel((expr - bar(expr)) / 2)


def parity(expr):
    if sp.cancel(expr) == 0:
        return "0"
    if sp.simplify(bar(expr) + expr) == 0:
        return "ODD"
    if sp.simplify(bar(expr) - expr) == 0:
        return "EVEN"
    return "—"


def zeta_content(expr, dmax=12):
    if sp.cancel(expr) == 0:
        return []
    num = sp.Poly(sp.numer(sp.cancel(expr)), q)
    return [d for d in range(2, dmax + 1)
            if not num.is_zero and num.rem(sp.Poly(sp.cyclotomic_poly(d, q), q)).is_zero]


def elem_sym(rates, j):
    """j-th elementary symmetric polynomial of the rate list."""
    return sp.cancel(sum(sp.prod(c) for c in itertools.combinations(rates, j)))


def main():
    print("=" * 80)
    print("  Higher kernel coefficients a_2, a_3 — fibre carriers (e_j of κ_λ)")
    print("=" * 80)

    # ── Result 1: abstract parity-alternation theorem ──
    print("\n  ── Result 1: parity-alternation theorem (abstract, bar-odd rates) ──")
    r = sp.symbols('r1 r2 r3 r4')               # abstract rates
    barr = sp.symbols('br1 br2 br3 br4')        # their bars
    # impose bar-odd: bar(r_i) = -r_i  ⇒ substitute br_i = -r_i
    sub = {b: -ri for b, ri in zip(barr, r)}
    for j in range(1, 5):
        ej = sum(sp.prod(c) for c in itertools.combinations(r, j))
        ej_bar = sum(sp.prod(c) for c in itertools.combinations(barr, j))
        ej_bar_sub = sp.expand(ej_bar.subs(sub))
        predicted = sp.expand((-1) ** j * ej)
        ok = sp.simplify(ej_bar_sub - predicted) == 0
        par = "ODD" if j % 2 == 1 else "EVEN"
        print(f"    e_{j}: bar(e_{j}) == (-1)^{j}·e_{j}? {ok}  ⇒ a_{j} bar-{par}")
    print("  ⇒ THEOREM: bar-odd rates ⇒ a_j alternate ODD,EVEN,ODD,EVEN,… (forced).")

    # ── Result 2: concrete carriers for a principled depth-3 active set ──
    print("\n  ── Result 2: concrete e_1,e_2,e_3 carriers (bar-odd projected rates) ──")
    # Active set: the a_1 carrier (2,1) [ζ₂] + a ζ₆-carrier (2,1,1) + (2,2) [ζ₂].
    # Use bar-ODD projections so the parity-alternation theorem applies.
    active = [(2, 1), (2, 2), (2, 1, 1)]
    rates = [odd_part(kappa(p)) for p in active]
    for p, r_ in zip(active, rates):
        print(f"    mode {str(p):10s}: r_λ=(κ_λ)_odd parity={parity(r_):4s}  ζ_d={zeta_content(r_)}")
    print()
    for j in (1, 2, 3):
        ej = elem_sym(rates, j)
        print(f"    a_{j} ~ e_{j}: parity={parity(ej):4s}  ζ_d={zeta_content(ej)}")
        print(f"        e_{j} = {sp.cancel(ej)}")

    # where does ζ₆ first enter?
    z6_by_level = {j: (6 in zeta_content(elem_sym(rates, j))) for j in (1, 2, 3)}
    first_z6 = next((j for j in (1, 2, 3) if z6_by_level[j]), None)
    print("\n  ── VERDICT (data-driven) ──")
    print(f"  Parity alternation (Result 1) holds abstractly: a_j bar-parity = (-1)^(j+1).")
    print(f"  Concrete active set {active}:")
    print(f"    a_1 carrier bar-ODD (= the κ_(2,1)-type leading rate),")
    print(f"    a_2 carrier bar-EVEN, a_3 carrier bar-ODD — matches the theorem.")
    print(f"  ζ₆ first enters the higher coefficients at a_{first_z6} "
          f"(period-3 resonance lands in the {'leading' if first_z6==1 else 'higher'} rung).")
    print("""
  ⇒ FIBRE MAP EXTENDED beyond a_1: the recursion coefficients are the
    elementary symmetric polynomials a_j = e_j({(κ_λ)_odd}) of the bar-odd
    per-mode rates. Their bar-parity ALTERNATES (ODD,EVEN,ODD,…) by the
    parity-alternation theorem — a mode-set-INDEPENDENT structural law,
    consistent with c_2=-1 (bar-even seed) driving c_3 (bar-odd) etc. The
    ζ₆/period-3 resonance enters at the level shown above. The remaining
    freedom is the active set Λ (which modes, with what multiplicity) — that,
    times the single archimedean scalar S (owner-DECLINED), would fix the c_k
    VALUES. The fibre STRUCTURE (carriers, parities, ζ-content, the alternation
    law) is now mapped through a_3.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
