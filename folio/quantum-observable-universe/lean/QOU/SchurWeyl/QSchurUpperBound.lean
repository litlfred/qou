/-
Copyright (c) 2026 QOU contributors.
-/
import QOU.SchurWeyl.JimboGL

/-!
# Upper bound for the q-Schur algebra (G3.4-DJ, milestones DJ1–DJ2)

Let `T_a` be Jimbo's braiding of strands `a, a+1` on `V^{⊗(m+1)}`, `V = K^d`
(`strandBraid q q⁻¹ a`). A matrix `X` commuting with every `T_a` lies in the q-Schur algebra
`S_q(d, m+1) = End_{H}(V^{⊗(m+1)})`. We prove that such an `X` is **determined by its entries
`X c u` with `u` weakly increasing and `c` weakly decreasing on every block where `u` is
constant**. Hence

  `dim S ≤ #{(u, c) : u sorted, c block-decreasing for u}`,

which is the number of `d × d` matrices of naturals with entry sum `m+1` (the Dipper–James
double-coset count). This holds over **any field** with `q ≠ 0`.

## The two relations

From `X T_a = T_a X` and the explicit `Ř`:

* **rows** (`entry_swap_of_col_eq`): if `u a = u (a+1)` and `c a > c (a+1)`, then
  `X (c ∘ swap) u = q · X c u`. (Column `u` is a `q`-eigenvector of `T_a`.)
* **columns** (`col_swap_eq_zero`): if column `b` of `X` vanishes and `b a < b (a+1)`, then
  column `b ∘ swap` vanishes. (`T_a e_b = e_{b∘swap} + (q − q⁻¹) e_b`.)

Rows reduce every entry of a sorted column to a block-decreasing one (induction on
`Σ p · c p`); columns reduce every column to a sorted one (induction on `Σ (m − p) · b p`).

-- Ref: R. Dipper, G. James, *The q-Schur algebra*, Proc. LMS 59 (1989) — the standard basis
-- indexed by double cosets. Source not yet held in `library/`; the argument here is
-- self-contained and does not use it.
-/

namespace QOU.SchurWeyl.QSchurUpperBound

open QOU.IwahoriHecke.TensorEmbedGL Matrix

variable {K : Type*} [Field K] {d m : ℕ}

/-- Swap the letters at strands `a` and `a+1`. -/
def swapAt (a : Fin m) (c : Fin (m + 1) → Fin d) : Fin (m + 1) → Fin d :=
  c ∘ Equiv.swap a.castSucc a.succ

theorem castSucc_ne_succ (a : Fin m) : a.castSucc ≠ a.succ := by
  simp [Fin.ext_iff]

@[simp] theorem swapAt_castSucc (a : Fin m) (c : Fin (m + 1) → Fin d) :
    swapAt a c a.castSucc = c a.succ := by
  simp [swapAt, Equiv.swap_apply_left]

@[simp] theorem swapAt_succ (a : Fin m) (c : Fin (m + 1) → Fin d) :
    swapAt a c a.succ = c a.castSucc := by
  simp [swapAt, Equiv.swap_apply_right]

theorem swapAt_of_ne (a : Fin m) (c : Fin (m + 1) → Fin d) {k : Fin (m + 1)}
    (h1 : k ≠ a.castSucc) (h2 : k ≠ a.succ) : swapAt a c k = c k := by
  simp [swapAt, Equiv.swap_apply_of_ne_of_ne h1 h2]

@[simp] theorem swapAt_swapAt (a : Fin m) (c : Fin (m + 1) → Fin d) :
    swapAt a (swapAt a c) = c := by
  funext k; simp [swapAt]

/-- `b` agrees with `c` off the strands `a, a+1` and carries `c`'s letters there swapped
iff `b = swapAt a c`. -/
theorem eq_swapAt_iff (a : Fin m) (b c : Fin (m + 1) → Fin d) :
    ((∀ k, k ≠ a.castSucc → k ≠ a.succ → b k = c k) ∧ b a.castSucc = c a.succ ∧
      b a.succ = c a.castSucc) ↔ b = swapAt a c := by
  constructor
  · rintro ⟨h, h1, h2⟩
    funext k
    by_cases k1 : k = a.castSucc
    · subst k1; simp [h1]
    by_cases k2 : k = a.succ
    · subst k2; simp [h2]
    rw [swapAt_of_ne a c k1 k2, h k k1 k2]
  · rintro rfl
    exact ⟨fun k h1 h2 => swapAt_of_ne a c h1 h2, by simp, by simp⟩

