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

    Supports QUOTIENT IDEALS: register a normal form as a formal
    variable ℵ_k. When ALL NF terms appear as a complete sub-expression,
    they are collapsed to the single formal variable (whole-atom quotient).

    Supports STRUCTURAL IDEALS I₁-I₇: factor out universal operations
    (σ₀-extension, YB reordering, Borromean prefix, etc.) to reduce
    term count toward the n_strands target.
    """

    def __init__(self):
        self.hecke_a = HA        # q − q⁻¹ (coeff of σ in Hecke relation)
        self.hecke_b = sp.Integer(1)  # constant in Hecke relation

        # Quotient relations: atom_id → {name, nf_terms, n_components}
        self._quotient_relations = {}

        # Structural ideal generators I₁-I₇
        # Each is a function that identifies and collapses structural patterns
        self._structural_ideals = []

    # ── Quotient ideal: formal atom variables ────────────────────

    def register_quotient(self, atom_id, nf_element, name=""):
        """Register a normal form as a quotient relation (whole-atom).

        atom_id: negative integer (e.g. -1 for ℵ₁)
        nf_element: SymbolicHeckeElement whose terms define the NF
        name: human-readable name

        When ALL terms of the NF appear proportionally in an element,
        they are collapsed to the single formal variable ℵ_k.
        """
        if atom_id >= 0:
            raise ValueError("atom_id must be negative")

        self._quotient_relations[atom_id] = {
            'name': name or f'atom_{-atom_id}',
            'atom_id': atom_id,
            'nf_terms': dict(nf_element.terms),
            'nf_words': set(nf_element.terms.keys()),
            'n_components': len(nf_element.terms),
        }

    def _try_whole_atom_quotient(self, elem):
        """Try to identify a complete atom NF in elem and collapse it.

        Whole-atom quotient: if ALL NF terms of atom k appear in elem
        with consistent proportional coefficients, replace them all
        with a single formal variable ℵ_k scaled by the common factor.

        Returns (new_elem, did_reduce).
        """
        for atom_id, info in self._quotient_relations.items():
            nf_terms = info['nf_terms']
            nf_words = info['nf_words']

            # Check: are all NF words present in elem?
            if not nf_words.issubset(set(elem.terms.keys())):
                continue

            # Check proportional coefficients: elem[w] / nf[w] should be constant
            ratios = []
            for w in nf_words:
                nf_c = nf_terms[w]
                elem_c = elem.terms[w]
                if nf_c == 0:
                    continue
                ratio = sp.simplify(elem_c / nf_c)
                ratios.append(ratio)

            if not ratios:
                continue

            # All ratios should be equal (the common factor)
            common = ratios[0]
            all_equal = all(sp.simplify(r - common) == 0 for r in ratios[1:])

            if not all_equal:
                # Check if integer multiples work (multiple copies)
                continue

            # All NF terms present with consistent ratio → collapse
            new_terms = dict(elem.terms)
            for w in nf_words:
                del new_terms[w]

            # Add formal variable with common factor
            formal_word = (atom_id,)
            new_terms[formal_word] = (
                new_terms.get(formal_word, sp.Integer(0))
                + sp.expand(common)
            )

            return SymbolicHeckeElement(new_terms), True

        return elem, False

    def _try_subword_quotient(self, elem):
        """Try to replace registered NF sub-words with formal variables.

        Per-term sub-word rewriting: if an NF word appears as a sub-word
        of some term in elem, factor it out.

        Returns (new_elem, did_reduce).
        """
        for atom_id, info in self._quotient_relations.items():
            nf_terms = info['nf_terms']

            for nf_word, nf_coeff in nf_terms.items():
                if nf_coeff == 0 or len(nf_word) == 0:
                    continue
                nf_len = len(nf_word)

                for word, coeff in list(elem.terms.items()):
                    if coeff == 0 or len(word) < nf_len:
                        continue

                    for pos in range(len(word) - nf_len + 1):
                        if word[pos:pos + nf_len] == nf_word:
                            prefix = word[:pos]
                            suffix = word[pos + nf_len:]
                            new_word = prefix + (atom_id,) + suffix

                            new_terms = dict(elem.terms)
                            new_terms[word] = sp.expand(
                                new_terms.get(word, sp.Integer(0)) - coeff)
                            if sp.simplify(new_terms.get(word, 0)) == 0:
                                new_terms.pop(word, None)
                            new_terms[new_word] = sp.expand(
                                new_terms.get(new_word, sp.Integer(0)) + coeff)

                            return SymbolicHeckeElement(new_terms), True

        return elem, False

    def collapse_formal_powers(self, elem):
        """Collapse consecutive runs of the same formal variable.

        ℵ₁·ℵ₁·ℵ₁ → (ℵ₁, completeness=3)

        Each formal variable ℵ_k has n_components (from its NF).
        A run of length n means n of those components were matched.
        completeness = n / n_components.

        We use (atom_id * 1000 - completeness) as the collapsed ID.
        E.g. ℵ₁ with completeness 3 → formal var -1003.

        Returns (new_elem, n_collapses, collapse_info).
        """
        new_terms = {}
        n_collapses = 0
        collapse_info = []

        for word, coeff in elem.terms.items():
            if coeff == 0:
                continue

            new_word = []
            i = 0
            while i < len(word):
                if word[i] < 0:
                    atom_id = word[i]
                    run_len = 1
                    while i + run_len < len(word) and word[i + run_len] == atom_id:
                        run_len += 1

                    if run_len > 1:
                        # Collapse: annotate with completeness
                        collapsed_id = atom_id * 1000 - run_len
                        new_word.append(collapsed_id)
                        n_collapses += 1

                        # Track completeness relative to NF size
                        info = self._quotient_relations.get(atom_id)
                        if info:
                            n_comp = info['n_components']
                            collapse_info.append({
                                'atom': info['name'],
                                'run_len': run_len,
                                'n_components': n_comp,
                                'completeness': run_len / n_comp,
                            })
                    else:
                        new_word.append(atom_id)

                    i += run_len
                else:
                    new_word.append(word[i])
                    i += 1

            new_w = tuple(new_word)
            new_terms[new_w] = sp.expand(
                new_terms.get(new_w, sp.Integer(0)) + coeff)

        return SymbolicHeckeElement(new_terms), n_collapses, collapse_info

    def factor_content_classes(self, elem):
        """Group terms by generator content (same set of σ_i, different ordering).

        Terms in the same content class are related by YB reorderings.
        The DOMINANT word (largest coefficient) represents the class.

        Returns dict: {content_tuple: [(word, coeff), ...]}.
        """
        classes = {}
        for w, c in elem.terms.items():
            # Content = sorted tuple of non-negative generators
            content = tuple(sorted(g for g in w if g >= 0))
            classes.setdefault(content, []).append((w, c))

        # Sort each class by coefficient magnitude (symbolic: use term count as proxy)
        for content in classes:
            classes[content].sort(key=lambda x: len(str(x[1])))

        return classes

    # ── Structural ideals I₁-I₇ ──────────────────────────────────

    def register_structural_ideal(self, name, pattern_fn):
        """Register a structural ideal generator.

        pattern_fn: callable(elem) → (new_elem, did_reduce)
        """
        self._structural_ideals.append({'name': name, 'fn': pattern_fn})

    def setup_standard_ideals(self):
        """Register the standard structural ideals I₁-I₇.

        These encode universal operations found in all atomic NFs:
          I₁: σ₀-extension (prepend leading quark crossing)
          I₂: YB reordering (Yang-Baxter related families)
          I₃: B₃ Borromean prefix (σ₀·σ₁·σ₀ proton core)
          I₄: 𝔫₁ neutron tail (σ₃·σ₄·σ₃·σ₅)
          I₅: Protium completeness (ℵ₁ⁿ counting)
          I₆: Structural defects (missing bond patterns)
          I₇: Electron bridge (σ₂·σ₃·σ₂ Borromean bridge)
        """

        def I1_sigma0_extension(elem):
            """I₁: Factor out σ₀-extension pairs.

            If two terms differ only by σ₀ prefix, they're in the same
            I₁ family. Collapse: c₁·w + c₂·σ₀·w → (c₁ + c₂/r₁)·w
            where r₁ is the universal extension ratio.
            """
            r1 = sp.Rational(315, 1000)  # +0.315 universal ratio (approx)
            new_terms = dict(elem.terms)
            did_reduce = False

            for word, coeff in list(elem.terms.items()):
                if coeff == 0:
                    continue
                # Check if σ₀·word also exists
                ext_word = (0,) + word
                if ext_word in new_terms and new_terms[ext_word] != 0:
                    ext_coeff = new_terms[ext_word]
                    # Check if ratio matches I₁
                    if word and len(word) > 0:
                        expected_ratio = sp.simplify(ext_coeff / coeff)
                        # If close to r₁, collapse
                        # For symbolic, we keep as-is but mark
                        pass  # TODO: symbolic ratio check

            return elem, False  # placeholder

        def I7_electron_bridge(elem):
            """I₇: Collapse σ₂·σ₃·σ₂ Borromean bridge sub-words."""
            bridge = (2, 3, 2)  # σ₂·σ₃·σ₂
            new_terms = dict(elem.terms)
            did_reduce = False

            for word, coeff in list(elem.terms.items()):
                if coeff == 0 or len(word) < 3:
                    continue
                for pos in range(len(word) - 2):
                    if word[pos:pos + 3] == bridge:
                        # This is a YB-reducible pattern → already handled by R3
                        # I₇ tracks it as a structural annotation
                        break

            return elem, False  # annotation only for now

        def I4_neutron_tail(elem):
            """I₄: Factor out neutron tail σ₃·σ₄·σ₃·σ₅.

            Terms containing the neutron tail sub-word can be factored
            as (prefix) · 𝔫₁ · (suffix). The 66/210 split in deuterium
            families: 66 complete (with 𝔫₁), 210 incomplete.
            """
            tail = (3, 4, 3, 5)
            new_terms = dict(elem.terms)
            did_reduce = False

            for word, coeff in list(elem.terms.items()):
                if coeff == 0 or len(word) < 4:
                    continue
                sigma_positions = [(i, word[i]) for i in range(len(word)) if word[i] >= 0]
                # Check contiguous sub-words
                for pos in range(len(word) - 3):
                    if word[pos:pos + 4] == tail:
                        # Replace with formal neutron tail variable (-2)
                        prefix = word[:pos]
                        suffix = word[pos + 4:]
                        new_word = prefix + (-2,) + suffix
                        del new_terms[word]
                        new_terms[new_word] = sp.expand(
                            new_terms.get(new_word, sp.Integer(0)) + coeff)
                        did_reduce = True
                        break
                if did_reduce:
                    break

            return SymbolicHeckeElement(new_terms), did_reduce

        # Register (placeholders — will be filled as patterns emerge)
        self.register_structural_ideal('I1_sigma0_ext', I1_sigma0_extension)
        self.register_structural_ideal('I4_neutron_tail', I4_neutron_tail)
        self.register_structural_ideal('I7_electron_bridge', I7_electron_bridge)

    def apply_structural_ideals(self, elem, max_passes=100):
        """Apply all registered structural ideals until convergence.

        Returns (new_elem, total_reductions, log).
        """
        total = 0
        log = []
        for _ in range(max_passes):
            any_reduced = False
            for ideal in self._structural_ideals:
                new_elem, did_reduce = ideal['fn'](elem)
                if did_reduce:
                    elem = new_elem
                    total += 1
                    log.append(ideal['name'])
                    any_reduced = True
                    break
            if not any_reduced:
                break
        return elem, total, log

    def extract_completeness_layers(self, elem, atom_id=-1):
        """Separate an element into completeness layers.

        For each term, count how many instances of ℵ_k appear.
        Group terms by this count.

        Returns dict: {n_formal: SymbolicHeckeElement}
        """
        layers = {}
        for word, coeff in elem.terms.items():
            n_formal = sum(1 for g in word if g == atom_id)
            if n_formal not in layers:
                layers[n_formal] = {}
            layers[n_formal][word] = coeff

        return {k: SymbolicHeckeElement(v) for k, v in layers.items()}

    # ── Crossing constructors ────────────────────────────────────

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

    def reduce(self, elem, max_iterations=10000, use_quotient=True):
        """Gröbner reduction with symbolic coefficients.

        Applies rules in order:
          R1: Hecke — σ_i² → (q−q⁻¹)σ_i + 1
          R2: Far-comm — σ_iσ_j → σ_jσ_i for |i−j| ≥ 2
          R3: Yang-Baxter — σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1}
          R4: Quotient — whole-atom NF → ℵ_k (if enabled)

        Returns (reduced_element, step_count_dict).
        """
        hecke_steps = 0
        yb_steps = 0
        fc_steps = 0
        quotient_steps = 0
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

            # Rule 4: Quotient reduction (after standard reduction pass)
            if use_quotient and self._quotient_relations:
                # Try whole-atom quotient first
                elem, did_q = self._try_whole_atom_quotient(elem)
                if did_q:
                    quotient_steps += 1
                    changed = True
                    continue

                # Then try sub-word quotient
                q_changed = True
                while q_changed:
                    elem, q_changed = self._try_subword_quotient(elem)
                    if q_changed:
                        quotient_steps += 1
                        changed = True

        return elem, {'hecke': hecke_steps, 'yb': yb_steps, 'fc': fc_steps,
                      'quotient': quotient_steps}

    # ── Markov trace ─────────────────────────────────────────────

    def markov_trace(self, elem, n_strands):
        """Compute Markov trace with symbolic coefficients."""
        total = sp.Integer(0)
        for word, coeff in elem.terms.items():
            total += coeff * self._trace_word(word, n_strands)
        return sp.simplify(total)

    def _trace_word(self, word, n_strands):
        """Recursive Markov trace of a braid monomial."""
        if not word:
            return sp.Integer(1)

        # Filter to non-negative generators (skip formal variables)
        gens = [g for g in word if g >= 0]
        if not gens:
            return sp.Integer(1)

        max_gen = max(gens)
        effective_n = max_gen + 2
        if n_strands > effective_n:
            n_strands = effective_n

        last_max_pos = len(word) - 1 - list(reversed(word)).index(max_gen)
        rotated = word[last_max_pos + 1:] + word[:last_max_pos]
        return z_markov * self._trace_word(rotated, n_strands)


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
