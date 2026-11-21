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

/-! ## Mathas' `D_μ`, and Proposition 3.3's length half in full generality

Everything above is stated for `sortPerm`, but its proof used only **one** property of
that permutation: it never inverts two labels that land in the *same* block.  Mathas
calls the permutations with that property `D_μ` and defines them tableau-side —

> `D_μ = { d ∈ S_n | t^μ d is row standard }`.  Then `D_μ` is a complete set of right
> coset representatives of `S_μ` in `S_n`.  Moreover, if `w ∈ S_μ` and `d ∈ D_μ` then
> `ℓ(wd) = ℓ(w) + ℓ(d)` and `T_{wd} = T_w T_d`.  *(Proposition 3.3)*

— and "`t^μ d` is row standard" is exactly that condition, since the rows of `t^μ` are
the blocks of `μ` in order.  Defining `D_μ` by the condition rather than by the tableau
keeps this file free of tableau machinery, and gives Prop 3.3's length half for every
`d`, not just the block-sorting one.
-/

/-- **Mathas' `D_μ`**: the permutations that never invert two labels landing in the same
block of `c`.

Tableau-side this is "`t^μ d` is row standard"; stated here as the order condition it
amounts to, since the rows of `t^μ` are `c`'s blocks in order. -/
def IsDistinguished (c : Composition n) (d : Perm (Fin n)) : Prop :=
  ∀ a b : Fin n, c.index (d a) = c.index (d b) → a < b → d a < d b

/-- `sortPerm` is distinguished — which is why the specialised proofs above worked. -/
theorem sortPerm_isDistinguished {c c' : Composition n} (m : BlockMatch c c') :
    IsDistinguished c (sortPerm m) := by
  intro a b hidx hab
  refine sortPerm_strictMono_within m a b ?_ hab
  rw [index_sortPerm, index_sortPerm] at hidx
  exact m.toEquiv.injective hidx

/-- **Proposition 3.3, length half.**  `ℓ(w·d) = ℓ(w) + ℓ(d)` for `w ∈ S_μ` and any
`d ∈ D_μ`.

This is what gives `T_{wd} = T_w T_d` through `TwBasis.Tw_mul_Tw`, and it is the fact
Mathas' whole coset bookkeeping runs on.  `length_mul_sortPerm_eq_add` is the `d =
sortPerm` case. -/
theorem length_mul_eq_add_of_isDistinguished {c : Composition (n + 1)}
    {d : Perm (Fin (n + 1))} (hd : IsDistinguished c d)
    {w : Perm (Fin (n + 1))} (hw : w ∈ youngOfComp c) :
    (permCoxeterSystem n).length (w * d)
      = (permCoxeterSystem n).length w + (permCoxeterSystem n).length d := by
  rw [length_mul_eq_add_iff]
  intro p hp
  rw [mem_invSet] at hp ⊢
  obtain ⟨hlt, hinv⟩ := hp
  refine ⟨hlt, ?_⟩
  -- the two images sit in different blocks: inside one block `d` cannot invert
  have hne : c.index (d p.1) ≠ c.index (d p.2) := fun heq =>
    absurd (hd p.1 p.2 heq hlt) (by omega)
  have hblock : c.index (d p.2) < c.index (d p.1) := by
    rcases lt_trichotomy (c.index (d p.2)) (c.index (d p.1)) with h | h | h
    · exact h
    · exact absurd h.symm hne
    · exact absurd (lt_of_index_lt c h) (by omega)
  show w (d p.2) < w (d p.1)
  refine lt_of_index_lt c ?_
  rw [index_apply_of_mem hw, index_apply_of_mem hw]
  exact hblock

/-- **`sortPerm` is minimal-length in its coset** — Mathas' `d ∈ D_μ` — given that it
is increasing inside each block of `c'`.

**Unconditional**, and now a one-line corollary of Proposition 3.3 above: the only
property of `sortPerm` it ever used is that it is distinguished.

The conclusion is what `T_v T_d = T_{vd}` needs, and hence what the intertwining
`T_d · x_μ = x_ν · T_d` runs on. -/
theorem length_mul_sortPerm_eq_add {c c' : Composition (n + 1)} (m : BlockMatch c c')
    {v : Perm (Fin (n + 1))} (hv : v ∈ youngOfComp c) :
    (permCoxeterSystem n).length (v * sortPerm m)
      = (permCoxeterSystem n).length v + (permCoxeterSystem n).length (sortPerm m) :=
  length_mul_eq_add_of_isDistinguished (sortPerm_isDistinguished m) hv

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

/-- Subtracting the sum of individual Coxeter lengths from the product Coxeter length cancels to zero (`qou-iqjk`). -/
theorem length_sortPerm_mul_sub_add_eq_zero {c c' : Composition (n + 1)} (m : BlockMatch c c')
    {w : Perm (Fin (n + 1))} (hw : w ∈ youngOfComp c') :
    (permCoxeterSystem n).length (sortPerm m * w)
      - ((permCoxeterSystem n).length (sortPerm m) + (permCoxeterSystem n).length w) = 0 := by
  rw [length_sortPerm_mul_eq_add m hw, Nat.sub_self]

end QOU.BraidKnot.CompositionMinimal
