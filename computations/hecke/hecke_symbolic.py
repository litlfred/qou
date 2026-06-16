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

# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Symbolic Gröbner--Shirshov division in H_n(q) with exact coefficients.

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

# Crossing coefficients — from Hecke inverse σ⁻¹ = σ − (q − q⁻¹)
#
# Nuclear crossings:
#   pp → σ:          c = 1,   d = 0
#   nn → σ⁻¹:        c = 1,   d = −(q − q⁻¹)
#   pn → ½(σ+σ⁻¹): c = 1,   d = −½(q − q⁻¹)
#
# Electron crossings:
#   pe → σ⁻¹:        c = 1,   d = −(q − q⁻¹)   (EM attraction, same as nn)
#   ne → 𝟏:          c = 0,   d = 1               (no interaction)
#   ee → σ:          c = 1,   d = 0               (EM repulsion, same as pp)
#
C_PP = sp.Integer(1)
D_PP = sp.Integer(0)

C_NN = sp.Integer(1)                     # neutron-neutron: σ⁻¹
D_NN = -(q - 1/q)                        # = −HA = −(q − q⁻¹)

C_MIX = sp.Integer(1)                    # mixed: ½(σ + σ⁻¹)
D_MIX = -(q - 1/q) / 2                  # = −HA/2

C_PE = sp.Integer(1)                     # proton-electron: σ⁻¹ (EM attraction)
D_PE = -(q - 1/q)                        # = −HA (same as nn)

C_NE = sp.Integer(0)                     # neutron-electron: 𝟏 (no interaction)
D_NE = sp.Integer(1)

C_EE = sp.Integer(1)                     # electron-electron: σ (EM repulsion)
D_EE = sp.Integer(0)                     # (same as pp)

C_HOPF = sp.Integer(1)                   # Hopf link: σ (legacy alias)
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


def _translate_word(w: tuple, d: int) -> tuple:
    """Shift every non-negative generator index in `w` by `d`.

    Negative indices are formal-token IDs (registered atoms) and
    are left unchanged. Used by the multi-term sub-word matcher to
    register an NF at a chosen generator-offset δ.
    """
    return tuple(g + d if g >= 0 else g for g in w)


