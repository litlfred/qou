/-
# Constructing the Wedderburn embedding

`QOU/HeckeAlgebra/Wedderburn.lean` used to declare `opaque wedderburnEmbed`,
with the explanation that the dimension identity `Σ_λ (f^λ)² = n!` is the
Robinson–Schensted–Knuth correspondence and is not available, "so the embedding
is axiomatised". Bean `qou-qb7p` measured what that costs: the constant showed
up as a **fourth axiom** beside `propext`, `Classical.choice` and `Quot.sound`
in any `#print axioms` that reached it. That declaration was deleted on
2026-09-05 (bean `qou-kp2z`) once this module replaced it; the past tense here
is deliberate, and the file it names now carries a note where it stood.

**The blocker is narrower than the axiom.** RSK is needed only to land in
`Fin (n!)` — not to build the embedding. On its natural index type the
block-diagonal assembly is an ordinary definition, and it is injective.

## The natural index

```
RegIndex n := Σ λ ⊢ n, Fin (f^λ) × Fin (f^λ)
```

This is the regular representation: each irrep `V_λ` appearing with multiplicity
`f^λ`. The first `Fin (f^λ)` says which copy, the second the position inside it,
so `Fintype.card (RegIndex n) = Σ_λ (f^λ)²` (`card_regIndex`) — the quantity RSK
identifies with `n!`, computed here rather than assumed.

## What is constructed, and what remains

* `blockDiagonal` — the assembly. An ordinary `def`; no axiom.
* `blockDiagonal_injective` — it is an **embedding**, not merely a map. The proof
  reads the `(0, i, j)` entry of each block, which needs `0 < f^λ`; that is
  `Hoefsmit.seminormalDim_pos'`, already proved.
* `card_regIndex` — `Σ_λ (f^λ)²`, from `Fintype.card_sigma`.
* `RSKDimIdentity n` — the one missing ingredient, **stated as a `Prop` rather
  than assumed**: `Σ_λ (f^λ)² = heckeDim n`.
* `wedderburnEmbedOf` and `wedderburnEmbedOf_injective` — given that identity,
  the embedding into `Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ`, injective.

So the black box is replaced by a construction plus one named classical lemma.
Nothing here proves RSK, and nothing here pads: a zero-padded map into
`Fin (n!)` would typecheck, look constructed, and fail to be injective — worse
than the honest `opaque` it would replace.

## Precedent

`seminormalDim` in `Hoefsmit.lean` was itself `opaque` until 2026-09-03, retired
with the note *"The stated blocker had been cleared; nobody came back to the
definition."* This is the same shape: the axiom outlived the obstruction that
justified it, over the part of the construction that never needed it.

Bean `qou-usol`.
-/

import Mathlib.Data.Matrix.Basic
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common
import QOU.HeckeAlgebra.Hoefsmit
import QOU.HeckeAlgebra.Wedderburn

namespace QOU.HeckeAlgebra.Wedderburn

open QOU.HeckeAlgebra QOU.HeckeAlgebra.Hoefsmit

/-- **The regular-representation index.** Each partition `λ ⊢ n` contributes
`f^λ` copies of an `f^λ`-dimensional space, so the cardinality is `Σ_λ (f^λ)²`
— the number RSK identifies with `n!`. -/
abbrev RegIndex (n : ℕ) : Type :=
  Σ lam : Nat.Partition n, Fin (seminormalDim lam) × Fin (seminormalDim lam)

/-- **Block-diagonal assembly, constructed.** The entry at `(λ, m, i), (μ, m', j)`
is `x_λ i j` when the partitions and the multiplicity indices agree, and `0`
otherwise. No axiom, and no dimension identity: the target index type is the one
the decomposition naturally lives on. -/
noncomputable def blockDiagonal {n : ℕ} (x : WedderburnDecomposition n) :
    Matrix (RegIndex n) (RegIndex n) ℝ := by
  classical
  exact fun p q =>
    if h : p.1 = q.1 then
      (if (h ▸ p.2).1 = q.2.1 then x q.1 (h ▸ p.2).2 q.2.2 else 0)
    else 0

/-- On a single block, with matching multiplicity index, the assembly returns the
block's own entry. This is the read-off `blockDiagonal_injective` uses. -/
theorem blockDiagonal_same {n : ℕ} (x : WedderburnDecomposition n)
    (lam : Nat.Partition n) (m i j : Fin (seminormalDim lam)) :
    blockDiagonal x ⟨lam, (m, i)⟩ ⟨lam, (m, j)⟩ = x lam i j := by
  classical
  simp [blockDiagonal]