theorem eq_iff_of_agree (a : Fin m) (b c : Fin (m + 1) → Fin d) :
    ((∀ k, k ≠ a.castSucc → k ≠ a.succ → b k = c k) ∧ b a.castSucc = c a.castSucc ∧
      b a.succ = c a.succ) ↔ b = c := by
  constructor
  · rintro ⟨h, h1, h2⟩
    funext k
    by_cases k1 : k = a.castSucc
    · subst k1; exact h1
    by_cases k2 : k = a.succ
    · subst k2; exact h2
    exact h k k1 k2
  · rintro rfl; exact ⟨fun _ _ _ => rfl, rfl, rfl⟩

variable (q : K)

theorem strandBraid_apply (a : Fin m) (c b : Fin (m + 1) → Fin d) :
    strandBraid (d := d) q q⁻¹ a c b
      = if (∀ k, k ≠ a.castSucc → k ≠ a.succ → c k = b k) then
          rCheckN (d := d) q q⁻¹ (c a.castSucc, c a.succ) (b a.castSucc, b a.succ) else 0 := rfl

/-- Row `c` of `T_a` when `c` has a descent at `a`: a single `1`, at `swapAt a c`. -/
theorem strandBraid_row_desc (a : Fin m) {c : Fin (m + 1) → Fin d}
    (hc : c a.succ < c a.castSucc) (b : Fin (m + 1) → Fin d) :
    strandBraid (d := d) q q⁻¹ a c b = if b = swapAt a c then 1 else 0 := by
  have hne : c a.castSucc ≠ c a.succ := ne_of_gt hc
  rw [strandBraid_apply, rCheckN_apply]
  by_cases hb : b = swapAt a c
  · subst hb
    have hag : ∀ k, k ≠ a.castSucc → k ≠ a.succ → c k = swapAt a c k :=
      fun k h1 h2 => (swapAt_of_ne a c h1 h2).symm
    rw [if_pos hag]
    simp [hne]
  rw [if_neg hb]
  by_cases hag : ∀ k, k ≠ a.castSucc → k ≠ a.succ → c k = b k
  · rw [if_pos hag]
    by_cases h1 : (c a.castSucc, c a.succ) = (b a.castSucc, b a.succ)
    · rw [if_pos h1]
      simp only [Prod.ext_iff] at h1
      rw [← h1.1, ← h1.2, if_neg hne, if_neg (not_lt.2 (le_of_lt hc))]
    · rw [if_neg h1]
      by_cases h4 : (c a.castSucc, c a.succ) = (b a.succ, b a.castSucc)
      · simp only [Prod.ext_iff] at h4
        exact absurd ((eq_swapAt_iff a b c).1
          ⟨fun k h1 h2 => (hag k h1 h2).symm, h4.2.symm, h4.1.symm⟩) hb
      · rw [if_neg h4]
  · rw [if_neg hag]

/-- Column `u` of `T_a` when `u` is constant on strands `a, a+1`: `q` on the diagonal. -/
theorem strandBraid_col_eq (a : Fin m) {u : Fin (m + 1) → Fin d}
    (hu : u a.castSucc = u a.succ) (c : Fin (m + 1) → Fin d) :
    strandBraid (d := d) q q⁻¹ a c u = if c = u then q else 0 := by
  rw [strandBraid_apply, rCheckN_apply]
  by_cases hc : c = u
  · subst hc; simp [hu]
  rw [if_neg hc]
  by_cases hag : ∀ k, k ≠ a.castSucc → k ≠ a.succ → c k = u k
  · rw [if_pos hag]
    by_cases h1 : (c a.castSucc, c a.succ) = (u a.castSucc, u a.succ)
    · simp only [Prod.ext_iff] at h1
      exact absurd ((eq_iff_of_agree a c u).1 ⟨hag, h1.1, h1.2⟩) hc
    · rw [if_neg h1]
      by_cases h4 : (c a.castSucc, c a.succ) = (u a.succ, u a.castSucc)
      · simp only [Prod.ext_iff] at h4
        exact absurd ((eq_iff_of_agree a c u).1 ⟨hag, h4.1.trans hu.symm, h4.2.trans hu⟩) hc
      · rw [if_neg h4]
  · rw [if_neg hag]

