import QOU.Mass.GammaGammaVertexOrder

/-!
# The confinement SDP on braid words, reading 3: Frobenius positivity selects `β_Bor`

Bean `qou-ales`, step 5. Owner ruling 2026-09-12 (chat): *"try PSD confinement 3
for now, but keep 1 2 for later."* Three readings of "the confinement SDP at `q₀`
selects a braid word" were on the table after steps 3 and 4:

1. **literal** — every Wedderburn projection `π_λ(w)` is `Matrix.PosSemidef`
   (step 1's `SDPSelected`; on `H₃` this admits a non-trivial γγ word iff some
   vertex power is `±1`, `vtx_pow_isHermitian_iff_scalar`, and for `1 < q ≤ 23/20`
   no `k ≤ 5` survives, `hoefsmit_vtx_pow_not_isHermitian`);
2. **symmetric part** — `π_λ(w) + π_λ(w)ᵀ` is PSD (`SymPSDFeasible` below);
3. **Frobenius positivity** — on every block carrying positive Markov weight
   `y_λ > 0`, the character `χ_λ(w) = tr π_λ(w)` is non-negative
   (`FrobeniusFeasible` below). This is the reading adopted *for now*.

This file formalises reading 3 and proves what it selects on `H₃`, and keeps
readings 1 and 2 on record by proving the only relation between them that is
free: **1 ⇒ 3 and 2 ⇒ 3** (a PSD matrix has non-negative trace; the symmetric
part has the same trace). Hence whatever readings 1 or 2 select later has cost
at least the reading-3 minimum (`FrobeniusSelected.cost_le_of_psdFeasible`,
`…_of_symPSDFeasible`).

## What is proved (all sorry-free)

* `frobeniusFeasible_iff_std` — for a γγ-word on `H₃`, reading-3 feasibility is
  decided by the `(2,1)` block alone: `(3)` and `(1³)` have character `1`.
* `vertexPow_frobeniusFeasible_iff` — for the vertex power `(σ₀σ₁⁻¹)^k` it is
  `0 < y_(2,1) → 0 ≤ tr V^k`, with `V` the vertex image of step 4.
* `hoefsmit_vertexPow_frobenius_table` — at the concrete Hoefsmit data, for every
  `1 < q ≤ 23/20` and every `y` with `y_(2,1) > 0`: `k = 1, 2, 4, 5` are
  **infeasible** and `k = 3` is **feasible** (the sign table of step 4,
  `chi_signs_of_small`, read as feasibility).
* `frobeniusSelected_borromean` — **the minimal non-zero Frobenius-feasible
  vertex power with `k ≤ 5`, cost = crossing count, is `k = 3`, i.e. `β_Bor`**,
  for every `1 < q ≤ 23/20` (the proton pin `q₀ ≈ 1.10998` is inside) and every
  positive weight on the `(2,1)` block. Under convention D at the pin the step-3
  witness has `y_(3) = 0.5054`, `y_(2,1) = 0.2473`, `y_(1³) = 0`; only the sign
  of `y_(2,1)` enters here.

## What is NOT proved

* Nothing about `k > 5` (the candidate set is `vertexPowCands 5`, the γγ words of
  `H₃` with at most ten crossings); `chi_signs_of_small` stops at five.
* Nothing about non-γγ letters (step-3 §4.2) or the `H₆` interface.
* Reading 3 is the owner's provisional choice, not a derivation of which
  reading the confinement SDP *means*; readings 1 and 2 stay recorded above.
* No AME, CODATA binding value or census is read anywhere in the cone.

## Base ring (§7c)

`FrobeniusFeasible` / `FrobeniusSelected` are over a generic
`[Ring R] [PartialOrder R]`. The comparisons with readings 1 and 2 use
`Matrix.PosSemidef.trace_nonneg`, which Mathlib states for `RCLike`, so they
are over `ℝ`; the `H₃` results are over `ℝ` as in steps 3 and 4.
-/

namespace QOU.Mass.GammaGammaFrobeniusSelection

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaSelectorH3
open QOU.Mass.GammaGammaVertexOrder

/-! ## Reading 3, abstractly -/

