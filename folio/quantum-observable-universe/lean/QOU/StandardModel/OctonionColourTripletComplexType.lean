import QOU.StandardModel.OctonionColourTripletSplitting

/-!
# QOU.StandardModel.OctonionColourTripletComplexType — the octonionic colour triple is complex type

The Schur–Weyl ledger of the eightfold-way chapter (`eightfold-open-problems.md`, row
"Octonionic `3` not excluded by the `Sym²` gate") records that the singlet count `0` of
`Sym²(𝟑)` for the Günaydin–Gürsey colour triple was a **cited** input
(`SU(3)_c`-irreducibility), not a proved one.  This module proves it, over `ℚ`, for the
concrete triple of `OctonionColourTripletSplitting`.

## Setting

`OctonionColourTripletSplitting` realises `𝕆 = ℂ ⊕ ℂ³` with complex structure `Le = L_{e₁}`,
and restricts the stabilizer `𝔰𝔲(3) = su3 stdIm ⊂ Der(𝕆)` faithfully and `ℂ`-linearly to
the 6-dimensional rational space `Fin 6 → ℚ` with complex structure `J6`
(`su3ToEndTriplet`, `su3ToEndTriplet_comm_J6`).  As a complex representation this is the
colour triple `𝟑 = (ℚ⁶, J6)`.

A `ℂ`-bilinear form `b` on `𝟑` is the same thing as a `ℚ`-bilinear form `β = Re b` on `ℚ⁶`
with `β (J6 x) y = β x (J6 y)` (because `b (i x) y = b x (i y)`), and `b` is
`𝔰𝔲(3)`-invariant iff `β` is.  So:

* an invariant vector of `Sym²(𝟑)` (a singlet of `𝟑 ⊗ 𝟑` in the symmetric channel),
* an invariant vector of `Λ²(𝟑)`, and
* an isomorphism `𝟑 ≅ 𝟑̄` (equivalently an invariant pairing `𝟑 ⊗ 𝟑 → 𝟏`)

are all such `β`.  We prove that the only one is `β = 0`.

## Main results

* `colourTriple_invariant_complexBilinear_eq_zero` — every `ℚ`-bilinear form on the triplet
  that is `J6`-compatible and `𝔰𝔲(3)`-invariant is zero.  Two explicit stabilizer elements
  `T₀, T₄` already force this.
* `colourTriple_sym2_singlet_eq_zero` — the symmetric case: `Sym²(𝟑)` has no singlet.  This
  discharges the cited input in the `Sym²`-gate ledger row: the octonionic triple **passes**
  the gate, not merely "is not excluded".
* `colourTriple_not_selfConjugate` — `𝟑 ≇ 𝟑̄` in the bilinear-form sense: complex type
  (Frobenius–Schur indicator `0`).
* `realSix_norm_not_complexBilinear` — contrast: the underlying real `ℚ⁶` does carry the
  invariant norm form (the identity matrix), and it fails exactly the `J6`-compatibility.  So
  the vanishing is a statement about the complex triple, not about the real 6.

Base ring `ℚ`; exact rational linear algebra; no analytic or empirical input.
-/

namespace QOU.StandardModel.ColourTripletComplexType

open QOU.MathlibExt.OctonionDerivations
open QOU.StandardModel

/-- The bilinear form with Gram matrix `B` on `ℚ⁶`: `β B x y = ∑ᵢ ∑ⱼ xᵢ Bᵢⱼ yⱼ`. -/
def β (B : Matrix (Fin 6) (Fin 6) ℚ) (x y : Fin 6 → ℚ) : ℚ :=
  ∑ i, ∑ j, x i * B i j * y j

/-! ## The complex structure in coordinates -/

/-- `J6` in coordinates (left multiplication by `e₁` on `e₂ … e₇`). -/
theorem J6_apply (x : Fin 6 → ℚ) : J6 x = ![-x 2, -x 5, x 0, -x 4, x 3, x 1] := by
  funext k
  fin_cases k <;> simp [J6, compressToTriplet, π6, emb6, Le, stdIm, octMul]

