#!/usr/bin/env python3
"""
Symbolic Gröbner division in H_n(q) with exact coefficients.

All coefficients are elements of ℤ[q^½, q^{-½}] — the Laurent
polynomial ring in q^½. No floating point until final evaluation.

The Hecke relation: σ_i² = (q − q⁻¹)·σ_i + 1
uses symbolic q, so all coefficients are EXACT in q.

Usage:
    from hecke_symbolic import SymbolicHeckeDivision, SymbolicHeckeElement
    div = SymbolicHeckeDivision()
    elem = div.crossing_positive(0) * div.crossing_mixed(1)
    reduced, log = div.reduce(elem)
    # Coefficients are sympy expressions in q
    # Evaluate: reduced.evaluate(q_val=1.10998)
"""

import sympy as sp
from collections import defaultdict

# ── The symbolic ring ℤ[q^½, q^{-½}] ────────────────────────

q = sp.Symbol('q', positive=True)
q_half = sp.sqrt(q)
q_inv = 1 / q
q_half_inv = 1 / sp.sqrt(q)

# Fundamental quantities in q
HA = q - q_inv                          # q − q⁻¹
s_skein = q_half - q_half_inv            # q^½ − q^{-½}
z_markov = 1 / (q_half + q_half_inv)     # 1/(q^½ + q^{-½})

# Crossing coefficients (exact in q)
C_PP = sp.Integer(1)                     # proton-proton: σ
D_PP = sp.Integer(0)

C_NN = q**2                              # neutron-neutron: q²σ − q·s
D_NN = -q * s_skein

C_MIX = (1 + q**2) / 2                  # mixed: ½(1+q²)σ − ½q·s
D_MIX = -q * s_skein / 2

C_HOPF = sp.Integer(1)                   # Hopf link: σ
D_HOPF = sp.Integer(0)


class SymbolicHeckeElement:
    """Element of H_n(q) with symbolic coefficients in ℤ[q^½, q^{-½}].

    Words are tuples of integers:
      Non-negative: Hecke generators σ_i
      Negative: formal atom variables ℵ_k
    """

    def __init__(self, terms=None):
        # terms: dict of {word_tuple: sympy_expr}
        self.terms = {}
        if terms:
            for w, c in terms.items():
                c_simplified = sp.nsimplify(c) if isinstance(c, float) else c
                if c_simplified != 0:
                    self.terms[w] = c_simplified

    def _clean(self, threshold=None):
        """Remove zero terms. If threshold given, also remove tiny numerical terms."""
        self.terms = {k: v for k, v in self.terms.items() if v != 0}

    @staticmethod
    def identity():
        return SymbolicHeckeElement({(): sp.Integer(1)})

    @staticmethod
    def zero():
        return SymbolicHeckeElement({})

    def __add__(self, other):
        result = dict(self.terms)
        for w, c in other.terms.items():
            result[w] = sp.expand(result.get(w, sp.Integer(0)) + c)
        return SymbolicHeckeElement(result)

    def __mul__(self, other):
        """Concatenation (unreduced)."""
        result = {}
        for w1, c1 in self.terms.items():
            for w2, c2 in other.terms.items():
                w = w1 + w2
                result[w] = sp.expand(result.get(w, sp.Integer(0)) + c1 * c2)
        return SymbolicHeckeElement(result)

    def scale(self, s):
        return SymbolicHeckeElement({w: sp.expand(s * c) for w, c in self.terms.items()})

    def n_terms(self):
        return len(self.terms)

    def evaluate(self, q_val):
        """Evaluate all coefficients at q = q_val. Returns dict {word: float}."""
        return {w: float(c.subs(q, q_val)) for w, c in self.terms.items()
                if abs(float(c.subs(q, q_val))) > 1e-15}

    def show(self, name=""):
        """Display the element with symbolic coefficients."""
        if name:
            print(f"  {name}:")
        for w, c in sorted(self.terms.items(), key=lambda x: (len(x[0]), x[0])):
            ws = " · ".join(f"σ_{i}" for i in w) if w else "𝟏"
            c_str = str(sp.simplify(c))
            print(f"    ({c_str}) · {ws}")