/-- **The assembly is injective — it is an embedding.** Two decompositions with
the same block-diagonal matrix agree block by block, read off at multiplicity
index `0`, which exists because `0 < f^λ`.

The positivity is taken as an explicit argument rather than invoked, and that is
deliberate. Current source proves it unconditionally —
`Hoefsmit.seminormalDim_pos' : 0 < seminormalDim lam`, added 2026-09-03 — but
**this container's restored olean snapshot predates that change**: it carries
only the older `seminormalDim_pos`, which takes a `0 < n` hypothesis that the
statement does not need (the empty diagram has exactly one standard tableau).
Rather than bolt a `0 < n` decoy onto the statement to satisfy a stale cache,
the hypothesis is named and discharged by the caller:

    blockDiagonal_injective (fun lam => Hoefsmit.seminormalDim_pos' lam)

which typechecks against current source. `lean`-direct verifies against the
oleans on disk, so this file is verified against the snapshot; the one-line
discharge above is what a fresh build supplies. -/
theorem blockDiagonal_injective {n : ℕ}
    (hpos : ∀ lam : Nat.Partition n, 0 < seminormalDim lam) :
    Function.Injective (blockDiagonal (n := n)) := by
  intro x y hxy
  funext lam i j
  set m : Fin (seminormalDim lam) := ⟨0, hpos lam⟩ with hm
  have := congrArg (fun M => M ⟨lam, (m, i)⟩ ⟨lam, (m, j)⟩) hxy
  simpa [blockDiagonal_same] using this

/-- `Fintype.card (RegIndex n) = Σ_λ (f^λ)²` — the quantity RSK identifies with
`n!`, computed rather than assumed. -/
theorem card_regIndex (n : ℕ) :
    Fintype.card (RegIndex n) = ∑ lam : Nat.Partition n, seminormalDim lam ^ 2 := by
  classical
  simp [RegIndex, Fintype.card_sigma, sq]

/-- **The one missing ingredient**, written down instead of assumed: the
Robinson–Schensted–Knuth dimension identity `Σ_λ (f^λ)² = n!`. Everything above
is independent of it; everything below is explicitly conditional on it.

⚠ **This is not a new statement.** The corpus already carries it as
`QOU.BraidKnot.OVTopAssembly.sum_numSYT_sq_eq_factorial`, and its status is
worth quoting exactly. `scripts/lean-axiom-guard.py` records it first as
`sorryAx` under "known-BAD: the RSK identity and everything reindexed from it",
and later as `clean` — with the guard's own warning attached, that `clean` was
reached "by moving its obligation into a class binder, which is the §3b-cond
pattern and is exactly what *conditional-proved ≠ premise-established* warns
about", and was "treated as a RED FLAG and checked three ways".

So the identity is available only conditionally, and `RSKDimIdentity` states the
same obligation **as an explicit hypothesis on the theorem** rather than inside
an ambient class binder — which is the difference the guard is complaining
about. Discharging it here additionally needs the `numSYT` ↔ `dimSYT` bridge
(`QOU/BraidKnot/SYTEncodingBridge.lean`), which is its own piece of work and is
not attempted. -/
def RSKDimIdentity (n : ℕ) : Prop :=
  ∑ lam : Nat.Partition n, seminormalDim lam ^ 2 = heckeDim n

/-- Given RSK, the regular index is equivalent to `Fin (n!)`. -/
noncomputable def regIndexEquiv {n : ℕ} (h : RSKDimIdentity n) :
    RegIndex n ≃ Fin (heckeDim n) :=
  Fintype.equivFinOfCardEq (by rw [card_regIndex]; exact h)

/-- **The Wedderburn embedding, given RSK.** This is what the former
`opaque wedderburnEmbed` was axiomatised to be — now a definition, with its one
hypothesis named. -/
noncomputable def wedderburnEmbedOf {n : ℕ} (h : RSKDimIdentity n)
    (x : WedderburnDecomposition n) :
    Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ :=
  Matrix.reindex (regIndexEquiv h) (regIndexEquiv h) (blockDiagonal x)

/-- And it is injective, so it deserves the name "embedding". -/
theorem wedderburnEmbedOf_injective {n : ℕ} (h : RSKDimIdentity n)
    (hpos : ∀ lam : Nat.Partition n, 0 < seminormalDim lam) :
    Function.Injective (wedderburnEmbedOf h) := by
  intro x y hxy
  apply blockDiagonal_injective hpos
  have := congrArg (fun M => Matrix.reindex (regIndexEquiv h).symm
    (regIndexEquiv h).symm M) hxy
  simpa [wedderburnEmbedOf, Matrix.reindex] using this

end QOU.HeckeAlgebra.Wedderburn
