import QOU.SchurWeyl.OcneanuWeight
import Mathlib.Tactic.LinearCombination

/-!
# QOU.SchurWeyl.OcneanuWeightWindowInvolution — which involution acts on `z` as `z ↦ h − z`

`h = q − q⁻¹`.  The positive window `0 ≤ z ≤ h` of the Ocneanu weights
(`QOU.SchurWeyl.PositiveWindow.forall_pos_iff`) is mapped to itself by `z ↦ h − z`, with
fixed point `h/2`.  This file identifies the involution behind that reflection and separates
it from the Kazhdan–Lusztig bar involution, with which it is easily confused.

## The two identities (over any field, `q ≠ 0`)

* **Sign-transpose** (`ocneanuWeight_transpose_reflect`):

      w_{μ'}(q, h − z) = w_μ(q, z).

  This is the weight-level shadow of the algebra automorphism `σ ↦ −σ⁻¹` of `H_n(q)`
  (coefficients untouched).  It preserves the Hecke relation (eigenvalues `q ↔ −q⁻¹`),
  sends `tr(σ) = z` to `tr(−σ⁻¹) = tr(h − σ) = h − z`, and carries `V_λ` to `V_{λ'}`
  (`computations/hecke_conjugation_duality_sign_probe.py` checks the last fact on words).
  Cell by cell: the factor of `(i,j)` at `z` equals the factor of `(j,i)` at `h − z`, and
  hook lengths are transpose-invariant (`hookLength_transpose`).

* **Bar** (`ocneanuWeight_bar`):

      w_μ(q⁻¹, z − h) = w_μ(q, z).

  This is the shadow of `σ ↦ σ⁻¹, q ↦ q⁻¹`, which fixes each `V_λ`.  Each cell factor
  picks up `−q^{−2(i+j+1)}` and each hook factor `−q^{−2·hook}`, and these cancel because
  `Σ hook = Σ (i + j + 1)` (`sum_hookLength`).

## What each one forces

* **The sign-transpose involution has a unique fixed parameter.**
  `transpose_symmetric_iff_half`: `w_{μ'}(q,z) = w_μ(q,z)` for every `μ` iff `z = h/2`
  (given `q ≠ 0`, `q² ≠ 1`, `q⁴ ≠ 1`, `2 ≠ 0`); the `n = 2` pair `(2) ↔ (1,1)` already forces it.

* **Bar-invariance does not.**  The bar-conjugate of the trace with parameter `z(q)` has
  parameter `z(q⁻¹) + h(q)`, so a bar-invariant trace needs `z(q) − z(q⁻¹) = h`
  (`BarInvariantParam`).  `barInvariant_iff_even`: writing `z = h/2 + u`, this holds iff `u` is
  bar-even — a whole function's worth of freedom.  Members proved here: `h/2`
  (`barInvariant_half`), every Ocneanu rank parameter `z_k = h q^{2k}/(q^{2k} − 1)`
  (`barInvariant_rank`; `z_1 = q`, `z_2 = q³/(q²+1)`), convention D itself
  (`barInvariant_conventionD`), and the mirror `h − z` of any member
  (`barInvariant_reflect`).  Inside the window, `h/2 + h²/(1+h²)` is bar-invariant and
  differs from `h/2` (checked exactly in
  `computations/deltalambda/ocneanu_window_involution_probe.py`).  So the bar involution
  alone does **not** single out `h/2` — scope (a): a statement about this one condition.

## Relation to the corpus (not new where it is not)

* The converse direction at character level — normalised transpose-symmetric weights give
  effective parameter `h/2` — is `QOU.BraidsAndKnots.markov_param_eq_half_h`
  (`TransposeSymmetricWeightsForceHalfH`).  What is added here is the identity on the
  Ocneanu closed form itself, valid at every `z`, from which the fixed-point statement follows.
* That convention D satisfies `bar(z) = z − h` and that `h/2` is the unique bar-**odd** member
  of that class is recorded in `docs/audits/2026-08-31-cds1-block-bar-defect-and-conjugation.md`
  (Result 4).  Adding the condition "bar-odd" (`z(q⁻¹) = −z(q)`) to bar-invariance is exactly
  adding sign-transpose invariance, and that is what pins `h/2`.
* Nothing here adopts a Markov parameter.  Convention D (owner ruling 2026-08-15) is
  bar-invariant and lies outside the window; this file says only which symmetry each
  parameter has.

## What is NOT claimed

That `ocneanuWeight` is the Markov trace's weight system at general `n` is proved only at
`n = 3` (`OcneanuWeightMarkov3`); the trace-level reading above is conditional on it.  The
identities themselves are unconditional statements about the closed form.  Whether either
invariance is *required* by any derivation in the corpus is not settled here.

## Base ring (§7c)

Generic `[Field R]`; `ℝ` appears nowhere.

`Ref: [jones1987]`, `[wenzl1988]`; the sign twist `σ ↦ −σ⁻¹` is standard, `[iwahori1964]`.

LaTeX label: `prop:ocneanu-weight-window-involution`
-/
namespace QOU.SchurWeyl.WindowInvolution
open QOU.SchurWeyl YoungDiagram

theorem prod_cells_transpose {M : Type*} [CommMonoid M] (mu : YoungDiagram)
    (f : ℕ × ℕ → M) :
    ∏ c ∈ mu.transpose.cells, f c = ∏ c ∈ mu.cells, f c.swap := by
  show ∏ c ∈ (Equiv.prodComm _ _).finsetCongr mu.cells, f c = _
  rw [Equiv.finsetCongr_apply, Finset.prod_map]
  rfl

theorem sum_cells_transpose {M : Type*} [AddCommMonoid M] (mu : YoungDiagram)
    (f : ℕ × ℕ → M) :
    ∑ c ∈ mu.transpose.cells, f c = ∑ c ∈ mu.cells, f c.swap := by
  show ∑ c ∈ (Equiv.prodComm _ _).finsetCongr mu.cells, f c = _
  rw [Equiv.finsetCongr_apply, Finset.sum_map]
  rfl

theorem card_filter_transpose (mu : YoungDiagram) (P : ℕ × ℕ → Prop) [DecidablePred P] :
    (mu.transpose.cells.filter P).card = (mu.cells.filter (fun e => P e.swap)).card := by
  rw [Finset.card_eq_sum_ones, Finset.card_eq_sum_ones, Finset.sum_filter, Finset.sum_filter,
    sum_cells_transpose]

theorem card_row_le (s : Finset (ℕ × ℕ)) {c : ℕ × ℕ} (hc : c ∈ s) :
    (s.filter (fun e => e.1 = c.1 ∧ c.2 ≤ e.2)).card
      = (s.filter (fun e => e.1 = c.1 ∧ c.2 < e.2)).card + 1 := by
  have : s.filter (fun e => e.1 = c.1 ∧ c.2 ≤ e.2)
      = insert c (s.filter (fun e => e.1 = c.1 ∧ c.2 < e.2)) := by
    ext e
    simp only [Finset.mem_filter, Finset.mem_insert]
    constructor
    · rintro ⟨he, h1, h2⟩
      rcases Nat.lt_or_eq_of_le h2 with h | h
      · exact Or.inr ⟨he, h1, h⟩
      · exact Or.inl (Prod.ext h1 h.symm)
    · rintro (rfl | ⟨he, h1, h2⟩)
      · exact ⟨hc, rfl, le_rfl⟩
      · exact ⟨he, h1, h2.le⟩
  rw [this, Finset.card_insert_of_notMem]
  simp

theorem card_col_le (s : Finset (ℕ × ℕ)) {c : ℕ × ℕ} (hc : c ∈ s) :
    (s.filter (fun e => e.2 = c.2 ∧ c.1 ≤ e.1)).card
      = (s.filter (fun e => e.2 = c.2 ∧ c.1 < e.1)).card + 1 := by
  have : s.filter (fun e => e.2 = c.2 ∧ c.1 ≤ e.1)
      = insert c (s.filter (fun e => e.2 = c.2 ∧ c.1 < e.1)) := by
    ext e
    simp only [Finset.mem_filter, Finset.mem_insert]
    constructor
    · rintro ⟨he, h1, h2⟩
      rcases Nat.lt_or_eq_of_le h2 with h | h
      · exact Or.inr ⟨he, h1, h⟩
      · exact Or.inl (Prod.ext h.symm h1)
    · rintro (rfl | ⟨he, h1, h2⟩)
      · exact ⟨hc, rfl, le_rfl⟩
      · exact ⟨he, h1, h2.le⟩
  rw [this, Finset.card_insert_of_notMem]
  simp

theorem hookLength_transpose (mu : YoungDiagram) {c : ℕ × ℕ} (hc : c ∈ mu.cells) :
    hookLength mu.transpose c.swap = hookLength mu c := by
  unfold hookLength
  rw [card_filter_transpose, card_filter_transpose]
  simp only [Prod.fst_swap, Prod.snd_swap]
  rw [card_row_le _ hc, card_col_le _ hc]
  omega


/-- Swap a double count: `Σ_c #{d ∈ s : P c d} = Σ_d #{c ∈ s : P c d}`. -/
theorem sum_card_filter_comm (s : Finset (ℕ × ℕ)) (P : ℕ × ℕ → ℕ × ℕ → Prop)
    [∀ c d, Decidable (P c d)] :
    ∑ c ∈ s, (s.filter (fun d => P c d)).card = ∑ d ∈ s, (s.filter (fun c => P c d)).card := by
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  exact Finset.sum_comm

theorem card_row_prefix (mu : YoungDiagram) {d : ℕ × ℕ} (hd : d ∈ mu.cells) :
    (mu.cells.filter (fun c => d.1 = c.1 ∧ c.2 ≤ d.2)).card = d.2 + 1 := by
  have : mu.cells.filter (fun c => d.1 = c.1 ∧ c.2 ≤ d.2)
      = (Finset.range (d.2 + 1)).map ⟨fun j => (d.1, j), fun a b h => by simpa using h⟩ := by
    ext ⟨a, b⟩
    simp only [Finset.mem_filter, Finset.mem_map, Finset.mem_range, Function.Embedding.coeFn_mk,
      Prod.mk.injEq]
    constructor
    · rintro ⟨-, h1, h2⟩
      exact ⟨b, by omega, h1, rfl⟩
    · rintro ⟨j, hj, rfl, rfl⟩
      refine ⟨?_, rfl, by omega⟩
      rw [YoungDiagram.mem_cells] at hd ⊢
      exact mu.up_left_mem le_rfl (by omega) hd
  rw [this, Finset.card_map, Finset.card_range]

theorem card_col_prefix (mu : YoungDiagram) {d : ℕ × ℕ} (hd : d ∈ mu.cells) :
    (mu.cells.filter (fun c => d.2 = c.2 ∧ c.1 < d.1)).card = d.1 := by
  have : mu.cells.filter (fun c => d.2 = c.2 ∧ c.1 < d.1)
      = (Finset.range d.1).map ⟨fun i => (i, d.2), fun a b h => by simpa using h⟩ := by
    ext ⟨a, b⟩
    simp only [Finset.mem_filter, Finset.mem_map, Finset.mem_range, Function.Embedding.coeFn_mk,
      Prod.mk.injEq]
    constructor
    · rintro ⟨-, h1, h2⟩
      exact ⟨a, h2, rfl, h1⟩
    · rintro ⟨i, hi, rfl, rfl⟩
      refine ⟨?_, rfl, hi⟩
      rw [YoungDiagram.mem_cells] at hd ⊢
      exact mu.up_left_mem hi.le le_rfl hd
  rw [this, Finset.card_map, Finset.card_range]

/-- **The hook lengths sum to `Σ_{(i,j)} (i + j + 1)`.** -/
theorem sum_hookLength (mu : YoungDiagram) :
    ∑ c ∈ mu.cells, hookLength mu c = ∑ c ∈ mu.cells, (c.1 + c.2 + 1) := by
  unfold hookLength
  rw [Finset.sum_add_distrib]
  rw [sum_card_filter_comm mu.cells (fun c d => d.1 = c.1 ∧ c.2 ≤ d.2),
    sum_card_filter_comm mu.cells (fun c d => d.2 = c.2 ∧ c.1 < d.1)]
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun d hd => ?_
  have e1 : (mu.cells.filter (fun c => d.1 = c.1 ∧ c.2 ≤ d.2)).card = d.2 + 1 :=
    card_row_prefix mu hd
  have e2 : (mu.cells.filter (fun c => d.2 = c.2 ∧ c.1 < d.1)).card = d.1 :=
    card_col_prefix mu hd
  simp only [e1, e2]
  omega


variable {R : Type*} [Field R]

/-- **Sign-transpose identity.** `w_{μ'}(q, h − z) = w_μ(q, z)`, `h = q − q⁻¹`. -/
theorem ocneanuWeight_transpose_reflect (q z : R) (hq : q ≠ 0) (mu : YoungDiagram) :
    ocneanuWeight q (q - q⁻¹ - z) mu.transpose = ocneanuWeight q z mu := by
  unfold ocneanuWeight
  rw [prod_cells_transpose, prod_cells_transpose]
  congr 1
  · refine Finset.prod_congr rfl fun c _ => ?_
    simp only [Prod.fst_swap, Prod.snd_swap]
    field_simp
    ring
  · refine Finset.prod_congr rfl fun c hc => ?_
    rw [hookLength_transpose mu hc]

/-- **Bar identity.** `w_μ(q⁻¹, z − h) = w_μ(q, z)`, `h = q − q⁻¹`. -/
theorem ocneanuWeight_bar (q z : R) (hq : q ≠ 0) (mu : YoungDiagram) :
    ocneanuWeight q⁻¹ (z - (q - q⁻¹)) mu = ocneanuWeight q z mu := by
  unfold ocneanuWeight
  have hnum : ∀ c : ℕ × ℕ,
      q⁻¹ ^ (2 * c.1) * (q⁻¹ ^ 2 - 1 - q⁻¹ * (z - (q - q⁻¹))) + q⁻¹ ^ (2 * c.2 + 1) * (z - (q - q⁻¹))
        = (-1) * (q⁻¹ ^ 2) ^ (c.1 + c.2 + 1)
            * (q ^ (2 * c.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * c.2 + 1) * z) := by
    intro c
    simp only [inv_pow, ← pow_mul]
    field_simp
    ring
  have hden : ∀ c : ℕ × ℕ, q⁻¹ ^ (2 * hookLength mu c) - 1
      = (-1) * (q⁻¹ ^ 2) ^ hookLength mu c * (q ^ (2 * hookLength mu c) - 1) := by
    intro c
    simp only [inv_pow, ← pow_mul]
    field_simp
    ring
  simp only [hnum, hden, Finset.prod_mul_distrib, Finset.prod_pow_eq_pow_sum, sum_hookLength]
  have h0 : (∏ _c ∈ mu.cells, (-1 : R)) * (q⁻¹ ^ 2) ^ ∑ c ∈ mu.cells, (c.1 + c.2 + 1) ≠ 0 := by
    refine mul_ne_zero ?_ (pow_ne_zero _ (pow_ne_zero _ (inv_ne_zero hq)))
    rw [Finset.prod_const]
    exact pow_ne_zero _ (by norm_num)
  exact mul_div_mul_left _ _ h0


/-- The one-row diagram `(2)`. -/
def row2 : YoungDiagram where
  cells := {(0, 0), (0, 1)}
  isLowerSet := by
    intro a b hba hb
    simp only [Finset.coe_insert, Finset.coe_singleton, Set.mem_insert_iff,
      Set.mem_singleton_iff] at hb ⊢
    obtain ⟨h1, h2⟩ := hba
    rcases hb with rfl | rfl
    · left; exact Prod.ext (Nat.le_zero.mp h1) (Nat.le_zero.mp h2)
    · rcases Nat.le_one_iff_eq_zero_or_eq_one.mp h2 with h | h
      · left; exact Prod.ext (Nat.le_zero.mp h1) h
      · right; exact Prod.ext (Nat.le_zero.mp h1) h

theorem ocneanuWeight_row2 (q z : R) :
    ocneanuWeight q z row2
      = ((q ^ 2 - 1) * ((q ^ 2 - 1 - q * z) + q ^ 3 * z))
          / ((q ^ 4 - 1) * (q ^ 2 - 1)) := by
  have h00 : hookLength row2 (0, 0) = 2 := by decide
  have h01 : hookLength row2 (0, 1) = 1 := by decide
  unfold ocneanuWeight
  show (∏ c ∈ ({(0, 0), (0, 1)} : Finset (ℕ × ℕ)), _) / (∏ c ∈ ({(0, 0), (0, 1)} : Finset (ℕ × ℕ)), _) = _
  rw [Finset.prod_pair (by decide), Finset.prod_pair (by decide), h00, h01]
  ring

theorem ocneanuWeight_row2_transpose (q z : R) :
    ocneanuWeight q z row2.transpose
      = ((q ^ 2 - 1) * (q ^ 2 * (q ^ 2 - 1 - q * z) + q * z))
          / ((q ^ 4 - 1) * (q ^ 2 - 1)) := by
  unfold ocneanuWeight
  rw [prod_cells_transpose, prod_cells_transpose]
  have h00 : hookLength row2.transpose (0, 0) = 2 := by
    simpa using hookLength_transpose row2 (c := (0, 0)) (by decide)
  have h10 : hookLength row2.transpose (1, 0) = 1 := by
    simpa using hookLength_transpose row2 (c := (0, 1)) (by decide)
  show (∏ c ∈ ({(0, 0), (0, 1)} : Finset (ℕ × ℕ)), _) / (∏ c ∈ ({(0, 0), (0, 1)} : Finset (ℕ × ℕ)), _) = _
  rw [Finset.prod_pair (by decide), Finset.prod_pair (by decide)]
  simp only [Prod.swap_prod_mk, h00, h10]
  ring

/-- **The sign-transpose involution has exactly one fixed Markov parameter, `z = h/2`.**

The weight system is transpose-symmetric (`w_{μ'} = w_μ` for every `μ`) iff `z = (q − q⁻¹)/2`.
The `n = 2` pair `(2) ↔ (1,1)` alone already forces it. -/
theorem transpose_symmetric_iff_half (q z : R) (hq : q ≠ 0) (hq2 : q ^ 2 - 1 ≠ 0)
    (hq4 : q ^ 4 - 1 ≠ 0) (h2 : (2 : R) ≠ 0) :
    (∀ mu : YoungDiagram, ocneanuWeight q z mu.transpose = ocneanuWeight q z mu)
      ↔ z = (q - q⁻¹) / 2 := by
  constructor
  · intro h
    have e := h row2
    rw [ocneanuWeight_row2_transpose, ocneanuWeight_row2] at e
    have hd : (q ^ 4 - 1) * (q ^ 2 - 1) ≠ 0 := mul_ne_zero hq4 hq2
    rw [div_left_inj' hd] at e
    -- e : (q²−1)(q²(q²−1−qz)+qz) = (q²−1)((q²−1−qz)+q³z)
    have e2 : (q ^ 2 - 1) * ((q ^ 2 - 1) * ((q ^ 2 - 1) - 2 * q * z)) = 0 := by
      linear_combination e
    rcases mul_eq_zero.mp e2 with h' | h'
    · exact absurd h' hq2
    rcases mul_eq_zero.mp h' with h'' | h''
    · exact absurd h'' hq2
    field_simp
    linear_combination -h''
  · rintro rfl mu
    have := ocneanuWeight_transpose_reflect q ((q - q⁻¹) / 2) hq mu
    have hh : q - q⁻¹ - (q - q⁻¹) / 2 = (q - q⁻¹) / 2 := by field_simp; ring
    rwa [hh] at this

/-! ### Bar-invariance of the parameter does not single out `h/2` -/

/-- The parameter condition for a bar-invariant Markov trace: `z(q) − z(q⁻¹) = q − q⁻¹`. -/
def BarInvariantParam (zf : R → R) (q : R) : Prop := zf q - zf q⁻¹ = q - q⁻¹

theorem barInvariant_half (q : R) (h2 : (2 : R) ≠ 0) :
    BarInvariantParam (fun x : R => (x - x⁻¹) / 2) q := by
  unfold BarInvariantParam
  simp only [inv_inv]
  field_simp
  ring

/-- The rank-`k` Ocneanu parameter `z_k = h q^{2k}/(q^{2k} − 1)` is bar-invariant. -/
theorem barInvariant_rank (k : ℕ) (q : R) (hq : q ≠ 0) (hk : q ^ (2 * k) - 1 ≠ 0) :
    BarInvariantParam (fun x : R => (x - x⁻¹) * x ^ (2 * k) / (x ^ (2 * k) - 1)) q := by
  unfold BarInvariantParam
  simp only [inv_inv, inv_pow]
  set Q := q ^ (2 * k) with hQ
  have hQ0 : Q ≠ 0 := pow_ne_zero _ hq
  have hk' : Q⁻¹ - 1 ≠ 0 := by
    intro h
    apply hk
    have : Q⁻¹ = 1 := by linear_combination h
    rw [inv_eq_one] at this
    rw [this]; ring
  have h1Q : 1 - Q ≠ 0 := fun h => hk (by linear_combination -h)
  field_simp
  ring

/-- Convention D, `z_D = q³/(q²+1)`, is bar-invariant. -/
theorem barInvariant_conventionD (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    BarInvariantParam (fun x : R => x ^ 3 / (x ^ 2 + 1)) q := by
  unfold BarInvariantParam
  simp only [inv_pow]
  have h' : (q ^ 2)⁻¹ + 1 ≠ 0 := by
    intro h
    apply hq2
    have : (q ^ 2)⁻¹ * (q ^ 2 + 1) = 0 := by
      rw [mul_add, inv_mul_cancel₀ (pow_ne_zero 2 hq)]; linear_combination h
    rcases mul_eq_zero.mp this with h1 | h1
    · exact absurd h1 (inv_ne_zero (pow_ne_zero 2 hq))
    · exact h1
  have h1q : 1 + q ^ 2 ≠ 0 := fun h => hq2 (by linear_combination h)
  field_simp
  ring

/-- The mirror `h − z` of a bar-invariant parameter is bar-invariant. -/
theorem barInvariant_reflect (zf : R → R) (q : R) (h : BarInvariantParam zf q) :
    BarInvariantParam (fun x : R => (x - x⁻¹) - zf x) q := by
  unfold BarInvariantParam at h ⊢
  simp only [inv_inv]
  linear_combination -h


/-- **Bar-invariance fixes only the bar-odd part of the parameter.** Writing `z = h/2 + u`,
the trace is bar-invariant iff `u` is bar-even: `u(q) = u(q⁻¹)`.  Any bar-even `u` is allowed. -/
theorem barInvariant_iff_even (u : R → R) (q : R) (h2 : (2 : R) ≠ 0) :
    BarInvariantParam (fun x : R => (x - x⁻¹) / 2 + u x) q ↔ u q = u q⁻¹ := by
  unfold BarInvariantParam
  simp only [inv_inv]
  generalize u q = a
  generalize u q⁻¹ = b
  have e : (q - q⁻¹) / 2 + a - ((q⁻¹ - q) / 2 + b) - (q - q⁻¹) = a - b := by
    field_simp
    ring
  constructor
  · intro h
    linear_combination -e + h
  · intro h
    linear_combination e + h

end QOU.SchurWeyl.WindowInvolution
