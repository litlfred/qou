"""Closed form of the γγ-bonded deuteron trace under convention D, as a function of q (bean qou-sv7h).

PROBE, adopts nothing. Computes, exactly in ℚ[q, q⁻¹, (q²+1)⁻¹], the convention-D Ocneanu traces
of the proton block, the neutron block and the bonded deuteron word
`hecke_flint.atom_word("pn", [(0, 1)], "over")` (γγ bond V³ = (σσ⁻¹)³, owner rulings 2026-11-20 and
2026-11-22), through the Temperley–Lieb engine `hecke_tl` (exact at z_D = q³/(q²+1)).

Result (x = q²):
    tr_atom / (tr_p · tr_n) − 1 = (q²−1)⁵ (q⁸+q⁴+1) / (q² (q²+1) N(x)),
    N(x) = x⁷ − 3x⁶ + 4x⁵ − 4x⁴ + 5x³ − 4x² + 3x − 1,
and N(1+t) has all coefficients positive, so the ratio exceeds 1 for every q > 1: under the log
law B = E₀·ln(tr_free/tr_atom) the bond alone unbinds the deuteron at every q > 1. The Lean twin
`QOU/MassTheory/GammaGammaDeuteronUnbinds.lean` proves the inequality from these closed forms.

Checks
  K1  each closed form equals the independent permutation-basis engine hecke_flint, exactly, at
      q = 11/10, 3/2, 2, 5 (no float anywhere; ℚ arithmetic).
  K2  the factorisation of ratio − 1 above, and positivity of the shifted coefficients of N,
      of the proton numerator and of the extra deuteron factor.

Run: python3 -u deuteron_closed_form_probe.py
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import flint  # noqa: E402
import sympy as sp  # noqa: E402

import hecke_flint as F  # noqa: E402
import hecke_tl as T  # noqa: E402

X = flint.fmpq_poly([0, 1])
D = flint.fmpq_poly([1, 0, 1])


class E:
    """P / (q^a (q²+1)^b) with P an exact fmpq_poly."""
    __slots__ = ("p", "a", "b")

    def __init__(self, p, a=0, b=0):
        self.p = p if isinstance(p, flint.fmpq_poly) else flint.fmpq_poly([p])
        self.a, self.b = a, b

    def _lift(self, a, b):
        return self.p * X ** (a - self.a) * D ** (b - self.b)

    def __add__(self, o):
        o = o if isinstance(o, E) else E(o)
        a, b = max(self.a, o.a), max(self.b, o.b)
        return E(self._lift(a, b) + o._lift(a, b), a, b)

    __radd__ = __add__

    def __neg__(self):
        return E(-self.p, self.a, self.b)

    def __mul__(self, o):
        o = o if isinstance(o, E) else E(o)
        return E(self.p * o.p, self.a + o.a, self.b + o.b)

    __rmul__ = __mul__


class SymRing:
    def __init__(self):
        self.q = E(X)
        self.qi = E(flint.fmpq_poly([1]), 1, 0)
        self.d = E(D, 1, 0)
        self.di = E(X, 0, 1)
        self.one, self.zero = E(1), E(0)
        self.half = E(flint.fmpq_poly([flint.fmpq(1, 2)]))
        self.coef = {"S": self.q, "I": self.qi, "A": self.d * self.half}


q = sp.symbols("q")


def to_sympy(e):
    num = sum(sp.Rational(int(c.p), int(c.q)) * q ** i for i, c in enumerate(e.p.coeffs()))
    return sp.factor(num / (q ** e.a * (q ** 2 + 1) ** e.b))


def shifted_coeffs(poly_in_x):
    x, t = sp.symbols("x t")
    return [int(c) for c in sp.Poly(sp.expand(poly_in_x(x).subs(x, 1 + t)), t).all_coeffs()]


def main():
    R = SymRing()
    words = {"p": F.atom_word("p", [], "over"), "n": F.atom_word("n", [], "over"),
             "atom": F.atom_word("pn", [(0, 1)], "over")}
    progs = {"p": T.word_program(3, words["p"]), "n": T.word_program(3, words["n"]),
             "atom": T.atom_program("pn", [(0, 1)], "over")}
    tr = {k: to_sympy(T.sweep_trace(progs[k], R)[0]) for k in progs}
    for k, v in tr.items():
        print(f"tr_{k} = {v}")

    # K1: exact equality with hecke_flint at rational q
    k1 = True
    for qv in (sp.Rational(11, 10), sp.Rational(3, 2), sp.Integer(2), sp.Integer(5)):
        fq = flint.fmpq(int(qv.p), int(qv.q))
        for k in tr:
            n = 6 if k == "atom" else 3
            ref = F.evalq(F.tr(n, words[k]), fq)
            ok = tr[k].subs(q, qv) == sp.Rational(int(ref.p), int(ref.q))
            k1 &= bool(ok)
    print("K1 closed forms equal hecke_flint exactly at q = 11/10, 3/2, 2, 5:", k1)

    # K2: factorisation and positivity certificates
    x = sp.symbols("x")
    N = lambda y: y**7 - 3*y**6 + 4*y**5 - 4*y**4 + 5*y**3 - 4*y**2 + 3*y - 1  # noqa: E731
    mP = lambda y: (y**9 - 3*y**8 + 7*y**7 - 8*y**6 + 10*y**5 - 9*y**4 + 10*y**3  # noqa: E731
                    - 6*y**2 + 3*y - 1)
    mA = lambda y: (2*y**9 - 7*y**8 + 12*y**7 - 15*y**6 + 17*y**5 - 15*y**4 + 14*y**3  # noqa: E731
                    - 9*y**2 + 4*y - 1)
    target = (q**2 - 1)**5 * (q**8 + q**4 + 1) / (q**2 * (q**2 + 1) * N(q**2))
    ratio_m1 = sp.cancel(tr["atom"] / (tr["p"] * tr["n"]) - 1)
    k2_factor = sp.cancel(ratio_m1 - target) == 0
    k2_forms = (sp.cancel(tr["p"] - (q**4 + 1) * mP(q**2) / (4 * q**9 * (q**2 + 1)**2)) == 0
                and sp.cancel(tr["n"] - (q**4 + 1) * N(q**2) / (4 * q**9)) == 0
                and sp.cancel(tr["atom"] - (q**4 + 1)**2 * mP(q**2) * mA(q**2)
                              / (16 * q**20 * (q**2 + 1)**3)) == 0)
    shifts = {"N": shifted_coeffs(N), "mP": shifted_coeffs(mP), "mA": shifted_coeffs(mA)}
    k2_pos = all(c > 0 for v in shifts.values() for c in v)
    print("K2 ratio - 1 factorisation:", k2_factor, " closed forms match Lean defs:", k2_forms,
          " shifted coefficients positive:", k2_pos, shifts)
    checks = {"K1_equals_hecke_flint_exact": bool(k1), "K2_factorisation": bool(k2_factor),
              "K2_lean_closed_forms": bool(k2_forms), "K2_shifted_coeffs_positive": bool(k2_pos)}
    assert all(checks.values()), checks

    q0 = sp.Rational("1.1099785827513808")  # proton pin, 16 digits; display only
    out = {
        "bean": "qou-sv7h",
        "q0Anchor": "independent",
        "q0AnchorReason": "symbolic in q; the single q0 row is a 16-digit display of the proton pin",
        "rulings": ["γγ bond V³ = (σσ⁻¹)³ (owner rulings 2026-11-20, 2026-11-22)",
                    "convention D: z = q³/(q²+1)",
                    "log law B = E₀·ln(tr_free/tr_atom) (owner-rulings 2026-11-25)"],
        "tr_p": str(tr["p"]), "tr_n": str(tr["n"]), "tr_atom": str(tr["atom"]),
        "ratio_minus_one": str(sp.factor(ratio_m1)),
        "shifted_coefficients_x_eq_1_plus_t": shifts,
        "ratio_minus_one_at_q0_16digit_display": str(sp.N(target.subs(q, q0), 15)),
        "checks": checks,
        "lean": "qou:QOU.MassTheory.GammaGammaDeuteron.one_lt_ratio",
        "note": "PROBE. The bond alone raises the deuteron trace for every q > 1, so it unbinds under "
                "the log law; scope (b) for this word and trace only, says nothing about a closure "
                "with further terms. No fit, no selection; AME not used.",
    }
    with open(os.path.join(HERE, "deuteron-closed-form.witness.json"), "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    print("wrote deuteron-closed-form.witness.json")


if __name__ == "__main__":
    main()
