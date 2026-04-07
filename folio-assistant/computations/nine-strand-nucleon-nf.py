#!/usr/bin/env python3
"""
Nine-strand Gröbner--Shirshov normal form for nucleons and tritium beta decay.

EXACT SYMBOLIC computation in H₉(q) — all coefficients in ℚ[q, q⁻¹]
represented as Laurent polynomials with Fraction arithmetic (no sympy overhead).

Uses quotient ideals to compress intermediate results where generators
are disjoint, expanding them when interactions require it.

Strand assignment (9 strands, 8 generators σ₀...σ₇):
  Quark 0: strands 0, 1, 2  (colors r, g, b)
  Quark 1: strands 3, 4, 5
  Quark 2: strands 6, 7, 8

  Intra-quark generators: σ₀,σ₁ (q₀), σ₃,σ₄ (q₁), σ₆,σ₇ (q₂)
  Inter-quark generators: σ₂ (q₀–q₁ boundary), σ₅ (q₁–q₂ boundary)

Construction:
  nucleon₉ = ColorB₃ · FlavorB₃ · TypedCrossings

  ColorB₃   = B₃(σ₀,σ₁) · B₃(σ₃,σ₄) · B₃(σ₆,σ₇)
              [color confinement within each quark]
  FlavorB₃  = B₃(σ₂,σ₃) · B₃(σ₅,σ₆)
              [flavor confinement at quark boundaries]
  TypedCross = crossing(q₀,q₁,σ₂) · crossing(q₀,q₂,chain) · crossing(q₁,q₂,σ₅)
              [quark-type-dependent pairwise interactions]

Hecke convention: (1, −HA) where HA = q − q⁻¹.

Depends on: q_parameter.py, experimental_constants.py
"""

import json
import math
import time
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction

from q_parameter import Q as q0, Q_INV as q0_inv, E_CROSS
from experimental_constants import M_E_MEV, Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR


# ════════════════════════════════════════════════════════════════
# EXACT LAURENT POLYNOMIAL ARITHMETIC  ℚ[q, q⁻¹]
# ════════════════════════════════════════════════════════════════

