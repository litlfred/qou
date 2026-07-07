**Conjecture (Brunnian property of $\mathcal{B}_3$).** *Let $\mathcal{B}_3 \subset \mathbb{R}^3$ be the standard Borromean link, presented as the closed braid $\overline{(\sigma_0\sigma_1^{-1})^3}$ in $B_3$. For each $i \in \{0, 1, 2\}$, let $\mathcal{B}_3 \setminus K_i$ denote the two-component sub-link obtained by removing the $i$-th component. Then $\mathcal{B}_3 \setminus K_i$ is topologically equivalent to the trivial two-component unlink $U_2$.*

This formalizes the confinement mechanism. Removing any single component dissolves the binding between the remaining two. This is the defining property of Brunnian links \cite{kawauchi1996}. Naive strand-deletion at the braid word level does not immediately yield the empty braid. Deleting the 0-th strand produces $(\sigma_0^{-1})^3 \in B_2$, whose closure is the negative trefoil $\overline{3_1}$. Topological equivalence to $U_2$ requires a sequence of Reidemeister moves.

## Lean structure

The statement is co-located with `def:borromean-baryon` under the `qou` Lake package. The substantive declarations live at [`QOU.KnotTheory.Brunnian`](../lean/QOU/KnotTheory/Brunnian.lean):

```lean
-- BraidWord-level naive component deletion.
def BraidWord.deleteComponent (β : BraidWord) (i : Fin β.strands) : BraidWord

-- Predicate: closure of β is the n-component trivial unlink.
def isUnlink (β : BraidWord) : Prop

-- The Brunnian property as a conjectural class instance.
theorem borromean_brunnian :
  ∀ i : Fin 3,
    isUnlink (borromeanRings.deleteComponent i) := by
  sorry  -- Ref: [kawauchi1996] Survey of Knot Theory §1.5
```

The `sorry` acts as a conjectural witness. The gap is the absence of Mathlib primitives for Reidemeister and Markov-move equivalence on braid-word closures. Formal topological equivalence to $U_2$ requires an explicit sequence of two R2 moves and one R3 move. This cannot be stated until the link-equivalence relation is formalized.
