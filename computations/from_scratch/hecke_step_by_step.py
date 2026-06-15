#!/usr/bin/env python3
"""From-scratch H_n(q) implementation with traced Hecke reductions.

Every operation logs:
  - the braid word being multiplied
  - which Hecke quadratic / braid relations fire
  - source and target GB filtration grade
  - jet order (running depth into the multiplicative integral)

NO dependencies on the existing folio-assistant compute infrastructure.
Built only on sympy for symbolic q-arithmetic.

Algebraic foundations
=====================

H_n(q) is the unital associative ℚ(q)-algebra on generators σ_1, …, σ_{n-1}
with relations:

  (H1) σ_i² = (q - q⁻¹) σ_i + 1                       (Hecke quadratic)
  (B1) σ_i σ_j = σ_j σ_i             for |i - j| ≥ 2  (far commutativity)
  (B2) σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}          (braid relation)

Inverse: σ_i⁻¹ = σ_i - h with h := q - q⁻¹.  Verify:
  σ_i (σ_i - h) = σ_i² - h σ_i = (h σ_i + 1) - h σ_i = 1.   ✓

GB filtration grade `ℓ(w)` is the Coxeter length of the underlying
permutation; reduces by 2 each time (H1) fires (σ_i² → linear-in-σ_i + 1).

Jet order is incremented at every reduction step.
"""
from __future__ import annotations
import sympy as sp
from dataclasses import dataclass, field
from typing import Optional


q = sp.Symbol('q', positive=True, real=True)
h = q - 1/q  # h := q - q^{-1}


@dataclass
class Term:
    """A single term in H_n(q): coefficient · σ-word."""
    coeff: sp.Expr           # in ℚ(q)
    word: tuple[int, ...]    # generator indices (1-indexed signed: -1 means σ_1^{-1})

    def __post_init__(self):
        # Normalize σ_i⁻¹ = σ_i - h: keep only positive powers in the word
        # by representing σ_i⁻¹ as a linear combo σ_i - h * 1 LATER.
        # For now allow negative entries; expansion happens during reduction.
        pass

    def __repr__(self):
        wstr = "·".join(
            (f"σ_{abs(i)}⁻¹" if i < 0 else f"σ_{i}") for i in self.word
        )
        if not wstr:
            wstr = "1"
        return f"{self.coeff}·{wstr}"


@dataclass
class HeckeElement:
    """Element of H_n(q) as a list of Terms (formal linear combination).

    Track GB filtration grade = max Coxeter length over all terms with
    nonzero coefficient.
    """
    n: int                              # H_n
    terms: list[Term] = field(default_factory=list)
    # Trace of all reductions applied so far
    trace: list[str] = field(default_factory=list)
    jet_order: int = 0                   # running depth

    def coxeter_length_of_word(self, word: tuple[int, ...]) -> int:
        """Crude Coxeter length: count of generators (without canonicalising).

        For canonical/reduced words this is exact. For non-reduced words
        it is an upper bound; the exact length requires a reduction.
        """
        # Map negative indices to positive (since σ_i⁻¹ = σ_i - h reduces
        # to a positive-σ_i contribution at the linear level; treat the
        # σ_i factor as a single generator for Coxeter length purposes).
        return len(word)

    def gb_grade(self) -> int:
        """Maximum Coxeter length over nonzero terms = GB filtration grade."""
        return max(
            (self.coxeter_length_of_word(t.word) for t in self.terms
             if sp.simplify(t.coeff) != 0),
            default=0,
        )

    def log(self, msg: str):
        self.trace.append(msg)

    def simplify(self):
        """Combine like terms; drop zero coefficients."""
        merged: dict[tuple[int, ...], sp.Expr] = {}
        for t in self.terms:
            merged[t.word] = sp.expand(merged.get(t.word, sp.Integer(0)) + t.coeff)
        self.terms = [
            Term(coeff=c, word=w)
            for w, c in merged.items()
            if sp.simplify(c) != 0
        ]


def expand_inverses(word: tuple[int, ...]) -> list[tuple[sp.Expr, tuple[int, ...]]]:
    """Replace σ_i⁻¹ → σ_i - h by distributing.

    Returns [(coeff, word), ...] — a sum of terms with all positive indices.
    Each σ_i⁻¹ is a 2-term sum {(1, σ_i), (-h, ε)}.
    """
    if not word:
        return [(sp.Integer(1), ())]
    head = word[0]
    rest_expansions = expand_inverses(word[1:])
    out = []
    for r_coeff, r_word in rest_expansions:
        if head < 0:
            # σ_|head|⁻¹ = σ_|head| - h
            out.append((r_coeff, (-head,) + r_word))
            out.append((-h * r_coeff, r_word))
        else:
            out.append((r_coeff, (head,) + r_word))
    return out