section Abstract

variable {R : Type*} [Ring R] [PartialOrder R]
variable {W ι : Type*} {d : ι → ℕ}

/-- **Frobenius feasibility** (reading 3 of the confinement SDP): on every
Wedderburn block `l` with positive Markov weight `y l`, the character
`tr (π_l w)` is non-negative. Blocks of weight `≤ 0` impose nothing. -/
def FrobeniusFeasible (B : WedderburnBlocks R W ι d) (y : ι → R) (w : W) : Prop :=
  ∀ l : ι, 0 < y l → 0 ≤ (B.proj w l).trace

/-- **Reading-3 selection**: `w` is a candidate, is Frobenius-feasible, and has
minimal cost among the Frobenius-feasible candidates. Mirror of step 1's
`SDPSelected` with `PSDFeasible` replaced by `FrobeniusFeasible`. -/
structure FrobeniusSelected (B : WedderburnBlocks R W ι d) (y : ι → R) (cands : Set W)
    (cost : W → R) (w : W) : Prop where
  /-- `w` is a candidate. -/
  mem : w ∈ cands
  /-- `w` is Frobenius-feasible. -/
  feasible : FrobeniusFeasible B y w
  /-- No Frobenius-feasible candidate is cheaper. -/
  minimal : ∀ w' ∈ cands, FrobeniusFeasible B y w' → cost w ≤ cost w'

/-- Two reading-3-selected words have equal cost. -/
theorem FrobeniusSelected.cost_eq {B : WedderburnBlocks R W ι d} {y : ι → R} {cands : Set W}
    {cost : W → R} {w₁ w₂ : W} (h₁ : FrobeniusSelected B y cands cost w₁)
    (h₂ : FrobeniusSelected B y cands cost w₂) : cost w₁ = cost w₂ :=
  le_antisymm (h₁.minimal w₂ h₂.mem h₂.feasible) (h₂.minimal w₁ h₁.mem h₁.feasible)

end Abstract

/-! ## Readings 1 and 2, kept on record: both imply reading 3 -/

section Readings

variable {W ι : Type*} {d : ι → ℕ}

/-- **Reading 2**: the symmetric part `π_l w + (π_l w)ᵀ` of every block is PSD. -/
def SymPSDFeasible (B : WedderburnBlocks ℝ W ι d) (w : W) : Prop :=
  ∀ l : ι, (B.proj w l + (B.proj w l).transpose).PosSemidef

/-- Reading 1 ⇒ reading 3: a PSD matrix has non-negative trace. -/
theorem FrobeniusFeasible.of_psdFeasible {B : WedderburnBlocks ℝ W ι d} (y : ι → ℝ) {w : W}
    (h : B.PSDFeasible w) : FrobeniusFeasible B y w :=
  fun l _ => (h l).trace_nonneg

/-- Reading 2 ⇒ reading 3: the symmetric part has trace `2 · tr (π_l w)`. -/
theorem FrobeniusFeasible.of_symPSDFeasible {B : WedderburnBlocks ℝ W ι d} (y : ι → ℝ) {w : W}
    (h : SymPSDFeasible B w) : FrobeniusFeasible B y w := by
  intro l _
  have ht := (h l).trace_nonneg
  rw [Matrix.trace_add, Matrix.trace_transpose] at ht
  linarith

