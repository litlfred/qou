import QOU.BraidKnot.CompositionYoung
import QOU.Hecke.LengthAdditive

/-!
# `sortPerm` is minimal-length in its coset

The intertwining `T_d · x_μ = x_ν · T_d` — Lemma 3.9's algebraic step — needs
`T_v T_d = T_{vd}` for every `v` in the Young subgroup, which is

    ℓ(v · d) = ℓ(v) + ℓ(d)     for all `v ∈ S_μ`,

i.e. Mathas' `d ∈ D_μ`.  This file proves it for `CompositionYoung.sortPerm`.

## The argument, and why it needs no Coxeter theory

`QOU.Hecke.LengthAdditive.length_mul_eq_add_iff` (#6444) reduces the whole question to
inversion sets — `ℓ(u·v) = ℓ(u) + ℓ(v) ↔ invSet v ⊆ invSet (u·v)` — **unconditionally**,
so nothing here touches the exchange condition that Mathlib lacks.

What remains is then two order facts about blocks:

* **Blocks are consecutive**, so a smaller block index means a smaller position
  (`lt_of_index_lt`).  This is assembled from Mathlib's `sizeUpTo` bounds.
* **A Young element preserves block indices**, by definition of `youngOfComp`.

Together: an inversion of `d` must straddle two *different* blocks (within one block
`d` is increasing), the blocks are then ordered the same way as the positions, and `v`
cannot move a label out of its block — so the inversion survives.
-/

namespace QOU.BraidKnot.CompositionMinimal

open QOU.BraidKnot.CompositionYoung QOU.Hecke.Inversions
open QOU.Hecke.SymmetricCoxeter Equiv

variable {n : ℕ}

/-- **Blocks of a composition are consecutive**: a smaller block index means a strictly
smaller position.

Assembled from `sizeUpTo_index_le`, `lt_sizeUpTo_index_succ` and `monotone_sizeUpTo`;
Mathlib has the three bounds but not this consequence. -/
theorem lt_of_index_lt (c : Composition n) {x y : Fin n} (h : c.index x < c.index y) :
    x < y := by
  have h1 : (x : ℕ) < c.sizeUpTo ((c.index x : ℕ) + 1) := c.lt_sizeUpTo_index_succ x
  have h2 : c.sizeUpTo ((c.index x : ℕ) + 1) ≤ c.sizeUpTo (c.index y : ℕ) :=
    c.monotone_sizeUpTo (by omega)
  have h3 : c.sizeUpTo (c.index y : ℕ) ≤ (y : ℕ) := c.sizeUpTo_index_le y
  omega

/-- The block index of `sortPerm m l`, in the direct form the argument below uses. -/
theorem index_sortPerm {c c' : Composition n} (m : BlockMatch c c') (l : Fin n) :
    c.index (sortPerm m l) = m.toEquiv (c'.index l) := by
  have := congrFun (inv_smul_index_sortPerm m) l
  simpa [smul_arrow_apply] using this

/-- A Young element does not move a label out of its block. -/
theorem index_apply_of_mem {c : Composition n} {v : Perm (Fin n)}
    (hv : v ∈ youngOfComp c) (x : Fin n) : c.index (v x) = c.index x := by
  have := (mem_youngOfComp.mp hv) (v x)
  simpa using this.symm

/-- The **value** of `sortPerm m l`: the start of its target block, plus its offset
inside its source block.

Both halves are Mathlib's (`coe_embedding`, `coe_invEmbedding`); `finCongr` does not
move a value, so the size-matching cast is invisible here. -/
theorem coe_sortPerm {c c' : Composition n} (m : BlockMatch c c') (l : Fin n) :
    ((sortPerm m l : Fin n) : ℕ)
      = c.sizeUpTo (m.toEquiv (c'.index l)) + ((l : ℕ) - c'.sizeUpTo (c'.index l)) := by
  simp [sortPerm, Composition.blocksFinEquiv, Equiv.sigmaCongr, Equiv.sigmaCongrLeft,
    Equiv.sigmaCongrRight, Composition.coe_embedding, Composition.coe_invEmbedding]

/-- **`sortPerm` is increasing inside each block** — it permutes the *rows*, keeping
each row's own order, which is how Mathas specifies `d`.

Both labels get the same block start and the same source offset base, so the
comparison reduces to the labels themselves. -/
theorem sortPerm_strictMono_within {c c' : Composition n} (m : BlockMatch c c')
    (a b : Fin n) (hidx : c'.index a = c'.index b) (hab : a < b) :
    sortPerm m a < sortPerm m b := by
  -- both offsets are measured from the *same* block start, once `hidx` is used
  have ha : c'.sizeUpTo (c'.index b : ℕ) ≤ (a : ℕ) := by
    rw [← hidx]; exact c'.sizeUpTo_index_le a
  have hlt : (a : ℕ) < b := hab
  rw [Fin.lt_def, coe_sortPerm, coe_sortPerm, hidx]
  omega

/-- **`sortPerm` is minimal-length in its coset** — Mathas' `d ∈ D_μ` — given that it
is increasing inside each block of `c'`.

**Unconditional.**  The within-block monotonicity it needs is
`sortPerm_strictMono_within` above, and the inversion-set criterion it runs on
(#6444) is itself unconditional — so this does not rest on the exchange condition
Mathlib lacks.

The conclusion is what `T_v T_d = T_{vd}` needs, and hence what the intertwining
`T_d · x_μ = x_ν · T_d` runs on. -/
theorem length_mul_sortPerm_eq_add {c c' : Composition (n + 1)} (m : BlockMatch c c')
    {v : Perm (Fin (n + 1))} (hv : v ∈ youngOfComp c) :
    (permCoxeterSystem n).length (v * sortPerm m)
      = (permCoxeterSystem n).length v + (permCoxeterSystem n).length (sortPerm m) := by
  rw [length_mul_eq_add_iff]
  intro p hp
  rw [mem_invSet] at hp ⊢
  obtain ⟨hlt, hinv⟩ := hp
  refine ⟨hlt, ?_⟩
  -- the two images sit in *different* blocks: within one block `sortPerm` increases
  have hne : c.index (sortPerm m p.1) ≠ c.index (sortPerm m p.2) := by
    intro heq
    rw [index_sortPerm, index_sortPerm] at heq
    exact absurd (sortPerm_strictMono_within m p.1 p.2 (m.toEquiv.injective heq) hlt)
      (by omega)
  -- so the block indices are ordered the same way as the images
  have hblock : c.index (sortPerm m p.2) < c.index (sortPerm m p.1) := by
    rcases lt_trichotomy (c.index (sortPerm m p.2)) (c.index (sortPerm m p.1)) with h | h | h
    · exact h
    · exact absurd h.symm hne
    · exact absurd (lt_of_index_lt c h) (by omega)
  -- and `v` cannot move a label out of its block
  show v (sortPerm m p.2) < v (sortPerm m p.1)
  refine lt_of_index_lt c ?_
  rw [index_apply_of_mem hv, index_apply_of_mem hv]
  exact hblock

/-! ## The mirror: `ℓ(d · w) = ℓ(d) + ℓ(w)`

`Tw_mul_Tw` is handed — `T_v · T_w = T_{w·v}` — so the two factors of Murphy's
`m_{st} = T_{d(s)}^* x_μ T_{d(t)}` need the length hypothesis on *both* sides.  The
one above covers `T_d · T_v`; this covers `T_v · T_d`.

The argument mirrors it and uses the same two block facts: an inversion of a Young
element lies **inside one block** (across blocks it cannot invert, since blocks are
ordered), and `sortPerm` is increasing inside a block, so it preserves that inversion.
-/

/-- **A Young element inverts only inside a block.**  Across two blocks the order is
fixed by the block order, so no inversion can straddle them. -/
theorem index_eq_of_mem_invSet {c : Composition n} {w : Perm (Fin n)}
    (hw : w ∈ youngOfComp c) {p : Fin n × Fin n} (hp : p ∈ invSet w) :
    c.index p.1 = c.index p.2 := by
  rw [mem_invSet] at hp
  obtain ⟨hlt, hinv⟩ := hp
  by_contra hne
  rcases lt_trichotomy (c.index p.1) (c.index p.2) with h | h | h
  · -- `p.1`'s block is lower, so `w p.1 < w p.2`: not an inversion
    refine absurd hinv (by
      have : w p.1 < w p.2 := by
        refine lt_of_index_lt c ?_
        rw [index_apply_of_mem hw, index_apply_of_mem hw]
        exact h
      omega)
  · exact hne h
  · exact absurd (lt_of_index_lt c h) (by omega)

/-- **The mirror length identity**: `ℓ(d · w) = ℓ(d) + ℓ(w)` for `w` in the Young
subgroup of `c'`.

Together with `length_mul_sortPerm_eq_add` this gives `Tw_mul_Tw` its hypothesis on
both sides, which is what the two-sided `m_{st}` needs. -/
theorem length_sortPerm_mul_eq_add {c c' : Composition (n + 1)} (m : BlockMatch c c')
    {w : Perm (Fin (n + 1))} (hw : w ∈ youngOfComp c') :
    (permCoxeterSystem n).length (sortPerm m * w)
      = (permCoxeterSystem n).length (sortPerm m) + (permCoxeterSystem n).length w := by
  rw [length_mul_eq_add_iff]
  intro p hp
  have hblock := index_eq_of_mem_invSet hw hp
  rw [mem_invSet] at hp ⊢
  obtain ⟨hlt, hinv⟩ := hp
  refine ⟨hlt, ?_⟩
  show sortPerm m (w p.2) < sortPerm m (w p.1)
  refine sortPerm_strictMono_within m _ _ ?_ hinv
  rw [index_apply_of_mem hw, index_apply_of_mem hw]
  exact hblock.symm

end QOU.BraidKnot.CompositionMinimal
