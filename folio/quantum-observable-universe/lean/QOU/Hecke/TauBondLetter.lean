import QOU.Hecke.TauStructureConstants

/-!
# QOU.Hecke.TauBondLetter — a generator used once is invisible to `τ` up to its shift

Let `s = s_i` be a simple reflection and let `a, b ∈ H_n(q)` be built from the
other generators only.  For the canonical trace `τ` (`τ(T_w) = δ_{w,1}`),

  `τ(a · (c • σ_i + d • 1) · b) = d · τ(a b)`.

So a single letter on a generator that occurs nowhere else contributes exactly
its **shift** `d`, and nothing from `σ_i`.  In particular a bare `σ_i` (`d = 0`)
used once forces `τ = 0`.

## Why it is true

By the trace property (`tau_mul_comm`) `τ(a σ_i b) = τ(σ_i · (b a))`, and `b a`
lies in the span of the `T_w` with `w` in the Young subgroup

  `P_i = { w : w preserves the block {0, …, i} }`,

because left multiplication by `σ_t` (`t ≠ i`) keeps that span (`σ_mul_Tw`, and
`w · s_t ∈ P_i`).  For `w ∈ P_i` the length goes **up** at `i`
(`w(i) ≤ i < w(i+1)`), so `σ_i T_w = T_{w s_i}` with no `T_w` term, and
`w s_i ∉ P_i` is never `1`.  Hence `τ(σ_i T_w) = 0` on all of that span.

No exchange condition and no double-coset machinery is used: the only facts are
`σ_mul_Tw`, `tau_Tw` and `tau_mul_comm`.

## Use

In the 3A-strand atom words of `computations/mass_at_3A_proper.py` every
inter-nucleon bond is one letter on a boundary generator `3k+2` that occurs
nowhere else.  Applied once per bond, this gives
`τ(W_atom) = (∏_k d_k) · τ(W_free)`.  The proton–proton letter is a bare `σ`, so
`τ(W_atom) = 0` exactly for any word with an adjacent `pp` pair.  Whether `τ` is
the Molien-weighted trace of the two-arm probe is a separate statement
(the Molien weights equal `1/s_λ`) and is **not** used or claimed here.

`Ref: [geckpfeiffer2000]` §8.1 (the trace `τ`); the lemma below is elementary.
-/

namespace QOU.Hecke.TwBasis

open QOU.Hecke.IwahoriHecke (σ)

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-! ### The Young subgroup preserving `{0, …, i}` -/

/-- `w` preserves the block `{0, …, i}` (equivalently `{i+1, …, n}`). -/
def PreservesBlock (i : Fin n) (w : Equiv.Perm (Fin (n + 1))) : Prop :=
  ∀ j : Fin (n + 1), w j ≤ i.castSucc ↔ j ≤ i.castSucc

theorem swap_le_castSucc_iff {i t : Fin n} (ht : t ≠ i) (j : Fin (n + 1)) :
    Equiv.swap t.castSucc t.succ j ≤ i.castSucc ↔ j ≤ i.castSucc := by
  have hti : t.val ≠ i.val := fun h => ht (Fin.ext h)
  by_cases h1 : j = t.castSucc
  · subst h1
    rw [Equiv.swap_apply_left]
    simp only [Fin.le_iff_val_le_val, Fin.val_succ, Fin.coe_castSucc]
    omega
  · by_cases h2 : j = t.succ
    · subst h2
      rw [Equiv.swap_apply_right]
      simp only [Fin.le_iff_val_le_val, Fin.val_succ, Fin.coe_castSucc]
      omega
    · rw [Equiv.swap_apply_of_ne_of_ne h1 h2]

theorem PreservesBlock.mul_swap {i t : Fin n} (ht : t ≠ i)
    {w : Equiv.Perm (Fin (n + 1))} (hw : PreservesBlock n i w) :
    PreservesBlock n i (w * Equiv.swap t.castSucc t.succ) := by
  intro j
  rw [Equiv.Perm.mul_apply, hw, swap_le_castSucc_iff n ht]

