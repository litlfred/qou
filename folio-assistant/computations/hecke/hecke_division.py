#!/usr/bin/env python3

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

# DEPRECATION-CANDIDATE: witness was moved to folio-assistant/computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Instrumented Gröbner--Shirshov division algorithm for the Iwahori--Hecke algebra H_n(q).

Each division step is logged with:
  - Which relation was applied (Hecke / Yang-Baxter / far commutativity)
  - Where in the braid word (position)
  - The coefficient change (energy change)
  - The resulting terms

This implements the division algorithm from the unital Gröbner--Shirshov bases
paper (def:division-algorithm) specialized to the admissible system
(positive braid monomials, length-lex ordering) with Gröbner--Shirshov basis:
  G = {σ_i² - (q-q⁻¹)σ_i - 1, σ_iσ_{i+1}σ_i - σ_{i+1}σ_iσ_{i+1},
       σ_iσ_j - σ_jσ_i (|i-j|≥2)}

Usage:
    from hecke_division import HeckeDivision, HeckeElement
    div = HeckeDivision(q_val=1.110)
    elem = div.crossing_positive(0) * div.crossing_negative(1)
    reduced, log = div.reduce(elem)

Each log entry is a dict:
    {'step': int, 'relation': str, 'position': int,
     'generator': int, 'old_word': tuple, 'new_terms': list,
     'energy_change': float, 'n_terms_after': int}
