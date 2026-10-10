import QOU.BraidKnot.CompositionCoset
import QOU.BraidKnot.CompositionMurphy

/-!
# Prop 3.3, existence: a non-distinguished element is shortenable inside `S_μ`

The uniqueness half is `CompositionCoset.isDistinguished_unique`.  Existence — every
right coset of `S_μ` contains a distinguished element — reduces to the shortening step:

    `d` not distinguished  ⇒  some `v ∈ S_μ` has `ℓ(v · d) < ℓ(d)`

after which the minimal-length element of a coset is distinguished, and there is one.
Measured before formalising, exhaustively over all 5316 right cosets for `n = 1..6`:
existence, "the minimum is distinguished", and this shortening step all hold
([`coset_minimal_is_distinguished_probe.py`](../../../../../computations/hecke/coset_minimal_is_distinguished_probe.py)).

## The handedness problem, and why it dissolves

`PermInversions.invCount_mul_swap` moves the inversion count by one under an adjacent
transposition, but on the **right**: `w * sᵢ`.  The step above is a **left**
multiplication.  They meet through `ℓ(x) = ℓ(x⁻¹)`:

    ℓ(sᵢ · d) = ℓ((sᵢ · d)⁻¹) = ℓ(d⁻¹ · sᵢ)

so the existing right-handed lemma applies to `d⁻¹`, and the descent condition it wants
— `d⁻¹ i < d⁻¹ (i+1)` or its reverse — is exactly the condition the block argument
below produces.  No new inversion machinery is needed.

## Finding an *adjacent* transposition inside the block

`d` not distinguished gives `a < b` with `d a`, `d b` in one block and `d b < d a`.
That is a transposition of two block elements, not an adjacent one.  Blocks are
**intervals** (`lt_of_index_lt` and `index_eq_of_between` below), so the whole range
`[d b, d a]` lies in that block, and along it `d⁻¹` starts high and ends low — hence it
descends across some *consecutive* pair, which is the `sᵢ ∈ S_μ` wanted.
-/

namespace QOU.BraidKnot.CompositionCosetExists

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.Hecke.SymmetricCoxeter QOU.Hecke.Inversions Equiv
open QOU.BraidKnot.CompositionMurphy QOU.BraidKnot.HeckeMurphy

variable {n : ℕ}

/-- **Blocks are intervals**: anything between two labels of one block is in that
block.  `lt_of_index_lt` gives the two inequalities; monotonicity of `index` does the
rest. -/
theorem index_eq_of_between (c : Composition n) {p x q : Fin n}
    (hpq : c.index p = c.index q) (h1 : p ≤ x) (h2 : x ≤ q) :
    c.index x = c.index p := by
  by_contra hne
  rcases lt_trichotomy (c.index x) (c.index p) with h | h | h
  · exact absurd (lt_of_index_lt c h) (by omega)
  · exact hne h
  · rw [hpq] at h
    exact absurd (lt_of_index_lt c h) (by omega)

/-- **A discrete descent exists**: if `f` weakly increases across every consecutive
pair inside `[p, q]`, then `f p ≤ f q`.

