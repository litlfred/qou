import Mathlib.Tactic
import QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
import QOU.MassTheory.ThreeRowExtensiveCumulant
import QOU.MassTheory.AdditiveResidualSimplex
import QOU.MassTheory.IsospinMirrorInvariance

/-!
# GPMT 3-Row Extensive Cumulant Sign-Window Inversion & `A = 3` Mirror Binding Bridge

This module bridges three formalizations in the QOU repository:

1. **The Geer–Patureau-Mirand–Turaev (GPMT) renormalized trace and modified quantum dimension**
   `dMod111 q = -q^3 / ((q^2 + 1)(q^4 + q^2 + 1))` on the Convention-D killed 3-row
   antisymmetric ideal `H_3(q) e_{(1^3)}`
   (`QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace`),
2. **The `q₀`-free `≥ 3`-row combinatorial Mayer cumulants**
   `(ν₂, ν₃, ν₄) = (0, -1, +2)` from the signed Springer-dimension stratum `sRow3`
   (`QOU.MassTheory.ThreeRowExtensiveCumulant`), and
3. **The coordination-simplex decomposition and `A = 3` mirror-nucleus (`³H` vs `³He`)
   two-term binding functional** (`QOU.MassTheory.AdditiveResidualSimplex` and
   `QOU.MassTheory.IsospinMirrorInvariance`).

## Physical and Mathematical Resolution of the Sign-Window Problem

In `QOU.MassTheory.ThreeRowExtensiveCumulant`, the unweighted `≥ 3`-row signed
Springer-dimension sum `sRow3` gives the forward Mayer cumulants
`ν₂ = 0`, `ν₃ = -1`, `ν₄ = +2`, whose sign pattern `(ν₃, ν₄) = (-, +)` is the
**exact opposite** of the physical nuclear binding residual window
`(μ₃, μ₄) = (+, -)` (3-body attraction `μ₃ > 0`, 4-body α-cluster saturation `μ₄ < 0`).

Why does the killed 3-row stratum acquire a negative renormalized weight?
Under Convention D (`z_D = q^3 / (q^2 + 1)`), the ordinary Ocneanu/Wedderburn weight
of the 3-row partition `(1^3)` vanishes identically (`w111_conventionD : w111 q (zD q) = 0`),
while its first-order Geer–Patureau-Mirand–Turaev (GPMT) renormalized modified quantum
dimension is the derivative `d_D(S^{(1^3)}) = dw_{(1^3)}/dz |_{z = z_D} = dMod111 q`.
Because the Convention-D root `z_D = q^3 / (q^2 + 1)` lies **strictly below** the
symmetric root `z = q` for every `q > 0`:
`z_D - q = -q / (q^2 + 1) < 0`,
the slope `dMod111 q = q^2 (z_D - q) / (q^4 + q^2 + 1)` is **strictly negative** for all
`q > 0` (`dMod111_neg_of_pos`), and equals `-1 / ([2]_q [3]_q)` in terms of standard
symmetric quantum integers `[2]_q = q + q⁻¹ > 0` and `[3]_q = q^2 + 1 + q^{-2} > 0`.

Multiplying the killed `≥ 3`-row stratum `sRow3` by its canonical GPMT modified quantum
dimension `dMod111 q < 0` inverts the `(-, +)` sign window to the physical `(+, -)`
window across all `q > 0` with **zero free parameters**:
* `mu2GPMT q = 0` (exact deuteron 2-body zero preserved),
* `mu3GPMT q = -dMod111 q > 0` (3-body attractive triangle cumulant),
* `mu4GPMT q = 2 * dMod111 q < 0` (4-body saturating tetrahedron cumulant),
* `BextGPMT q 2 = 0`, `BextGPMT q 3 > 0`, `BextGPMT q 4 = 6 * BextGPMT q 3 > 0`.

## Two-Term Mirror Binding Decomposition at `A = 3` (`³H` vs `³He`)