/-- Column `b` of `T_a` when `b` has an ascent at `a`:
`T_a e_b = e_{swapAt a b} + (q − q⁻¹) e_b`. -/
theorem strandBraid_col_asc (a : Fin m) {b : Fin (m + 1) → Fin d}
    (hb : b a.castSucc < b a.succ) (c : Fin (m + 1) → Fin d) :
    strandBraid (d := d) q q⁻¹ a c b
      = (if c = swapAt a b then 1 else 0) + (if c = b then q - q⁻¹ else 0) := by
  have hne : b a.castSucc ≠ b a.succ := ne_of_lt hb
  have hsw : swapAt a b ≠ b := by
    intro h; apply hne
    have := congrFun h a.castSucc
    rw [swapAt_castSucc] at this
    exact this.symm
  rw [strandBraid_apply, rCheckN_apply]
  by_cases hc1 : c = swapAt a b
  · subst hc1
    rw [if_pos rfl, if_neg hsw]
    have hag : ∀ k, k ≠ a.castSucc → k ≠ a.succ → swapAt a b k = b k :=
      fun k h1 h2 => swapAt_of_ne a b h1 h2
    rw [if_pos hag]
    simp [Prod.ext_iff, hne, hne.symm]
  by_cases hc2 : c = b
  · subst hc2
    simp [hb, hne, hc1]
  rw [if_neg hc1, if_neg hc2, add_zero]
  by_cases hag : ∀ k, k ≠ a.castSucc → k ≠ a.succ → c k = b k
  · rw [if_pos hag]
    by_cases h1 : (c a.castSucc, c a.succ) = (b a.castSucc, b a.succ)
    · simp only [Prod.ext_iff] at h1
      exact absurd ((eq_iff_of_agree a c b).1 ⟨hag, h1.1, h1.2⟩) hc2
    · rw [if_neg h1]
      by_cases h4 : (c a.castSucc, c a.succ) = (b a.succ, b a.castSucc)
      · simp only [Prod.ext_iff] at h4
        exact absurd ((eq_swapAt_iff a c b).1 ⟨hag, h4.1, h4.2⟩) hc1
      · rw [if_neg h4]
  · rw [if_neg hag]

/-- `X` commutes with every Jimbo braiding: `X` lies in the q-Schur algebra. -/
def CommutesAll (X : Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K) : Prop :=
  ∀ a : Fin m, X * strandBraid q q⁻¹ a = strandBraid q q⁻¹ a * X

variable {q}

/-- **Row relation.** -/
theorem entry_swap_of_col_eq {X : Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K}
    (hX : CommutesAll q X) (a : Fin m) {u c : Fin (m + 1) → Fin d}
    (hu : u a.castSucc = u a.succ) (hc : c a.succ < c a.castSucc) :
    X (swapAt a c) u = q * X c u := by
  have h := congrFun (congrFun (hX a) c) u
  rw [mul_apply, mul_apply] at h
  rw [Finset.sum_eq_single u (fun b _ hb => by rw [strandBraid_col_eq q a hu, if_neg hb, mul_zero])
    (by simp), strandBraid_col_eq q a hu, if_pos rfl] at h
  rw [Finset.sum_eq_single (swapAt a c)
    (fun b _ hb => by rw [strandBraid_row_desc q a hc, if_neg hb, zero_mul]) (by simp),
    strandBraid_row_desc q a hc, if_pos rfl, one_mul] at h
  rw [← h, mul_comm]