/-- On the block-preserving locus the length goes **up** at `i`. -/
theorem PreservesBlock.lt {i : Fin n} {w : Equiv.Perm (Fin (n + 1))}
    (hw : PreservesBlock n i w) : w i.castSucc < w i.succ := by
  have h1 : w i.castSucc ≤ i.castSucc := (hw _).mpr le_rfl
  have h2 : ¬ w i.succ ≤ i.castSucc := by
    rw [hw]
    simp only [Fin.le_iff_val_le_val, Fin.val_succ, Fin.coe_castSucc]
    omega
  exact lt_of_le_of_lt h1 (not_le.mp h2)

/-- `w · s_i` is never the identity when `w` preserves the block. -/
theorem PreservesBlock.mul_swap_self_ne_one {i : Fin n} {w : Equiv.Perm (Fin (n + 1))}
    (hw : PreservesBlock n i w) : w * Equiv.swap i.castSucc i.succ ≠ 1 := by
  intro h
  have hlt := hw.lt
  have hw' : w = Equiv.swap i.castSucc i.succ := by
    have := congrArg (· * Equiv.swap i.castSucc i.succ) h
    simpa [mul_assoc] using this
  rw [hw', Equiv.swap_apply_left, Equiv.swap_apply_right] at hlt
  exact absurd hlt (not_lt.mpr (le_of_lt (Fin.castSucc_lt_succ i)))

/-! ### The span of the block-preserving `T_w` -/

/-- `span_K { T_w : w preserves {0, …, i} }`. -/
noncomputable def blockSpan (i : Fin n) : Submodule K (QOU.Hecke.IwahoriHecke K q n) :=
  Submodule.span K (Tw K q n '' {w | PreservesBlock n i w})

theorem one_mem_blockSpan (i : Fin n) : (1 : QOU.Hecke.IwahoriHecke K q n) ∈ blockSpan K q n i := by
  rw [← Tw_one K q n]
  exact Submodule.subset_span ⟨1, fun j => Iff.rfl, rfl⟩

/-- Left multiplication by `σ_t`, `t ≠ i`, preserves the block span. -/
theorem σ_mul_mem_blockSpan {i t : Fin n} (ht : t ≠ i)
    {x : QOU.Hecke.IwahoriHecke K q n} (hx : x ∈ blockSpan K q n i) :
    σ K q n t * x ∈ blockSpan K q n i := by
  have hle : blockSpan K q n i
      ≤ (blockSpan K q n i).comap (LinearMap.mulLeft K (σ K q n t)) := by
    refine Submodule.span_le.mpr ?_
    rintro _ ⟨w, hw, rfl⟩
    have hws : Tw K q n (w * Equiv.swap t.castSucc t.succ) ∈ blockSpan K q n i :=
      Submodule.subset_span ⟨_, PreservesBlock.mul_swap n ht hw, rfl⟩
    have hw1 : Tw K q n w ∈ blockSpan K q n i := Submodule.subset_span ⟨w, hw, rfl⟩
    show σ K q n t * Tw K q n w ∈ blockSpan K q n i
    rw [σ_mul_Tw]
    split_ifs
    · exact hws
    · exact Submodule.add_mem _ (Submodule.smul_mem _ _ hw1) (Submodule.smul_mem _ _ hws)
  exact hle hx

/-- `τ(σ_i · x) = 0` on the block span. -/
theorem tau_σ_mul_of_mem_blockSpan (i : Fin n)
    {x : QOU.Hecke.IwahoriHecke K q n} (hx : x ∈ blockSpan K q n i) :
    tau K q n (σ K q n i * x) = 0 := by
  have hle : blockSpan K q n i
      ≤ LinearMap.ker ((tau K q n).comp (LinearMap.mulLeft K (σ K q n i))) := by
    refine Submodule.span_le.mpr ?_
    rintro _ ⟨w, hw, rfl⟩
    show tau K q n (σ K q n i * Tw K q n w) = 0
    rw [σ_mul_Tw_of_lt K q n i w (PreservesBlock.lt n hw), tau_Tw,
      if_neg (PreservesBlock.mul_swap_self_ne_one n hw)]
  exact hle hx

/-! ### The subalgebra generated by the other generators -/

/-- The subalgebra of `H_n(q)` generated by every `σ_t` with `t ≠ i`. -/
noncomputable def avoiding (i : Fin n) : Subalgebra K (QOU.Hecke.IwahoriHecke K q n) :=
  Algebra.adjoin K {x | ∃ t : Fin n, t ≠ i ∧ x = σ K q n t}

/-- The elements that map the block span into itself under left multiplication. -/
noncomputable def blockStab (i : Fin n) : Subalgebra K (QOU.Hecke.IwahoriHecke K q n) where
  carrier := {a | ∀ x ∈ blockSpan K q n i, a * x ∈ blockSpan K q n i}
  mul_mem' {a b} ha hb x hx := by rw [mul_assoc]; exact ha _ (hb x hx)
  add_mem' {a b} ha hb x hx := by rw [add_mul]; exact Submodule.add_mem _ (ha x hx) (hb x hx)
  algebraMap_mem' r x hx := by
    rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
    exact Submodule.smul_mem _ r hx

theorem avoiding_le_blockStab (i : Fin n) : avoiding K q n i ≤ blockStab K q n i := by
  refine Algebra.adjoin_le ?_
  rintro _ ⟨t, ht, rfl⟩ x hx
  exact σ_mul_mem_blockSpan K q n ht hx

theorem mem_blockSpan_of_mem_avoiding {i : Fin n}
    {a : QOU.Hecke.IwahoriHecke K q n} (ha : a ∈ avoiding K q n i) :
    a ∈ blockSpan K q n i := by
  simpa using avoiding_le_blockStab K q n i ha 1 (one_mem_blockSpan K q n i)

/-! ### The bond-letter identity -/

/-- **`τ(a · σ_i · b) = 0`** when `a` and `b` avoid `σ_i`. -/
theorem tau_mul_σ_mul_eq_zero {i : Fin n} {a b : QOU.Hecke.IwahoriHecke K q n}
    (ha : a ∈ avoiding K q n i) (hb : b ∈ avoiding K q n i) :
    tau K q n (a * σ K q n i * b) = 0 := by
  rw [tau_mul_comm, ← mul_assoc, tau_mul_comm]
  exact tau_σ_mul_of_mem_blockSpan K q n i
    (mem_blockSpan_of_mem_avoiding K q n (Subalgebra.mul_mem _ hb ha))

/-- **A letter `c • σ_i + d • 1` on a generator used nowhere else contributes
    exactly its shift:** `τ(a · (c • σ_i + d • 1) · b) = d · τ(a b)`. -/
theorem tau_bond_letter {i : Fin n} {a b : QOU.Hecke.IwahoriHecke K q n}
    (ha : a ∈ avoiding K q n i) (hb : b ∈ avoiding K q n i) (c d : K) :
    tau K q n (a * (c • σ K q n i + d • (1 : QOU.Hecke.IwahoriHecke K q n)) * b)
      = d * tau K q n (a * b) := by
  rw [mul_add, add_mul, map_add, mul_smul_comm, smul_mul_assoc, map_smul,
    tau_mul_σ_mul_eq_zero K q n ha hb, mul_smul_comm, mul_one, smul_mul_assoc, map_smul,
    smul_eq_mul, mul_zero, zero_add, smul_eq_mul]

/-- **A bare generator used once kills `τ`** — the `d = 0` case. -/
theorem tau_bare_bond_eq_zero {i : Fin n} {a b : QOU.Hecke.IwahoriHecke K q n}
    (ha : a ∈ avoiding K q n i) (hb : b ∈ avoiding K q n i) (c : K) :
    tau K q n (a * (c • σ K q n i) * b) = 0 := by
  have := tau_bond_letter K q n ha hb c 0
  simpa using this

end QOU.Hecke.TwBasis