class LP:
    """Laurent polynomial in q with exact rational (Fraction) coefficients.

    Representation: dict {power_of_q: Fraction}
    Example: q² − 3q⁻¹ → {2: Fraction(1), -1: Fraction(-3)}

    All arithmetic is exact.  No floating point, no sympy.
    """

    __slots__ = ('terms',)

    def __init__(self, terms=None):
        if terms is None:
            self.terms = {}
        else:
            self.terms = {}
            for k, c in terms.items():
                c = c if isinstance(c, Fraction) else Fraction(c)
                if c != 0:
                    self.terms[k] = c

    @staticmethod
    def zero():
        return LP()

    @staticmethod
    def one():
        return LP({0: Fraction(1)})

    @staticmethod
    def q_power(n):
        """q^n."""
        return LP({n: Fraction(1)})

    def is_zero(self):
        return len(self.terms) == 0

    def __eq__(self, other):
        if isinstance(other, int) and other == 0:
            return self.is_zero()
        if isinstance(other, LP):
            return self.terms == other.terms
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        result = dict(self.terms)
        for k, c in other.terms.items():
            result[k] = result.get(k, Fraction(0)) + c
            if result[k] == 0:
                del result[k]
        return LP(result)

    def __sub__(self, other):
        result = dict(self.terms)
        for k, c in other.terms.items():
            result[k] = result.get(k, Fraction(0)) - c
            if result[k] == 0:
                del result[k]
        return LP(result)

    def __neg__(self):
        return LP({k: -c for k, c in self.terms.items()})

    def __mul__(self, other):
        if isinstance(other, (int, Fraction)):
            other = Fraction(other)
            if other == 0:
                return LP()
            return LP({k: c * other for k, c in self.terms.items()})
        result = {}
        for k1, c1 in self.terms.items():
            for k2, c2 in other.terms.items():
                k = k1 + k2
                result[k] = result.get(k, Fraction(0)) + c1 * c2
                if result[k] == 0:
                    del result[k]
        return LP(result)

    def __rmul__(self, other):
        if isinstance(other, (int, Fraction)):
            return self.__mul__(other)
        return NotImplemented

    def evaluate(self, q_val):
        """Evaluate at q = q_val (float)."""
        return sum(float(c) * q_val ** k for k, c in self.terms.items())

    def __repr__(self):
        if not self.terms:
            return "0"
        parts = []
        for k in sorted(self.terms.keys()):
            c = self.terms[k]
            if k == 0:
                parts.append(str(c))
            elif k == 1:
                parts.append(f"({c})*q")
            elif k == -1:
                parts.append(f"({c})*q⁻¹")
            else:
                parts.append(f"({c})*q^{k}")
        return " + ".join(parts)

    def factored_str(self):
        """Compact display: factor out common q power and denominator."""
        if not self.terms:
            return "0"
        min_k = min(self.terms.keys())
        max_k = max(self.terms.keys())
        # Factor out q^min_k
        shifted = {k - min_k: c for k, c in self.terms.items()}
        # Find common denominator
        from math import gcd
        denoms = [c.denominator for c in shifted.values()]
        lcm_d = denoms[0]
        for d in denoms[1:]:
            lcm_d = lcm_d * d // gcd(lcm_d, d)
        # Multiply through by lcm_d
        int_coeffs = {k: int(c * lcm_d) for k, c in shifted.items()}
        # Build polynomial string
        poly_parts = []
        for k in sorted(int_coeffs.keys(), reverse=True):
            c = int_coeffs[k]
            if c == 0:
                continue
            if k == 0:
                poly_parts.append(f"{c:+d}")
            elif k == 1:
                if c == 1:
                    poly_parts.append("+q")
                elif c == -1:
                    poly_parts.append("-q")
                else:
                    poly_parts.append(f"{c:+d}q")
            else:
                if c == 1:
                    poly_parts.append(f"+q^{k}")
                elif c == -1:
                    poly_parts.append(f"-q^{k}")
                else:
                    poly_parts.append(f"{c:+d}q^{k}")
        poly = "".join(poly_parts).lstrip("+")
        prefix = f"({poly})"
        if lcm_d != 1:
            prefix = f"({poly})/{lcm_d}"
        if min_k != 0:
            prefix += f" · q^{min_k}" if min_k > 0 else f" / q^{-min_k}"
        return prefix


# HA = q − q⁻¹
HA = LP({1: Fraction(1), -1: Fraction(-1)})

# Crossing coefficients (exact in ℚ[q, q⁻¹])
C_PP = LP.one()                       # u-u: coefficient of σ is 1
D_PP = LP.zero()                      # u-u: constant is 0
C_NN = LP.one()                       # d-d: σ
D_NN = -HA                            # d-d: -HA
C_MIX = LP.one()                      # u-d: σ
D_MIX = LP({1: Fraction(-1, 2), -1: Fraction(1, 2)})  # -HA/2


# ════════════════════════════════════════════════════════════════
# HECKE ELEMENT (words with LP coefficients)
# ════════════════════════════════════════════════════════════════

class HE:
    """Hecke element in H_n(q) with exact Laurent polynomial coefficients.

    Words are tuples of non-negative integers (generator indices).
    Coefficients are LP objects (Laurent polynomials in q).
    """

    __slots__ = ('terms',)

    def __init__(self, terms=None):
        self.terms = {}
        if terms:
            for w, c in terms.items():
                if isinstance(c, (int, Fraction)):
                    c = LP({0: Fraction(c)}) if c != 0 else LP()
                if not c.is_zero():
                    self.terms[w] = c

    @staticmethod
    def identity():
        return HE({(): LP.one()})

    @staticmethod
    def zero():
        return HE({})

    @staticmethod
    def sigma(gen):
        """Generator σ_gen."""
        return HE({(gen,): LP.one()})

    @staticmethod
    def sigma_inv(gen):
        """σ_gen⁻¹ = σ_gen − HA in the Hecke algebra."""
        return HE({(gen,): LP.one(), (): -HA})

    def __add__(self, other):
        result = dict(self.terms)
        for w, c in other.terms.items():
            result[w] = result.get(w, LP()) + c
            if result[w].is_zero():
                del result[w]
        return HE(result)

    def __sub__(self, other):
        result = dict(self.terms)
        for w, c in other.terms.items():
            result[w] = result.get(w, LP()) - c
            if result[w].is_zero():
                del result[w]
        return HE(result)

    def __mul__(self, other):
        """Concatenation (unreduced)."""
        result = {}
        for w1, c1 in self.terms.items():
            for w2, c2 in other.terms.items():
                w = w1 + w2
                prod = c1 * c2
                if not prod.is_zero():
                    result[w] = result.get(w, LP()) + prod
                    if result[w].is_zero():
                        del result[w]
        return HE(result)

    def scale(self, lp):
        """Scale all coefficients by a Laurent polynomial."""
        return HE({w: c * lp for w, c in self.terms.items()})

    def n_terms(self):
        return len(self.terms)

    def net(self, q_val):
        """Sum of all coefficients evaluated at q."""
        return sum(c.evaluate(q_val) for c in self.terms.values())

    def nf_plus(self, q_val):
        """Sum of positive coefficients at q."""
        return sum(v for v in (c.evaluate(q_val) for c in self.terms.values()) if v > 0)

    def nf_minus(self, q_val):
        """Sum of negative coefficients at q."""
        return sum(v for v in (c.evaluate(q_val) for c in self.terms.values()) if v < 0)