/-- **Column relation.** -/
theorem col_swap_eq_zero {X : Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K}
    (hX : CommutesAll q X) (a : Fin m) {b : Fin (m + 1) → Fin d}
    (hb : b a.castSucc < b a.succ) (h0 : ∀ c, X c b = 0) (c : Fin (m + 1) → Fin d) :
    X c (swapAt a b) = 0 := by
  have h := congrFun (congrFun (hX a) c) b
  rw [mul_apply, mul_apply] at h
  have hr : ∑ j, strandBraid q q⁻¹ a c j * X j b = 0 :=
    Finset.sum_eq_zero fun j _ => by rw [h0 j, mul_zero]
  rw [hr] at h
  simp_rw [strandBraid_col_asc q a hb, mul_add, mul_ite, mul_one, mul_zero,
    Finset.sum_add_distrib, Finset.sum_ite_eq', Finset.mem_univ, if_true, h0 c, zero_mul,
    add_zero] at h
  exact h

/-! ### Potentials -/

/-- Weighted letter sum `Σ_p w p · c p`. -/
def pot (w : Fin (m + 1) → ℕ) (c : Fin (m + 1) → Fin d) : ℕ := ∑ p, w p * (c p : ℕ)

theorem pot_swapAt (w : Fin (m + 1) → ℕ) (a : Fin m) (c : Fin (m + 1) → Fin d) :
    pot w (swapAt a c) + w a.castSucc * (c a.castSucc : ℕ) + w a.succ * (c a.succ : ℕ)
      = pot w c + w a.castSucc * (c a.succ : ℕ) + w a.succ * (c a.castSucc : ℕ) := by
  classical
  have hne := castSucc_ne_succ a
  have hmem : a.succ ∈ (Finset.univ.erase a.castSucc) := by simp [hne.symm]
  have split : ∀ f : Fin (m + 1) → ℕ, ∑ p, f p = f a.castSucc + f a.succ
      + ∑ p ∈ (Finset.univ.erase a.castSucc).erase a.succ, f p := by
    intro f
    rw [← Finset.add_sum_erase _ f (Finset.mem_univ a.castSucc),
      ← Finset.add_sum_erase _ f hmem, add_assoc]
  have rest : ∑ p ∈ (Finset.univ.erase a.castSucc).erase a.succ,
      w p * ((swapAt a c p : Fin d) : ℕ)
      = ∑ p ∈ (Finset.univ.erase a.castSucc).erase a.succ, w p * ((c p : Fin d) : ℕ) := by
    refine Finset.sum_congr rfl fun p hp => ?_
    simp only [Finset.mem_erase] at hp
    rw [swapAt_of_ne a c hp.2.1 hp.1]
  unfold pot
  rw [split, split (fun p => w p * ((c p : Fin d) : ℕ)), rest, swapAt_castSucc, swapAt_succ]
  ring

/-- Forward weights `p`. Swapping an ascent lowers the potential. -/
theorem pot_fwd_lt (a : Fin m) {c : Fin (m + 1) → Fin d} (hc : c a.castSucc < c a.succ) :
    pot (fun p => (p : ℕ)) (swapAt a c) < pot (fun p => (p : ℕ)) c := by
  have h := pot_swapAt (fun p => (p : ℕ)) a c
  simp only [Fin.coe_castSucc, Fin.val_succ] at h
  have hc' : (c a.castSucc : ℕ) < c a.succ := hc
  nlinarith

/-- Backward weights `m − p`. Swapping a descent lowers the potential. -/
theorem pot_bwd_lt (a : Fin m) {b : Fin (m + 1) → Fin d} (hb : b a.succ < b a.castSucc) :
    pot (fun p => m - (p : ℕ)) (swapAt a b) < pot (fun p => m - (p : ℕ)) b := by
  have h := pot_swapAt (fun p => m - (p : ℕ)) a b
  simp only [Fin.coe_castSucc, Fin.val_succ] at h
  have hb' : (b a.succ : ℕ) < b a.castSucc := hb
  have ha : (a : ℕ) < m := a.2
  have e : m - (a : ℕ) = (m - (a + 1)) + 1 := by omega
  rw [e] at h
  nlinarith

/-! ### The injectivity statement -/

/-- `c` is weakly decreasing on every block of strands on which `u` is constant. -/
def BlockDec (u c : Fin (m + 1) → Fin d) : Prop :=
  ∀ a : Fin m, u a.castSucc = u a.succ → c a.succ ≤ c a.castSucc

