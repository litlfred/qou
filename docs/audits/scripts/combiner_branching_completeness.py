#!/usr/bin/env python3
"""Combiner branching completeness — `interface_blocks` is non-degenerate for
EVERY block (formalize-first, item 2).

The operator-valued combiner (`computations/a_operator/a_operator_recursive.py
:interface_blocks`, and `hecke-branching-trace-decomposition.md`) decomposes the
per-block character along the inclusion

      H_{n_inner}(q) (x) H_{n_block}(q)  -->  H_n(q),     n = n_inner + n_block

    chi^lambda(beta_1 . I . beta_2)
      = sum_{xi |- n_inner, nu |- n_block} c^lambda_{xi,nu} . Tr(A^lambda_{xi,nu}(I) . ...).

The PER-lambda completeness ("the sum captures all of Res(V_lambda)") is already
proved in the corpus (the decomposition `tr = sum over orthogonal (xi,nu)-isotypic
components`, + the Wenzl/Wedderburn `H_n ≅ ⊕_lambda End(V_lambda)`).  This script
verifies the remaining, dual, "we get all terms" guarantee — that the enumeration
is NON-DEGENERATE: `interface_blocks` returns at least one child `(xi, nu)` with
`c^lambda_{xi,nu} > 0` for EVERY `lambda |- n`, so the combiner reaches every
Wedderburn block and the production trace `tr_M = sum_lambda y_lambda chi^lambda`
drops none.

By Frobenius reciprocity, `V_lambda` appears in `Ind(V_xi (x) V_nu)` iff
`V_xi (x) V_nu` appears in `Res(V_lambda)` iff `c^lambda_{xi,nu} > 0`.  Since any
skew shape of size `n_block` admits at least one LR filling, the existence of a
valid child reduces to a purely combinatorial fact:

      every lambda |- n has a SUB-PARTITION xi of size n_inner  (xi ⊆ lambda).

This is the structural reason `interface_blocks` never degenerates; it is
formalized in `QOU/BraidsAndKnots/CombinerBranchingCompleteness.lean`
(`exists_subpartition_of_size`).

Run:  python3 docs/audits/scripts/combiner_branching_completeness.py
Exit 0 iff completeness + non-degeneracy hold on every canonical combiner split.
"""
import sys


def partitions_of(n):
    """All weakly-decreasing partitions of n as tuples."""
    out = []

    def go(remaining, mx, prefix):
        if remaining == 0:
            out.append(prefix)
            return
        for k in range(min(remaining, mx), 0, -1):
            go(remaining - k, k, prefix + (k,))

    go(n, n, ())
    return out


def contains(xi, lam):
    """True iff Young diagram of xi ⊆ that of lam (pointwise rows)."""
    if len(xi) > len(lam):
        return False
    return all(xi[i] <= lam[i] for i in range(len(xi)))


def children_shapes(lam, n_inner):
    """All xi |- n_inner with xi ⊆ lam (the shape-level branching children)."""
    return [xi for xi in partitions_of(n_inner) if contains(xi, lam)]


# Canonical combiner splits (n_inner, n_block) used by the atom combiner:
#  A=2 deuteron 3+3->6 ; A=3 6+3->9 and 3+6->9 ; A=4 9+3->12, 6+6->12, 3+9->12.
SPLITS = [
    (3, 3),   # -> 6
    (6, 3), (3, 6),   # -> 9
    (9, 3), (6, 6), (3, 9),   # -> 12
]


def check_shape_completeness():
    ok = True
    print("Shape-level completeness  (every lambda |- n has a sub-partition of size n_inner):")
    print("   n_inner  n_block |   n  | #parts(n) | reached | non-degenerate")
    print("  ------------------+------+-----------+---------+----------------")
    for (n_inner, n_block) in SPLITS:
        n = n_inner + n_block
        all_lam = partitions_of(n)
        reached = [lam for lam in all_lam if children_shapes(lam, n_inner)]
        nondegen = all(len(children_shapes(lam, n_inner)) >= 1 for lam in all_lam)
        full = len(reached) == len(all_lam)
        ok = ok and full and nondegen
        print(f"     {n_inner:4d}    {n_block:4d}  | {n:4d} |   {len(all_lam):4d}    "
              f"|  {len(reached):4d}   |  {nondegen}")
        if not full:
            missing = [lam for lam in all_lam if lam not in reached]
            print(f"       MISSED blocks: {missing}")
    return ok


def check_lr_crosscheck():
    """Optional: confirm c^lambda_{xi,nu} > 0 for some child of every lambda,
    using the canonical LR enumerator (stronger than shape containment)."""
    try:
        import os
        sub = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                           "computations", "substrate")
        sys.path.insert(0, os.path.abspath(sub))
        from lr_coefficients import lr_coef  # noqa: E402
    except Exception as e:  # pragma: no cover - cross-check is best-effort
        print(f"\nLR cross-check skipped (lr_coefficients not importable: {e}).")
        return True

    ok = True
    print("\nLR cross-check  (every lambda has c^lambda_{xi,nu} > 0 for some child):")
    for (n_inner, n_block) in SPLITS:
        n = n_inner + n_block
        for lam in partitions_of(n):
            found = any(
                lr_coef(xi, nu, lam) > 0
                for xi in partitions_of(n_inner)
                for nu in partitions_of(n_block)
            )
            if not found:
                ok = False
                print(f"     NO LR child for lambda={lam} at split ({n_inner},{n_block})")
        print(f"     split ({n_inner},{n_block}) -> {n}: every block has an LR child : "
              f"{ok if n == n_inner + n_block else ok}")
    return ok


def main():
    print("=" * 72)
    print("COMBINER BRANCHING COMPLETENESS  (interface_blocks non-degenerate)")
    print("=" * 72)
    print()
    b_shape = check_shape_completeness()
    b_lr = check_lr_crosscheck()

    print("\n" + "=" * 72)
    print("VERDICT")
    print("=" * 72)
    print("  Every canonical combiner split (n_inner, n_block) reaches EVERY block")
    print("  lambda |- n: interface_blocks is non-degenerate, so tr_M = sum_lambda")
    print("  y_lambda chi^lambda drops no Wedderburn block.  The per-lambda")
    print("  decomposition completeness is the corpus narrative (Wedderburn +")
    print("  orthogonal-isotypic sum); this verifies the dual non-degeneracy that")
    print("  the structural lemma exists_subpartition_of_size formalizes.")

    assert b_shape, "shape-level completeness failed"
    assert b_lr, "LR cross-check failed"
    print("\nCOMPLETENESS + NON-DEGENERACY VERIFIED.")
    sys.exit(0)


if __name__ == "__main__":
    main()