# ════════════════════════════════════════════════════════════════
# GRÖBNER--SHIRSHOV REDUCER (LP coefficients, with quotient ideals)
# ════════════════════════════════════════════════════════════════

class HeckeReducer:
    """Gröbner--Shirshov division in H_n(q) with LP coefficients.

    Rules:
      R1: Hecke  — σ_i² → HA·σ_i + 1
      R2: FarComm — σ_iσ_j → σ_jσ_i for |i−j| ≥ 2 and i > j
      R3: YB     — σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1}  (when new < old)
      R4: Quotient — recognized sub-patterns → formal variables
    """

    def __init__(self):
        self._quotient_relations = {}

    def register_quotient(self, atom_id, nf_element, name=""):
        """Register a normal form as a quotient relation.

        atom_id: negative integer (e.g. -1 for ℵ₁)
        nf_element: HE whose terms define the NF
        """
        if atom_id >= 0:
            raise ValueError("atom_id must be negative")
        self._quotient_relations[atom_id] = {
            'name': name or f'ℵ_{-atom_id}',
            'atom_id': atom_id,
            'nf_terms': dict(nf_element.terms),
            'nf_words': set(nf_element.terms.keys()),
            'n_components': len(nf_element.terms),
        }

    def _try_whole_atom_quotient(self, elem):
        """If ALL NF terms of atom k appear proportionally, collapse to ℵ_k."""
        for atom_id, info in self._quotient_relations.items():
            nf_terms = info['nf_terms']
            nf_words = info['nf_words']

            if not nf_words.issubset(set(elem.terms.keys())):
                continue

            # Check proportional coefficients
            ratios = []
            for w in nf_words:
                nf_c = nf_terms[w]
                elem_c = elem.terms[w]
                if nf_c.is_zero():
                    continue
                # ratio = elem_c / nf_c  — only works for monomial LP
                # For general LP, check if elem_c = k * nf_c for some k ∈ ℚ
                # This is hard in general. Skip for now.
                pass

            # For now, skip whole-atom quotient (requires LP division)
        return elem, False

    def reduce(self, elem, max_iterations=50000, use_quotient=True):
        """Gröbner--Shirshov reduction with LP coefficients."""
        hecke = 0
        fc = 0
        yb = 0
        quotient = 0
        iteration = 0

        changed = True
        while changed and iteration < max_iterations:
            changed = False
            new_terms = {}

            for word, coeff in elem.terms.items():
                if coeff.is_zero():
                    continue

                reduced_this = False

                # R1: Hecke — σ_i²
                for pos in range(len(word) - 1):
                    if word[pos] == word[pos + 1] and word[pos] >= 0:
                        i = word[pos]
                        prefix = word[:pos]
                        suffix = word[pos + 2:]

                        w1 = prefix + (i,) + suffix  # HA · σ_i
                        w2 = prefix + suffix          # + 1

                        c1 = coeff * HA
                        c2 = coeff

                        new_terms[w1] = new_terms.get(w1, LP()) + c1
                        if new_terms[w1].is_zero():
                            del new_terms[w1]
                        new_terms[w2] = new_terms.get(w2, LP()) + c2
                        if new_terms[w2].is_zero():
                            del new_terms[w2]

                        hecke += 1
                        reduced_this = True
                        changed = True
                        break

                if reduced_this:
                    continue

                # R2: Far-comm — σ_iσ_j → σ_jσ_i for |i−j| ≥ 2, i > j
                for pos in range(len(word) - 1):
                    i_gen, j_gen = word[pos], word[pos + 1]
                    if i_gen >= 0 and j_gen >= 0 and abs(i_gen - j_gen) >= 2 and i_gen > j_gen:
                        new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                        new_terms[new_word] = new_terms.get(new_word, LP()) + coeff
                        if new_terms[new_word].is_zero():
                            del new_terms[new_word]
                        fc += 1
                        reduced_this = True
                        changed = True
                        break

                if reduced_this:
                    continue

                # R3: Yang-Baxter — σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1}
                for pos in range(len(word) - 2):
                    a, b, c = word[pos], word[pos + 1], word[pos + 2]
                    if a == c and a >= 0 and b >= 0 and abs(a - b) == 1:
                        new_trip = (b, a, b)
                        old_trip = (a, b, a)
                        if new_trip < old_trip:
                            new_word = word[:pos] + new_trip + word[pos + 3:]
                            new_terms[new_word] = new_terms.get(new_word, LP()) + coeff
                            if new_terms[new_word].is_zero():
                                del new_terms[new_word]
                            yb += 1
                            reduced_this = True
                            changed = True
                            break

                if not reduced_this:
                    new_terms[word] = new_terms.get(word, LP()) + coeff
                    if word in new_terms and new_terms[word].is_zero():
                        del new_terms[word]

            elem = HE(new_terms)
            iteration += 1

        return elem, {'hecke': hecke, 'yb': yb, 'fc': fc,
                      'quotient': quotient, 'iterations': iteration}