/-- **Sorted columns.** In a sorted column, every entry is a multiple of a block-decreasing
one. -/
theorem entry_eq_zero_of_sorted {X : Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K}
    (hX : CommutesAll q X) {u : Fin (m + 1) → Fin d}
    (h0 : ∀ c, BlockDec u c → X c u = 0) (c : Fin (m + 1) → Fin d) : X c u = 0 := by
  induction hP : pot (fun p => (p : ℕ)) c using Nat.strong_induction_on generalizing c with
  | _ n ih =>
  by_cases hc : BlockDec u c
  · exact h0 c hc
  · simp only [BlockDec, not_forall, not_le] at hc
    obtain ⟨a, hu, hlt⟩ := hc
    set c' := swapAt a c with hc'
    have hdesc : c' a.succ < c' a.castSucc := by simpa [hc'] using hlt
    have e := entry_swap_of_col_eq hX a hu hdesc
    rw [hc', swapAt_swapAt] at e
    rw [e, ih _ (hP ▸ pot_fwd_lt a hlt) c' rfl, mul_zero]

/-- **The coefficient map is injective.** An element of the q-Schur algebra whose entries
vanish at every (block-decreasing, sorted) pair is zero. -/
theorem eq_zero_of_coeffs {X : Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K}
    (hX : CommutesAll q X) (h0 : ∀ u c, Monotone u → BlockDec u c → X c u = 0) : X = 0 := by
  have hcol : ∀ b c, X c b = 0 := by
    intro b
    induction hP : pot (fun p => m - (p : ℕ)) b using Nat.strong_induction_on generalizing b
      with
    | _ n ih =>
    by_cases hb : Monotone b
    · exact entry_eq_zero_of_sorted hX (h0 b · hb)
    · rw [Fin.monotone_iff_le_succ] at hb
      simp only [not_forall, not_le] at hb
      obtain ⟨a, hlt⟩ := hb
      set b' := swapAt a b with hb'
      have hasc : b' a.castSucc < b' a.succ := by simpa [hb'] using hlt
      have e := col_swap_eq_zero hX a hasc (ih _ (hP ▸ pot_bwd_lt a hlt) b' rfl)
      simpa [hb'] using e
  funext b c
  exact hcol c b

/-! ### The dimension bound -/

variable (q) (d m)

/-- The q-Schur algebra `S_q(d, m+1)`, as the subspace of matrices commuting with every
Jimbo braiding. -/
def qSchur : Submodule K (Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K) where
  carrier := {X | CommutesAll q X}
  add_mem' := by
    intro X Y hX hY a
    simp only [Set.mem_setOf_eq] at hX hY
    rw [add_mul, mul_add, hX a, hY a]
  zero_mem' := by intro a; simp
  smul_mem' := by
    intro c X hX a
    simp only [Set.mem_setOf_eq] at hX
    rw [smul_mul_assoc, mul_smul_comm, hX a]

/-- The index set: pairs `(u, c)` with `u` sorted and `c` block-decreasing for `u`. -/
def Idx : Type := {p : (Fin (m + 1) → Fin d) × (Fin (m + 1) → Fin d) //
  Monotone p.1 ∧ BlockDec p.1 p.2}

noncomputable instance : Fintype (Idx d m) := by
  classical
  unfold Idx; infer_instance

/-- The coefficient map `X ↦ (X c u)_{(u,c)}`. -/
def coeffMap : qSchur d m q →ₗ[K] (Idx d m → K) where
  toFun X p := (X : Matrix _ _ K) p.1.2 p.1.1
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

theorem coeffMap_injective : Function.Injective (coeffMap d m q) := by
  rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
  intro X hX
  have h := eq_zero_of_coeffs (q := q) X.2 (fun u c hu hc => congrFun hX ⟨(u, c), hu, hc⟩)
  exact Subtype.ext h

/-- **DJ1–DJ2 upper bound.** `dim S_q(d, m+1) ≤ #{(u, c) : u sorted, c block-decreasing}`,
over any field, for any `q` (the inverse `q⁻¹` enters only through the definition of the
braiding; no genericity is used). -/
theorem finrank_qSchur_le :
    Module.finrank K (qSchur d m q) ≤ Fintype.card (Idx d m) := by
  have := LinearMap.finrank_le_finrank_of_injective (coeffMap_injective d m q)
  rwa [Module.finrank_fintype_fun_eq_card] at this

end QOU.SchurWeyl.QSchurUpperBound
