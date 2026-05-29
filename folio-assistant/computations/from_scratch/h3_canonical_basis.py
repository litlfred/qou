#!/usr/bin/env python3
"""From-scratch reduction to H_3(q)'s canonical 6-element basis.

H_3(q) has dimension 6 over ℚ(q), with basis indexed by S_3 elements:
  {1, σ_1, σ_2, σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1}

The longest element σ_1σ_2σ_1 = σ_2σ_1σ_2 (braid relation).

This script extends `hecke_step_by_step.py` with the braid relation
σ_iσ_{i+1}σ_i = σ_{i+1}σ_iσ_{i+1} and reduces any H_3(q) element to
this 6-basis.  Every step is logged with:
  - rule fired (Hecke quadratic, braid relation, far-commutativity)
  - source GB filtration grade
  - target grades after split

NO dependencies on existing folio-assistant compute infrastructure.
"""
from __future__ import annotations
import sympy as sp
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hecke_step_by_step import (
    HeckeElement, Term, q, h, expand_inverses, from_braid_word,
)


# ─── H_3 canonical basis ─────────────────────────────────────────────────

# Each basis element is a "canonical" word: lex-smallest reduced word
# in S_3 generators. The 6 elements:
H3_BASIS = [
    (),                  # 1 — identity, length 0
    (1,),                # σ_1, length 1
    (2,),                # σ_2, length 1
    (1, 2),              # σ_1 σ_2, length 2
    (2, 1),              # σ_2 σ_1, length 2
    (1, 2, 1),           # σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2 (longest), length 3
]


def normalize_to_h3_basis(elt: HeckeElement, max_iters: int = 50) -> dict:
    """Reduce a HeckeElement (after Hecke-quadratic normalize) to a
    linear combination of the H_3 canonical basis elements.

    Returns dict {basis_word: coefficient_in_q}.

    Logs every braid-relation firing.
    """
    # First do the Hecke-quadratic + inverse-expansion normalization
    from hecke_step_by_step import normalize as base_normalize
    elt = base_normalize(elt)

    # Now apply braid relations + far-commutativity to canonicalize
    # to one of H3_BASIS words.
    for it in range(max_iters):
        progressed = False
        new_terms = []
        for t in elt.terms:
            w = t.word
            # Try braid relation: any (1,2,1) → (2,1,2)?  No — the
            # OPPOSITE: (2,1,2) → (1,2,1) (lex-smaller).  Both are valid
            # representatives of the longest element.  Choose (1,2,1).
            #
            # Pattern: ...,2,1,2,... → ...,1,2,1,...  (decrements lex)
            replaced = False
            for i in range(len(w) - 2):
                if w[i:i+3] == (2, 1, 2):
                    new_w = w[:i] + (1, 2, 1) + w[i+3:]
                    elt.log(
                        f"  braid relation: {w} → {new_w} "
                        f"(grade {len(w)} → {len(new_w)})"
                    )
                    new_terms.append(Term(coeff=t.coeff, word=new_w))
                    replaced = True
                    progressed = True
                    break
            if replaced:
                continue
            # Apply far-commutativity (no σ_3 in H_3, so nothing to do)
            # Apply Hecke quadratic again if any new (i, i) pair appeared
            # from braid moves
            squared = False
            for i in range(len(w) - 1):
                if w[i] == w[i + 1] and w[i] > 0:
                    k = w[i]
                    pre, suf = w[:i], w[i + 2:]
                    elt.log(
                        f"  σ²-reduction (after braid): {w} → "
                        f"h·{pre + (k,) + suf} + {pre + suf}"
                    )
                    new_terms.append(Term(coeff=t.coeff * h, word=pre + (k,) + suf))
                    new_terms.append(Term(coeff=t.coeff, word=pre + suf))
                    squared = True
                    progressed = True
                    break
            if squared:
                continue
            new_terms.append(t)
        elt.terms = new_terms
        elt.simplify()
        elt.jet_order += 1
        if not progressed:
            break

    # Now collect into basis
    basis_coeffs = {b: sp.Integer(0) for b in H3_BASIS}
    leftover = []
    for t in elt.terms:
        if t.word in basis_coeffs:
            basis_coeffs[t.word] = sp.expand(basis_coeffs[t.word] + t.coeff)
        else:
            leftover.append(t)

    if leftover:
        elt.log(f"WARNING: {len(leftover)} terms not reduced to basis: "
                f"{[(repr(t)) for t in leftover[:3]]}")

    return basis_coeffs


def coxeter_length_for_basis_word(w):
    """Coxeter length for the H_3 basis (= length of the canonical word)."""
    # All basis words are reduced; length == word length
    return len(w)


def display_basis_coeffs(basis_coeffs: dict):
    """Pretty-print the H_3 basis decomposition + GB filtration grades."""
    print(f"  {'basis':>14}  {'grade':>5}  {'coefficient':>40}")
    print("  " + "-" * 64)
    for w in H3_BASIS:
        c = sp.simplify(basis_coeffs[w])
        if c == 0:
            continue
        wstr = "·".join(f"σ_{i}" for i in w) if w else "1"
        grade = coxeter_length_for_basis_word(w)
        print(f"  {wstr:>14}  {grade:>5}  {sp.nsimplify(c)}")


if __name__ == "__main__":
    print("=" * 78)
    print("From-scratch reduction of D's SDP-canonical braid to H_3 basis")
    print("=" * 78)

    elt = from_braid_word(n=3, braid_word=[1, -2, 1, 1, 1, -2])
    print(f"  Input: braid word [1, -2, 1, 1, 1, -2] in B_3")
    print()

    basis_coeffs = normalize_to_h3_basis(elt)

    print("Reduction trace (last 10 events):")
    for line in elt.trace[-10:]:
        print(f"  {line}")
    print(f"\nFinal jet order: {elt.jet_order}")
    print()

    print("D's image in H_3(q) — canonical basis decomposition:")
    print()
    display_basis_coeffs(basis_coeffs)
    print()

    # Evaluate at q_0 = 1.11 numerically
    q0 = sp.Rational(11099785827513808, 10**16)
    print(f"At q_0 = {float(q0):.10f}:")
    for w in H3_BASIS:
        c = sp.simplify(basis_coeffs[w])
        if c == 0:
            continue
        c_q0 = float(c.subs(q, q0).evalf(30))
        wstr = "·".join(f"σ_{i}" for i in w) if w else "1"
        print(f"  c_{wstr:<10} = {c_q0:>+12.6f}")