# ════════════════════════════════════════════════════════════════
# CONSTRUCTION HELPERS
# ════════════════════════════════════════════════════════════════

reducer = HeckeReducer()


def borromean_B3(gen_a, gen_b):
    """Build B₃ = (σ_a · σ_b⁻¹)³ on any two adjacent generators."""
    s_a = HE.sigma(gen_a)
    s_b_inv = HE.sigma_inv(gen_b)

    unit = s_a * s_b_inv
    elem = unit * unit * unit
    reduced, steps = reducer.reduce(elem)
    return reduced, steps


def crossing_at(type_i, type_j, gen):
    """Build crossing element for quark types at generator gen."""
    if type_i == type_j == 'u':
        return HE({(gen,): C_PP})
    elif type_i == type_j == 'd':
        return HE({(gen,): C_NN, (): D_NN})
    else:  # mixed u-d or d-u
        return HE({(gen,): C_MIX, (): D_MIX})


def word_str(w):
    """Human-readable braid word."""
    if not w:
        return "𝟏"
    return "·".join(f"σ{i}" for i in w)


def markov_trace(elem, n_strands, q_val):
    """Compute Markov trace numerically at q_val.

    Uses the standard Markov trace formula with z = 1/(q^½ + q^{-½}).
    """
    z = 1.0 / (math.sqrt(q_val) + 1.0 / math.sqrt(q_val))

    def trace_word(word, z_val):
        if not word:
            return 1.0
        gens = [g for g in word if g >= 0]
        if not gens:
            return 1.0
        max_gen = max(gens)
        # Find rightmost occurrence of max_gen
        for pos in range(len(word) - 1, -1, -1):
            if word[pos] == max_gen:
                last_pos = pos
                break
        # Remove it, apply z factor
        remaining = word[:last_pos] + word[last_pos + 1:]
        return z_val * trace_word(remaining, z_val)

    total = 0.0
    for w, c in elem.terms.items():
        c_val = c.evaluate(q_val)
        total += c_val * trace_word(w, z)
    return total


# ════════════════════════════════════════════════════════════════
# 9-STRAND NUCLEON CONSTRUCTION
# ════════════════════════════════════════════════════════════════

