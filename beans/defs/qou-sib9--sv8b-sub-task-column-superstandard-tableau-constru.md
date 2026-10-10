---
# qou-sib9
title: 'sv8b sub-task: column-superstandard tableau — construction FOUND (orderIsoOfFin on col-then-row lex), but blocked by a Prod LinearOrder instance diamond'
status: completed
type: task
priority: normal
created_at: 2026-08-08T00:29:51Z
updated_at: 2026-08-08T00:47:43Z
---


## The construction (works — definition compiles)

`Specht.Tableau μ` is *definitionally* `Fin (nOf μ) ≃ μ.cells`, and `nOf μ = μ.cells.card`
by `rfl`. So the column-superstandard tableau **is** the order isomorphism for the
column-then-row lex order on cells — no hand-rolled enumeration needed:

```lean
def cellLinearOrder : LinearOrder (ℕ × ℕ) :=
  LinearOrder.lift' (fun c : ℕ × ℕ => (toLex (c.2, c.1) : ℕ ×ₗ ℕ)) (by
    intro a b h
    have h' : ((a.2, a.1) : ℕ × ℕ) = (b.2, b.1) := h
    exact Prod.ext (congrArg Prod.snd h') (congrArg Prod.fst h'))

attribute [local instance] cellLinearOrder

noncomputable def colSuperstandard (μ : YoungDiagram) : Specht.Tableau μ :=
  (μ.cells.orderIsoOfFin rfl).toEquiv        -- ✅ compiles
```

Verified against v4.24.0 oleans: `Finset.orderIsoOfFin : (s : Finset α) → s.card = k →
Fin k ≃o {x // x ∈ s}` has exactly the needed shape, and the `rfl` discharges
`μ.cells.card = Specht.nOf μ`.

## 🛑 The blocker: a `Prod` order instance diamond — READ BEFORE RETRYING

`ℕ × ℕ` **already carries Mathlib's componentwise order** `Prod.instLE_mathlib`. Adding a
`LinearOrder (ℕ × ℕ)` instance creates a diamond, and it bites asymmetrically:

- the **bare** definition above elaborates fine (the local instance wins where nothing
  competes);
- but the moment a declaration **annotates the type**, Lean resolves `LE` to the ambient
  componentwise instance and you get:

```
type mismatch
  has type      @OrderIso (Fin μ.cells.card) _ instLEFin
                  (@Subtype.instLE _ instDistribLatticeOfLinearOrder.toSemilatticeInf.toLE _)
  but expected  @OrderIso (Fin (Specht.nOf μ)) _ instLEFin
                  (@Subtype.instLE _ Prod.instLE_mathlib _)
```

i.e. `instDistribLatticeOfLinearOrder…` (mine) vs `Prod.instLE_mathlib` (Mathlib's). Every
downstream order lemma — `lt_iff`, the lex unfolding via `Prod.Lex.lt_iff`, and the
same-column count — needs to state the order, so all of them hit this.

**Do not just retry with more `show`/`unfold` plumbing — that was tried and the mismatch is
instance-level, not syntactic.** Pick one of:

1. **Type synonym** (preferred): put the order on a `def Cell := ℕ × ℕ` synonym (or reuse
   `ℕ ×ₗ ℕ` directly with a swap equiv on cells) so no instance competes on `ℕ × ℕ` itself.
2. **Numeric key**: order by an injective `key c = c.2 * W + c.1` into `ℕ` (with `W` a row
   bound), avoiding any `Prod` order entirely.
3. Build the equiv from an explicitly sorted `List` with a supplied relation, bypassing
   `orderIsoOfFin`.

Option 1 or 2 keeps `ℕ × ℕ`'s Mathlib order untouched, which is the safe end-state — a
competing `LinearOrder (ℕ × ℕ)` in the library tree would be a hazard for every other file
that reasons about cells.

## Why this tableau is wanted

Per bean `sv8b`, the column-superstandard tableau does not exist anywhere in the tree
(`grep colSuperstandard` empty, re-confirmed 2026-08-08) and is a named sub-task of
`seminormalVector_base_exists`. `sv8b`'s audit also warns that the *row*-superstandard
polytabloid (`SytRowSuperstandard`, which does exist) is **not** an eigenvector — so
building toward it would be proving a false statement.

Once constructed, the immediate payoff is the first half of the eigen-equation: for `s` at
cell `(i, j)`, the same-column count in
`OVBaseSeminormalVector.jm_polytabloid_split` should be exactly `i`, because under
column-then-row lex the labels below `s` in its column are precisely the `i` labels
preceding it there. That plus `content (i,j) = j − i` reduces the whole gap to the
off-column Garnir collapse.