/-! ## Two explicit elements of the colour stabilizer -/

/-- First stabilizer element, as an `8 × 8` matrix (support on `e₂ … e₇`). -/
def D₀ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), ((-1) : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), ((-1) : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- Second stabilizer element, as an `8 × 8` matrix (support on `e₂ … e₇`). -/
def D₄ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), ((-1) : ℚ);
    (0 : ℚ), (0 : ℚ), ((-1) : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

theorem D₀_isDer (u v : Fin 8 → ℚ) :
    D₀.mulVec (octMul u v) = octMul (D₀.mulVec u) v + octMul u (D₀.mulVec v) := by
  funext k
  fin_cases k <;> simp [D₀, octMul, Matrix.mulVec, dotProduct, Fin.sum_univ_eight] <;> ring

theorem D₄_isDer (u v : Fin 8 → ℚ) :
    D₄.mulVec (octMul u v) = octMul (D₄.mulVec u) v + octMul u (D₄.mulVec v) := by
  funext k
  fin_cases k <;> simp [D₄, octMul, Matrix.mulVec, dotProduct, Fin.sum_univ_eight] <;> ring

/-- `D₀` as an element of `su3 stdIm`: a derivation that kills `e₁`. -/
def S₀ : ↥(su3 stdIm) :=
  ⟨⟨Matrix.mulVecLin D₀, mem_Der𝕆_of_isDer D₀_isDer⟩, by
    rw [mem_su3_iff]
    funext k
    fin_cases k <;> simp [D₀, stdIm, Matrix.mulVec, dotProduct, Fin.sum_univ_eight]⟩

/-- `D₄` as an element of `su3 stdIm`: a derivation that kills `e₁`. -/
def S₄ : ↥(su3 stdIm) :=
  ⟨⟨Matrix.mulVecLin D₄, mem_Der𝕆_of_isDer D₄_isDer⟩, by
    rw [mem_su3_iff]
    funext k
    fin_cases k <;> simp [D₄, stdIm, Matrix.mulVec, dotProduct, Fin.sum_univ_eight]⟩

/-- The triplet restriction of `S₀`. -/
def T₀ : Module.End ℚ (Fin 6 → ℚ) := su3ToEndTriplet S₀

/-- The triplet restriction of `S₄`. -/
def T₄ : Module.End ℚ (Fin 6 → ℚ) := su3ToEndTriplet S₄

theorem T₀_apply (x : Fin 6 → ℚ) : T₀ x = ![-x 4, 0, x 3, -x 2, x 0, 0] := by
  funext k
  fin_cases k <;>
    simp [T₀, S₀, D₀, su3ToEndTriplet_apply, π6, emb6, Matrix.mulVec, dotProduct,
      Fin.sum_univ_eight]

theorem T₄_apply (x : Fin 6 → ℚ) : T₄ x = ![x 2, -x 5, -x 0, 0, 0, x 1] := by
  funext k
  fin_cases k <;>
    simp [T₄, S₄, D₄, su3ToEndTriplet_apply, π6, emb6, Matrix.mulVec, dotProduct,
      Fin.sum_univ_eight]

/-! ## The vanishing theorem -/

set_option linter.unusedSimpArgs false in
set_option linter.unreachableTactic false in
set_option linter.unnecessarySeqFocus false in
/-- **Core computation.**  A `J6`-compatible bilinear form invariant under the two stabilizer
elements `T₀, T₄` is zero.  Each entry of `B` is an explicit rational combination of the
instantiated hypotheses (certificate generated by exact Gaussian elimination over `ℚ`). -/
theorem eq_zero_of_T₀_T₄ (B : Matrix (Fin 6) (Fin 6) ℚ)
    (hJ : ∀ x y, β B (J6 x) y = β B x (J6 y))
    (h0 : ∀ x y, β B (T₀ x) y + β B x (T₀ y) = 0)
    (h4 : ∀ x y, β B (T₄ x) y + β B x (T₄ y) = 0) :
    B = 0 := by
  ext i j
  simp only [Matrix.zero_apply]
  fin_cases i <;> fin_cases j
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 0 1) (Pi.single 2 1) + (1/2) * h4 (Pi.single 0 1) (Pi.single 2 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 0 1) (Pi.single 5 1) - h0 (Pi.single 3 1) (Pi.single 5 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (-1/2) * hJ (Pi.single 0 1) (Pi.single 0 1) + (-1/2) * h4 (Pi.single 0 1) (Pi.single 0 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 0 1) (Pi.single 4 1) + h4 (Pi.single 0 1) (Pi.single 4 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      -hJ (Pi.single 0 1) (Pi.single 3 1) - h4 (Pi.single 0 1) (Pi.single 3 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      -hJ (Pi.single 0 1) (Pi.single 1 1) + h0 (Pi.single 3 1) (Pi.single 1 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      -h0 (Pi.single 1 1) (Pi.single 4 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 1 1) (Pi.single 5 1) + (-1/2) * h4 (Pi.single 1 1) (Pi.single 5 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      h0 (Pi.single 1 1) (Pi.single 3 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      -h0 (Pi.single 1 1) (Pi.single 2 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      h0 (Pi.single 1 1) (Pi.single 0 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (-1/2) * hJ (Pi.single 1 1) (Pi.single 1 1) + (1/2) * h4 (Pi.single 1 1) (Pi.single 1 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 0 1) (Pi.single 0 1) + (-1/2) * h4 (Pi.single 0 1) (Pi.single 0 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      h0 (Pi.single 3 1) (Pi.single 1 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 0 1) (Pi.single 2 1) + (-1/2) * h4 (Pi.single 0 1) (Pi.single 2 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      -h4 (Pi.single 0 1) (Pi.single 3 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      -h4 (Pi.single 0 1) (Pi.single 4 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      h0 (Pi.single 3 1) (Pi.single 5 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      -hJ (Pi.single 0 1) (Pi.single 4 1) + hJ (Pi.single 3 1) (Pi.single 2 1) - h0 (Pi.single 0 1) (Pi.single 2 1) - h4 (Pi.single 0 1) (Pi.single 4 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 3 1) (Pi.single 5 1) - h0 (Pi.single 0 1) (Pi.single 5 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 0 1) (Pi.single 3 1) - hJ (Pi.single 3 1) (Pi.single 0 1) + h0 (Pi.single 0 1) (Pi.single 0 1) + h4 (Pi.single 0 1) (Pi.single 3 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (-1/2) * hJ (Pi.single 0 1) (Pi.single 2 1) + hJ (Pi.single 3 1) (Pi.single 4 1) - h0 (Pi.single 0 1) (Pi.single 4 1) + (-1/2) * h4 (Pi.single 0 1) (Pi.single 2 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 0 1) (Pi.single 0 1) - hJ (Pi.single 3 1) (Pi.single 3 1) + h0 (Pi.single 0 1) (Pi.single 3 1) + (1/2) * h4 (Pi.single 0 1) (Pi.single 0 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      -hJ (Pi.single 3 1) (Pi.single 1 1) + h0 (Pi.single 0 1) (Pi.single 1 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 0 1) (Pi.single 3 1) + h0 (Pi.single 0 1) (Pi.single 0 1) + h4 (Pi.single 0 1) (Pi.single 3 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      h0 (Pi.single 0 1) (Pi.single 1 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 0 1) (Pi.single 4 1) + h0 (Pi.single 0 1) (Pi.single 2 1) + h4 (Pi.single 0 1) (Pi.single 4 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 0 1) (Pi.single 0 1) + h0 (Pi.single 0 1) (Pi.single 3 1) + (1/2) * h4 (Pi.single 0 1) (Pi.single 0 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 0 1) (Pi.single 2 1) + h0 (Pi.single 0 1) (Pi.single 4 1) + (1/2) * h4 (Pi.single 0 1) (Pi.single 2 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      h0 (Pi.single 0 1) (Pi.single 5 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 1 1) (Pi.single 0 1) + h0 (Pi.single 1 1) (Pi.single 3 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 1 1) (Pi.single 1 1) + (1/2) * h4 (Pi.single 1 1) (Pi.single 1 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 1 1) (Pi.single 2 1) + h0 (Pi.single 1 1) (Pi.single 4 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 1 1) (Pi.single 3 1) + h0 (Pi.single 1 1) (Pi.single 0 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      hJ (Pi.single 1 1) (Pi.single 4 1) + h0 (Pi.single 1 1) (Pi.single 2 1)
  · linear_combination (norm := (simp [β, J6_apply, T₀_apply, T₄_apply, Fin.sum_univ_six, Pi.single_apply] <;> ring1))
      (1/2) * hJ (Pi.single 1 1) (Pi.single 5 1) + (1/2) * h4 (Pi.single 1 1) (Pi.single 5 1)

/-- **The colour triple carries no invariant `ℂ`-bilinear form.**  Every `ℚ`-bilinear form on
the triplet space that is `J6`-compatible (i.e. the real part of a `ℂ`-bilinear form on `𝟑`)
and invariant under the whole colour stabilizer `𝔰𝔲(3) = su3 stdIm` vanishes. -/
theorem colourTriple_invariant_complexBilinear_eq_zero (B : Matrix (Fin 6) (Fin 6) ℚ)
    (hJ : ∀ x y, β B (J6 x) y = β B x (J6 y))
    (hinv : ∀ D : ↥(su3 stdIm), ∀ x y,
      β B (su3ToEndTriplet D x) y + β B x (su3ToEndTriplet D y) = 0) :
    B = 0 :=
  eq_zero_of_T₀_T₄ B hJ (hinv S₀) (hinv S₄)

/-- **`Sym²(𝟑)` has no singlet.**  The symmetric case of the theorem above: the singlet count
of `Sym²` of the octonionic colour triple is `0`, so the triple passes the `Sym²` gate.  This
was the cited `SU(3)_c`-irreducibility input of the Schur–Weyl ledger. -/
theorem colourTriple_sym2_singlet_eq_zero (B : Matrix (Fin 6) (Fin 6) ℚ)
    (_hsymm : B.transpose = B)
    (hJ : ∀ x y, β B (J6 x) y = β B x (J6 y))
    (hinv : ∀ D : ↥(su3 stdIm), ∀ x y,
      β B (su3ToEndTriplet D x) y + β B x (su3ToEndTriplet D y) = 0) :
    B = 0 :=
  colourTriple_invariant_complexBilinear_eq_zero B hJ hinv

/-- **Complex type.**  No nonzero invariant pairing `𝟑 ⊗ 𝟑 → 𝟏` exists, so `𝟑 ≇ 𝟑̄`
(Frobenius–Schur indicator `0`): the triple is neither real nor quaternionic. -/
theorem colourTriple_not_selfConjugate :
    ¬ ∃ B : Matrix (Fin 6) (Fin 6) ℚ, B ≠ 0 ∧
      (∀ x y, β B (J6 x) y = β B x (J6 y)) ∧
      (∀ D : ↥(su3 stdIm), ∀ x y,
        β B (su3ToEndTriplet D x) y + β B x (su3ToEndTriplet D y) = 0) := by
  rintro ⟨B, hB, hJ, hinv⟩
  exact hB (colourTriple_invariant_complexBilinear_eq_zero B hJ hinv)

/-- **Contrast: the real `6` is not the complex `3`.**  The norm form (Gram matrix `1`) on the
underlying `ℚ⁶` is symmetric and nonzero, but it is `J6`-*anti*-compatible, so it is not the
real part of any `ℂ`-bilinear form on `𝟑`.  The `J6` condition in the theorems above is
therefore doing real work. -/
theorem realSix_norm_not_complexBilinear :
    ¬ ∀ x y, β (1 : Matrix (Fin 6) (Fin 6) ℚ) (J6 x) y = β 1 x (J6 y) := by
  intro h
  have := h (Pi.single 2 1) (Pi.single 0 1)
  simp [β, J6_apply, Pi.single_apply, Matrix.one_apply] at this
  norm_num at this

end QOU.StandardModel.ColourTripletComplexType