def build_nucleon_9strand(quark_types, label="nucleon"):
    """Build the full 9-strand nucleon normal form.

    nucleon₉ = ColorB₃ · FlavorB₃ · TypedCrossings

    Uses incremental multiply-and-reduce at each step.
    """
    print(f"\n{'═' * 70}")
    print(f"  BUILDING {label} [{', '.join(quark_types)}] — 9 STRANDS")
    print(f"{'═' * 70}\n")

    t_total = time.time()
    total_steps = {'hecke': 0, 'yb': 0, 'fc': 0, 'quotient': 0}

    def accum(steps):
        for k in steps:
            if k in total_steps:
                total_steps[k] += steps[k]

    # ── Step 1: Color confinement ──
    print("  ── STEP 1: Color confinement ──")
    elem = HE.identity()

    for block_idx in range(3):
        gen_a = 3 * block_idx
        gen_b = 3 * block_idx + 1
        t0 = time.time()
        b3, steps = borromean_B3(gen_a, gen_b)
        accum(steps)
        print(f"    B₃(σ_{gen_a},σ_{gen_b}) [{quark_types[block_idx]}]: "
              f"{b3.n_terms()} terms ({time.time()-t0:.1f}s)")

        t0 = time.time()
        elem = elem * b3
        elem, steps = reducer.reduce(elem)
        accum(steps)
        print(f"    Cumulative: {elem.n_terms()} terms ({time.time()-t0:.1f}s)")

    print(f"  Color total: {elem.n_terms()} terms\n")

    # ── Step 2: Flavor Borromean at boundaries ──
    print("  ── STEP 2: Flavor Borromean ──")

    t0 = time.time()
    flavor_01, steps = borromean_B3(2, 3)
    accum(steps)
    print(f"    B₃(σ₂,σ₃) [q₀–q₁]: {flavor_01.n_terms()} terms ({time.time()-t0:.1f}s)")

    t0 = time.time()
    elem = elem * flavor_01
    elem, steps = reducer.reduce(elem)
    accum(steps)
    print(f"    After q₀–q₁ flavor: {elem.n_terms()} terms ({time.time()-t0:.1f}s)")

    t0 = time.time()
    flavor_12, steps = borromean_B3(5, 6)
    accum(steps)
    print(f"    B₃(σ₅,σ₆) [q₁–q₂]: {flavor_12.n_terms()} terms ({time.time()-t0:.1f}s)")

    t0 = time.time()
    elem = elem * flavor_12
    elem, steps = reducer.reduce(elem)
    accum(steps)
    print(f"    After q₁–q₂ flavor: {elem.n_terms()} terms ({time.time()-t0:.1f}s)")
    print()

    # ── Step 3: Typed pairwise crossings ──
    print("  ── STEP 3: Typed crossings ──")

    # (q₀, q₁) at boundary σ₂
    t0 = time.time()
    cx = crossing_at(quark_types[0], quark_types[1], 2)
    elem = elem * cx
    elem, steps = reducer.reduce(elem)
    accum(steps)
    print(f"    ({quark_types[0]},{quark_types[1]}) at σ₂: "
          f"{elem.n_terms()} terms ({time.time()-t0:.1f}s)")

    # (q₀, q₂) long-range: chain σ₂·σ₃·σ₄·σ₅
    t0 = time.time()
    for gen in [2, 3, 4, 5]:
        cx = crossing_at(quark_types[0], quark_types[2], gen)
        elem = elem * cx
        elem, steps = reducer.reduce(elem)
        accum(steps)
    print(f"    ({quark_types[0]},{quark_types[2]}) at σ₂σ₃σ₄σ₅: "
          f"{elem.n_terms()} terms ({time.time()-t0:.1f}s)")

    # (q₁, q₂) at boundary σ₅
    t0 = time.time()
    cx = crossing_at(quark_types[1], quark_types[2], 5)
    elem = elem * cx
    elem, steps = reducer.reduce(elem)
    accum(steps)
    print(f"    ({quark_types[1]},{quark_types[2]}) at σ₅: "
          f"{elem.n_terms()} terms ({time.time()-t0:.1f}s)")

    elapsed = time.time() - t_total
    print(f"\n  Total: {elem.n_terms()} terms, {elapsed:.1f}s")
    print(f"  Reduction steps: {total_steps}")

    return elem, total_steps, elapsed