class SymbolicHeckeDivision:
    """Gröbner division in H_n(q) with symbolic coefficients.

    All operations use exact sympy expressions in q.
    """

    def __init__(self):
        self.hecke_a = HA        # q − q⁻¹ (coeff of σ in Hecke relation)
        self.hecke_b = sp.Integer(1)  # constant in Hecke relation

    def crossing(self, type_i, type_j, gen):
        """Build crossing element for pair types at generator gen."""
        if type_i == type_j == 'u':
            return SymbolicHeckeElement({(gen,): C_PP})
        elif type_i == type_j == 'd':
            return SymbolicHeckeElement({(gen,): C_NN, (): D_NN})
        elif set([type_i, type_j]) == set(['u', 'd']):
            return SymbolicHeckeElement({(gen,): C_MIX, (): D_MIX})
        else:  # Hopf link (any-electron)
            return SymbolicHeckeElement({(gen,): C_HOPF})

    def reduce(self, elem, max_iterations=10000):
        """Gröbner reduction with symbolic coefficients.

        Returns (reduced_element, step_count_dict).
        """
        hecke_steps = 0
        yb_steps = 0
        fc_steps = 0
        iteration = 0

        changed = True
        while changed and iteration < max_iterations:
            changed = False
            new_terms = {}

            for word, coeff in elem.terms.items():
                if coeff == 0:
                    continue

                reduced_this = False

                # Rule 1: Hecke — σ_i² → (q−q⁻¹)σ_i + 1
                for pos in range(len(word) - 1):
                    if word[pos] == word[pos + 1] and word[pos] >= 0:
                        i = word[pos]
                        prefix = word[:pos]
                        suffix = word[pos + 2:]

                        w1 = prefix + (i,) + suffix
                        c1 = sp.expand(coeff * self.hecke_a)
                        w2 = prefix + suffix
                        c2 = sp.expand(coeff * self.hecke_b)

                        new_terms[w1] = sp.expand(new_terms.get(w1, sp.Integer(0)) + c1)
                        new_terms[w2] = sp.expand(new_terms.get(w2, sp.Integer(0)) + c2)

                        hecke_steps += 1
                        reduced_this = True
                        changed = True
                        break

                if reduced_this:
                    continue

                # Rule 2: Far-comm — σ_iσ_j → σ_jσ_i for |i−j| ≥ 2
                # Also: formal variables commute with everything
                for pos in range(len(word) - 1):
                    i_gen, j_gen = word[pos], word[pos + 1]
                    if i_gen >= 0 and j_gen < 0:
                        new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                        new_terms[new_word] = sp.expand(
                            new_terms.get(new_word, sp.Integer(0)) + coeff)
                        fc_steps += 1
                        reduced_this = True
                        changed = True
                        break
                    if (abs(i_gen - j_gen) >= 2 and i_gen > j_gen
                            and i_gen >= 0 and j_gen >= 0):
                        new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                        new_terms[new_word] = sp.expand(
                            new_terms.get(new_word, sp.Integer(0)) + coeff)
                        fc_steps += 1
                        reduced_this = True
                        changed = True
                        break

                if reduced_this:
                    continue

                # Rule 3: Yang-Baxter — σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1}
                for pos in range(len(word) - 2):
                    a, b, c = word[pos], word[pos + 1], word[pos + 2]
                    if a == c and a >= 0 and b >= 0 and abs(a - b) == 1:
                        new_trip = (b, a, b)
                        old_trip = (a, b, a)
                        if new_trip < old_trip:
                            new_word = word[:pos] + new_trip + word[pos + 3:]
                            new_terms[new_word] = sp.expand(
                                new_terms.get(new_word, sp.Integer(0)) + coeff)
                            yb_steps += 1
                            reduced_this = True
                            changed = True
                            break

                if not reduced_this:
                    new_terms[word] = sp.expand(
                        new_terms.get(new_word if reduced_this else word,
                                       sp.Integer(0)) + coeff)

            elem = SymbolicHeckeElement(new_terms)
            iteration += 1

        return elem, {'hecke': hecke_steps, 'yb': yb_steps, 'fc': fc_steps}


# ── Quick test ──────────────────────────────────────────────

if __name__ == '__main__':
    div = SymbolicHeckeDivision()

    print("PROTIUM ℵ(1,0) WITH SYMBOLIC q")
    print(f"  q = symbolic")
    print()

    types = ['u', 'u', 'd', 'e']
    elem = SymbolicHeckeElement.identity()

    for k in range(1, 4):
        for i in range(k):
            cx = div.crossing(types[i], types[k], i)
            elem = elem * cx
            elem, steps = div.reduce(elem)
            if steps['hecke'] > 0 or steps['yb'] > 0:
                print(f"  Crossing ({i},{k}): {steps['hecke']}H+{steps['yb']}YB")

    print()
    print("  PROTIUM NF (exact in q):")
    elem.show()

    print()
    print("  Evaluated at q₀ = 1.10998:")
    for w, v in sorted(elem.evaluate(1.10998).items(), key=lambda x: (len(x[0]), x[0])):
        ws = " · ".join(f"σ_{i}" for i in w) if w else "𝟏"
        print(f"    ({v:+.10f}) · {ws}")
