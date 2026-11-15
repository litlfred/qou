/-
# The γγ selector at `H₃`: `SDPSelected` instantiated on the nucleon algebra

Bean `qou-ales`, step 3 (owner ruling 2026-09-08: every canonical braid word is
*selected* by γγ pair production + the confinement SDP at `q₀`, never by
census). Step 1 (`QOU.Mass.GammaGammaWordSelection`) stated the two predicates
— `GammaGammaWord` and `SDPSelected` — abstractly and instantiated only `H₂`.
This file instantiates them at **`H₃`**, the algebra of one nucleon, whose
Wedderburn decomposition is

    H₃(q) ≅ (3) ⊕ (2,1) ⊕ (1³),     dimensions 1, 2, 1,

with `σᵢ ↦ q` on `(3)`, `σᵢ ↦ −q⁻¹` on `(1³)`, and the Hoefsmit orthogonal form
on `(2,1)`: `σ₀ ↦ diag(q, −q⁻¹)`, `σ₁ ↦ [[a, b], [b, a']]` with
`a = h/(1 − q⁴)`, `a' = h/(1 − q⁻⁴)`, `b = √(a·a' + 1)`, `h = q − q⁻¹`
(`computations/hoefsmit_mpmath.py`, `pyhecke.syt_prefix_cache.BlockCache`).

## What is proved (all sorry-free; every claim was measured at the proton `q₀`
before being stated)

* `gammaGamma_inH3_eq_vertexPow` — inside `H₃` (generators `0, 1` only) the
  γγ-produced words are exactly the powers `(σ₀σ₁⁻¹)^k`. So the candidate set
  the probe scans is one-dimensional in `k`; that is a theorem, not a choice.