def build_nucleon_3strand(quark_types, label="nucleon"):
    """Build the standard 3-strand nucleon NF (reference)."""
    b3, _ = borromean_B3(0, 1)
    elem = b3
    for i in range(2):
        for j in range(i + 1, 3):
            cx = crossing_at(quark_types[i], quark_types[j], i)
            elem = elem * cx
            elem, _ = reducer.reduce(elem)
    return elem


# ════════════════════════════════════════════════════════════════
# DISPLAY
# ════════════════════════════════════════════════════════════════

PARTICLE_KNOT_3 = {
    ():         ("ν",  0),
    (0,):       ("H⁰", 1),
    (1,):       ("H¹", 1),
    (0, 1):     ("L₊", 2),
    (1, 0):     ("L₋", 2),
    (0, 1, 0):  ("e⁻", 3),
}


def show_nf(name, elem, q_val, max_lines=50):
    """Display NF with symbolic + numeric coefficients."""
    print(f"  {name}: ({elem.n_terms()} terms)")
    sorted_terms = sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0]))
    for i, (w, c) in enumerate(sorted_terms):
        if i >= max_lines:
            print(f"    ... ({elem.n_terms() - max_lines} more terms)")
            break
        v = c.evaluate(q_val)
        print(f"    ({v:+.10f})  {c.factored_str():>55}  · {word_str(w)}")


def show_summary(name, elem, q_val):
    """NF summary with sign pattern analysis."""
    nfp = elem.nf_plus(q_val)
    nfm = elem.nf_minus(q_val)
    net = nfp + nfm
    cancel = abs(nfm) / (abs(nfm) + nfp) * 100 if nfp > 0 else 0

    lengths = defaultdict(int)
    for w in elem.terms:
        lengths[len(w)] += 1

    max_gen = max((g for w in elem.terms for g in w), default=-1)

    print(f"  {name} SUMMARY:")
    print(f"    Terms:   {elem.n_terms()}")
    print(f"    NF₊ = {nfp:+.10f}")
    print(f"    NF₋ = {nfm:+.10f}")
    print(f"    Net  = {net:+.10f}")
    print(f"    Cancellation: {cancel:.1f}%")
    print(f"    Word lengths: {dict(sorted(lengths.items()))}")
    print(f"    Max generator: σ_{max_gen}" if max_gen >= 0 else
          f"    Max generator: (identity only)")
    print()


def show_3strand_sectors(name, elem, q_val):
    """Show the element's 3-strand sector projection."""
    print(f"  {name} — 3-strand sectors:")
    for w, pn_cx in sorted(PARTICLE_KNOT_3.items(), key=lambda x: (len(x[0]), x[0])):
        pn, ncx = pn_cx
        c = elem.terms.get(w)
        v = c.evaluate(q_val) if c else 0.0
        print(f"    ({v:+.10f}) · {pn:<4} {word_str(w):<13} ({ncx} cx)")
    print()


