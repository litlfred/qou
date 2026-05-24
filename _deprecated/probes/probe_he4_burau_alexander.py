#!/usr/bin/env python3
"""probe_he4_burau_alexander.py — Alexander polynomial via Burau rep.

Strengthens F1 question 2 by computing the Alexander polynomial
of each ⁴He compositional closure, which is a finer link invariant
than just the component count.

Background: SnapPy's alexander_polynomial requires Sage; Sage isn't
installable in our environment.  Burau representation gives
Alexander directly via numpy/sympy: for braid β ∈ B_n,

  Δ_β(t) = det(I_{n-1} - Burau_reduced(β))  /  (1 + t + ... + t^{n-1})

(up to normalization).  Pure linear algebra in Z[t, t⁻¹] — no
topology library needed.

Burau representation σ_i ∈ B_n → GL_{n-1}(Z[t, t⁻¹]):
    σ_i acts on V = Z[t, t⁻¹]^{n-1} as identity on basis vectors
    e_j (j ≠ i-1, i, i+1), and on the (i-1, i, i+1) block as:
      e_{i-1} ↦ e_{i-1} + e_i              (if i > 1)
      e_i     ↦ -t·e_i + t·e_{i+1}          (if i < n-1)
      e_{i+1} ↦ e_{i+1}

(Standard reduced Burau, B_n on Z[t, t⁻¹]^{n-1} indexed 0..n-2.)

Output: he4-burau-alexander.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from probe_he4_jsj_topology import he4_compositional_braids  # noqa: E402


def burau_generator(i: int, n: int, t: sp.Symbol) -> sp.Matrix:
    """Reduced Burau matrix for σ_i ∈ B_n on Z[t, t⁻¹]^{n-1}.

    i is 1-indexed: i ∈ {1, ..., n-1}.  Returns (n-1)×(n-1) matrix.
    """
    dim = n - 1
    M = sp.eye(dim)
    # Convert i to 0-indexed for matrix indexing
    j = i - 1
    if j == 0:
        # σ_1: top boundary. M[0,1] only exists when dim > 1 (i.e. n ≥ 3)
        M[0, 0] = -t
        if dim > 1:
            M[0, 1] = 1
    elif j == dim - 1:
        # σ_{n-1}: bottom boundary
        M[j, j - 1] = t
        M[j, j] = -t
    else:
        # Internal σ_i: blocks rows j-1, j, j+1
        M[j, j - 1] = t
        M[j, j] = -t
        M[j, j + 1] = 1
    return M


def burau_inverse(i: int, n: int, t: sp.Symbol) -> sp.Matrix:
    """Reduced Burau for σ_i⁻¹: inverse of burau_generator."""
    return burau_generator(i, n, t).inv()


def burau_of_word(word: list[int], n: int, t: sp.Symbol) -> sp.Matrix:
    """Burau matrix of a 1-indexed signed braid word."""
    dim = n - 1
    M = sp.eye(dim)
    for g in word:
        if g > 0:
            M = M @ burau_generator(g, n, t)
        elif g < 0:
            M = M @ burau_inverse(-g, n, t)
        else:
            raise ValueError("zero generator index not allowed")
    return M


def alexander_polynomial(word: list[int], n: int) -> sp.Expr:
    """Alexander polynomial of the braid closure via Burau.

    Δ_β(t) = det(I_{n-1} − Burau_reduced(β))

    Note: this is NOT normalised; the "true" Alexander polynomial
    is this expression up to multiplication by ±t^k.  For comparison
    of compositions, the unnormalised form is fine — they're the
    same UP TO units iff the braids are isotopic, but the unnormalised
    forms differ visibly when the topologies differ.
    """
    t = sp.Symbol("t")
    M = burau_of_word(word, n, t)
    I = sp.eye(n - 1)
    delta = (I - M).det()
    return sp.expand(delta)


def main() -> int:
    print("=" * 90)
    print("  Burau / Alexander polynomial for ⁴He compositional closures")
    print("=" * 90)
    print()
    braids = he4_compositional_braids()
    results = {}
    for name, (word, n) in braids.items():
        print(f"  --- {name} ---")
        print(f"  word length: {len(word)}, n_strands: {n}")
        try:
            delta = alexander_polynomial(word, n)
            # Normalise: divide by common t^k factor if any
            delta_str = str(delta)
            print(f"  Δ(t) = {delta_str[:80]}{'…' if len(delta_str) > 80 else ''}")
            # Evaluate at t = -1 (determinant), t = 1 (Alexander at 1)
            try:
                det_m1 = int(delta.subs(sp.Symbol("t"), -1))
                det_1 = int(delta.subs(sp.Symbol("t"), 1))
            except Exception:
                det_m1 = "n/a"
                det_1 = "n/a"
            print(f"  Δ(-1) = {det_m1}  (link determinant)")
            print(f"  Δ(1)  = {det_1}")
            results[name] = {
                "word_length": len(word),
                "n_strands": n,
                "alexander_polynomial": str(delta),
                "determinant": det_m1,
                "alexander_at_t_1": det_1,
            }
        except Exception as e:
            print(f"  FAILED: {type(e).__name__}: {e}")
            results[name] = {"error": f"{type(e).__name__}: {e}"}
        print()

    # Comparison
    print("  Distinguishing the four compositions:")
    print(f"  {'composition':<22} {'Δ(-1) determinant':>18} {'Δ(1)':>10}")
    print("  " + "-" * 60)
    for name, r in results.items():
        det = r.get("determinant", "?")
        d1 = r.get("alexander_at_t_1", "?")
        print(f"  {name:<22} {str(det):>18} {str(d1):>10}")
    print()

    from witness_base import WitnessBuilder
    builder = (
        WitnessBuilder("he4-burau-alexander", engine="sympy")
        .set_description(
            "Burau-representation Alexander polynomial of ⁴He "
            "compositional braid closures.  Strengthens F1 question 2 "
            "(Model B knot identification) beyond component counts by "
            "computing the Alexander polynomial directly via the "
            "reduced Burau matrix representation B_n → GL_{n-1}(Z[t,t⁻¹]).  "
            "Pure numpy/sympy — no Sage / SnapPy / Regina dependency."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-three-pr-integration.md"
        )
        .add_data("compositions", results)
        .add_caveat(
            "Alexander polynomial is well-defined up to multiplication "
            "by ±t^k.  This probe records the unnormalised form; "
            "comparison of compositions is via Δ(-1) (determinant, "
            "scalar invariant) and Δ(1).  Two braid closures are "
            "isotopic ⇒ same Δ up to ±t^k; the contrapositive (different "
            "Δ(-1) ⇒ NOT isotopic) is what we use here."
        )
        .add_caveat(
            "Burau is faithful only at B_3 (Long–Paton 1993).  For "
            "n ≥ 5 the Burau representation has a non-trivial kernel; "
            "different braids can have the same Alexander polynomial.  "
            "At n = 12 (here), Δ-comparison is a necessary but not "
            "sufficient condition for non-isotopy."
        )
        .add_caveat(
            "NEGATIVE RESULT: All four compositions give Δ(t) = 0 "
            "(degenerate multi-component-link case).  The Alexander "
            "polynomial does NOT distinguish them.  The strongest "
            "available invariant without Sage remains the Markov "
            "trace τ_M(β) at q_0 — see "
            "probe_he4_compositional_consistency.py (PR #670) which "
            "shows canonical=0.0553, D⊕D=0.151, T⊕p=0.111, ³He⊕n=0.191 "
            "(all four distinct)."
        )
    )
    out = builder.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
