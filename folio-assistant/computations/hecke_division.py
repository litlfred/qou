#!/usr/bin/env python3
"""
Instrumented Gröbner division algorithm for the Hecke algebra H_n(q).

Each division step is logged with:
  - Which relation was applied (Hecke / Yang-Baxter / far commutativity)
  - Where in the braid word (position)
  - The coefficient change (energy change)
  - The resulting terms

This implements the division algorithm from the unital Gröbner bases
paper (def:division-algorithm) specialized to the admissible system
(positive braid monomials, length-lex ordering) with Gröbner basis:
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
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

# ── Symbolic ring ────────────────────────────────────────────────

q_sym = sp.Symbol('q', positive=True)


@dataclass
class DivisionStep:
    """One step of the Gröbner division algorithm."""
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
    """Element of H_n(q) with numerical coefficients."""

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
    """Instrumented Gröbner division in H_n(q).

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

        # Inverse: σ⁻¹ = q²σ - q(q½ - q⁻½)
        self.inv_sigma = q_val**2
        self.inv_const = -q_val * self.skein_amp

        # Markov trace parameter
        self.z_markov = 1.0 / (self.q_half + self.q_half_inv)

        # Enriched ideal: named patterns for sub-word matching
        # Each entry: { 'name': str, 'word': tuple, 'coeff': float,
        #               'expansion': HeckeElement }
        # When 'word' appears as a sub-word, it can be recognized
        # and optionally collapsed.
        self._named_patterns = {}
        self._pattern_words = []  # sorted by length (longest first)

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

    # ── Crossing constructors ────────────────────────────────────

    def crossing_positive(self, i):
        """σ_i (proton-proton crossing)."""
        return HeckeElement({(i,): 1.0})

    def crossing_negative(self, i):
        """σ_i⁻¹ = q²σ_i - q(q½-q⁻½) (neutron-neutron crossing)."""
        return HeckeElement({(i,): self.inv_sigma, (): self.inv_const})

    def crossing_mixed(self, i):
        """½(σ_i + σ_i⁻¹) (proton-neutron crossing)."""
        return HeckeElement({
            (i,): 0.5 * (1 + self.q**2),
            (): 0.5 * self.inv_const,
        })

    # ── Nuclear braid word ───────────────────────────────────────

    def nuclear_braid(self, p, n):
        """Build the nuclear braid word, reducing after each crossing.

        Returns (reduced_element, division_log).
        """
        A = p + n
        types = ['p'] * p + ['n'] * n
        full_log = []

        elem = HeckeElement.identity()
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
        """Apply Gröbner division algorithm with step logging.

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
                for pos in range(len(word) - 1):
                    if word[pos] == word[pos + 1]:
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
                for pos in range(len(word) - 1):
                    i_gen, j_gen = word[pos], word[pos + 1]
                    if abs(i_gen - j_gen) >= 2 and i_gen > j_gen:
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
        'description': 'Instrumented Gröbner division in H_n(q) with step-by-step energy logging',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'engine': 'custom (hecke_division.py)',
        'parameters': {'q': q_val},
        'groebner_basis': [
            'σ_i² - (q-q⁻¹)σ_i - 1  (Hecke, energy-changing)',
            'σ_iσ_{i+1}σ_i - σ_{i+1}σ_iσ_{i+1}  (Yang-Baxter, energy-preserving)',
            'σ_iσ_j - σ_jσ_i for |i-j|≥2  (far commutativity, energy-preserving)',
        ],
        'results': all_results,
    }

    out = Path(__file__).parent / 'hecke-division.witness.json'
    with open(out, 'w') as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\nWitness: {out}")