In Section 3, we combine the strong-sector mirror invariance of
`QOU.MassTheory.IsospinMirrorInvariance` with the inter-nucleon pairwise electromagnetic
operator on a general 3-nucleon state `(q₁, q₂, q₃)`. Under the global isospin mirror
`s ↦ -s` exchanging `³H = (p, n, n)` (`s = (+1, -1, -1)`, charges `(1, 0, 0)`) and
`³He = (n, p, p)` (`s = (-1, +1, +1)`, charges `(0, 1, 1)`):
* Both the isospin-signed 2-body strong exchange matrix `isospinExchange mag s` and the
  GPMT 3-row extensive core `BextGPMT q 3` are strictly invariant under `s ↦ -s`, so the
  strong contribution to `B(³H) - B(³He)` vanishes identically.
* The mirror binding difference is determined purely by the inter-nucleon pairwise
  charge operator `∑_{i < j} q_i q_j`, which evaluates to `0` on `³H` (`1·0 + 1·0 + 0·0 = 0`)
  and `1` on `³He` (`0·1 + 0·1 + 1·1 = 1`), yielding `B(³H) - B(³He) = c_EM > 0`.

## Derivation Seams & Scope (Inherited from `ThreeRowExtensiveCumulant.lean`)

* **`sRow3` table seam:** Per `QOU.MassTheory.ThreeRowExtensiveCumulant`, `sRow3` is a
  concrete integer table (`3 ↦ -1, 4 ↦ -2, 5 ↦ 4, _ ↦ 0`); the hook-length sum identity
  `sRow3 k = ∑_{λ ⊢ k, ℓ(λ) ≥ 3} (-1)^{n(λ)} f^λ` is verified in the companion Python
  probe (`computations/deltalambda/threerow_extensive_cumulant_forward_probe.py`), not
  formalized via SYT combinatorics in Lean. Every theorem in Section 2 is therefore
  Lean-proved for the table `sRow3`.
* **Sign-window inversion vs. magnitude ratio:** Uniform renormalization by the `H_3(q)`
  GPMT modified quantum dimension `dMod111 q < 0` inverts the table's `(-, +)` sign
  pattern into the physical `(+, -)` nuclear binding sign window (`mu3GPMT q > 0`,
  `mu4GPMT q < 0`) for all `q > 0`, while preserving the 1-scale magnitude ratios
  `mu4GPMT q = -2 * mu3GPMT q` and `BextGPMT q 4 = 6 * BextGPMT q 3`. Closing the
  `A = 4` magnitude ratio (`|μ₄ / μ₃| ≈ 9.75`) requires per-partition `H_4(q)` GPMT
  modified-dimension weights on `(2,1,1)` vs `(1^4)`.
-/

namespace QOU.MassTheory
namespace GPMTThreeRowCumulantBridge

open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
open QOU.MassTheory.ThreeRowExtensiveCumulant

/-! ## Section 1: Strict Negativity & Quantum-Integer Identity of GPMT `dMod111` -/

section GPMTModifiedDimensionSign

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- For any `q : R`, `q^2 + 1` is strictly positive in a strict ordered field. -/
theorem sq_add_one_pos (q : R) : 0 < q ^ 2 + 1 := by
  positivity

/-- For any `q : R`, `q^4 + q^2 + 1` is strictly positive in a strict ordered field. -/
theorem pow_four_add_sq_add_one_pos (q : R) : 0 < q ^ 4 + q ^ 2 + 1 := by
  have hq4 : 0 ≤ q ^ 4 := by positivity
  have hq2 : 0 ≤ q ^ 2 := by positivity
  linarith

