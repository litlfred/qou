import QOU.MathlibExt.QPlancherel

/-!
# QOU.BraidKnot.jet_filtered_knot_factor — conjectural class (§3b)

**§3b class axiomatisation** for content block
[`conj:jet-filtered-knot-factor`](../../../quantum-observable-universe/mass-theory/jet-filtered-knot-factor.md):
*The Bethe–Weizsäcker knot factor $a(Z, N)$ is the Jones polynomial of
the nuclear quotient braid $\bar\beta$ (Part 4; Parts 1–3 established in
the manuscript).*

This is a **conjecture**: the class carries the conjecture's actual
content as the `factor_is_jones` field; no global instance is provided
(per AGENTS.md §3b-tax), representing the honest open state.

**Mathlib-infra pass (2026-06-25, Tier 1).** The established Part-1
per-level invariant is the $q$-Plancherel-weighted character average
$a_k = \frac{\sum_\lambda w_\lambda \chi_\lambda}{\sum_\lambda w_\lambda
\dim}$ with $w_\lambda = d_q(\lambda)^2 / Z_q(k)$. That Wedderburn weight
is now the **real** `QOU.MathlibExt.QPlancherel.measure` (built over the
`QDimension` / `HasPartitionFunction` typeclasses); `jetWedderburnWeight`
below is that measure, and `jetWedderburnWeight_nonneg` is an **unconditional
proof** of its positivity (from `QPlancherel.measure_nonneg`). Only the
characters $\chi_\lambda$ and the open Part-4 Jones identification stay
abstract.
-/

namespace QOU.BraidKnot

open QOU.MathlibExt.QPlancherel

section JetWeights

variable (R : Type*) [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The per-jet-level **Wedderburn weight** $w_\lambda = d_q(\lambda)^2 /
    Z_q(k)$ feeding the established per-level invariant $a_k$ (manuscript
    Part 1), realised as the canonical $q$-Plancherel measure.

    §7c: stated over a generic ordered field `R`; the `q`-Plancherel measure
    it wraps is itself generic (`QOU.MathlibExt.QPlancherel.measure`), so
    nothing here is archimedean. The archimedean evaluation is the
    instantiation `R := ℝ` at the substrate. -/
noncomputable def jetWedderburnWeight (Λ : Type) [QDimension Λ R]
    [HasPartitionFunction Λ R] (lam : Λ) (k : ℕ) : R :=
  measure (R := R) (Λ := Λ) lam k

/-- The jet Wedderburn weights are non-negative — an **unconditional**
    consequence of $q$-Plancherel positivity. -/
theorem jetWedderburnWeight_nonneg (Λ : Type) [QDimension Λ R]
    [HasPartitionFunction Λ R] (lam : Λ) (k : ℕ) :
    0 ≤ jetWedderburnWeight R Λ lam k :=
  measure_nonneg (R := R) (Λ := Λ) lam k

/-- Vanishing of the per-level jet weight on any partition with zero
    $q$-dimension $d_q(\lambda) = 0$. -/
theorem jetWeight_eq_zero_of_dq_zero (Λ : Type) [QDimension Λ R]
    [HasPartitionFunction Λ R] (lam : Λ) (k : ℕ)
    (hdq : (QDimension.dq lam : R) = 0) :
    jetWedderburnWeight R Λ lam k = 0 :=
  measure_eq_zero_of_dq_zero (R := R) (Λ := Λ) lam k hdq

/-- Rescaling the per-level jet weight by the partition function $Z_q(k)$
    recovers the squared $q$-dimension $d_q(\lambda)^2$. -/
theorem jetWeight_mul_partitionFunction (Λ : Type) [QDimension Λ R]
    [HasPartitionFunction Λ R] (lam : Λ) (k : ℕ) :
    HasPartitionFunction.Z (Λ := Λ) k * jetWedderburnWeight R Λ lam k =
      (QDimension.dq lam : R) ^ 2 :=
  measure_mul_partitionFunction (R := R) (Λ := Λ) lam k

end JetWeights

/-- **Jet-filtered knot factor** $a(Z, N) = J_{\bar\beta}(q)$.

    Conjectural class — see
    [`conj:jet-filtered-knot-factor`](../../../quantum-observable-universe/mass-theory/jet-filtered-knot-factor.md). -/
class jet_filtered_knot_factor (R : Type*) where
  /-- The Bethe–Weizsäcker knot factor $a(Z, N)$ multiplying the bulk
      binding (the $q$-Plancherel-weighted per-level invariant of Part 1,
      with weights `jetWedderburnWeight`). -/
  knotFactor : ℕ → ℕ → R
  /-- The Jones polynomial $J_{\bar\beta}(q)$ of the nuclear quotient
      braid (each nucleon collapsed to one effective crossing). -/
  jonesQuotient : ℕ → ℕ → R
  /-- **The conjecture** (Part 4): the BW knot factor equals the Jones
      polynomial of the nuclear quotient braid, for every $(Z, N)$. -/
  factor_is_jones : ∀ Z N : ℕ, knotFactor Z N = jonesQuotient Z N

-- Per AGENTS.md §3b-cond we provide NO global instance.
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/jet-filtered-knot-factor.ts

namespace jet_filtered_knot_factor

/-- Conditional on `jet_filtered_knot_factor`, the difference between the
    per-nucleus factor and the quotient braid invariant vanishes at every $(Z, N)$. -/
theorem factor_sub_eq_zero {R : Type*} [AddGroup R]
    [h : jet_filtered_knot_factor R] (Z N : ℕ) :
    h.knotFactor Z N - h.jonesQuotient Z N = 0 :=
  sub_eq_zero.mpr (h.factor_is_jones Z N)

/-- Conditional on `jet_filtered_knot_factor`, any scalar multiple of the
    per-nucleus factor agrees with the corresponding multiple of the quotient invariant. -/
theorem weighted_factor_eq {R : Type*} [Mul R]
    [h : jet_filtered_knot_factor R] (w : R) (Z N : ℕ) :
    w * h.knotFactor Z N = w * h.jonesQuotient Z N := by
  rw [h.factor_is_jones Z N]

/-- Conditional on `jet_filtered_knot_factor`, differences of the per-nucleus
    factor across two $(Z, N)$ pairs match differences of the quotient invariant. -/
theorem factor_diff_eq {R : Type*} [AddGroup R]
    [h : jet_filtered_knot_factor R] (Z₁ N₁ Z₂ N₂ : ℕ) :
    h.knotFactor Z₁ N₁ - h.knotFactor Z₂ N₂ =
      h.jonesQuotient Z₁ N₁ - h.jonesQuotient Z₂ N₂ := by
  rw [h.factor_is_jones Z₁ N₁, h.factor_is_jones Z₂ N₂]

/-- Falsifiability witness: if two candidate tables disagree at some $(Z, N)$,
    no `jet_filtered_knot_factor` instance can simultaneously realise both. -/
theorem not_of_mismatch {R : Type*} (f g : ℕ → ℕ → R) (Z N : ℕ)
    (hne : f Z N ≠ g Z N) :
    ¬ ∃ h : jet_filtered_knot_factor R, h.knotFactor = f ∧ h.jonesQuotient = g := by
  rintro ⟨h, rfl, rfl⟩
  exact hne (h.factor_is_jones Z N)

end jet_filtered_knot_factor

end QOU.BraidKnot
