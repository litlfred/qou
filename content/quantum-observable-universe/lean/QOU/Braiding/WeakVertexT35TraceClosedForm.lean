import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# Closed form for the weak-vertex form factor `W(q) = tr_M((σ₀σ₁)⁵)` in `H₃(q)`

`rem:hadron-half-life-fermi` lists the weak-vertex form factor — the canonical Markov trace of
the `T(3,5)` torus braid `(σ₀σ₁)⁵ ∈ H₃(q)` — as an *open computation*, and `prop:hadron-half-life`'s
Lean (`BetaRateData.W2`, PR #6631) carries it as positive data with no closed form.  This file
supplies the closed form, derived through the Wedderburn decomposition of `H₃(q)`:

    W(q) = tr_M((σ₀σ₁)⁵) = q² (q¹² + q⁸ − 1) / (q² + 1)²          (convention D)

## The derivation, and what each theorem carries

`H₃(q) ≅ K ⊕ M₂(K) ⊕ K` (Wedderburn), with the trivial block `σᵢ ↦ q`, the sign block
`σᵢ ↦ −q⁻¹`, and the two-dimensional block in Young seminormal form — the same matrices as
`QOU.Archimedean.HeckeH3.stdRep3_gen0/1`, re-stated here over a generic field because the
convention-D Markov parameter `z = q³/(q² + 1)` needs `(q² + 1)⁻¹`, which the Laurent ring
`ℤ[t, t⁻¹]` of that file does not contain.

The canonical Markov trace (Ocneanu; convention D, owner ruling R1 2026-08-15) is the linear
functional on `H₃(q)` whose values on the six reduced-word basis elements are

    tr_M(1) = 1,  tr_M(σ₀) = tr_M(σ₁) = z,  tr_M(σ₀σ₁) = tr_M(σ₁σ₀) = z²,  tr_M(σ₀σ₁σ₀) = h z² + z

with `h = q − q⁻¹`, `z = q³/(q² + 1)` — exactly the table `pyhecke.gram.TR_M` and
`computations/markov/markov_trace_canonical.py` implement.  Being a trace, it is a linear
combination of the three irreducible characters, `tr_M = Σ_λ y_λ χ_λ`.  Solving the three
equations `tr_M(1) = 1`, `tr_M(σ₀) = z`, `tr_M(σ₀σ₁) = z²` for the weights gives

    y₍₃₎ = (q⁴ + 1)/(q² + 1)²,   y₍₂₁₎ = q²/(q² + 1)²,   y₍₁₁₁₎ = 0,

and `y₍₁₁₁₎ = 0` is the statement that convention D is the `SU(2)` (Temperley–Lieb) trace.
`ocneanuD_basis_*` below verifies that the functional built from these weights reproduces all
**six** basis values — three more than were used to solve for it, which is the check that the
weights are right.  A linear functional on the six-dimensional `H₃(q)` is determined by its
values on a basis, so that functional **is** `tr_M`; that last (standard) step — that the six
reduced words are a basis — is not formalised here and is the one thing the reader supplies.

On the `T(3,5)` braid: `(σ₀σ₁)³ = Δ²` is the full twist, which acts on the `(2,1)` block as the
identity (`stdGen_M_cubed_eq_one`, the generic-field form of
`QOU.Archimedean.HeckeH3.stdRep3_M_cubed_eq_one`), so `(σ₀σ₁)⁵` acts there as `(σ₀σ₁)²`, whose
trace is `−1` (`chi21_T35`); on the trivial block it is `q¹⁰`.  Hence

    W(q) = y₍₃₎ q¹⁰ − y₍₂₁₎ = q²(q¹² + q⁸ − 1)/(q² + 1)²                (`weakVertexTrace_eq`).

## Cross-check against the Jones polynomial

`T(3,5)` is the knot `10₁₂₄`, `V(t) = t⁴ + t⁶ − t¹⁰`.  The numerator of `W` is `q²² · V(q⁻²)`
(`weakVertexTrace_numerator_eq_jones`), the mirror/writhe normalisation of the Ocneanu trace of a
positive braid on three strands.  This is an identity of Laurent polynomials, independent of the
Wedderburn route, and pins the result to a published invariant.

## Value at the substrate

At the proton pin `q₀ ≈ 1.10998`, `W(q₀) ≈ 1.18748` (`weakVertexTrace_near_q0`).  The value
`≈ 0.7036` published in `obs:hadron-half-life-verification` is reproduced by neither convention
(D: `1.1875`; C, `z = √q/(q+1)`: `0.9063`); it descends from the deprecated convention-C
`hecke_division` pipeline (`computations/_deprecated/t35-full-calculation.py`).  That is a
published-value change and is recorded, not edited, here — bean `qou-egvf`.

Numerical provenance: `computations/markov/weak_vertex_t35_trace.py` (canonical `tr_M_word`,
sympy-exact and `mpmath` at the proton pin).

Refs:
- [jones1987] Hecke algebra representations of braid groups and link polynomials.
- [wenzl1988] Hecke algebras of type `A_n` and subfactors.
- [ram1997] Seminormal representations of Weyl groups and Iwahori–Hecke algebras.
-/

namespace QOU.Braiding.WeakVertexT35

open Matrix

variable {K : Type*} [Field K]

/-! ## §1  The seminormal `(2,1)` block over a field -/

/-- `σ₀` on the `(2,1)` block, Young seminormal form: `⎡ q  1 ⎤ ⎣ 0  −q⁻¹ ⎦`. -/
noncomputable def stdGen0 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![q, 1; 0, -q⁻¹]

/-- `σ₁` on the `(2,1)` block, Young seminormal form: `⎡ −q⁻¹  0 ⎤ ⎣ 1  q ⎦`. -/
noncomputable def stdGen1 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![-q⁻¹, 0; 1, q]

/-- Hecke quadratic relation for `σ₀`: `σ₀² = (q − q⁻¹) σ₀ + 1`. -/
theorem stdGen0_hecke (q : K) (hq : q ≠ 0) :
    stdGen0 q * stdGen0 q = (q - q⁻¹) • stdGen0 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdGen0, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- Hecke quadratic relation for `σ₁`. -/
theorem stdGen1_hecke (q : K) (hq : q ≠ 0) :
    stdGen1 q * stdGen1 q = (q - q⁻¹) • stdGen1 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdGen1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- Braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁` on the `(2,1)` block. -/
theorem stdGen_braid (q : K) (hq : q ≠ 0) :
    stdGen0 q * stdGen1 q * stdGen0 q = stdGen1 q * stdGen0 q * stdGen1 q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdGen0, stdGen1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- `σ₀σ₁` on the `(2,1)` block is `⎡ 0  q ⎤ ⎣ −q⁻¹  −1 ⎦`. -/
theorem stdGen_M (q : K) (hq : q ≠ 0) :
    stdGen0 q * stdGen1 q = !![0, q; -q⁻¹, -1] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdGen0, stdGen1, Matrix.mul_apply, Fin.sum_univ_two, hq]

/-- **The full twist is trivial on `(2,1)`**: `(σ₀σ₁)³ = 1`, for every `q ≠ 0`.  This is the
`q`-independent fact behind the whole computation — `(σ₀σ₁)³ = Δ²` acts on the `(2,1)` block by
`q^{2·(content sum)}` and the content sum of `(2,1)` is `0`. -/
theorem stdGen_M_cubed_eq_one (q : K) (hq : q ≠ 0) :
    (stdGen0 q * stdGen1 q) ^ 3 = 1 := by
  rw [stdGen_M q hq, pow_succ, sq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, hq]

/-- `(σ₀σ₁)⁵ = (σ₀σ₁)²` on the `(2,1)` block. -/
theorem stdGen_M_pow_five (q : K) (hq : q ≠ 0) :
    (stdGen0 q * stdGen1 q) ^ 5 = (stdGen0 q * stdGen1 q) ^ 2 := by
  have h3 := stdGen_M_cubed_eq_one q hq
  calc (stdGen0 q * stdGen1 q) ^ 5
      = (stdGen0 q * stdGen1 q) ^ 3 * (stdGen0 q * stdGen1 q) ^ 2 := by rw [← pow_add]
    _ = (stdGen0 q * stdGen1 q) ^ 2 := by rw [h3, one_mul]

/-- The `(2,1)` character of the `T(3,5)` braid: `χ₍₂₁₎((σ₀σ₁)⁵) = −1`, independent of `q`. -/
theorem chi21_T35 (q : K) (hq : q ≠ 0) :
    ((stdGen0 q * stdGen1 q) ^ 5).trace = -1 := by
  rw [stdGen_M_pow_five q hq, stdGen_M q hq, sq, Matrix.trace_fin_two]
  simp [Matrix.mul_apply, Fin.sum_univ_two]
  field_simp
  ring

/-! ## §2  The convention-D Markov trace as a Wedderburn functional -/

/-- Convention-D Markov parameter `z = q³/(q² + 1)` (owner ruling R1, 2026-08-15). -/
noncomputable def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- Hecke parameter `h = q − q⁻¹`. -/
noncomputable def hq (q : K) : K := q - q⁻¹

/-- Wedderburn weight of the trivial block `(3)`. -/
noncomputable def yTriv (q : K) : K := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- Wedderburn weight of the `(2,1)` block. -/
noncomputable def yStd (q : K) : K := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- The Wedderburn functional `y₍₃₎ · χ₍₃₎ + y₍₂₁₎ · χ₍₂₁₎` (the sign block has weight `0`),
applied to an element given by its trivial-block value `a` and its `(2,1)`-block matrix `M`. -/
noncomputable def ocneanuD (q : K) (a : K) (M : Matrix (Fin 2) (Fin 2) K) : K :=
  yTriv q * a + yStd q * M.trace

/-- The weights sum to `1` with the sign block absent: `y₍₃₎ + 2 y₍₂₁₎ = 1`, i.e. `tr_M(1) = 1`. -/
theorem ocneanuD_basis_one (q : K) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD q 1 1 = 1 := by
  simp only [ocneanuD, yTriv, yStd, Matrix.trace_one, Fintype.card_fin]
  field_simp
  ring

/-- `tr_M(σ₀) = z`. -/
theorem ocneanuD_basis_sigma0 (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD q q (stdGen0 q) = zD q := by
  simp only [ocneanuD, yTriv, yStd, zD, stdGen0, Matrix.trace_fin_two_of]
  field_simp
  ring

/-- `tr_M(σ₁) = z`. -/
theorem ocneanuD_basis_sigma1 (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD q q (stdGen1 q) = zD q := by
  simp only [ocneanuD, yTriv, yStd, zD, stdGen1, Matrix.trace_fin_two_of]
  field_simp
  ring

/-- `tr_M(σ₀σ₁) = z²`. -/
theorem ocneanuD_basis_sigma01 (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD q (q ^ 2) (stdGen0 q * stdGen1 q) = zD q ^ 2 := by
  simp only [ocneanuD, yTriv, yStd, zD, stdGen_M q hq0, Matrix.trace_fin_two_of]
  field_simp
  ring

/-- `tr_M(σ₁σ₀) = z²`. -/
theorem ocneanuD_basis_sigma10 (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD q (q ^ 2) (stdGen1 q * stdGen0 q) = zD q ^ 2 := by
  simp only [ocneanuD, yTriv, yStd, zD, Matrix.trace_fin_two, stdGen0, stdGen1,
    Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.empty_val', Matrix.cons_val_fin_one]
  field_simp
  ring

/-- `tr_M(σ₀σ₁σ₀) = h z² + z`. -/
theorem ocneanuD_basis_sigma010 (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD q (q ^ 3) (stdGen0 q * stdGen1 q * stdGen0 q) = hq q * zD q ^ 2 + zD q := by
  simp only [ocneanuD, yTriv, yStd, zD, hq, Matrix.trace_fin_two, stdGen0, stdGen1,
    Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.empty_val', Matrix.cons_val_fin_one]
  field_simp
  ring

/-! ## §3  The closed form -/

/-- The weak-vertex form factor `W(q) = q²(q¹² + q⁸ − 1)/(q² + 1)²`. -/
noncomputable def weakVertexTrace (q : K) : K :=
  q ^ 2 * (q ^ 12 + q ^ 8 - 1) / (q ^ 2 + 1) ^ 2

/-- **Main result.** The convention-D Markov trace of the `T(3,5)` braid `(σ₀σ₁)⁵ ∈ H₃(q)` —
trivial-block value `q¹⁰`, `(2,1)`-block matrix `(σ₀σ₁)⁵` — is `q²(q¹² + q⁸ − 1)/(q² + 1)²`. -/
theorem weakVertexTrace_eq (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD q (q ^ 10) ((stdGen0 q * stdGen1 q) ^ 5) = weakVertexTrace q := by
  simp only [ocneanuD, yTriv, yStd, weakVertexTrace, chi21_T35 q hq0]
  field_simp
  ring

/-- The Wedderburn form of the answer: `W(q) = y₍₃₎ q¹⁰ − y₍₂₁₎`. -/
theorem weakVertexTrace_eq_wedderburn (q : K) (h2 : q ^ 2 + 1 ≠ 0) :
    weakVertexTrace q = yTriv q * q ^ 10 - yStd q := by
  simp only [weakVertexTrace, yTriv, yStd]
  field_simp

/-- **Jones cross-check.** `T(3,5) = 10₁₂₄` has `V(t) = t⁴ + t⁶ − t¹⁰`; the numerator of `W` is
`q²² · V(q⁻²)`. -/
theorem weakVertexTrace_numerator_eq_jones (q : K) (hq0 : q ≠ 0) :
    q ^ 2 * (q ^ 12 + q ^ 8 - 1) = q ^ 22 * ((q⁻¹) ^ 8 + (q⁻¹) ^ 12 - (q⁻¹) ^ 20) := by
  field_simp

/-- `W(1) = 1/4`: at the classical point the `T(3,5)` trace collapses to the `SU(2)` weight
`y₍₃₎(1) − y₍₂₁₎(1) = 1/2 − 1/4`. -/
theorem weakVertexTrace_one : weakVertexTrace (1 : K) = 1 / 4 := by
  simp only [weakVertexTrace]
  norm_num

/-- Numerical envelope at the proton pin `q₀ = 1.1099785827513808…`: `1.187 < W(q₀) < 1.188`
(the producer reports `1.18748…`). -/
theorem weakVertexTrace_near_q0 :
    (1.187 : ℝ) < weakVertexTrace (1.1099785827513808 : ℝ) ∧
      weakVertexTrace (1.1099785827513808 : ℝ) < 1.188 := by
  simp only [weakVertexTrace]
  constructor <;> norm_num

end QOU.Braiding.WeakVertexT35
