/-
# QOU.MassTheory.MagnusPairingSignStructure — why the linear Magnus pairing can carry a sign the quadrature cannot

Bean `qou-dp32` (deuteron Magnus continuation). The probe
`computations/deltalambda/deuteron_magnus_omega2_sign_probe.py` decides, numerically at the
proton `q₀`, that the second-order Magnus binding pairing `tr_M(ρ·Ω₂)` is sign-indefinite —
the property the traceless interface curvature `F_q` could NOT have, because a traceless
curvature enters the binding only through the non-negative quadrature `‖F_q‖²`.

This file proves the STRUCTURAL DICHOTOMY behind that verdict, in three sorry-free facts. It
formalizes *why the two routes differ in sign structure*; it does NOT derive the deuteron MeV
binding (that needs the open Δ_λ normalization — see the audit) and asserts no physical value.

1. `trace_commutator_eq_zero` — the (cyclic) trace of a commutator vanishes. This is the
   `ρ = I` control of the pairing: with the identity density the linear Magnus term is
   identically `0`, so it is NOT pinned to a sign the way a square is. General `CommRing`.

2. `trace_mul_transpose_nonneg` — the Frobenius quadrature `tr(F·Fᵀ) = Σ (F i j)²` is
   non-negative. This is the wall: `‖F_q‖²` is a sum of squares, so it can never be the
   binding-REDUCING (negative-at-A=2) term. Over `ℝ`.

3. `magnus_pairing_sign_indefinite` — a single commutator `⁅A,B⁆`, paired against two
   different densities, realizes BOTH a strictly positive and a strictly negative trace. So
   the linear pairing genuinely ESCAPES the non-negativity of (2): unlike `tr(F·Fᵀ)`, it is
   not sign-fixed. This is the exact structural content the probe observed (4 partitions
   positive, 5 negative, 2 exactly zero at A=2). Concrete `Fin 2` integer witnesses.

   That split read "2 positive, 7 negative" until 2026-09-13 — the pre-ruling figure. The
   2026-09-05 intra-nucleon ordering ruling (bean `qou-hu1f`) made the borromean word
   `(σ₀σ₁⁻¹)³` canonical in place of the grouped one, which changes the per-partition
   traces. Only the count moved: sign-indefiniteness, the property this file formalizes,
   holds under both words AND under either partition-weight family (bean `qou-za3q`),
   because it is a statement about a commutator's trace pairing, not about the weight.

Together: (2) traps the quadrature at `≥ 0`; (1)+(3) show the linear Magnus pairing is free of
that trap. That is the whole reason `qou-dp32` is LIVE where the quadrature route `qou-jqof`
was excluded.

Base ring (§7c): (1) is a generic `CommRing` identity; (2) needs an ordering, stated over `ℝ`;
(3) is over `ℤ` (exact, decidable). No archimedean construct enters (1).
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.MassTheory

open Matrix

/-- **The `ρ = I` control.** The trace of a commutator vanishes: `tr(A·B − B·A) = 0`, by
cyclicity of the trace. Consequently the linear Magnus pairing `tr(ρ·Ω₂)` with `ρ = I` and
`Ω₂` a sum of commutators is identically zero — it carries no built-in sign, and is therefore
free (unlike a quadrature) to be negative for a suitable density. -/
theorem trace_commutator_eq_zero {R : Type*} [CommRing R] {n : Type*} [Fintype n]
    (A B : Matrix n n R) : (A * B - B * A).trace = 0 := by
  rw [Matrix.trace_sub, Matrix.trace_mul_comm, sub_self]

/-- **The wall.** The Frobenius quadrature `tr(F·Fᵀ) = Σᵢⱼ (F i j)²` is non-negative. A
traceless curvature `F_q` enters the binding only through this square, so it can never supply a
binding-reducing (negative) contribution — the reason the quadrature route `qou-jqof` is
excluded from being the missing negative-at-A=2 term. -/
theorem trace_mul_transpose_nonneg {n : Type*} [Fintype n]
    (F : Matrix n n ℝ) : 0 ≤ (F * Fᵀ).trace := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply]
  exact Finset.sum_nonneg fun i _ => Finset.sum_nonneg fun j _ => mul_self_nonneg _