Stated as the contrapositive of what is wanted, because that is the direction the
induction runs. -/
theorem le_of_adjacent_le (f : Fin (n + 1) → ℕ) {p q : Fin (n + 1)} (hpq : p ≤ q)
    (h : ∀ i : Fin n, p ≤ i.castSucc → i.succ ≤ q → f i.castSucc ≤ f i.succ) :
    f p ≤ f q := by
  obtain ⟨k, hk⟩ : ∃ k, (q : ℕ) = (p : ℕ) + k := ⟨(q : ℕ) - (p : ℕ), by omega⟩
  induction k generalizing q with
  | zero =>
    have : p = q := Fin.ext (by omega)
    rw [this]
  | succ m ih =>
    have hqpos : 0 < (q : ℕ) := by omega
    have hqlt : (q : ℕ) - 1 < n + 1 := by omega
    set q' : Fin (n + 1) := ⟨(q : ℕ) - 1, hqlt⟩ with hq'
    have hpq' : p ≤ q' := by simp only [hq', Fin.le_def]; omega
    have hstep : f p ≤ f q' := by
      refine ih hpq' (fun i hi hiq => h i hi ?_) (by simp only [hq']; omega)
      exact le_trans hiq (by simp only [hq', Fin.le_def]; omega)
    -- the last step from `q'` to `q` is one adjacent pair
    have hilt : (q : ℕ) - 1 < n := by omega
    set i : Fin n := ⟨(q : ℕ) - 1, hilt⟩ with hi
    have hcast : i.castSucc = q' := Fin.ext (by simp [hi, hq'])
    have hsucc : i.succ = q := Fin.ext (by simp [hi]; omega)
    have := h i (by rw [hcast]; exact hpq') (by rw [hsucc])
    rw [hcast, hsucc] at this
    exact le_trans hstep this

/-- **The shortening step's combinatorial half**: a non-distinguished `d` admits an
**adjacent** transposition lying inside a block of `c`, across which `d⁻¹` descends.

`sᵢ` is then in `S_μ` (its two labels share a block), and `ℓ(d⁻¹ · sᵢ) < ℓ(d⁻¹)` by
`invCount_mul_swap` — which is `ℓ(sᵢ · d) < ℓ(d)`. -/
theorem exists_block_adjacent_descent {c : Composition (n + 1)}
    {d : Perm (Fin (n + 1))} (hnd : ¬ IsDistinguished c d) :
    ∃ i : Fin n, c.index i.castSucc = c.index i.succ ∧
      (d⁻¹) i.succ < (d⁻¹) i.castSucc := by
  simp only [IsDistinguished, not_forall, not_lt] at hnd
  obtain ⟨a, b, hidx, hab, hle⟩ := hnd
  have hne : d a ≠ d b := fun h => absurd (d.injective h) (by omega)
  have hba : d b < d a := lt_of_le_of_ne hle (fun h => hne h.symm)
  -- `d⁻¹` starts high at `d b` and ends low at `d a`
  have hfp : (d⁻¹) (d a) < (d⁻¹) (d b) := by
    simp only [Perm.inv_apply_self]; exact hab
  by_contra hcon
  push_neg at hcon
  -- no consecutive descent inside the block ⇒ `d⁻¹` weakly increases across `[d b, d a]`
  have := le_of_adjacent_le (fun x => ((d⁻¹) x : ℕ)) (le_of_lt hba)
    (fun i hi hiq => ?_)
  · simp only at this
    omega
  · have hblk : c.index i.castSucc = c.index i.succ := by
      have h1 := index_eq_of_between c hidx.symm hi (le_trans (le_of_lt (Fin.castSucc_lt_succ i)) hiq)
      have h2 := index_eq_of_between c hidx.symm (le_trans hi (le_of_lt (Fin.castSucc_lt_succ i))) hiq
      rw [h1, h2]
    have := hcon i hblk
    omega

/-- **The shortening step.**  A non-distinguished `d` is not minimal in its coset:
some `v ∈ S_μ` strictly shortens it.

This is claim (C) of the probe, now proved.  With it, the minimal-length element of a
coset is distinguished, which is the existence half of Proposition 3.3.

The length computation is where the handedness dissolves: `sᵢ` is an involution, so
`(sᵢ · d)⁻¹ = d⁻¹ · sᵢ`, and `length_inv` turns the left multiplication into the right
one that `invCount_mul_swap` already handles. -/
theorem exists_shorter_of_not_isDistinguished {c : Composition (n + 1)}
    {d : Perm (Fin (n + 1))} (hnd : ¬ IsDistinguished c d) :
    ∃ v ∈ youngOfComp c, (permCoxeterSystem n).length (v * d)
      < (permCoxeterSystem n).length d := by
  obtain ⟨i, hblk, hdesc⟩ := exists_block_adjacent_descent hnd
  refine ⟨sw i, mem_youngOfComp_sw.mpr hblk, ?_⟩
  -- `(sᵢ · d)⁻¹ = d⁻¹ · sᵢ`, since `sᵢ` is an involution
  have hinv : (sw i * d)⁻¹ = d⁻¹ * sw i := by
    simp [sw, mul_inv_rev, Equiv.swap_inv]
  have hL : (permCoxeterSystem n).length (sw i * d)
      = (permCoxeterSystem n).length (d⁻¹ * sw i) := by
    rw [← (permCoxeterSystem n).length_inv (sw i * d), hinv]
  have hR : (permCoxeterSystem n).length d
      = (permCoxeterSystem n).length d⁻¹ := ((permCoxeterSystem n).length_inv d).symm
  rw [hL, hR, length_eq_invCount, length_eq_invCount]
  rcases invCount_mul_swap d⁻¹ i with ⟨hup, -⟩ | ⟨-, hdown⟩
  · exact absurd hup (by omega)
  · simpa [sw] using Nat.lt_of_succ_le (le_of_eq hdown)

/-! ## Proposition 3.3, assembled

Existence by induction on length: a non-distinguished element is strictly shortened
inside `S_μ`, so descending must halt, and it can only halt at a distinguished one.
With `CompositionCoset.isDistinguished_unique` that is Mathas' statement in full —
`D_μ` meets every right coset of `S_μ` **exactly once**.
-/

/-- **Existence**: every right coset of `S_μ` contains a distinguished element. -/
theorem exists_isDistinguished_mem_coset (c : Composition (n + 1))
    (w : Perm (Fin (n + 1))) :
    ∃ d, IsDistinguished c d ∧ d * w⁻¹ ∈ youngOfComp c := by
  generalize hk : (permCoxeterSystem n).length w = k
  induction k using Nat.strong_induction_on generalizing w with
  | _ k ih =>
    by_cases hd : IsDistinguished c w
    · exact ⟨w, hd, by simp⟩
    · obtain ⟨v, hv, hlt⟩ := exists_shorter_of_not_isDistinguished hd
      obtain ⟨d, hdd, hdm⟩ := ih _ (hk ▸ hlt) (v * w) rfl
      refine ⟨d, hdd, ?_⟩
      have hrw : d * w⁻¹ = (d * (v * w)⁻¹) * v := by group
      rw [hrw]
      exact mul_mem hdm hv

/-- **Mathas, Proposition 3.3** — the transversal statement.

`D_μ` is a complete set of right coset representatives of `S_μ` in `S_n`: every coset
contains a distinguished element, and only one.

The length half — `ℓ(w·d) = ℓ(w) + ℓ(d)` for `w ∈ S_μ`, `d ∈ D_μ`, which is what gives
`T_{wd} = T_w T_d` — is
`CompositionMinimal.length_mul_eq_add_of_isDistinguished`. -/
theorem existsUnique_isDistinguished_mem_coset (c : Composition (n + 1))
    (w : Perm (Fin (n + 1))) :
    ∃! d, IsDistinguished c d ∧ d * w⁻¹ ∈ youngOfComp c := by
  obtain ⟨d, hdd, hdm⟩ := exists_isDistinguished_mem_coset c w
  refine ⟨d, ⟨hdd, hdm⟩, ?_⟩
  rintro e ⟨hed, hem⟩
  refine QOU.BraidKnot.CompositionCoset.isDistinguished_unique hed hdd ?_
  -- `d · e⁻¹ = (d · w⁻¹) · (e · w⁻¹)⁻¹`, a product of two members of `S_μ`
  have hrw : d * e⁻¹ = (d * w⁻¹) * (e * w⁻¹)⁻¹ := by group
  rw [hrw]
  exact mul_mem hdm (inv_mem hem)

end QOU.BraidKnot.CompositionCosetExists