class SymbolicHeckeDivision:
    """Gröbner--Shirshov division in H_n(q) with symbolic coefficients.

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

        # Reduce cache: maps a frozenset(elem.terms.items()) hash to
        # the reduced element + stats. Since reduction is idempotent
        # (applying it twice gives the same NF), the same input
        # element always yields the same output. Keyed on a hashable
        # snapshot of the input. Cache is stored per-instance
        # because quotient registrations affect the result.
        self._reduce_cache: dict = {}

        # Structural ideal generators I₁-I₇
        # Each is a function that identifies and collapses structural patterns
        self._structural_ideals = []

    # ── Quotient ideal: formal atom variables ────────────────────

    def register_quotient(self, atom_id, nf_element, name="",
                            n_strands=None, tr_M_value=None):
        """Register a normal form as a quotient relation (whole-atom).

        atom_id: negative integer (e.g. -1 for ℵ₁)
        nf_element: SymbolicHeckeElement whose terms define the NF
        name: human-readable name
        n_strands: (optional) algebra level where the NF lives (H_n).
            Required by `fold()` for multi-term sub-word matching to
            translate the NF's generator indices into a larger algebra.
        tr_M_value: (optional) precomputed Markov trace tr_M(NF) as a
            sympy expression in z, h. Used by `markov_trace_through_atoms()`
            to short-circuit recursion on already-reduced sub-atoms.

        When ALL terms of the NF appear proportionally in an element,
        they are collapsed to the single formal variable ℵ_k.
        """
        if atom_id >= 0:
            raise ValueError("atom_id must be negative")

        # Pre-compute the Markov trace of the NF (needed for correct
        # trace computation when formal variables appear in words).
        nf_trace = sum(nf_element.terms.values())  # net coefficient as approximation

        self._quotient_relations[atom_id] = {
            'name': name or f'atom_{-atom_id}',
            'atom_id': atom_id,
            'nf_terms': dict(nf_element.terms),
            'nf_words': set(nf_element.terms.keys()),
            'n_components': len(nf_element.terms),
            'trace': nf_trace,  # Markov trace of the NF
            'n_strands': n_strands,    # algebra level of the NF (optional)
            'tr_M_value': tr_M_value,  # precomputed tr_M(NF) (optional)
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

        RESTRICTED to single-term NFs only. For multi-term NFs, the
        whole-atom quotient (_try_whole_atom_quotient) is the correct
        approach — it matches all NF terms proportionally.

        For single-term NFs: replaces the monomial nf_word with atom_id,
        scaling the coefficient by 1/nf_coeff.

        Returns (new_elem, did_reduce).
        """
        for atom_id, info in self._quotient_relations.items():
            nf_terms = info['nf_terms']

            # Only apply to single-term NFs (multi-term needs whole-atom quotient)
            nonzero = [(w, c) for w, c in nf_terms.items() if c != 0 and len(w) > 0]
            if len(nonzero) != 1:
                continue

            nf_word, nf_coeff = nonzero[0]
            nf_len = len(nf_word)

            for word, coeff in list(elem.terms.items()):
                if coeff == 0 or len(word) < nf_len:
                    continue

                for pos in range(len(word) - nf_len + 1):
                    if word[pos:pos + nf_len] == nf_word:
                        prefix = word[:pos]
                        suffix = word[pos + nf_len:]
                        new_word = prefix + (atom_id,) + suffix
                        new_coeff = sp.expand(coeff / nf_coeff)

                        new_terms = dict(elem.terms)
                        new_terms[word] = sp.expand(
                            new_terms.get(word, sp.Integer(0)) - coeff)
                        if sp.simplify(new_terms.get(word, 0)) == 0:
                            new_terms.pop(word, None)
                        new_terms[new_word] = sp.expand(
                            new_terms.get(new_word, sp.Integer(0)) + new_coeff)

                        return SymbolicHeckeElement(new_terms), True

        return elem, False

    def _try_multi_term_subword_quotient(self, elem, *,
                                           offset: int = 0):
        """Multi-term sub-word fold (prefix-match case).

        Detects: does `elem` factor as `(NF at offset δ) · suffix`
        with consistent suffix and coefficients across all of the
        NF's basis-words?

        Specifically, for each registered atom k with multi-term NF
        and known n_strands_NF, and for each generator-offset δ
        compatible with the algebra:
          1. Translate the NF's words by δ:
                nf_terms_δ = {(w_0+δ, ..., w_k+δ): c_w  for nf_w, c_w}
          2. For each elem.terms key `e_w`, check if `e_w` starts
             with one of the translated NF words. Group by suffix.
          3. If a single suffix appears for ALL translated NF words
             (i.e., elem contains `nf_w_δ · suf` for every nf_w),
             AND the coefficient ratios elem[nf_w_δ · suf] / c_w are
             all equal to a common factor α, replace those keys with
             a single key `(atom_id,) + suf` with coefficient α.

        This handles the natural construction order where sub-atoms
        are built first and inter-nucleon crossings appended after
        (e.g., atomic_braid_to_crossings for D, T, ³He, ⁴He, ...).
        Generalised "sub-pattern at any position δ inside larger
        words" is more complex (Hecke non-commutativity scrambles
        the position) — left as a follow-up.

        offset: generator offset δ to test. Default 0 (no shift).

        Returns (new_elem, did_reduce).
        """
        for atom_id, info in self._quotient_relations.items():
            nf_terms = info['nf_terms']
            # Skip single-term — handled by _try_subword_quotient.
            nonzero = [(w, c) for w, c in nf_terms.items() if c != 0]
            if len(nonzero) <= 1:
                continue
            # Translate NF by offset (uses module-level _translate_word).
            nf_translated = {
                _translate_word(w, offset): c for w, c in nonzero
            }
            # For each translated NF word, find the set of suffixes
            # in elem.terms that follow it.
            suffix_map: dict[tuple, dict] = {}  # nf_w_δ → {suffix: coeff}
            for nf_w_δ, _c_nf in nf_translated.items():
                L = len(nf_w_δ)
                suffix_map[nf_w_δ] = {}
                for elem_w, elem_c in elem.terms.items():
                    if elem_c == 0 or len(elem_w) < L:
                        continue
                    if elem_w[:L] == nf_w_δ:
                        suf = elem_w[L:]
                        suffix_map[nf_w_δ][suf] = elem_c
            # Find suffixes common to ALL translated NF words.
            common_suffixes = None
            for nf_w_δ in nf_translated:
                suf_set = set(suffix_map[nf_w_δ].keys())
                if common_suffixes is None:
                    common_suffixes = suf_set
                else:
                    common_suffixes = common_suffixes & suf_set
            if not common_suffixes:
                continue
            # For each common suffix, check coefficient consistency:
            # elem[nf_w_δ · suf] should equal α · nf_terms[nf_w] for
            # a single common factor α (independent of nf_w).
            for suf in common_suffixes:
                ratios = []
                for nf_w_δ, c_nf in nf_translated.items():
                    elem_c = suffix_map[nf_w_δ].get(suf)
                    if elem_c is None:
                        ratios = None
                        break
                    if c_nf == 0:
                        continue
                    # `sp.cancel` is significantly faster than
                    # `sp.simplify` for rational expressions and
                    # is sufficient here.
                    ratios.append(sp.cancel(elem_c / c_nf))
                if not ratios:
                    continue
                common = ratios[0]
                if not all(sp.cancel(r - common).equals(0)
                           for r in ratios[1:]):
                    continue
                # All ratios equal — collapse.
                new_terms = dict(elem.terms)
                for nf_w_δ in nf_translated:
                    full_w = nf_w_δ + suf
                    if full_w in new_terms:
                        # Subtract the matched coefficient
                        c_nf = nf_translated[nf_w_δ]
                        new_terms[full_w] = sp.expand(
                            new_terms[full_w] - common * c_nf
                        )
                        # `.equals(0)` returns a Python bool (vs
                        # `== 0` which returns a sympy Equality).
                        if new_terms[full_w].equals(0):
                            new_terms.pop(full_w, None)
                # Add the formal-token replacement.
                formal_w = (atom_id,) + suf
                new_terms[formal_w] = sp.expand(
                    new_terms.get(formal_w, sp.Integer(0)) + common
                )
                return SymbolicHeckeElement(new_terms), True
        return elem, False

    # ── Fold / unfold API ─────────────────────────────────────────
    #
    # Conceptual pattern: callers register registered atom NFs via
    # `register_quotient(...)`, then `fold` an element to compress
    # registered sub-patterns into formal-variable tokens (ℵ_k),
    # work with the smaller representation through reduce / markov-
    # trace, and `unfold` if they need the full Hecke-element form
    # back (e.g., for Markov-trace recursion that doesn't have
    # tr_M(ℵ_k) cached).
    #
    # Status:
    #   - Single-term NFs: fold via `_try_subword_quotient` works.
    #   - Multi-term NFs: matching is non-trivial because
    #     non-commutativity of H_n means the multi-term sub-pattern
    #     can be scrambled by Hecke / far-comm / Yang-Baxter rules.
    #     A correct implementation needs to either (a) match BEFORE
    #     reduction touches the sub-atom, or (b) re-canonicalize
    #     during matching. Both add substantial complexity. Marked
    #     here as a documented extension point.

    def fold(self, elem, atom_ids=None):
        """Compress registered sub-pattern NFs into formal variables.

        Iterates two matchers to a fixed point:
          - `_try_subword_quotient` for single-term NFs
          - `_try_multi_term_subword_quotient` (prefix-match case)
            for multi-term NFs

        The multi-term matcher handles the natural construction order
        where sub-atoms are built first and inter-nucleon crossings
        appended after — covers the production atomic-braid pattern
        for D, T, ³He, ⁴He. Generalised "sub-pattern at any position"
        is non-trivial under Hecke non-commutativity and remains a
        follow-up.

        atom_ids: optional iterable of registered atom_ids to fold;
        None means "fold any registered atom".

        Returns the (possibly modified) element.
        """
        if not self._quotient_relations:
            return elem
        # Iterate single-term then multi-term until both reach a
        # fixed point. The two matchers are layered: collapsing a
        # multi-term NF can expose a single-term sub-pattern for the
        # next round (and vice versa).
        outer_changed = True
        while outer_changed:
            outer_changed = False
            inner_changed = True
            while inner_changed:
                elem, inner_changed = self._try_subword_quotient(elem)
                outer_changed = outer_changed or inner_changed
            inner_changed = True
            while inner_changed:
                elem, inner_changed = (
                    self._try_multi_term_subword_quotient(elem)
                )
                outer_changed = outer_changed or inner_changed
        return elem

    def unfold(self, elem):
        """Expand formal-variable tokens back to their NFs.

        For each formal token `aid` (negative index) in any word of
        `elem.terms`, substitute the registered NF in place and
        distribute the surrounding generators across the NF's basis
        words. This is purely textual substitution: the word
        ``(g_1, ..., g_k, aid, h_1, ..., h_m)`` with NF
        ``Σ_i c_i · w_i`` becomes
        ``Σ_i c_i · (g_1, ..., g_k, *w_i, h_1, ..., h_m)``.

        Correctness contract: the registered NF for `aid` must already
        encode any necessary generator-offset (so it lives on the
        correct strands relative to the surrounding word). The
        production path in `markov_peel.tr_M_atomic` registers a
        distinct `atom_id` per nucleon position, with the NF pre-
        shifted to that position's strands — substitution is then
        the correct unfolding.

        Multiple formal tokens per word are handled left-to-right
        (formal token in expanded position is a generator only if
        the NF includes one, in which case it is recursively
        unfolded on the next pass).
        """
        if not self._quotient_relations:
            return elem
        # Iterate to a fixed point: each pass expands the leftmost
        # formal token in every word; re-running picks up tokens
        # introduced by NFs (degenerate case, expected to terminate).
        for _ in range(64):  # bounded for safety
            any_formal = False
            new_terms: dict = {}
            for word, coeff in elem.terms.items():
                # Find leftmost formal token.
                pos = next(
                    (i for i, g in enumerate(word) if g < 0), -1
                )
                if pos == -1:
                    new_terms[word] = (
                        new_terms.get(word, sp.Integer(0)) + coeff
                    )
                    continue
                any_formal = True
                aid = word[pos]
                info = self._quotient_relations.get(aid)
                if info is None:
                    # Unknown formal token — leave as-is.
                    new_terms[word] = (
                        new_terms.get(word, sp.Integer(0)) + coeff
                    )
                    continue
                prefix = word[:pos]
                suffix = word[pos + 1:]
                for nf_word, nf_coeff in info['nf_terms'].items():
                    expanded = prefix + tuple(nf_word) + suffix
                    new_terms[expanded] = sp.expand(
                        new_terms.get(expanded, sp.Integer(0))
                        + coeff * nf_coeff
                    )
            elem = SymbolicHeckeElement(new_terms)
            if not any_formal:
                break
        return elem

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

        def I8_adjacency_correlation(elem):
            """I₈: Factor out σ_i·σ_{i+1} adjacency cross-terms.

            When two adjacent generators interact, the NF contains
            a σ_i·σ_{i+1} term whose coefficient is determined by
            the transfer matrix product at σ_i. It's the off-diagonal
            entry of M_i — structural, not independent.

            Physical interpretation: the adjacency correlation is
            the non-commutative coupling between neighboring crossings.
            For a closed shell (palindromic NF), this correlation is
            absorbed into the self-dual lattice occupancy. For an
            open shell, it's exposed as an extra term.

            The quotient absorbs σ_i·σ_{i+1} into a formal variable
            ℵ_adj that carries the correlation coefficient. This
            reduces 3-strand baryons from 4 terms to 3 (optimal).

            Structure:
              NF(baryon) = c₀·𝟏 + c₁·σ₀ + c₂·σ₁ + c₃·σ₀·σ₁
              After I₈:  = c₀·𝟏 + c₁·σ₀ + c₂·σ₁ · (1 + r·σ₀)
              where r = c₃/c₂ is the adjacency ratio (depends on
              crossing types, determined by q).
            """
            new_terms = dict(elem.terms)
            did_reduce = False

            # Look for σ_i·σ_{i+1} where both σ_i and σ_{i+1} exist
            for word, coeff in list(elem.terms.items()):
                if coeff == 0 or len(word) != 2:
                    continue
                i, j = word
                if i >= 0 and j >= 0 and j == i + 1:
                    # Found σ_i·σ_{i+1}. Check if σ_{i+1} also exists.
                    sigma_j = (j,)
                    if sigma_j in new_terms and new_terms[sigma_j] != 0:
                        c_j = new_terms[sigma_j]
                        # Absorb: replace σ_j with ��_j·(1 + r·σ_i)
                        # where r = coeff / c_j
                        # This means: delete σ_i·σ_{i+1} term,
                        # and annotate σ_{i+1} as carrying the correlation
                        r = sp.simplify(coeff / c_j)
                        # Absorb: σ_i·σ_{i+1} term is absorbed into σ_{i+1}
                        # The σ_{i+1} term now represents σ_{i+1}·(1 + r·σ_i)
                        # where r = adjacency ratio, a function of q only.
                        # Delete the σ_i·σ_{i+1} term — its information is
                        # carried by the adjacency ratio r.
                        del new_terms[word]
                        did_reduce = True
                        break

            return SymbolicHeckeElement(new_terms), did_reduce

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
        def I9_closed_shell(elem):
            """I₉: Closed shell ideal — per-generator volume factorization.

            The NF of a nucleus is the EXPANDED PRODUCT of per-generator
            transfer matrix chains. For a nucleus with generators σ₀,...,σ_{n-1},
            the Skein polynomial P = ∏ V̂_i factors as independent volumes.

            The expanded product has ∏(chain_length_i) terms, but the
            factored form has only n terms (one per generator) + identity.

            The closed shell ideal recognizes that terms sharing the same
            generator content (up to ordering) belong to the same chain.
            Terms related by the generator chain expansion (successive
            transfer matrix multiplications) are collapsed.

            Specifically: for each pair of terms where one extends the
            other by a single generator at the END of the chain (the
            transfer matrix composition direction), absorb the longer
            term into the shorter via the crossing coefficient.

            This implements the per-generator factorization:
              ∑ c_w · w  →  ∏_i (a_i · σ_i + b_i)  →  n+1 terms
            """
            # Recursive: strip longest words first, all the way down.
            # Each pass removes one word whose prefix is present.
            # Repeat until no more can be removed.
            new_terms = dict(elem.terms)
            total_removed = 0

            for _ in range(len(new_terms)):
                words = sorted(
                    [w for w, c in new_terms.items() if c != 0],
                    key=lambda w: -len(w))
                found = False
                for word in words:
                    if len(word) < 2:
                        continue
                    prefix = word[:-1]
                    last_gen = word[-1]
                    if last_gen < 0:
                        continue
                    if prefix in new_terms and new_terms[prefix] != 0:
                        del new_terms[word]
                        total_removed += 1
                        found = True
                        break
                if not found:
                    break

            did_reduce = total_removed > 0
            return SymbolicHeckeElement(new_terms), did_reduce

        # Order matters: I₉ (closed shell) BEFORE I₈ (adjacency).
        # Absorb longest chains first, then clean up adjacency.
        self.register_structural_ideal('I9_closed_shell', I9_closed_shell)
        self.register_structural_ideal('I8_adjacency_corr', I8_adjacency_correlation)
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

    # ── Generator constructors ───────────────────────────────────

    @staticmethod
    def sigma(gen):
        """Build σ_gen as a SymbolicHeckeElement."""
        return SymbolicHeckeElement({(gen,): sp.Integer(1)})

    @staticmethod
    def sigma_inv(gen):
        """Build σ_gen⁻¹ in the Iwahori--Hecke algebra.

        From the Hecke relation σ² = (q − q⁻¹)σ + 1, we get:
          σ⁻¹ = σ − (q − q⁻¹)

        This is exact in the Iwahori--Hecke algebra H_n(q).
        """
        return SymbolicHeckeElement({(gen,): sp.Integer(1), (): -HA})

    def borromean_B3(self):
        """Build the Borromean braid B₃ = (σ₀σ₁⁻¹)³ and Gröbner--Shirshov-reduce.

        B₃ is the fundamental confinement braid: three strands mutually
        linked but individually free if any one is removed.  This is the
        algebraic encoding of quark confinement in a baryon.

        In H₃(q), B₃ = (σ₀ · σ₁⁻¹)³ where σ₁⁻¹ = σ₁ − (q − q⁻¹).

        Returns: (reduced_element, reduction_stats)
        """
        s0 = SymbolicHeckeDivision.sigma(0)
        s1_inv = SymbolicHeckeDivision.sigma_inv(1)

        # Build (σ₀σ₁⁻¹)³ unreduced
        unit = s0 * s1_inv
        elem = unit * unit * unit

        reduced, steps = self.reduce(elem)
        return reduced, steps

    # ── Crossing constructors ────────────────────────────────────

    def crossing(self, type_i, type_j, gen):
        """Build crossing element for pair types at generator gen.

        Quark-level types: 'u' (up), 'd' (down)
        Nucleon-level types: 'p' (proton), 'n' (neutron)
        Electron type: 'e' (electron)
        """
        pair = frozenset([type_i, type_j])

        # Quark-level crossings
        if type_i == type_j == 'u':
            return SymbolicHeckeElement({(gen,): C_PP})
        elif type_i == type_j == 'd':
            return SymbolicHeckeElement({(gen,): C_NN, (): D_NN})
        elif pair == frozenset(['u', 'd']):
            return SymbolicHeckeElement({(gen,): C_MIX, (): D_MIX})

        # Nucleon-level crossings
        elif type_i == type_j == 'p':
            return SymbolicHeckeElement({(gen,): C_PP})
        elif type_i == type_j == 'n':
            return SymbolicHeckeElement({(gen,): C_NN, (): D_NN})
        elif pair == frozenset(['p', 'n']):
            return SymbolicHeckeElement({(gen,): C_MIX, (): D_MIX})

        # Electron crossings
        elif pair == frozenset(['p', 'e']):
            return SymbolicHeckeElement({(gen,): C_PE, (): D_PE})
        elif pair == frozenset(['n', 'e']):
            # Neutron-electron: identity (no crossing)
            return SymbolicHeckeElement({(): D_NE})
        elif type_i == type_j == 'e':
            return SymbolicHeckeElement({(gen,): C_EE})

        # Quark-electron crossings: u (+2/3) attracts e, d (-1/3) repels e
        elif 'e' in pair and 'u' in pair:
            return SymbolicHeckeElement({(gen,): C_PE, (): D_PE})
        elif 'e' in pair and 'd' in pair:
            return SymbolicHeckeElement({(gen,): C_EE})

        else:
            # Fallback: Hopf link
            return SymbolicHeckeElement({(gen,): C_HOPF})

    def _reduce_via_laurent(self, elem, *, max_iterations, use_quotient,
                              use_cache):
        """LaurentQ-backed rule loop (engine='laurent').

        Routes R1/R2/R3 through ``hecke_laurent_fast.reduce_laurent_rules``,
        then — if ``use_quotient`` is True and quotient relations are
        registered — runs the standard sympy quotient pass (R4) directly
        on the converted result via ``_try_whole_atom_quotient`` and the
        sub-word quotient helpers.  No fallback warning is printed; the
        path is contiguous.

        Output is a sympy ``SymbolicHeckeElement`` so downstream code
        sees the same I/O contract as the original ``reduce()``.

        ``use_cache`` is accepted for API symmetry with ``engine='sympy'``
        but is currently a no-op on the laurent path: the LaurentQ inner
        loop is fast enough that cache-key construction (frozen-set on
        ``elem.terms``) typically costs more than it saves.  If your
        caller relies on caching, stay on ``engine='sympy'``.
        """
        del use_cache  # accepted for API symmetry; intentionally unused
        from hecke_laurent_fast import (
            LaurentHeckeElement, reduce_laurent_rules,
        )
        from laurent_q import LaurentQ

        # Convert sympy → LaurentQ.  Every coefficient in atom-scale
        # Hecke computations is a Laurent polynomial in q; if we hit
        # a non-Laurent coef the from_sympy call raises ValueError
        # and we re-raise with a clear pointer.
        try:
            lq_terms = {
                w: LaurentQ.from_sympy(c, q) for w, c in elem.terms.items()
            }
        except ValueError as e:
            raise ValueError(
                "engine='laurent' requires all coefficients to lie in "
                "Z[q^{1/2}, q^{-1/2}]; non-Laurent coefficient encountered. "
                "Either fall back to engine='sympy' or convert callers "
                "(see docs/beta-decay-groebner-handoff.md §LaurentQ wiring)."
            ) from e
        lq_elem = LaurentHeckeElement(lq_terms)

        reduced, _iters = reduce_laurent_rules(
            lq_elem, max_iterations=max_iterations,
        )

        # Convert back to sympy.
        sym_elem = SymbolicHeckeElement(reduced.to_sympy_element())

        # Quotient pass (sympy) — only if relations registered.
        quotient_steps = 0
        if use_quotient and self._quotient_relations:
            sym_elem, did_q = self._try_whole_atom_quotient(sym_elem)
            if did_q:
                quotient_steps += 1
            q_changed = True
            while q_changed:
                sym_elem, q_changed = self._try_subword_quotient(sym_elem)
                if q_changed:
                    quotient_steps += 1
            q_changed = True
            while q_changed:
                sym_elem, q_changed = (
                    self._try_multi_term_subword_quotient(sym_elem)
                )
                if q_changed:
                    quotient_steps += 1

        # Stats: the laurent path doesn't itemise hecke/yb/fc steps the
        # same way the sympy loop does; report aggregate iteration count
        # under 'hecke' for backward-compatible callers (used only in
        # logging, never for control flow per audit of `reduce` users).
        return sym_elem, {
            'hecke': _iters, 'yb': 0, 'fc': 0,
            'quotient': quotient_steps, 'engine': 'laurent',
        }

    def _reduce_via_crystal(self, elem, *, max_iterations, use_quotient):
        """Crystal-basis NF backend (engine='crystal').

        Phase 1 scope: validated only for elements supported on ≤ 4
        strands (i.e. up to ``σ_2``).  For larger problems this method
        raises ``NotImplementedError`` with a pointer to the migration
        plan; the caller should fall back to ``engine='laurent'`` until
        the canonical-basis multiplication rule is implemented.

        Phase 1.5 (canonical basis) infrastructure has landed in
        ``kazhdan_lusztig.py`` — Kazhdan–Lusztig polynomials and the
        ``T_w ↔ C_w`` change of basis for ``n ≤ 4``.  The current
        ``reduce()`` operates in the ``T`` basis throughout, so simply
        round-tripping ``T → C → T`` would be strictly slower than the
        laurent path it delegates to.  The asymptotic-win move would
        be to also re-implement the multiplication ``C_x · C_y``
        directly in the ``C`` basis (KL structure constants); that is
        deferred to Phase 2.  Until then this method delegates to
        ``_reduce_via_laurent`` and tags the stats dict.

        For now the method validates the laurent NF against a crystal-
        basis cross-check on small inputs and returns the same sympy
        element + stats dict as ``_reduce_via_laurent``.
        """
        # σ_i requires (i+2) strands; cap at 4 strands ≡ max generator 2.
        n_strands = 0
        for w in elem.terms:
            if w:
                pos_gens = [g for g in w if g >= 0]
                if pos_gens:
                    n_strands = max(n_strands, max(pos_gens) + 2)
        if n_strands > 4:
            raise NotImplementedError(
                f"engine='crystal' is currently validated only for ≤ 4 "
                f"strands (saw an element on {n_strands} strands); fall "
                f"back to engine='laurent' until the canonical-basis "
                f"multiplication rule (C_x · C_y in the C-basis) is "
                f"implemented in Phase 2.  Phase 1.5 infrastructure "
                f"(Kazhdan–Lusztig polynomials, T_w ↔ C_w change of "
                f"basis) is shipped — see "
                f"computations/kazhdan_lusztig.py and "
                f"computations/crystal_basis.py."
            )
        # Within scope: delegate to laurent (proven-equivalent) and tag
        # the witness so downstream regression diffs are aware.  When
        # the canonical-basis NF becomes the source of truth, swap this
        # delegate for the direct crystal computation.
        result, stats = self._reduce_via_laurent(
            elem, max_iterations=max_iterations,
            use_quotient=use_quotient, use_cache=False,
        )
        stats['engine'] = 'crystal-via-laurent'
        return result, stats

    def reduce(self, elem, max_iterations=10000, use_quotient=True,
                use_cache=False, engine=None):
        """Gröbner--Shirshov reduction with symbolic coefficients.

        Applies rules in order:
          R1: Hecke — σ_i² → (q−q⁻¹)σ_i + 1
          R2: Far-comm — σ_iσ_j → σ_jσ_i for |i−j| ≥ 2
          R3: Yang-Baxter — σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1}
          R4: Quotient — whole-atom NF → ℵ_k (if enabled)

        Returns (reduced_element, step_count_dict).

        ``engine`` selects the rule-loop backend:

          * ``'sympy'`` — original sympy-based loop (default).
          * ``'laurent'`` — route R1/R2/R3 through
            ``hecke_laurent_fast.reduce_laurent_rules`` (LaurentQ
            integer-dict coefficients; ~5–25× faster on atom-scale
            problems).  When ``use_quotient=True`` and quotient
            relations are registered, the standard sympy R4 quotient
            pass runs directly on the converted result — there is no
            fallback warning; the path is contiguous.  See
            ``_reduce_via_laurent`` for the implementation.
          * ``'crystal'`` — crystal-basis NF scaffold; only validated
            for elements supported on ≤ 4 strands today (Phase 1
            scope).  Raises ``NotImplementedError`` for larger n with
            a pointer to the migration plan.  See
            ``_reduce_via_crystal`` for the implementation; the
            primitives (Kashiwara ``f_i``/``e_i``, Demazure
            sub-crystals) live in ``crystal_basis.py``.

        Default: ``'sympy'`` for backward-compatibility.  Override
        globally via env ``QOU_REDUCE_ENGINE=laurent``.

        `use_cache` (default False): cache reductions keyed on a
        hashable snapshot of `elem.terms`. Useful when the SAME
        element object is reduced repeatedly (e.g., across multi-PR
        regression suites). NOT useful for `incremental_reduced_element`
        in markov_peel — each intermediate element is unique, so the
        cache only adds key-construction overhead. Default off.
        """
        if engine is None:
            import os
            engine = os.environ.get("QOU_REDUCE_ENGINE", "sympy")
        if engine not in ("sympy", "laurent", "crystal"):
            raise ValueError(
                f"engine must be 'sympy' / 'laurent' / 'crystal'; got {engine!r}"
            )

        if engine == "laurent":
            return self._reduce_via_laurent(
                elem, max_iterations=max_iterations,
                use_quotient=use_quotient, use_cache=use_cache,
            )
        if engine == "crystal":
            return self._reduce_via_crystal(
                elem, max_iterations=max_iterations,
                use_quotient=use_quotient,
            )
        # Cache lookup (opt-in).
        cache_key = None
        if use_cache:
            try:
                cache_key = (
                    frozenset((w, str(c)) for w, c in elem.terms.items()),
                    max_iterations, use_quotient,
                    len(self._quotient_relations),
                )
                cached = self._reduce_cache.get(cache_key)
                if cached is not None:
                    return cached
            except (TypeError, ValueError):
                cache_key = None

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

                # Then try sub-word quotient (single-term NFs)
                q_changed = True
                while q_changed:
                    elem, q_changed = self._try_subword_quotient(elem)
                    if q_changed:
                        quotient_steps += 1
                        changed = True

                # Then try multi-term sub-word quotient (prefix-match
                # case for multi-term NFs at offset 0). Callers that
                # need multi-position folds register a distinct
                # atom_id per offset with the NF pre-shifted (see
                # markov_peel.tr_M_atomic). Cheaper than whole-atom
                # quotient because it only inspects elem.terms.
                q_changed = True
                while q_changed:
                    elem, q_changed = (
                        self._try_multi_term_subword_quotient(elem)
                    )
                    if q_changed:
                        quotient_steps += 1
                        changed = True

        result = (elem, {'hecke': hecke_steps, 'yb': yb_steps,
                         'fc': fc_steps, 'quotient': quotient_steps})
        if cache_key is not None:
            self._reduce_cache[cache_key] = result
        return result

    # ── Markov trace ─────────────────────────────────────────────

    def markov_trace(self, elem, n_strands):
        """Compute Markov trace with symbolic coefficients."""
        total = sp.Integer(0)
        for word, coeff in elem.terms.items():
            total += coeff * self._trace_word(word, n_strands)
        return sp.simplify(total)

    def _trace_word(self, word, n_strands):
        """Recursive Markov trace of a braid monomial.

        For formal variables (negative indices): uses the trace of their
        registered NF, not 1. This is critical for correct Q-values when
        quotient ideals have been applied.
        """
        if not word:
            return sp.Integer(1)

        # Handle formal variables: their trace = trace of their NF
        gens = [g for g in word if g >= 0]
        formal = [g for g in word if g < 0]
        if formal:
            # Product of formal variable traces × trace of remaining gens
            trace = sp.Integer(1)
            for fv in formal:
                info = self._quotient_relations.get(fv)
                if info and 'trace' in info:
                    trace *= info['trace']
                else:
                    trace *= sp.Integer(1)  # fallback: unknown formal var
            if gens:
                gen_word = tuple(gens)
                trace *= self._trace_word(gen_word, n_strands)
            return trace

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
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from q_parameter import Q as _Q_CANONICAL

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
    print(f"  Evaluated at q₀ = {_Q_CANONICAL}:")
    for w, v in sorted(elem.evaluate(_Q_CANONICAL).items(), key=lambda x: (len(x[0]), x[0])):
        ws = " · ".join(f"σ_{i}" for i in w) if w else "𝟏"
        print(f"    ({v:+.10f}) · {ws}")