/-- The reading-3 minimum is a lower bound for anything reading 1 can select. -/
theorem FrobeniusSelected.cost_le_of_psdFeasible {B : WedderburnBlocks ℝ W ι d} {y : ι → ℝ}
    {cands : Set W} {cost : W → ℝ} {w : W} (h : FrobeniusSelected B y cands cost w)
    {w' : W} (hm : w' ∈ cands) (hp : B.PSDFeasible w') : cost w ≤ cost w' :=
  h.minimal w' hm (FrobeniusFeasible.of_psdFeasible y hp)

/-- The reading-3 minimum is a lower bound for anything reading 2 can select. -/
theorem FrobeniusSelected.cost_le_of_symPSDFeasible {B : WedderburnBlocks ℝ W ι d} {y : ι → ℝ}
    {cands : Set W} {cost : W → ℝ} {w : W} (h : FrobeniusSelected B y cands cost w)
    {w' : W} (hm : w' ∈ cands) (hp : SymPSDFeasible B w') : cost w ≤ cost w' :=
  h.minimal w' hm (FrobeniusFeasible.of_symPSDFeasible y hp)

/-- In particular a reading-1 selection (step 1's `SDPSelected`) never undercuts a
reading-3 selection on the same candidates and cost. -/
theorem SDPSelected.frobenius_cost_le {B : WedderburnBlocks ℝ W ι d} {y : ι → ℝ}
    {cands : Set W} {cost : W → ℝ} {w w' : W} (hf : FrobeniusSelected B y cands cost w)
    (hs : SDPSelected B cands cost w') : cost w ≤ cost w' :=
  hf.cost_le_of_psdFeasible hs.mem hs.psd

end Readings

/-! ## Reading 3 on `H₃` -/

section H3

/-- **For a γγ-word, reading-3 feasibility is decided by the `(2,1)` block**: the
`(3)` and `(1³)` characters of a γγ-word are both `1`. -/
theorem frobeniusFeasible_iff_std {q h : ℝ} (hq : 0 < q) (S : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
    (y : H3Block → ℝ) {w : Word} (hw : GammaGammaWord w) :
    FrobeniusFeasible (h3Blocks q h S) y w ↔ (0 < y .std → 0 ≤ (stdImage S h w).trace) := by
  constructor
  · intro hf hy
    exact hf .std hy
  · intro hs l hl
    cases l with
    | triv =>
      show 0 ≤ (Matrix.diagonal fun _ => trivChar q w).trace
      rw [trivChar_eq_one hq.ne' hw, Matrix.trace_diagonal]
      exact Finset.sum_nonneg fun _ _ => zero_le_one
    | std => exact hs hl
    | sgn =>
      show 0 ≤ (Matrix.diagonal fun _ => altChar q w).trace
      rw [altChar_eq_one hq.ne' hw, Matrix.trace_diagonal]
      exact Finset.sum_nonneg fun _ _ => zero_le_one

/-- The empty word (the identity of `H₃`) is Frobenius-feasible: `tr 1 = 2`. -/
theorem nil_frobeniusFeasible {q h : ℝ} (hq : 0 < q) (S : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
    (y : H3Block → ℝ) : FrobeniusFeasible (h3Blocks q h S) y [] := by
  rw [frobeniusFeasible_iff_std hq S y .nil, stdImage_nil]
  intro _
  rw [Matrix.trace_one]
  exact Nat.cast_nonneg _

/-- As for reading 1 (`sdpSelected_nil`): with the crossing-count cost the empty
word is reading-3-selected whenever it is a candidate. The content is in the
*non-zero* selection below. -/
theorem frobeniusSelected_nil {q h : ℝ} (hq : 0 < q) (S : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
    (y : H3Block → ℝ) (cands : Set Word) (hmem : [] ∈ cands) :
    FrobeniusSelected (h3Blocks q h S) y cands (fun w => (w.length : ℝ)) [] where
  mem := hmem
  feasible := nil_frobeniusFeasible hq S y
  minimal := fun w' _ _ => by simp

/-- **Vertex powers**: reading-3 feasibility of `(σ₀σ₁⁻¹)^k` is the sign of the
`(2,1)` character `tr V^k` of step 4, when the block carries positive weight. -/
theorem vertexPow_frobeniusFeasible_iff {q a b a' h : ℝ} (hq : 0 < q) (y : H3Block → ℝ)
    (k : ℕ) :
    FrobeniusFeasible (h3Blocks q h (hoefsmitGen q a b a')) y (vertexPow k) ↔
      (0 < y .std → 0 ≤ (vtx q a b a' h ^ k).trace) := by
  rw [frobeniusFeasible_iff_std hq _ y (vertexPow_gammaGamma k), stdImage_vertexPow]
  rfl

end H3

/-! ## The concrete Hoefsmit data on the interval `1 < q ≤ 23/20` -/

section Hoefsmit

/-- The `H₃` block data at the concrete Hoefsmit `(2,1)` matrices of step 3. -/
noncomputable def hoefsmitH3 (q : ℝ) : WedderburnBlocks ℝ Word H3Block H3Block.dim :=
  h3Blocks q (hOf q) (hoefsmitGen q (hoefsmitA q) (hoefsmitB q) (hoefsmitA' q))

/-- The vertex image at the concrete Hoefsmit data. -/
noncomputable def hoefsmitVtx (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  vtx q (hoefsmitA q) (hoefsmitB q) (hoefsmitA' q) (hOf q)

theorem hoefsmitH3_vertexPow_iff {q : ℝ} (hq : 0 < q) (y : H3Block → ℝ) (k : ℕ) :
    FrobeniusFeasible (hoefsmitH3 q) y (vertexPow k) ↔
      (0 < y .std → 0 ≤ (hoefsmitVtx q ^ k).trace) :=
  vertexPow_frobeniusFeasible_iff hq y k

/-- The six Hoefsmit relations step 4's generic lemmas take as hypotheses, all
discharged from `1 < q` (as in `hoefsmit_vtx_pow_not_isHermitian`). -/
theorem hoefsmit_relations {q : ℝ} (hq1 : 1 < q) :
    q * q⁻¹ = 1 ∧ hOf q = q - q⁻¹ ∧ hoefsmitA q * (1 - q ^ 4) = hOf q ∧
      hoefsmitA' q = -q ^ 4 * hoefsmitA q ∧
      hoefsmitB q ^ 2 = hoefsmitA q * hoefsmitA' q + 1 ∧ q ^ 2 ≠ 1 := by
  have hq : 0 < q := by linarith
  have hqne : q ≠ 1 := hq1.ne'
  have hq0 : q ≠ 0 := hq.ne'
  have h4 := one_sub_pow_four_ne_zero hq hqne
  refine ⟨mul_inv_cancel₀ hq0, rfl, ?_, ?_, hoefsmitB_sq hq hqne, ?_⟩
  · unfold hoefsmitA; field_simp
  · have h4m : q ^ 4 - 1 ≠ 0 := by intro h; apply h4; linarith
    unfold hoefsmitA' hoefsmitA
    rw [show (1 : ℝ) - (q ^ 4)⁻¹ = (q ^ 4 - 1) / q ^ 4 by field_simp]
    rw [div_div_eq_mul_div]
    field_simp
    ring
  · intro h
    have : q = 1 := by nlinarith
    exact hqne this

/-- `0 < h² ≤ 1/10` on the interval (`h_sq_le_of_q_le` plus `h > 0`). -/
theorem hOf_sq_bounds {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    0 < hOf q ^ 2 ∧ hOf q ^ 2 ≤ 1 / 10 := by
  refine ⟨?_, h_sq_le_of_q_le hq1.le hq2⟩
  have : 0 < hOf q := by
    unfold hOf
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
    linarith
  positivity

/-- The step-4 Chebyshev closed forms at the concrete data, `x = h²`. -/
theorem hoefsmitVtx_traces {q : ℝ} (hq1 : 1 < q) :
    (hoefsmitVtx q ^ 1).trace = -1 - hOf q ^ 2 ∧
      (hoefsmitVtx q ^ 2).trace = (hOf q ^ 2) ^ 2 + 2 * hOf q ^ 2 - 1 ∧
      (hoefsmitVtx q ^ 3).trace = 2 - 3 * (hOf q ^ 2) ^ 2 - (hOf q ^ 2) ^ 3 ∧
      (hoefsmitVtx q ^ 4).trace =
        (hOf q ^ 2) ^ 4 + 4 * (hOf q ^ 2) ^ 3 + 2 * (hOf q ^ 2) ^ 2 - 4 * hOf q ^ 2 - 1 ∧
      (hoefsmitVtx q ^ 5).trace =
        -(hOf q ^ 2) ^ 5 - 5 * (hOf q ^ 2) ^ 4 - 5 * (hOf q ^ 2) ^ 3 + 5 * (hOf q ^ 2) ^ 2
          + 5 * hOf q ^ 2 - 1 := by
  obtain ⟨hqinv, hh, ha, ha', hb, hq21⟩ := hoefsmit_relations hq1
  unfold hoefsmitVtx
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [trace_vtx_pow_one hqinv hh ha ha' hb hq21]
  · rw [trace_vtx_pow_two hqinv hh ha ha' hb hq21]; ring
  · rw [trace_vtx_pow_three hqinv hh ha ha' hb hq21]; ring
  · rw [trace_vtx_pow_four hqinv hh ha ha' hb hq21]; ring
  · rw [trace_vtx_pow_five hqinv hh ha ha' hb hq21]; ring

/-- **The step-4 sign table as reading-3 feasibility**, for every `1 < q ≤ 23/20`
and every weight with `y_(2,1) > 0`: `k = 1, 2, 4, 5` infeasible, `k = 3`
feasible. -/
theorem hoefsmit_vertexPow_frobenius_table {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) :
    ¬ FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 1) ∧
      ¬ FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 2) ∧
      FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 3) ∧
      ¬ FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 4) ∧
      ¬ FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 5) := by
  have hq : 0 < q := by linarith
  obtain ⟨hx, hx1⟩ := hOf_sq_bounds hq1 hq2
  obtain ⟨s1, s2, s3, s4, s5⟩ := chi_signs_of_small hx hx1
  obtain ⟨t1, t2, t3, t4, t5⟩ := hoefsmitVtx_traces hq1
  simp only [hoefsmitH3_vertexPow_iff hq y]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro hf; have := hf hy; rw [t1] at this; linarith
  · intro hf; have := hf hy; rw [t2] at this; linarith
  · intro _; rw [t3]; exact s3.le
  · intro hf; have := hf hy; rw [t4] at this; linarith
  · intro hf; have := hf hy; rw [t5] at this; linarith

/-- The candidate set: the γγ words of `H₃` with `1 ≤ k ≤ n` vertices, i.e. the
**non-zero** vertex powers (owner ruling 2026-08-30: minimal *non-zero* feasible). -/
def vertexPowCands (n : ℕ) : Set Word := {w | ∃ k, 1 ≤ k ∧ k ≤ n ∧ w = vertexPow k}

theorem borromean_mem_vertexPowCands : borromean ∈ vertexPowCands 5 :=
  ⟨3, by norm_num, by norm_num, vertexPow_three.symm⟩

/-- **Reading 3 selects `β_Bor`**: for every `1 < q ≤ 23/20` (the proton pin is
inside) and every Markov weight with `y_(2,1) > 0`, the minimal-crossing
Frobenius-feasible non-zero vertex power with `k ≤ 5` is `k = 3`, the
Borromean word. -/
theorem frobeniusSelected_borromean {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) :
    FrobeniusSelected (hoefsmitH3 q) y (vertexPowCands 5) (fun w => (w.length : ℝ))
      borromean := by
  obtain ⟨n1, n2, f3, n4, n5⟩ := hoefsmit_vertexPow_frobenius_table hq1 hq2 y hy
  refine ⟨borromean_mem_vertexPowCands, ?_, ?_⟩
  · rw [← vertexPow_three]; exact f3
  · rintro w' ⟨k, hk1, hk5, rfl⟩ hf
    rw [← vertexPow_three]
    interval_cases k
    · exact absurd hf n1
    · exact absurd hf n2
    · exact le_rfl
    · exact absurd hf n4
    · exact absurd hf n5

/-- Any reading-3-selected word on these candidates has six crossings. -/
theorem frobeniusSelected_length_eq_six {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) {w : Word}
    (hw : FrobeniusSelected (hoefsmitH3 q) y (vertexPowCands 5) (fun w => (w.length : ℝ)) w) :
    w.length = 6 := by
  have h := hw.cost_eq (frobeniusSelected_borromean hq1 hq2 y hy)
  have : (w.length : ℝ) = ((vertexPow 3).length : ℝ) := by
    simpa [vertexPow_three] using h
  rw [vertexPow_length] at this
  exact_mod_cast this

end Hoefsmit

end QOU.Mass.GammaGammaFrobeniusSelection