/-- **Root Ordering Theorem (`z_D < q` for all `q > 0`)**:
The Convention-D Markov root `z_D = q^3 / (q^2 + 1)` lies strictly below the
symmetric `(3)` Markov root `z = q` for all `q > 0`, with exact gap
`zD q - q = -q / (q^2 + 1) < 0`. This root ordering is the structural origin
of the negative sign of the GPMT modified quantum dimension `d_D(S^{(1^3)})`. -/
theorem zD_sub_self_eq (q : R) :
    zD q - q = -q / (q ^ 2 + 1) := by
  have hq2 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  unfold zD
  rw [div_sub' hq2]
  ring

/-- For all `q > 0`, `zD q - q < 0` (`zD q < q`). -/
theorem zD_sub_self_neg_of_pos (q : R) (hq : 0 < q) :
    zD q - q < 0 := by
  rw [zD_sub_self_eq q, neg_div]
  exact neg_neg_of_pos (div_pos hq (sq_add_one_pos q))

/-- **Strict Negativity of the GPMT Modified Quantum Dimension `d_D(S^{(1^3)})`**:
For every `q > 0` in a linear ordered field `R`,
`dMod111 q = -q^3 / ((q^2 + 1)(q^4 + q^2 + 1)) < 0`. -/
theorem dMod111_neg_of_pos (q : R) (hq : 0 < q) :
    dMod111 q < 0 := by
  unfold dMod111
  rw [neg_div]
  apply neg_neg_of_pos
  apply div_pos
  · exact pow_pos hq 3
  · exact mul_pos (sq_add_one_pos q) (pow_four_add_sq_add_one_pos q)

/-- Symmetric quantum integer `[2]_q = q + q⁻¹`. -/
def qInt2 (q : R) : R := q + q⁻¹

/-- Symmetric quantum integer `[3]_q = q^2 + 1 + q^{-2}`. -/
def qInt3 (q : R) : R := q ^ 2 + 1 + q⁻¹ ^ 2

/-- For all `q > 0`, the symmetric quantum integers `[2]_q` and `[3]_q` are strictly positive. -/
theorem qInt2_pos_of_pos (q : R) (hq : 0 < q) : 0 < qInt2 q := by
  unfold qInt2
  positivity

/-- For all `q > 0`, `[3]_q = q^2 + 1 + q^{-2} > 0`. -/
theorem qInt3_pos_of_pos (q : R) (hq : 0 < q) : 0 < qInt3 q := by
  unfold qInt3
  positivity

/-- **Quantum-Integer Reciprocal Form of `dMod111`**:
For every `q ≠ 0`, the GPMT modified quantum dimension of the killed `(1^3)` sector
equals `-1 / ([2]_q [3]_q)`. Thus `-dMod111 q = 1 / ([2]_q [3]_q) > 0` is the positive
reciprocal of the symmetric quantum-integer product `[2]_q [3]_q`, while the minus sign
comes strictly from the orientation of the simple zero `(z - z_D)` relative to `(z - q)`. -/
theorem dMod111_eq_neg_inv_qInt2_mul_qInt3 (q : R) (hq : q ≠ 0) :
    dMod111 q = -1 / (qInt2 q * qInt3 q) := by
  have hq2 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt (pow_four_add_sq_add_one_pos q)
  unfold dMod111 qInt2 qInt3
  have hfac2 : q + q⁻¹ = (q ^ 2 + 1) / q := by
    field_simp
  have hfac3 : q ^ 2 + 1 + q⁻¹ ^ 2 = (q ^ 4 + q ^ 2 + 1) / q ^ 2 := by
    field_simp
  rw [hfac2, hfac3]
  field_simp

end GPMTModifiedDimensionSign

/-! ## Section 2: GPMT-Weighted `≥ 3`-Row Cumulants & Sign-Window Inversion -/

section GPMTWeightedThreeRowCumulants

variable {R : Type*} [Field R]

/-- The GPMT-renormalized `≥ 3`-row single-algebra trace stratum at cluster size `A`:
weights the combinatorial signed-Springer-dimension sum `sRow3 A` by the GPMT
modified quantum dimension `dMod111 q` of the killed 3-row ideal. -/
def sRow3GPMT (q : R) (A : ℕ) : R :=
  dMod111 q * (sRow3 A : R)

/-- GPMT-weighted 2-body (edge) Mayer cumulant `μ₂^{\mathrm{GPMT}}(q) = S_{\mathrm{GPMT}}(2)`. -/
def mu2GPMT (q : R) : R :=
  sRow3GPMT q 2

/-- GPMT-weighted 3-body (triangle) Mayer cumulant
`μ₃^{\mathrm{GPMT}}(q) = S_{\mathrm{GPMT}}(3) - 3 · μ₂^{\mathrm{GPMT}}(q)`. -/
def mu3GPMT (q : R) : R :=
  sRow3GPMT q 3 - 3 * mu2GPMT q

/-- GPMT-weighted 4-body (tetrahedron) Mayer cumulant
`μ₄^{\mathrm{GPMT}}(q) = S_{\mathrm{GPMT}}(4) - 6 · μ₂^{\mathrm{GPMT}}(q) - 4 · μ₃^{\mathrm{GPMT}}(q)`. -/
def mu4GPMT (q : R) : R :=
  sRow3GPMT q 4 - 6 * mu2GPMT q - 4 * mu3GPMT q

/-- Exact linearity of the Mayer cumulant inversion under GPMT renormalization:
`mu2GPMT q = dMod111 q * nu2`, `mu3GPMT q = dMod111 q * nu3`, `mu4GPMT q = dMod111 q * nu4`. -/
theorem muGPMT_eq_dMod111_mul_nu (q : R) :
    mu2GPMT q = dMod111 q * (nu2 : R) ∧
    mu3GPMT q = dMod111 q * (nu3 : R) ∧
    mu4GPMT q = dMod111 q * (nu4 : R) := by
  refine ⟨?_, ?_, ?_⟩
  · unfold mu2GPMT sRow3GPMT nu2 Salg
    rfl
  · unfold mu3GPMT mu2GPMT sRow3GPMT nu3 nu2 Salg
    push_cast
    ring
  · unfold mu4GPMT mu3GPMT mu2GPMT sRow3GPMT nu4 nu3 nu2 Salg
    push_cast
    ring

/-- Explicit closed forms of `(mu2GPMT q, mu3GPMT q, mu4GPMT q)` in terms of `dMod111 q`:
`mu2GPMT q = 0`, `mu3GPMT q = -dMod111 q`, `mu4GPMT q = 2 * dMod111 q`. -/
theorem muGPMT_closed_forms (q : R) :
    mu2GPMT q = 0 ∧
    mu3GPMT q = -dMod111 q ∧
    mu4GPMT q = 2 * dMod111 q := by
  rcases muGPMT_eq_dMod111_mul_nu q with ⟨h2, h3, h4⟩
  rcases nu_values with ⟨hnu2, hnu3, hnu4⟩
  rw [h2, h3, h4, hnu2, hnu3, hnu4]
  push_cast
  refine ⟨by ring, by ring, by ring⟩

/-- **GPMT 3-Row Cumulant Sign-Window Inversion Theorem**:
For all `q > 0`, weighting the killed `≥ 3`-row stratum by its canonical GPMT modified
quantum dimension `dMod111 q` preserves the exact 2-body deuteron zero (`mu2GPMT q = 0`)
and **inverts** the unweighted `(-, +)` sign pattern (`forward_sign_window_opposite`)
into the physical `(+, -)` nuclear binding sign window:
`0 < mu3GPMT q` (3-body attraction) and `mu4GPMT q < 0` (4-body saturation), with
`mu4GPMT q = -2 * mu3GPMT q`. -/
theorem gpmt_threeRow_cumulant_signs [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : 0 < q) :
    mu2GPMT q = 0 ∧
    (0 < mu3GPMT q ∧ mu4GPMT q < 0) ∧
    mu4GPMT q = -2 * mu3GPMT q := by
  rcases muGPMT_closed_forms q with ⟨h2, h3, h4⟩
  have hd : dMod111 q < 0 := dMod111_neg_of_pos q hq
  refine ⟨h2, ⟨?_, ?_⟩, ?_⟩
  · linarith
  · linarith
  · linarith

/-- The GPMT-weighted extensive cluster functional `BextGPMT q A = dMod111 q * Bext A`
(Reading Y of `ThreeRowExtensiveCumulant` renormalized by `dMod111 q`). -/
def BextGPMT (q : R) (A : ℕ) : R :=
  ∑ k ∈ Finset.range (A + 1), (A.choose k : R) * sRow3GPMT q k

/-- Factorization `BextGPMT q A = dMod111 q * (Bext A : R)`. -/
theorem BextGPMT_eq_dMod111_mul_Bext (q : R) (A : ℕ) :
    BextGPMT q A = dMod111 q * (Bext A : R) := by
  unfold BextGPMT Bext sRow3GPMT
  push_cast
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl ?_
  intro k _
  ring

/-- Concrete values and strict positivity of the GPMT-renormalized extensive cluster
binding at `A = 2, 3, 4` for all `q > 0`:
* `BextGPMT q 2 = 0` (deuteron carries zero `≥ 3`-row cluster content),
* `BextGPMT q 3 = -dMod111 q > 0` (`A = 3` triton/helium-3 core is strictly attractive),
* `BextGPMT q 4 = -6 * dMod111 q = 6 * BextGPMT q 3 > 0` (`A = 4` alpha-particle core). -/
theorem BextGPMT_values_and_pos [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : 0 < q) :
    BextGPMT q 2 = 0 ∧
    BextGPMT q 3 = -dMod111 q ∧
    BextGPMT q 4 = -6 * dMod111 q ∧
    0 < BextGPMT q 3 ∧
    0 < BextGPMT q 4 ∧
    BextGPMT q 4 = 6 * BextGPMT q 3 := by
  have hd : dMod111 q < 0 := dMod111_neg_of_pos q hq
  have h2 : BextGPMT q 2 = 0 := by
    rw [BextGPMT_eq_dMod111_mul_Bext, Bext_two]
    simp
  have h3 : BextGPMT q 3 = -dMod111 q := by
    rw [BextGPMT_eq_dMod111_mul_Bext, Bext_three]
    push_cast
    ring
  have h4 : BextGPMT q 4 = -6 * dMod111 q := by
    rw [BextGPMT_eq_dMod111_mul_Bext, Bext_four]
    push_cast
    ring
  refine ⟨h2, h3, h4, by linarith, by linarith, by linarith⟩

/-- Over `ℝ`, the GPMT-weighted cumulants `(mu2GPMT q, mu3GPMT q, mu4GPMT q)` satisfy the
exact coordination-simplex equations `simplexA2`, `simplexA3`, `simplexA4` of
`QOU.MassTheory.AdditiveResidualSimplex` for the single-algebra GPMT stratum
`m₂ = 0`, `m₃ = -dMod111 q`, `m₄ = 2 * dMod111 q`, and discharge the deuteron
hypothesis `simplexA2 = 0`. -/
theorem simplex_gpmt_cumulants_real (q : ℝ) :
    simplexA2 (mu2GPMT q) (mu3GPMT q) (mu4GPMT q) = 0 ∧
    simplexA3 (mu2GPMT q) (mu3GPMT q) (mu4GPMT q) = -dMod111 q ∧
    simplexA4 (mu2GPMT q) (mu3GPMT q) (mu4GPMT q) = -2 * dMod111 q := by
  rcases muGPMT_closed_forms q with ⟨h2, h3, h4⟩
  unfold simplexA2 simplexA3 simplexA4
  rw [h2, h3, h4]
  refine ⟨by ring, by ring, by ring⟩

end GPMTWeightedThreeRowCumulants

/-! ## Section 3: Two-Term `A = 3` Mirror Binding Theorem (`³H` vs `³He`) -/

section TwoTermMirrorBindingA3

variable {R : Type*} [CommRing R]

/-- Electric charge projection `q(s) = (1 + s) / 2` in doubled units (`2 q(s) = 1 + s`),
or direct nucleon electric charge tuple `(q₁, q₂, q₃) : Fin 3 → R`.
For a 3-nucleon system with nucleon charges `qN : Fin 3 → R`, the inter-nucleon
pairwise electromagnetic charge operator counts the proton-proton pairs:
`pairChargeA3 qN = qN 0 * qN 1 + qN 0 * qN 2 + qN 1 * qN 2`. -/
def pairChargeA3 (qN : Fin 3 → R) : R :=
  qN 0 * qN 1 + qN 0 * qN 2 + qN 1 * qN 2

/-- Nucleon electric charges of the triton `³H = (p, n, n)`: `![1, 0, 0]`. -/
def tritonCharges : Fin 3 → R := ![1, 0, 0]

/-- Nucleon electric charges of helium-3 `³He = (n, p, p)`: `![0, 1, 1]`. -/
def helium3Charges : Fin 3 → R := ![0, 1, 1]

/-- Nucleon isospin labels of the triton `³H = (p, n, n)`: `![1, -1, -1]`. -/
def tritonIsospin : Fin 3 → R := ![1, -1, -1]

/-- Nucleon isospin labels of helium-3 `³He = (n, p, p)`: `![-1, 1, 1]`. -/
def helium3Isospin : Fin 3 → R := ![-1, 1, 1]

/-- `³He` is the exact global isospin mirror `s ↦ -s` of `³H`. -/
theorem helium3Isospin_eq_neg_tritonIsospin :
    helium3Isospin = (fun i => -(tritonIsospin i : R)) := by
  funext i
  fin_cases i <;> simp [helium3Isospin, tritonIsospin]

/-- The triton electric charge vector `tritonCharges` satisfies the Gell-Mann–Nishijima
relation `2 * q_i = 1 + s_i` with `tritonIsospin`. -/
theorem two_mul_tritonCharges_eq_one_add_tritonIsospin (i : Fin 3) :
    2 * (tritonCharges i : R) = 1 + tritonIsospin i := by
  fin_cases i <;> (simp [tritonCharges, tritonIsospin]; try ring)

/-- The helium-3 electric charge vector `helium3Charges` satisfies the Gell-Mann–Nishijima
relation `2 * q_i = 1 + s_i` with `helium3Isospin`. -/
theorem two_mul_helium3Charges_eq_one_add_helium3Isospin (i : Fin 3) :
    2 * (helium3Charges i : R) = 1 + helium3Isospin i := by
  fin_cases i <;> (simp [helium3Charges, helium3Isospin]; try ring)

/-- The inter-nucleon pairwise electromagnetic charge operator vanishes on `³H = (p, n, n)`. -/
theorem pairChargeA3_triton :
    pairChargeA3 (tritonCharges : Fin 3 → R) = 0 := by
  unfold pairChargeA3 tritonCharges
  simp

/-- The inter-nucleon pairwise electromagnetic charge operator equals `1` on `³He = (n, p, p)`. -/
theorem pairChargeA3_helium3 :
    pairChargeA3 (helium3Charges : Fin 3 → R) = 1 := by
  unfold pairChargeA3 helium3Charges
  simp

/-- Two-term `A = 3` nuclear binding functional combining:
1. Any strong binding functional `F_strong` of the isospin-signed exchange determinant
   `(isospinExchange mag s).det` and the `A = 3` GPMT 3-body core `B3_core`, and
2. The repulsive inter-nucleon pairwise electromagnetic interaction `-c_EM * pairChargeA3 qN`. -/
def bindingTwoTermA3 (F_strong : R → R → R) (mag : Fin 3 → Fin 3 → R) (B3_core c_EM : R)
    (s qN : Fin 3 → R) : R :=
  F_strong (isospinExchange mag s).det B3_core - c_EM * pairChargeA3 qN

/-- **`A = 3` Two-Term Mirror Binding Splitting Theorem (`B(³H) - B(³He) = c_EM`)**:
In the two-term `A = 3` nuclear binding functional, the strong-exchange determinant
`(isospinExchange mag s).det` and the GPMT 3-body core `B3_core` are identical for
`³H = (p, n, n)` and its mirror `³He = (n, p, p)` and cancel completely in the mirror
difference `B(³H) - B(³He)`, leaving the pure inter-nucleon pairwise electromagnetic
coupling `c_EM`. -/
theorem twoTerm_mirror_split_A3 (F_strong : R → R → R) (mag : Fin 3 → Fin 3 → R)
    (B3_core c_EM : R) :
    bindingTwoTermA3 F_strong mag B3_core c_EM tritonIsospin tritonCharges -
      bindingTwoTermA3 F_strong mag B3_core c_EM helium3Isospin helium3Charges = c_EM := by
  unfold bindingTwoTermA3
  rw [helium3Isospin_eq_neg_tritonIsospin, isospinExchange_det_mirror_invariant,
    pairChargeA3_triton, pairChargeA3_helium3]
  ring

end TwoTermMirrorBindingA3

end GPMTThreeRowCumulantBridge
end QOU.MassTheory