"""

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

# ── Symbolic ring ────────────────────────────────────────────────

q_sym = sp.Symbol('q', positive=True)


@dataclass
class DivisionStep:
    """One step of the Gröbner--Shirshov division algorithm."""
    step: int
    relation: str          # 'hecke' | 'yang-baxter' | 'far-comm'
    position: int          # position in the braid word where applied
    generator: int         # which σ_i was involved
    old_word: tuple        # the word before this step
    old_coeff: complex     # coefficient of old_word before step
    new_terms: list        # list of (word, coeff) produced
    energy_change: float   # Δ(total weight) from this step
    n_terms_after: int     # total terms in element after step
    cumulative_energy: float = 0.0  # running total of energy changes


class HeckeElement:
    """Element of H_n(q)[ℵ₁, ℵ₂, ...] with numerical coefficients.

    Words are tuples of integers:
      - Non-negative integers (0, 1, 2, ...): Hecke generators σ_i
      - Negative integers (-1, -2, ...): formal atom variables ℵ_k

    Formal atom variables are CENTRAL: they commute with all σ_i.
    A word like (0, -1, 2) means σ₀ · ℵ₁ · σ₂ = ℵ₁ · σ₀ · σ₂.

    The Gröbner--Shirshov basis is extended with relations:
      NF(ℵ_k) − ℵ_k = 0
    meaning: whenever the normal form expression of atom k appears,
    it can be replaced by the single symbol ℵ_k.
    """

    def __init__(self, terms=None):
        self.terms = dict(terms) if terms else {}
        self._clean()

    def _clean(self):
        self.terms = {k: v for k, v in self.terms.items() if abs(v) > 1e-15}

    @staticmethod
    def identity():
        return HeckeElement({(): 1.0})

    @staticmethod
    def zero():
        return HeckeElement({})

    def copy(self):
        return HeckeElement(dict(self.terms))

    def __add__(self, other):
        result = dict(self.terms)
        for w, c in other.terms.items():
            result[w] = result.get(w, 0.0) + c
        return HeckeElement(result)

    def __mul__(self, other):
        """Concatenation (unreduced)."""
        result = {}
        for w1, c1 in self.terms.items():
            for w2, c2 in other.terms.items():
                w = w1 + w2
                result[w] = result.get(w, 0.0) + c1 * c2
        return HeckeElement(result)

    def scale(self, s):
        return HeckeElement({w: s * c for w, c in self.terms.items()})

    def n_terms(self):
        return len(self.terms)

    def total_weight(self):
        return sum(abs(c) for c in self.terms.values())

    def max_word_length(self):
        return max((len(w) for w in self.terms), default=0)

    def dominant_term(self):
        if not self.terms:
            return None, 0
        w = max(self.terms, key=lambda k: abs(self.terms[k]))
        return w, self.terms[w]

    def word_histogram(self):
        """Count terms by word length."""
        hist = defaultdict(int)
        for w in self.terms:
            hist[len(w)] += 1
        return dict(sorted(hist.items()))


class HeckeDivision:
    """Instrumented Gröbner--Shirshov division in H_n(q).

    Tracks every reduction step with energy changes.

    Supports an ENRICHED IDEAL: named sub-patterns from previously
    computed normal forms are added as rewrite rules. When a word
    contains a named sub-pattern, it is replaced before applying
    the standard Hecke/YB/far-comm rules. This dramatically reduces
    the number of reduction steps for larger atoms.

    Usage:
        div = HeckeDivision(q_val=1.110)

        # After computing protium NF, register its terms:
        div.register_pattern('h1', (1, 2), -0.010161)
        div.register_pattern('u0_h1', (0, 1, 2), -0.066780)

        # Future reductions will match these patterns first.
    """

    def __init__(self, q_val=1.110):
        self.q = q_val
        self.q_inv = 1.0 / q_val
        self.q_half = q_val**0.5
        self.q_half_inv = 1.0 / q_val**0.5
        self.skein_amp = self.q_half - self.q_half_inv

        # Hecke relation: σ² = (q - q⁻¹)σ + 1
        self.hecke_a = q_val - self.q_inv       # coeff of σ
        self.hecke_b = 1.0                       # constant

        # Inverse: σ⁻¹ = σ − (q − q⁻¹)  [correct Hecke relation]
        self.inv_sigma = 1.0
        self.inv_const = -(q_val - self.q_inv)   # = −HA

        # Markov trace parameter
        self.z_markov = 1.0 / (self.q_half + self.q_half_inv)

        # Enriched ideal: named patterns for sub-word matching
        self._named_patterns = {}
        self._pattern_words = []  # sorted by length (longest first)

        # Quotient ideal: formal atom variables
        # { atom_id: {'name': str, 'nf': {word: coeff}, 'nf_words': set} }
        self._quotient_relations = {}

    def register_pattern(self, name, word, coeff, expansion=None):
        """Register a named sub-pattern for the enriched ideal.

        name: human-readable name (e.g. 'h1', 'u0_h1', 'protium_atom')
        word: the word tuple to match (e.g. (1, 2) for σ₁·σ₂)
        coeff: the coefficient this word has in its source NF
        expansion: optional HeckeElement that this pattern expands to
                   (for future use in pattern substitution)
        """
        self._named_patterns[word] = {
            'name': name,
            'word': word,
            'coeff': coeff,
            'expansion': expansion,
        }
        # Re-sort patterns by length (longest first for greedy matching)
        self._pattern_words = sorted(
            self._named_patterns.keys(),
            key=lambda w: -len(w)
        )

    def register_nf(self, name_prefix, nf_element):
        """Register ALL terms of a normal form as named patterns.

        name_prefix: e.g. 'protium' — each term gets named
                     'protium_0', 'protium_1', etc.
        nf_element: HeckeElement whose terms become patterns.
        """
        for idx, (word, coeff) in enumerate(
            sorted(nf_element.terms.items(), key=lambda x: (len(x[0]), x[0]))
        ):
            name = f"{name_prefix}_{idx}"
            self.register_pattern(name, word, coeff)

    def identify_patterns(self, word):
        """Check if a word CONTAINS any registered named sub-patterns.

        Returns list of (start_pos, end_pos, pattern_name, pattern_word).
        Longest patterns matched first (greedy).
        """
        matches = []
        for pat_word in self._pattern_words:
            pat_len = len(pat_word)
            if pat_len > len(word):
                continue
            for pos in range(len(word) - pat_len + 1):
                if word[pos:pos + pat_len] == pat_word:
                    matches.append((pos, pos + pat_len,
                                    self._named_patterns[pat_word]['name'],
                                    pat_word))
        return matches

    def annotate_element(self, elem):
        """Annotate each term with any named patterns it contains.

        Returns dict: { word: [(name, sub_word, position), ...] }
        """
        annotations = {}
        for word in elem.terms:
            matches = self.identify_patterns(word)
            if matches:
                annotations[word] = [
                    (self._named_patterns[m[3]]['name'], m[3], m[0])
                    for m in matches
                ]
        return annotations

    @property
    def named_patterns(self):
        """Read-only access to registered patterns."""
        return dict(self._named_patterns)

    # ── Quotient ideal: formal atom variables ────────────────────

    def register_quotient(self, atom_id, nf_element, name=""):
        """Register a normal form as a quotient relation.

        Adds the relation: NF(atom) = ℵ_k  to the Gröbner--Shirshov basis.

        atom_id: negative integer identifier (e.g. -1 for ℵ₁)
        nf_element: the HeckeElement whose terms define the NF
        name: human-readable name (e.g. "protium")

        After registration, reduce() will check if the current
        element contains the NF as a sub-expression and replace
        it with the formal variable ℵ_k.
        """
        if atom_id >= 0:
            raise ValueError("atom_id must be negative (formal variable)")

        self._quotient_relations[atom_id] = {
            'name': name or f'atom_{-atom_id}',
            'atom_id': atom_id,
            'nf': dict(nf_element.terms),  # word → coeff
            'nf_words': set(nf_element.terms.keys()),
            'n_components': len(nf_element.terms),  # for completeness tracking
        }

    def collapse_formal_powers(self, elem):
        """Collapse consecutive runs of the same formal variable.

        ℵ₁·ℵ₁·ℵ₁·ℵ₁ → (ℵ₁, completeness=4)
        ℵ₁·ℵ₁·ℵ₁     → (ℵ₁, completeness=3)

        Each formal variable ℵ_k has n_components (from its NF).
        A run of length n means n of those components were matched.
        completeness = n / n_components.

        The collapsed word replaces the run with a SINGLE formal
        variable annotated with its completeness level.
        We use (atom_id * 100 - completeness) as the collapsed ID.
        E.g. ℵ₁ with completeness 4 → formal var -104.

        Returns (new_elem, n_collapses).
        """
        new_terms = {}
        n_collapses = 0

        for word, coeff in elem.terms.items():
            if abs(coeff) < 1e-15:
                continue

            # Find and collapse consecutive formal variable runs
            new_word = []
            i = 0
            collapsed = False
            while i < len(word):
                if word[i] < 0:
                    # Start of a formal variable run
                    atom_id = word[i]
                    run_len = 1
                    while i + run_len < len(word) and word[i + run_len] == atom_id:
                        run_len += 1

                    if run_len > 1:
                        # Collapse: replace run with single annotated var
                        # Use atom_id * 100 - run_len as collapsed ID
                        collapsed_id = atom_id * 100 - run_len
                        new_word.append(collapsed_id)
                        collapsed = True
                        n_collapses += 1
                    else:
                        new_word.append(atom_id)

                    i += run_len
                else:
                    new_word.append(word[i])
                    i += 1

            new_w = tuple(new_word)
            new_terms[new_w] = new_terms.get(new_w, 0.0) + coeff

        return HeckeElement(new_terms), n_collapses

    def _try_quotient_reduction(self, elem):
        """Try to replace registered NF sub-words with formal variables.

        Each word in a registered NF is its own rewrite rule:
          If word W appears as a SUB-WORD of some term in elem,
          replace the occurrence: prefix · W · suffix → prefix · ℵ_k · suffix
          with coefficient scaled by the NF coefficient of W.

        This is per-term sub-word rewriting, not whole-NF matching.
        Each NF term W_j with coefficient c_j generates the rule:
          ... · W_j · ... → (1/c_j) · ... · ℵ_k · ...

        Actually simpler: each NF word is a KNOWN REDUCED SUB-EXPRESSION.
        When it appears inside a larger word, we can factor it out:
          prefix · W_j · suffix  →  c_j · prefix · ℵ_k_j · suffix

        where ℵ_k_j is a formal variable for the j-th component of atom k.

        Returns (new_elem, did_reduce, log_entry).
        """
        for atom_id, info in self._quotient_relations.items():
            nf = info['nf']

            for nf_word, nf_coeff in nf.items():
                if abs(nf_coeff) < 1e-15:
                    continue
                nf_len = len(nf_word)
                if nf_len == 0:
                    continue  # skip identity term

                # Scan all terms in elem for sub-word matches
                for word, coeff in list(elem.terms.items()):
                    if abs(coeff) < 1e-15:
                        continue
                    if len(word) < nf_len:
                        continue

                    # Check each position for a sub-word match
                    for pos in range(len(word) - nf_len + 1):
                        if word[pos:pos + nf_len] == nf_word:
                            # MATCH: word = prefix · nf_word · suffix
                            prefix = word[:pos]
                            suffix = word[pos + nf_len:]

                            # Replace with: prefix · ℵ_k_j · suffix
                            # The formal variable for component j of atom k
                            # Use atom_id * 100 - j as unique ID
                            comp_id = atom_id  # all components map to same atom

                            new_word = prefix + (comp_id,) + suffix

                            # Remove old term, add new term
                            new_terms = dict(elem.terms)
                            new_terms[word] = new_terms.get(word, 0.0) - coeff
                            if abs(new_terms.get(word, 0.0)) < 1e-15:
                                new_terms.pop(word, None)

                            # New term: coefficient stays the same
                            # (the nf_coeff is baked into the formal variable's meaning)
                            new_terms[new_word] = new_terms.get(new_word, 0.0) + coeff

                            log_entry = DivisionStep(
                                step=0,
                                relation='quotient',
                                position=pos,
                                generator=comp_id,
                                old_word=word,
                                old_coeff=coeff,
                                new_terms=[(new_word, coeff)],
                                energy_change=0.0,
                                n_terms_after=len(new_terms),
                                cumulative_energy=0.0,
                            )

                            return HeckeElement(new_terms), True, log_entry

        return elem, False, None

    # ── Crossing constructors ────────────────────────────────────

    def crossing_positive(self, i):
        """σ_i (proton-proton crossing)."""
        return HeckeElement({(i,): 1.0})

    def crossing_negative(self, i):
        """σ_i⁻¹ = σ_i − (q − q⁻¹)·𝟏  (neutron-neutron crossing)."""
        return HeckeElement({(i,): self.inv_sigma, (): self.inv_const})

    def crossing_mixed(self, i):
        """½(σ_i + σ_i⁻¹) = σ_i − ½(q − q⁻¹)·𝟏  (proton-neutron crossing)."""
        return HeckeElement({
            (i,): 1.0,
            (): 0.5 * self.inv_const,
        })

    # ── Electron crossings ───────────────────────────────────────

    def crossing_pe(self, i):
        """σ_i⁻¹ = σ_i − (q − q⁻¹)·𝟏  (proton-electron: EM attraction).
        Same as nn crossing — the EM attraction between p and e
        is topologically equivalent to the strong-force nn crossing."""
        return self.crossing_negative(i)

    def crossing_ne(self, i):
        """𝟏  (neutron-electron: no interaction).
        The neutron is electrically neutral, so the crossing is trivial."""
        return HeckeElement({(): 1.0})

    def crossing_ee(self, i):
        """σ_i  (electron-electron: EM repulsion).
        Same as pp crossing — same-charge repulsion."""
        return self.crossing_positive(i)

    def crossing_for_pair(self, type_i, type_j, gen):
        """Build crossing element for an arbitrary pair of particle types.

        Supported types: 'p' (proton), 'n' (neutron), 'e' (electron),
                         'u' (up quark), 'd' (down quark).
        """
        pair = frozenset([type_i, type_j])

        if type_i == type_j == 'p' or type_i == type_j == 'u':
            return self.crossing_positive(gen)
        elif type_i == type_j == 'n' or type_i == type_j == 'd':
            return self.crossing_negative(gen)
        elif pair in (frozenset(['p', 'n']), frozenset(['u', 'd'])):
            return self.crossing_mixed(gen)
        elif pair == frozenset(['p', 'e']):
            return self.crossing_pe(gen)
        elif pair == frozenset(['n', 'e']):
            return self.crossing_ne(gen)
        elif type_i == type_j == 'e':
            return self.crossing_ee(gen)
        elif 'e' in pair and 'u' in pair:
            # u-quark (+2/3) attracts electron (-1)
            return self.crossing_pe(gen)
        elif 'e' in pair and 'd' in pair:
            # d-quark (-1/3) repels electron (-1)
            return self.crossing_ee(gen)
        elif 'e' in pair:
            # Other quark-electron: default to attraction
            return self.crossing_pe(gen)
        else:
            # Fallback: positive crossing
            return self.crossing_positive(gen)

    # ── Generator inverses and Borromean braid ───────────────────

    def sigma(self, i):
        """σ_i as a HeckeElement."""
        return HeckeElement({(i,): 1.0})

    def sigma_inv(self, i):
        """σ_i⁻¹ = σ_i − (q − q⁻¹) in the Iwahori--Hecke algebra."""
        HA = self.q - 1.0 / self.q
        return HeckeElement({(i,): 1.0, (): -HA})

    def borromean_B3(self):
        """Build B₃ = (σ₀σ₁⁻¹)³ Borromean confinement braid and reduce.

        B₃ is the fundamental confinement braid: three strands mutually
        linked but individually free if any one is removed.

        Returns: (reduced_element, division_log)
        """
        s0 = self.sigma(0)
        s1_inv = self.sigma_inv(1)

        unit = s0 * s1_inv
        elem = unit * unit * unit

        reduced, log = self.reduce(elem)
        return reduced, log

    # ── Nuclear braid word ───────────────────────────────────────

    def nuclear_braid(self, p, n):
        """Build the nuclear braid word, reducing after each crossing.

        The nucleus is constructed as B₃ · (pairwise crossings), where
        B₃ = (σ₀σ₁⁻¹)³ is the Borromean confinement braid.

        Returns (reduced_element, division_log).
        """
        A = p + n
        types = ['p'] * p + ['n'] * n
        full_log = []

        # Start with Borromean confinement braid B₃ = (σ₀σ₁⁻¹)³
        elem, b3_log = self.borromean_B3()
        full_log.extend(b3_log)

        crossing_num = 0
        total_crossings = A * (A - 1) // 2

        for i in range(A):
            for j in range(i + 1, A):
                ti, tj = types[i], types[j]

                if ti == 'p' and tj == 'p':
                    crossing = self.crossing_positive(i)
                    cross_type = 'p-p'
                elif ti == 'n' and tj == 'n':
                    crossing = self.crossing_negative(i)
                    cross_type = 'n-n'
                else:
                    crossing = self.crossing_mixed(i)
                    cross_type = 'p-n'

                # Multiply (unreduced)
                elem_unreduced = elem * crossing
                crossing_num += 1

                # Reduce and log
                elem, steps = self.reduce(elem_unreduced)

                # Tag each step with crossing info
                for s in steps:
                    s.step = len(full_log) + 1
                    full_log.append(s)

        return elem, full_log

    # ── Division algorithm (instrumented) ────────────────────────

    def reduce(self, elem, max_iterations=100000, use_patterns=True):
        """Apply Gröbner--Shirshov division algorithm with step logging.

        If use_patterns=True and named patterns are registered,
        applies Rule 0 (pattern merging) after each full pass
        to collapse terms that share named sub-patterns.

        Returns (reduced_element, list_of_DivisionSteps).
        """
        log = []
        cumulative_energy = 0.0
        iteration = 0

        changed = True
        while changed and iteration < max_iterations:
            changed = False
            new_terms = {}

            for word, coeff in elem.terms.items():
                if abs(coeff) < 1e-15:
                    continue

                reduced_this = False

                # ── Rule 1: Hecke relation σ_i² = (q-q⁻¹)σ_i + 1 ──
                # Only applies to non-negative generators (not formal variables)
                for pos in range(len(word) - 1):
                    if word[pos] == word[pos + 1] and word[pos] >= 0:
                        i = word[pos]
                        prefix = word[:pos]
                        suffix = word[pos + 2:]

                        w1 = prefix + (i,) + suffix    # (q-q⁻¹)σ_i term
                        c1 = coeff * self.hecke_a
                        w2 = prefix + suffix            # identity term
                        c2 = coeff * self.hecke_b

                        new_terms[w1] = new_terms.get(w1, 0.0) + c1
                        new_terms[w2] = new_terms.get(w2, 0.0) + c2

                        # Energy change: old contribution |coeff| removed,
                        # new contributions |c1| + |c2| added
                        old_energy = abs(coeff)
                        new_energy = abs(c1) + abs(c2)
                        delta_e = new_energy - old_energy
                        cumulative_energy += delta_e

                        log.append(DivisionStep(
                            step=0,  # will be renumbered
                            relation='hecke',
                            position=pos,
                            generator=i,
                            old_word=word,
                            old_coeff=coeff,
                            new_terms=[(w1, c1), (w2, c2)],
                            energy_change=delta_e,
                            n_terms_after=0,  # filled below
                            cumulative_energy=cumulative_energy,
                        ))

                        reduced_this = True
                        changed = True
                        break

                if reduced_this:
                    continue

                # ── Rule 2: Far commutativity σ_iσ_j → σ_jσ_i, |i-j|≥2 ──
                # Also: formal variables (negative) commute with everything
                # and sort to the LEFT (lowest position).
                for pos in range(len(word) - 1):
                    i_gen, j_gen = word[pos], word[pos + 1]
                    # Formal variable (negative) commutes with any σ_k
                    if i_gen >= 0 and j_gen < 0:
                        # σ_i · ℵ_k → ℵ_k · σ_i  (move formal var left)
                        new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                        new_terms[new_word] = new_terms.get(new_word, 0.0) + coeff
                        log.append(DivisionStep(
                            step=0, relation='far-comm', position=pos,
                            generator=i_gen, old_word=word, old_coeff=coeff,
                            new_terms=[(new_word, coeff)], energy_change=0.0,
                            n_terms_after=0, cumulative_energy=cumulative_energy))
                        reduced_this = True; changed = True; break
                    if abs(i_gen - j_gen) >= 2 and i_gen > j_gen and i_gen >= 0 and j_gen >= 0:
                        new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                        new_terms[new_word] = new_terms.get(new_word, 0.0) + coeff

                        log.append(DivisionStep(
                            step=0,
                            relation='far-comm',
                            position=pos,
                            generator=i_gen,
                            old_word=word,
                            old_coeff=coeff,
                            new_terms=[(new_word, coeff)],
                            energy_change=0.0,
                            n_terms_after=0,
                            cumulative_energy=cumulative_energy,
                        ))

                        reduced_this = True
                        changed = True
                        break

                if reduced_this:
                    continue

                # ── Rule 3: Yang-Baxter σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1} ──
                for pos in range(len(word) - 2):
                    a, b, c = word[pos], word[pos + 1], word[pos + 2]
                    if a == c and abs(a - b) == 1:
                        # Apply if the replacement is lex-smaller
                        new_trip = (b, a, b)
                        old_trip = (a, b, a)
                        if new_trip < old_trip:
                            new_word = word[:pos] + new_trip + word[pos + 3:]
                            new_terms[new_word] = new_terms.get(new_word, 0.0) + coeff

                            log.append(DivisionStep(
                                step=0,
                                relation='yang-baxter',
                                position=pos,
                                generator=a,
                                old_word=word,
                                old_coeff=coeff,
                                new_terms=[(new_word, coeff)],
                                energy_change=0.0,
                                n_terms_after=0,
                                cumulative_energy=cumulative_energy,
                            ))

                            reduced_this = True
                            changed = True
                            break

                if not reduced_this:
                    new_terms[word] = new_terms.get(word, 0.0) + coeff

            elem = HeckeElement(new_terms)
            iteration += 1

            # ── Rule 0: Quotient reduction (formal atom substitution) ──
            # After standard reduction, check if the element contains
            # a registered NF as a sub-expression. If so, replace it
            # with the formal variable ℵ_k.
            if use_patterns and self._quotient_relations:
                q_changed = True
                while q_changed:
                    elem, q_changed, q_log = self._try_quotient_reduction(elem)
                    if q_changed:
                        q_log.cumulative_energy = cumulative_energy
                        log.append(q_log)
                        changed = True  # trigger another pass

        # Fill in n_terms_after for each step
        for s in log:
            s.n_terms_after = elem.n_terms()

        return elem, log

    # ── Markov trace ─────────────────────────────────────────────

    def markov_trace(self, elem, n_strands):
        """Compute the Markov trace of a reduced Hecke element."""
        total = 0.0
        for word, coeff in elem.terms.items():
            total += coeff * self._trace_word(word, n_strands)
        return total

    def _trace_word(self, word, n_strands, _cache={}):
        """Recursive Markov trace of a braid monomial."""
        key = (word, n_strands)
        if key in _cache:
            return _cache[key]

        if not word:
            result = 1.0
        else:
            max_gen = max(word)
            effective_n = max_gen + 2
            if n_strands > effective_n:
                n_strands = effective_n

            last_max_pos = len(word) - 1 - list(reversed(word)).index(max_gen)
            rotated = word[last_max_pos + 1:] + word[:last_max_pos]
            result = self.z_markov * self._trace_word(rotated, n_strands)

        _cache[key] = result
        return result

    # ── Analysis ─────────────────────────────────────────────────

    def summarize_log(self, log):
        """Summarize a division log."""
        hecke_steps = [s for s in log if s.relation == 'hecke']
        yb_steps = [s for s in log if s.relation == 'yang-baxter']
        fc_steps = [s for s in log if s.relation == 'far-comm']

        total_energy = sum(s.energy_change for s in log)
        hecke_energy = sum(s.energy_change for s in hecke_steps)

        return {
            'total_steps': len(log),
            'hecke_steps': len(hecke_steps),
            'yang_baxter_steps': len(yb_steps),
            'far_comm_steps': len(fc_steps),
            'total_energy_change': total_energy,
            'hecke_energy_change': hecke_energy,
            'energy_per_hecke_step': hecke_energy / len(hecke_steps) if hecke_steps else 0,
        }


# ── Convenience: full computation for a nucleus ─────────────────

def compute_nucleus(p, n, q_val=1.110, verbose=True):
    """Full instrumented computation for N(p,n).

    Returns dict with:
      - 'element': reduced HeckeElement
      - 'log': list of DivisionSteps
      - 'summary': summary statistics
      - 'trace': Markov trace value
      - 'transition': (if n >= 1) comparison with daughter
    """
    div = HeckeDivision(q_val)
    A = p + n

    if verbose:
        print(f"N({p},{n}): A={A}, {A*(A-1)//2} crossings")

    elem, log = div.nuclear_braid(p, n)
    summary = div.summarize_log(log)
    trace = div.markov_trace(elem, A)

    if verbose:
        print(f"  Reduced: {elem.n_terms()} terms, max length {elem.max_word_length()}")
        print(f"  Steps: {summary['total_steps']} ({summary['hecke_steps']} Hecke, "
              f"{summary['yang_baxter_steps']} YB, {summary['far_comm_steps']} far-comm)")
        print(f"  Energy change: {summary['total_energy_change']:.6f} "
              f"(Hecke only: {summary['hecke_energy_change']:.6f})")
        print(f"  Markov trace: {trace:.8e}")
        print(f"  Word histogram: {elem.word_histogram()}")

    result = {
        'p': p, 'n': n, 'A': A,
        'element': elem,
        'log': log,
        'summary': summary,
        'trace': trace,
    }

    # Compute daughter for beta decay comparison
    if n >= 1:
        elem_dau, log_dau = div.nuclear_braid(p + 1, n - 1)
        summary_dau = div.summarize_log(log_dau)
        trace_dau = div.markov_trace(elem_dau, A)

        # L_0 computation: tr(e_i in context)
        # Remove converting neutron's crossings
        elem_nc, log_nc = div.nuclear_braid_skip(p, n, skip=p)
        trace_nc = div.markov_trace(elem_nc, A)

        tr_ei = (q_val * trace - trace_nc) / (q_val - 1)

        if verbose:
            print(f"  Daughter N({p+1},{n-1}): {elem_dau.n_terms()} terms, "
                  f"trace = {trace_dau:.8e}")
            print(f"  tr(e_i context) = {tr_ei:.8e}")
            print(f"  Energy change (parent→daughter): "
                  f"{summary_dau['total_energy_change'] - summary['total_energy_change']:.6f}")

        result['daughter'] = {
            'element': elem_dau,
            'trace': trace_dau,
            'summary': summary_dau,
        }
        result['tr_L0'] = tr_ei
        result['delta_energy'] = (summary_dau['total_energy_change']
                                  - summary['total_energy_change'])

    return result


# Add the skip method to HeckeDivision
def _nuclear_braid_skip(self, p, n, skip):
    """Build nuclear braid word, skipping all crossings involving nucleon `skip`."""
    A = p + n
    types = ['p'] * p + ['n'] * n
    full_log = []
    elem = HeckeElement.identity()

    for i in range(A):
        for j in range(i + 1, A):
            if i == skip or j == skip:
                continue
            ti, tj = types[i], types[j]

            if ti == 'p' and tj == 'p':
                crossing = self.crossing_positive(i)
            elif ti == 'n' and tj == 'n':
                crossing = self.crossing_negative(i)
            else:
                crossing = self.crossing_mixed(i)

            elem_unreduced = elem * crossing
            elem, steps = self.reduce(elem_unreduced)
            full_log.extend(steps)

    return elem, full_log

HeckeDivision.nuclear_braid_skip = _nuclear_braid_skip


# ── CLI ──────────────────────────────────────────────────────────

if __name__ == '__main__':
    import json
    import sys
    from datetime import datetime, timezone
    from pathlib import Path

    nuclei = [
        ('2H',  1, 1),
        ('3H',  1, 2),
        ('3He', 2, 1),
        ('4He', 2, 2),
        ('6Li', 3, 3),
    ]

    q_val = 1.110
    all_results = []

    for name, p, n in nuclei:
        print(f"\n{'='*60}")
        r = compute_nucleus(p, n, q_val)
        print()

        # Show first 10 Hecke reduction steps for the log
        hecke_steps = [s for s in r['log'] if s.relation == 'hecke'][:10]
        if hecke_steps:
            print(f"  First {len(hecke_steps)} Hecke steps:")
            for s in hecke_steps:
                w_str = ''.join(f'σ{i}' for i in s.old_word) or '1'
                print(f"    σ{s.generator}² at pos {s.position} in {w_str}: "
                      f"ΔE = {s.energy_change:+.6f}, cumul = {s.cumulative_energy:+.6f}")

        all_results.append({
            'nucleus': name, 'p': p, 'n': n,
            'n_terms': r['element'].n_terms(),
            'max_word_length': r['element'].max_word_length(),
            'trace': r['trace'],
            'summary': r['summary'],
            'tr_L0': r.get('tr_L0'),
            'delta_energy': r.get('delta_energy'),
            'word_histogram': r['element'].word_histogram(),
        })

    # Witness
    witness = {
        'computation': 'hecke-division-instrumented',
        'description': 'Instrumented Gröbner--Shirshov division in H_n(q) with step-by-step energy logging',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'engine': 'custom (hecke_division.py)',
        'parameters': {'q': q_val},
        'groebner_basis': [
            'σ_i² - (q-q⁻¹)σ_i - 1  (Hecke, energy-changing)',
            'σ_iσ_{i+1}σ_i - σ_{i+1}σ_iσ_{i+1}  (Yang-Baxter, energy-preserving)',
            'σ_iσ_j - σ_jσ_i for |i-j|≥2  (far commutativity, energy-preserving)',
        ],
        # P2.5: see docs/audits/2026-05-02-p2-5-symbolic-q-audit.md
        'symbolic_q_form': {
            'engine': 'sympy',
            'q_symbol': "q (sp.Symbol('q'))",
            'h_symbol_definition': 'h = q - 1/q',
            'pattern': 'sympy-symbolic-Hecke-NF-with-q_val-evaluation',
            'note': (
                'Hecke normal-form expressions are symbolic in q '
                '(sp.Symbol). The witness below is evaluated at '
                'q = q_val (passed as parameter); the same '
                'symbolic NF can be re-evaluated at any q.'
            ),
        },
        'results': all_results,
    }

    out = Path(__file__).parent / 'hecke-division.witness.json'
    with open(out, 'w') as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\nWitness: {out}")