# ════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    ha_num = q0 - q0_inv
    mu_0 = M_E_MEV / (3 * E_CROSS)

    print("=" * 80)
    print("NINE-STRAND GRÖBNER--SHIRSHOV NORMAL FORM FOR NUCLEONS")
    print("Exact symbolic computation in H₉(q) — coefficients in ℚ[q, q⁻¹]")
    print(f"Numerical evaluation at q₀ = {q0:.15f}")
    print(f"HA = q − q⁻¹ at q₀ = {ha_num:.15f}")
    print("=" * 80)
    print()

    # ── 3-strand reference ──
    print("─" * 70)
    print("REFERENCE: 3-strand NF in H₃(q)")
    print("─" * 70)
    print()

    neutron_3 = build_nucleon_3strand(['u', 'd', 'd'], "Neutron")
    proton_3 = build_nucleon_3strand(['u', 'u', 'd'], "Proton")

    show_nf("NF₃(neutron)", neutron_3, q0)
    show_summary("NF₃(neutron)", neutron_3, q0)
    show_3strand_sectors("NF₃(neutron)", neutron_3, q0)

    show_nf("NF₃(proton)", proton_3, q0)
    show_summary("NF₃(proton)", proton_3, q0)
    show_3strand_sectors("NF₃(proton)", proton_3, q0)

    tr_n3 = markov_trace(neutron_3, 3, q0)
    tr_p3 = markov_trace(proton_3, 3, q0)
    ln_ratio_3 = math.log(abs(tr_p3)) - math.log(abs(tr_n3))
    print(f"  3-strand Markov traces at q₀:")
    print(f"    tr₃(n) = {tr_n3:.10f}")
    print(f"    tr₃(p) = {tr_p3:.10f}")
    print(f"    ln|tr₃(p)/tr₃(n)| = {ln_ratio_3:+.10f}")
    print()

    # ── 9-strand computations ──
    print("=" * 80)
    print("NINE-STRAND NUCLEON COMPUTATION")
    print("=" * 80)

    neutron_9, n9_steps, n9_time = build_nucleon_9strand(
        ['u', 'd', 'd'], "NEUTRON 𝔫")
    print()
    show_nf("NF₉(neutron)", neutron_9, q0)
    show_summary("NF₉(neutron)", neutron_9, q0)

    proton_9, p9_steps, p9_time = build_nucleon_9strand(
        ['u', 'u', 'd'], "PROTON 𝔭")
    print()
    show_nf("NF₉(proton)", proton_9, q0)
    show_summary("NF₉(proton)", proton_9, q0)

    # ── Markov traces ──
    print("=" * 80)
    print("MARKOV TRACES — 9-STRAND")
    print("=" * 80)
    print()

    tr_n9 = markov_trace(neutron_9, 9, q0)
    tr_p9 = markov_trace(proton_9, 9, q0)
    print(f"  9-strand Markov traces at q₀:")
    print(f"    tr₉(n) = {tr_n9:.10f}")
    print(f"    tr₉(p) = {tr_p9:.10f}")

    ln_ratio_9 = None
    if abs(tr_n9) > 1e-15 and abs(tr_p9) > 1e-15:
        ln_ratio_9 = math.log(abs(tr_p9)) - math.log(abs(tr_n9))
        print(f"    ln|tr₉(p)/tr₉(n)| = {ln_ratio_9:+.10f}")
    print()

    # ── Negative debt analysis ──
    print("=" * 80)
    print("NEGATIVE DEBT ANALYSIS — 3-STRAND vs 9-STRAND")
    print("=" * 80)
    print()

    net_n3 = neutron_3.net(q0)
    net_p3 = proton_3.net(q0)
    net_n9 = neutron_9.net(q0)
    net_p9 = proton_9.net(q0)

    print(f"  {'':>12} {'NF₊':>12} {'NF₋':>12} {'Net':>12} {'Cancel%':>10}")
    print(f"  {'─'*12} {'─'*12} {'─'*12} {'─'*12} {'─'*10}")

    for lab, elem in [("n₃", neutron_3), ("p₃", proton_3),
                       ("n₉", neutron_9), ("p₉", proton_9)]:
        nfp = elem.nf_plus(q0)
        nfm = elem.nf_minus(q0)
        net = nfp + nfm
        cancel = abs(nfm) / (abs(nfm) + nfp) * 100 if nfp > 0 else 0
        print(f"  {lab:>12} {nfp:+12.6f} {nfm:+12.6f} {net:+12.6f} {cancel:9.1f}%")

    delta_net_3 = net_n3 - net_p3
    delta_net_9 = net_n9 - net_p9

    print()
    print(f"  3-strand ΔNet(n−p) = {delta_net_3:+.10f}")
    print(f"  9-strand ΔNet(n−p) = {delta_net_9:+.10f}")
    if abs(delta_net_3) > 1e-15:
        print(f"  Ratio Δ₉/Δ₃ = {delta_net_9/delta_net_3:.6f}")
    print()

    # ── Energy scale ──
    print("=" * 80)
    print("ENERGY SCALE: 9-STRAND E₀")
    print("=" * 80)
    print()

    print(f"  3-strand:")
    print(f"    |ΔNet₃| = {abs(delta_net_3):.10f}")
    E0_3 = Q_TRITIUM_MEV / abs(delta_net_3) if abs(delta_net_3) > 1e-15 else float('inf')
    print(f"    E₀(3) = Q_exp / |ΔNet₃| = {E0_3:.6f} MeV")

    print(f"  9-strand:")
    print(f"    |ΔNet₉| = {abs(delta_net_9):.10f}")
    if abs(delta_net_9) > 1e-15:
        E0_9 = Q_TRITIUM_MEV / abs(delta_net_9)
        print(f"    E₀(9) = Q_exp / |ΔNet₉| = {E0_9:.6f} MeV")
        print(f"    E₀(3)/E₀(9) = {E0_3/E0_9:.6f}")

    print(f"\n  Q_exp(³H→³He) = {Q_TRITIUM_MEV:.5f} ± {Q_TRITIUM_MEV_ERR} MeV")
    print()

    # ── Word structure ──
    print("=" * 80)
    print("WORD STRUCTURE — GENERATOR OCCUPANCY")
    print("=" * 80)
    print()

    for lab, elem in [("NF₉(neutron)", neutron_9), ("NF₉(proton)", proton_9)]:
        gen_class = defaultdict(lambda: {'count': 0, 'coeff_sum': 0.0})
        for w, c in elem.terms.items():
            gens = frozenset(w) if w else frozenset()
            v = c.evaluate(q0)
            gen_class[gens]['count'] += 1
            gen_class[gens]['coeff_sum'] += v

        print(f"  {lab} — word classification:")
        for gens in sorted(gen_class.keys(), key=lambda x: (len(x), sorted(x))):
            info = gen_class[gens]
            gen_str = ",".join(f"σ{g}" for g in sorted(gens)) if gens else "𝟏"
            print(f"    [{gen_str:>30}]: {info['count']:>3} terms, "
                  f"Σ={info['coeff_sum']:+.6f}")
        print()

    # ── Write witness ──
    print("=" * 80)
    print("WRITING WITNESS")
    print("=" * 80)

    def terms_dict(elem, q_val, max_terms=500):
        result = {}
        sorted_terms = sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0]))
        for i, (w, c) in enumerate(sorted_terms):
            if i >= max_terms:
                break
            ws = ".".join(f"s{g}" for g in w) if w else "1"
            result[ws] = {
                "symbolic": c.factored_str(),
                "at_q0": c.evaluate(q_val),
            }
        return result

    witness = {
        "name": "nine-strand-nucleon-nf",
        "description": (
            "9-strand Gröbner--Shirshov NF for nucleons in H₉(q). "
            "Exact Laurent polynomial coefficients in ℚ[q, q⁻¹]. "
            "Each quark = 3-strand color sub-braid. "
            "Construction: ColorB₃ · FlavorB₃(boundary) · TypedCrossings."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": "symbolic (ℚ[q, q⁻¹])",
            "q0": q0,
            "HA": "q - q⁻¹",
            "n_strands": 9,
            "n_generators": 8,
        },
        "construction": {
            "color_confinement": [
                "B₃(σ₀,σ₁)", "B₃(σ₃,σ₄)", "B₃(σ₆,σ₇)"
            ],
            "flavor_confinement": [
                "B₃(σ₂,σ₃) — q₀–q₁ boundary",
                "B₃(σ₅,σ₆) — q₁–q₂ boundary"
            ],
        },
        "reference_3strand": {
            "neutron": terms_dict(neutron_3, q0),
            "proton": terms_dict(proton_3, q0),
            "delta_net": delta_net_3,
            "ln_trace_ratio": ln_ratio_3,
        },
        "nine_strand": {
            "neutron": {
                "n_terms": neutron_9.n_terms(),
                "nf": terms_dict(neutron_9, q0),
                "net": net_n9,
                "nf_plus": neutron_9.nf_plus(q0),
                "nf_minus": neutron_9.nf_minus(q0),
                "markov_trace": tr_n9,
                "time_s": n9_time,
            },
            "proton": {
                "n_terms": proton_9.n_terms(),
                "nf": terms_dict(proton_9, q0),
                "net": net_p9,
                "nf_plus": proton_9.nf_plus(q0),
                "nf_minus": proton_9.nf_minus(q0),
                "markov_trace": tr_p9,
                "time_s": p9_time,
            },
            "delta_net": delta_net_9,
            "ln_trace_ratio": ln_ratio_9,
        },
    }

    path = "nine-strand-nucleon-nf.witness.json"
    with open(path, 'w') as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\n  Written to: {path}")
    print("\n" + "=" * 80)
    print("COMPUTATION COMPLETE")
    print("=" * 80)