def reduce_squares(word: tuple[int, ...]) -> list[tuple[sp.Expr, tuple[int, ...]]]:
    """Apply Hecke quadratic σ_i² = h σ_i + 1 wherever consecutive i's appear.

    Returns the linear combination after one reduction step (or the input
    if no reduction is possible).  Records:
      - position of the σ_i² that was fired
      - source grade ℓ_source = len(word)
      - target grades after split: max(len(word) - 2 + 1, len(word) - 2)
    """
    for i in range(len(word) - 1):
        if word[i] == word[i + 1] and word[i] > 0:
            # σ_k² at position i
            k = word[i]
            prefix = word[:i]
            suffix = word[i + 2:]
            # σ_k² → h σ_k + 1
            return [
                (h, prefix + (k,) + suffix),     # h σ_k component
                (sp.Integer(1), prefix + suffix), # 1 component
            ]
    return [(sp.Integer(1), word)]


def normalize(elt: HeckeElement, max_steps: int = 100) -> HeckeElement:
    """Iteratively expand inverses then reduce σ_i² until no reductions apply.

    Logs every reduction step with grade transitions and jet order.
    """
    # Step 1: expand all σ_i⁻¹ into linear combinations of positive-σ words
    new_terms = []
    for t in elt.terms:
        for c, w in expand_inverses(t.word):
            new_terms.append(Term(coeff=t.coeff * c, word=w))
    elt.terms = new_terms
    elt.simplify()
    elt.log(f"After inverse expansion: {len(elt.terms)} terms, "
            f"max grade {elt.gb_grade()}")
    elt.jet_order += 1

    # Step 2: iteratively apply Hecke quadratic
    for step in range(max_steps):
        progressed = False
        new_terms = []
        for t in elt.terms:
            reductions = reduce_squares(t.word)
            if len(reductions) == 1 and reductions[0][1] == t.word:
                # No reduction applied
                new_terms.append(t)
            else:
                progressed = True
                source_grade = elt.coxeter_length_of_word(t.word)
                for c, w in reductions:
                    target_grade = elt.coxeter_length_of_word(w)
                    elt.log(
                        f"  step {elt.jet_order}: σ²-reduction at "
                        f"{t.word} → coeff {c}·{w}, grade {source_grade}→"
                        f"{target_grade}"
                    )
                    new_terms.append(Term(coeff=t.coeff * c, word=w))
        elt.terms = new_terms
        elt.simplify()
        elt.jet_order += 1
        if not progressed:
            break
    else:
        elt.log(f"WARNING: reached max_steps={max_steps} in normalize()")
    elt.log(f"After σ²-reduction: {len(elt.terms)} terms, "
            f"max grade {elt.gb_grade()}, jet order {elt.jet_order}")
    return elt


def from_braid_word(n: int, braid_word: list[int]) -> HeckeElement:
    """Inject a B_n braid word into H_n(q) as a single Hecke element."""
    elt = HeckeElement(n=n)
    elt.terms = [Term(coeff=sp.Integer(1), word=tuple(braid_word))]
    elt.log(f"H_{n}(q): inject braid word {braid_word}, "
            f"initial grade {elt.gb_grade()}")
    return elt


# ─── Demo on D's SDP-canonical braid word ─────────────────────────────────
if __name__ == "__main__":
    print("=" * 78)
    print("From-scratch H_3(q) on D's SDP-canonical braid")
    print("=" * 78)
    # SDP-canonical D: braid = [1, -2, 1, 1, 1, -2] in B_3
    elt = from_braid_word(n=3, braid_word=[1, -2, 1, 1, 1, -2])
    print(f"  Initial element: {elt.terms[0]!r}")
    print(f"  Initial GB grade: {elt.gb_grade()}")
    print(f"  Initial jet order: {elt.jet_order}")
    print()

    elt = normalize(elt)
    print()
    print("Reduction trace:")
    for line in elt.trace:
        print(f"  {line}")
    print()
    print(f"Final GB grade: {elt.gb_grade()}")
    print(f"Final jet order: {elt.jet_order}")
    print(f"Number of terms: {len(elt.terms)}")
    print()
    print("Final element (first 8 terms):")
    for t in elt.terms[:8]:
        print(f"  {t!r}")
    if len(elt.terms) > 8:
        print(f"  ... ({len(elt.terms) - 8} more)")