* `trivChar_eq_one` — the `(3)`-block image of every γγ-word is `1`
  (companion of step 1's `altChar_eq_one` for the `(1³)` block).
* `psdFeasible_iff_std` — for a γγ-word, **PSD feasibility reduces to the
  `(2,1)` block**: both one-dimensional blocks are the `1×1` matrix `1`.
* `vertex_std_not_isHermitian` / `vertex_not_psdFeasible` — the `(2,1)` image
  of a single pair-production vertex `σ₀σ₁⁻¹` is **not symmetric** (its
  off-diagonal entries are `q·b` and `−q⁻¹·b`), hence not `Matrix.PosSemidef`,
  whenever `b ≠ 0`. This is the `H₃` analogue of step 1's `σ₀` being
  infeasible on `H₂`, and it is what the probe measures for all `k ≤ 5`: no
  nonempty vertex power has a symmetric `(2,1)` image at the proton pin.
* `hoefsmitB_pos`, `hoefsmit_std_sigma1_hecke` — the concrete Hoefsmit data
  has `b² = [3]_q/[2]_q² > 0` (so `b ≠ 0` is *derived*, not assumed, for every
  `0 < q ≠ 1`) and satisfies the Hecke relation `σ₁² = h·σ₁ + 1`. A wrong
  `a`, `a'` or `b` would fail the second theorem.
* `nil_psdFeasible`, `sdpSelected_nil` — the empty word is PSD-feasible, and
  under the corpus cost (crossing count) it is what the *literal*
  `SDPSelected` selects over any candidate set containing it. This is the
  same shape as `H₂`, where `k = 0` is PSD and the corpus's selection rule
  (owner ruling 2026-08-30, bean `qou-1qsw`) is the minimal **non-zero**
  feasible word. Which non-zero words are feasible under which reading of
  "PSD" is the probe's job; this file fixes what the literal predicate says.

## Base ring (§7c)

`trivChar`, `vertexPow`, `InH3`, and the block-image fold are over a generic
`[Field R]`. Everything involving `Matrix.PosSemidef`, `Real.sqrt`, or an
order is on `ℝ` and sits at the end.

Nothing here reads AME, CODATA, or a census.
-/
import QOU.Mass.GammaGammaWordSelection
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.Mass.GammaGammaSelectorH3

open QOU.Mass.GammaGammaWordSelection

/-! ## γγ-words inside `H₃` are the vertex powers -/

/-- `(σ₀σ₁⁻¹)^k`, as the nested product the `GammaGammaWord` constructors
produce (`vertexPow 3 = borromean`). -/
def vertexPow : ℕ → Word
  | 0 => []
  | k + 1 => vertex 0 ++ vertexPow k

theorem vertexPow_gammaGamma (k : ℕ) : GammaGammaWord (vertexPow k) := by
  induction k with
  | zero => exact .nil
  | succ k ih => exact .cons 0 ih

theorem vertexPow_three : vertexPow 3 = borromean := rfl

theorem vertexPow_length (k : ℕ) : (vertexPow k).length = 2 * k := by
  induction k with
  | zero => rfl
  | succ k ih => rw [vertexPow, length_vertex_append, ih]; ring

/-- A word lies in `H₃` iff it uses only the generators `σ₀, σ₁`. -/
def InH3 (w : Word) : Prop := ∀ c ∈ w, c.gen ≤ 1

theorem inH3_vertexPow (k : ℕ) : InH3 (vertexPow k) := by
  induction k with
  | zero => intro c hc; simp [vertexPow] at hc
  | succ k ih =>
    intro c hc
    rw [vertexPow, List.mem_append] at hc
    rcases hc with hc | hc
    · simp only [vertex, List.mem_cons, List.not_mem_nil, or_false] at hc
      rcases hc with rfl | rfl <;> simp
    · exact ih c hc

/-- **Inside `H₃`, every γγ-produced word is a vertex power.** A vertex
`σᵢσᵢ₊₁⁻¹` uses generator `i + 1`, so `i + 1 ≤ 1` forces `i = 0`. -/
theorem gammaGamma_inH3_eq_vertexPow {w : Word} (hw : GammaGammaWord w) (h3 : InH3 w) :
    ∃ k, w = vertexPow k := by
  induction hw with
  | nil => exact ⟨0, rfl⟩
  | cons i hw' ih =>
    have hi : i = 0 := by
      have := h3 ⟨i + 1, false⟩ (by simp [vertex])
      simp only at this
      omega
    subst hi
    obtain ⟨k, hk⟩ := ih (fun c hc => h3 c (List.mem_append_right _ hc))
    exact ⟨k + 1, by rw [vertexPow, hk]⟩

/-! ## The trivial character (the `(3)` block) -/

section TrivChar

variable {R : Type*} [Field R]

/-- The one-dimensional **trivial** representation `σᵢ ↦ q` (so `σᵢ⁻¹ ↦ q⁻¹`),
evaluated on a word: the `(3)` block of `H₃(q)`, and the `(n)` block of any
`Hₙ(q)`. -/
def trivChar (q : R) (w : Word) : R :=
  (w.map fun c => if c.pos then q else q⁻¹).prod

theorem trivChar_append (q : R) (u v : Word) :
    trivChar q (u ++ v) = trivChar q u * trivChar q v := by
  simp [trivChar, List.map_append, List.prod_append]

theorem trivChar_vertex {q : R} (hq : q ≠ 0) (i : ℕ) : trivChar q (vertex i) = 1 := by
  simp [trivChar, vertex, hq]

/-- **The `(3)`-block image of every γγ-produced word is `1`.** -/
theorem trivChar_eq_one {q : R} (hq : q ≠ 0) {w : Word} (h : GammaGammaWord w) :
    trivChar q w = 1 := by
  induction h with
  | nil => simp [trivChar]
  | cons i _ ih => rw [trivChar_append, trivChar_vertex hq, ih, one_mul]

/-- A single positive crossing has trivial character `q` (it is not a unit of
the character, so `q ≠ 1` distinguishes it from every γγ-word). -/
theorem trivChar_single (q : R) (i : ℕ) : trivChar q [⟨i, true⟩] = q := by
  simp [trivChar]

end TrivChar

/-! ## The `(2,1)` block: word images under a two-generator matrix rep -/

section Std

variable {R : Type*} [Field R]

/-- Image of one crossing under generator matrices `S 0 = ρ(σ₀)`, `S 1 = ρ(σ₁)`,
with `σᵢ⁻¹ ↦ ρ(σᵢ) − h·1` (the Hecke relation `σ² = hσ + 1`). -/
def crossingImage (S : ℕ → Matrix (Fin 2) (Fin 2) R) (h : R) (c : Crossing) :
    Matrix (Fin 2) (Fin 2) R :=
  if c.pos then S c.gen else S c.gen - h • (1 : Matrix (Fin 2) (Fin 2) R)

/-- Left-to-right product of the crossing images: the `(2,1)`-block image of a
word. -/
def stdImage (S : ℕ → Matrix (Fin 2) (Fin 2) R) (h : R) (w : Word) :
    Matrix (Fin 2) (Fin 2) R :=
  (w.map (crossingImage S h)).prod

theorem stdImage_nil (S : ℕ → Matrix (Fin 2) (Fin 2) R) (h : R) : stdImage S h [] = 1 := by
  simp [stdImage]

theorem stdImage_vertex_zero (S : ℕ → Matrix (Fin 2) (Fin 2) R) (h : R) :
    stdImage S h (vertex 0) = S 0 * (S 1 - h • (1 : Matrix (Fin 2) (Fin 2) R)) := by
  simp [stdImage, vertex, crossingImage]

/-- Hoefsmit orthogonal form of `σ₀` on `(2,1)`: `diag(q, −q⁻¹)`. -/
def hoefsmitSigma0 (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 0; 0, -q⁻¹]

/-- Hoefsmit orthogonal form of `σ₁` on `(2,1)`: the symmetric `[[a, b], [b, a']]`. -/
def hoefsmitSigma1 (a b a' : R) : Matrix (Fin 2) (Fin 2) R := !![a, b; b, a']

/-- The two generator matrices as a function of the generator index (only
`0` and `1` occur in an `H₃` word). -/
def hoefsmitGen (q a b a' : R) : ℕ → Matrix (Fin 2) (Fin 2) R
  | 0 => hoefsmitSigma0 q
  | _ => hoefsmitSigma1 a b a'

/-- The `(2,1)` image of the pair-production vertex, entrywise. -/
theorem stdImage_vertex_entries (q a b a' h : R) :
    stdImage (hoefsmitGen q a b a') h (vertex 0) =
      !![q * (a - h), q * b; -q⁻¹ * b, -q⁻¹ * (a' - h)] := by
  rw [stdImage_vertex_zero]
  simp only [hoefsmitGen, hoefsmitSigma0, hoefsmitSigma1]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]

end Std

/-! ## Archimedean specialisation: `H₃` on `ℝ` -/

section H3

/-- The three Wedderburn blocks of `H₃(q)`. -/
inductive H3Block
  | triv
  | std
  | sgn
  deriving DecidableEq

/-- Their dimensions `1, 2, 1`. -/
def H3Block.dim : H3Block → ℕ
  | .triv => 1
  | .std => 2
  | .sgn => 1

/-- **`H₃` Wedderburn block data on words**: `(3)` by the trivial character,
`(2,1)` by the Hoefsmit image with generator matrices `S`, `(1³)` by the
alternating character. -/
noncomputable def h3Blocks (q h : ℝ) (S : ℕ → Matrix (Fin 2) (Fin 2) ℝ) :
    WedderburnBlocks ℝ Word H3Block H3Block.dim where
  proj w
    | .triv => Matrix.diagonal fun _ => trivChar q w
    | .std => stdImage S h w
    | .sgn => Matrix.diagonal fun _ => altChar q w

/-- **For a γγ-word, PSD feasibility is decided by the `(2,1)` block alone**:
the `(3)` and `(1³)` images are both the `1×1` matrix `1`, which is PSD. -/
theorem psdFeasible_iff_std {q h : ℝ} (hq : 0 < q) (S : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
    {w : Word} (hw : GammaGammaWord w) :
    (h3Blocks q h S).PSDFeasible w ↔ (stdImage S h w).PosSemidef := by
  constructor
  · intro hf
    exact hf .std
  · intro hs l
    cases l with
    | triv =>
      show (Matrix.diagonal fun _ => trivChar q w).PosSemidef
      rw [trivChar_eq_one hq.ne' hw]
      exact Matrix.posSemidef_diagonal_iff.mpr fun _ => zero_le_one
    | std => exact hs
    | sgn =>
      show (Matrix.diagonal fun _ => altChar q w).PosSemidef
      rw [altChar_eq_one hq.ne' hw]
      exact Matrix.posSemidef_diagonal_iff.mpr fun _ => zero_le_one

/-- The empty word (the identity of `H₃`) is PSD-feasible. -/
theorem nil_psdFeasible {q h : ℝ} (hq : 0 < q) (S : ℕ → Matrix (Fin 2) (Fin 2) ℝ) :
    (h3Blocks q h S).PSDFeasible [] := by
  rw [psdFeasible_iff_std hq S .nil, stdImage_nil]
  exact Matrix.PosSemidef.one

/-- **The `(2,1)` image of one pair-production vertex is not symmetric** when the
block is irreducible (`b ≠ 0`): its off-diagonal entries are `q·b` and
`−q⁻¹·b`, equal only if `b·(q + q⁻¹) = 0`. -/
theorem vertex_std_not_isHermitian {q a b a' h : ℝ} (hq : 0 < q) (hb : b ≠ 0) :
    ¬ (stdImage (hoefsmitGen q a b a') h (vertex 0)).IsHermitian := by
  intro H
  have h01 := H.apply 0 1
  rw [stdImage_vertex_entries] at h01
  simp only [star_trivial, Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.empty_val', Matrix.cons_val_fin_one] at h01
  -- h01 : -q⁻¹ * b = q * b
  have hpos : 0 < q + q⁻¹ := by positivity
  have : b * (q + q⁻¹) = 0 := by linear_combination -h01
  rcases mul_eq_zero.mp this with hb0 | hz
  · exact hb hb0
  · exact hpos.ne' hz

/-- Hence a single vertex `σ₀σ₁⁻¹` is **not** PSD-feasible on `H₃` — the
`(2,1)` block fails the Hermitian half of `Matrix.PosSemidef`. Mirror of
step 1's `h2_two_feasible_one_not` (`σ₀` infeasible on `H₂`). -/
theorem vertex_not_psdFeasible {q a b a' h : ℝ} (hq : 0 < q) (hb : b ≠ 0) :
    ¬ (h3Blocks q h (hoefsmitGen q a b a')).PSDFeasible (vertex 0) := by
  intro hf
  exact vertex_std_not_isHermitian hq hb (hf .std).1

/-- **What the literal `SDPSelected` selects on `H₃` with the crossing-count
cost**: the empty word, whenever it is a candidate. The non-zero selection is
the probe's question (owner ruling 2026-08-30: minimal *non-zero* feasible). -/
theorem sdpSelected_nil {q h : ℝ} (hq : 0 < q) (S : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
    (cands : Set Word) (hmem : [] ∈ cands) :
    SDPSelected (h3Blocks q h S) cands (fun w => (w.length : ℝ)) [] where
  mem := hmem
  psd := nil_psdFeasible hq S
  minimal := fun w' _ _ => by simp

end H3

/-! ## The concrete Hoefsmit `(2,1)` data: `b ≠ 0` is derived, and the Hecke
relation holds -/

section Hoefsmit

/-- `h = q − q⁻¹`. -/
noncomputable def hOf (q : ℝ) : ℝ := q - q⁻¹

/-- `a = h/(1 − q⁴)` (content distance `ρ = −2` for the swap `(2 3)` on the
tableau `[[1,2],[3]]`). -/
noncomputable def hoefsmitA (q : ℝ) : ℝ := hOf q / (1 - q ^ 4)

/-- `a' = h/(1 − q⁻⁴)`. -/
noncomputable def hoefsmitA' (q : ℝ) : ℝ := hOf q / (1 - (q ^ 4)⁻¹)

/-- `[2]_q = q + q⁻¹`. -/
noncomputable def qTwo (q : ℝ) : ℝ := q + q⁻¹

/-- `[3]_q = q² + 1 + q⁻²`. -/
noncomputable def qThree (q : ℝ) : ℝ := q ^ 2 + 1 + (q ^ 2)⁻¹

/-- `b = √(a·a' + 1)`, the Hoefsmit off-diagonal entry. -/
noncomputable def hoefsmitB (q : ℝ) : ℝ := Real.sqrt (hoefsmitA q * hoefsmitA' q + 1)

theorem one_sub_pow_four_ne_zero {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) : 1 - q ^ 4 ≠ 0 := by
  intro h
  have h4 : q ^ 4 = 1 := by linarith
  have : q = 1 := by
    have := pow_eq_one_iff_of_nonneg hq.le (by norm_num : (4 : ℕ) ≠ 0) |>.mp h4
    exact this
  exact hq1 this

/-- `a + a' = h`: the two diagonal entries sum to the trace `q − q⁻¹` of `σ₁`. -/
theorem hoefsmitA_add_A' {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    hoefsmitA q + hoefsmitA' q = hOf q := by
  have h4 := one_sub_pow_four_ne_zero hq hq1
  have hq0 : q ≠ 0 := hq.ne'
  have h4m : q ^ 4 - 1 ≠ 0 := by intro h; apply h4; linarith
  unfold hoefsmitA hoefsmitA'
  rw [show (1 : ℝ) - (q ^ 4)⁻¹ = (q ^ 4 - 1) / q ^ 4 by field_simp]
  rw [div_div_eq_mul_div]
  field_simp
  ring

/-- `a·a' + 1 = [3]_q / [2]_q²` — so the Hoefsmit `b²` is a ratio of quantum
integers, independent of the square root's sign convention. -/
theorem hoefsmitA_mul_A'_add_one {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    hoefsmitA q * hoefsmitA' q + 1 = qThree q / qTwo q ^ 2 := by
  have h4 := one_sub_pow_four_ne_zero hq hq1
  have hq0 : q ≠ 0 := hq.ne'
  have h4m : q ^ 4 - 1 ≠ 0 := by intro h; apply h4; linarith
  have h2 : qTwo q ≠ 0 := by unfold qTwo; positivity
  unfold hoefsmitA hoefsmitA' hOf qThree qTwo
  rw [show (1 : ℝ) - (q ^ 4)⁻¹ = (q ^ 4 - 1) / q ^ 4 by field_simp]
  rw [div_div_eq_mul_div]
  field_simp
  ring

theorem qThree_div_qTwo_sq_pos {q : ℝ} (hq : 0 < q) : 0 < qThree q / qTwo q ^ 2 := by
  unfold qThree qTwo; positivity

/-- **`b > 0` for every `0 < q ≠ 1`** — the `(2,1)` block is irreducible and the
hypothesis of `vertex_not_psdFeasible` is met by the actual Hoefsmit data. -/
theorem hoefsmitB_pos {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) : 0 < hoefsmitB q := by
  unfold hoefsmitB
  rw [hoefsmitA_mul_A'_add_one hq hq1]
  exact Real.sqrt_pos.mpr (qThree_div_qTwo_sq_pos hq)

theorem hoefsmitB_sq {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    hoefsmitB q ^ 2 = hoefsmitA q * hoefsmitA' q + 1 := by
  unfold hoefsmitB
  rw [Real.sq_sqrt]
  rw [hoefsmitA_mul_A'_add_one hq hq1]
  exact (qThree_div_qTwo_sq_pos hq).le

/-- **The Hoefsmit `σ₁` satisfies the Hecke relation `σ₁² = h·σ₁ + 1`** — a wrong
`a`, `a'` or `b` fails this. -/
theorem hoefsmit_std_sigma1_hecke {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    hoefsmitSigma1 (hoefsmitA q) (hoefsmitB q) (hoefsmitA' q) *
        hoefsmitSigma1 (hoefsmitA q) (hoefsmitB q) (hoefsmitA' q) =
      hOf q • hoefsmitSigma1 (hoefsmitA q) (hoefsmitB q) (hoefsmitA' q) + 1 := by
  have hsum := hoefsmitA_add_A' hq hq1
  have hsq := hoefsmitB_sq hq hq1
  unfold hoefsmitSigma1
  ext i j
  fin_cases i <;> fin_cases j
  · simp [Matrix.mul_apply, Fin.sum_univ_two]
    linear_combination hsq + hoefsmitA q * hsum
  · simp [Matrix.mul_apply, Fin.sum_univ_two]
    linear_combination hoefsmitB q * hsum
  · simp [Matrix.mul_apply, Fin.sum_univ_two]
    linear_combination hoefsmitB q * hsum
  · simp [Matrix.mul_apply, Fin.sum_univ_two]
    linear_combination hsq + hoefsmitA' q * hsum

/-- The `σ₀` matrix satisfies the Hecke relation too (its entries are the two
eigenvalues). -/
theorem hoefsmit_std_sigma0_hecke {q : ℝ} (hq : 0 < q) :
    hoefsmitSigma0 q * hoefsmitSigma0 q = hOf q • hoefsmitSigma0 q + 1 := by
  have hq0 : q ≠ 0 := hq.ne'
  unfold hoefsmitSigma0 hOf
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **The concrete `H₃` vertex is not PSD-feasible for any `0 < q ≠ 1`.** No
hypothesis on `b` remains: it is the Hoefsmit value. -/
theorem hoefsmit_vertex_not_psdFeasible {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    ¬ (h3Blocks q (hOf q)
        (hoefsmitGen q (hoefsmitA q) (hoefsmitB q) (hoefsmitA' q))).PSDFeasible (vertex 0) :=
  vertex_not_psdFeasible hq (hoefsmitB_pos hq hq1).ne'

end Hoefsmit

end QOU.Mass.GammaGammaSelectorH3