/-- **The escape.** The linear commutator-trace pairing is genuinely sign-indefinite: one fixed
commutator `⁅A,B⁆`, paired against two different densities `ρ₊, ρ₋`, gives a strictly positive
and a strictly negative trace. So — unlike the non-negative quadrature of
`trace_mul_transpose_nonneg` — the pairing is not sign-fixed, which is exactly why the
second-order Magnus term can carry the sign the traceless `F_q` could not.

Witnesses: `A = e₀₁`, `B = e₁₀` give `⁅A,B⁆ = diag(1,−1)`; then `ρ₊ = diag(1,0)` yields trace
`+1` and `ρ₋ = diag(0,1)` yields trace `−1`. -/
theorem magnus_pairing_sign_indefinite :
    ∃ A B ρp ρn : Matrix (Fin 2) (Fin 2) ℤ,
      0 < (ρp * (A * B - B * A)).trace ∧ (ρn * (A * B - B * A)).trace < 0 := by
  refine ⟨!![0, 1; 0, 0], !![0, 0; 1, 0], !![1, 0; 0, 0], !![0, 0; 0, 1], ?_, ?_⟩ <;> decide

/-- **Scalar density control.** Any scalar-multiple density `ρ = c • 1` annihilates
    a commutator `A * B - B * A` in trace, extending the `ρ = I` control to all
    central scalar weights. -/
theorem trace_scalar_mul_commutator_eq_zero {R : Type*} [CommRing R]
    {n : Type*} [Fintype n] [DecidableEq n] (c : R) (A B : Matrix n n R) :
    ((c • (1 : Matrix n n R)) * (A * B - B * A)).trace = 0 := by
  rw [smul_mul_assoc, one_mul, Matrix.trace_smul, trace_commutator_eq_zero, smul_zero]

/-- **Row-cap reduction for Wenzl vs. Plancherel weights (bean `qou-za3q`).**
    If a partition-weight family `w` vanishes on all shapes with more than `r` rows
    (`∀ i ∈ s, r < rows i → w i = 0`, the Wenzl level-`r` row cap), then the
    full weighted Magnus pairing sum over `s` equals the sum restricted to
    shapes with `rows i ≤ r`. -/
theorem weighted_pairing_annihilated_of_row_cap {R : Type*} [CommRing R]
    {ι : Type*} (s : Finset ι) (rows : ι → ℕ) (r : ℕ) (w t : ι → R)
    (hcap : ∀ i ∈ s, r < rows i → w i = 0) :
    ∑ i ∈ s, w i * t i = ∑ i ∈ s.filter (fun i => rows i ≤ r), w i * t i := by
  symm
  refine Finset.sum_subset (Finset.filter_subset _ s) ?_
  intro i his hnot
  rw [Finset.mem_filter] at hnot
  have hgt : r < rows i := Nat.lt_of_not_ge (fun hle => hnot ⟨his, hle⟩)
  rw [hcap i his hgt, zero_mul]

/-- **Exact tail isolation between uncapped and row-capped weights (bean `qou-za3q`).**
    For any weight `w` and any level `r`, the full partition sum decomposes as the
    sum over surviving shapes (`rows i ≤ r`) plus the sum over shapes annihilated by
    the level-`r` row cap (`r < rows i`). -/
theorem weighted_pairing_split_by_row_cap {R : Type*} [CommRing R]
    {ι : Type*} (s : Finset ι) (rows : ι → ℕ) (r : ℕ) (w t : ι → R) :
    ∑ i ∈ s, w i * t i =
      (∑ i ∈ s.filter (fun i => rows i ≤ r), w i * t i) +
      (∑ i ∈ s.filter (fun i => ¬ rows i ≤ r), w i * t i) := by
  exact (Finset.sum_filter_add_sum_filter_not s (fun i => rows i ≤ r) (fun i => w i * t i)).symm

end QOU.MassTheory
