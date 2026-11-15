import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# QOU.Mass.HeckeStokesEigenvalues — Hecke monodromy eigenvalues and the `[2]_q` origin of τ

This file supplies the Lean link between the **Yekutieli non-abelian Stokes** step of the
categorical chain and the lever-1 trace `τ` being a function of the quantum integer `[2]_q`.

**Step 2 of the chain (non-abelian Stokes; `mass-theory/pre-archimedean-derivation-chain.md`,
`prop:hecke-spectral-sequence`).** The polynomial `F(σ) = σ² − (q − q⁻¹)σ − 1` is **not a
curvature**. It is the *monodromy quadratic*: the eigenvalue relation satisfied by the exchange
monodromy of a **flat** connection. (A curved connection has path-dependent holonomy and gives no
braid representation at all.) For the 𝔰𝔩₂ Knizhnik–Zamolodchikov connection it is *derived* from
the Casimir eigenvalues `½` (triplet) and `−3/2` (singlet): on two points,
`QOU.Mass.KohnoTwoPoint.kzExchange_quad`, sorry-free. For the framework's own substrate
connection it remains the hypothesis of the §3b class `QOU.Mass.HeckeMonodromy` (2026-09-06;
cheat-sheet §2a), since that connection is not constructed and is not shown to be KZ
(bean `qou-d0qq`). The factorisation below is unconditional algebra. (The declaration names keep
the historical word "curvature"; read it as "monodromy quadratic".) The two roots of that characteristic polynomial
are the Hecke eigenvalues — the symmetric (`L₊`) and antisymmetric (`L₋`) braiding channels of
the Hecke–Skein convention (AGENTS.md §7a):

  `λ₊ = q`  (positive crossing),   `λ₋ = −q⁻¹`  (negative crossing).

**Why this matters for τ.** `TauQuantumIntegerForm` proves `τ(q) = 3(3[2]² + 2)/(4([2]+2))` with
`[2] = [2]_q = q + q⁻¹`, hence **bar-even** (`τ(q⁻¹) = τ(q)`). This file pins *where* that even
structure comes from: the quantum dimension `[2]_q` is the **gap** `λ₊ − λ₋` between the two
Stokes/Hecke eigenvalues, which is bar-even — whereas their **sum** `λ₊ + λ₋ = q − q⁻¹` (the
linear coefficient of the monodromy quadratic) is bar-odd. So τ's bar-evenness is inherited from the
quantum dimension (the eigenvalue gap), not from the eigenvalue sum.

Ground ring: a generic field (the identities are fibre-level / q-formal, no `ℝ` ordering needed),
matching the §7c base-ring discipline and `TauQuantumIntegerForm`.
-/

namespace QOU.Mass.HeckeStokes

variable {K : Type*} [Field K]

/-- **The monodromy quadratic factors into the two Hecke eigenvalues.**
The characteristic polynomial `X² − (q − q⁻¹)X − 1` of the exchange monodromy factors as `(X − q)(X + q⁻¹)`:
roots `λ₊ = q` (symmetric channel `L₊`) and `λ₋ = −q⁻¹` (antisymmetric channel `L₋`). -/
theorem stokes_curvature_factors (q : K) (hq : q ≠ 0) (X : K) :
    X ^ 2 - (q - q⁻¹) * X - 1 = (X - q) * (X + q⁻¹) := by
  field_simp
  ring

/-- The two Hecke eigenvalues have **product `−1`** (`λ₊ · λ₋`, the Hecke-generator determinant). -/
theorem stokes_eigenvalues_prod (q : K) (hq : q ≠ 0) :
    q * (-q⁻¹) = -1 := by
  rw [mul_neg, mul_inv_cancel₀ hq]

/-- Their **sum is the linear coefficient `q − q⁻¹` of the monodromy quadratic** (`λ₊ + λ₋`), which is **bar-odd**. -/
theorem stokes_eigenvalues_sum (q : K) :
    q + (-q⁻¹) = q - q⁻¹ := by
  ring

/-- **The quantum dimension `[2]_q = q + q⁻¹` is the eigenvalue gap `λ₊ − λ₋`.**
`q − (−q⁻¹) = q + q⁻¹`. This bar-even combination — not the bar-odd sum above — is what `τ`
is built from (`TauQuantumIntegerForm`), which is why `τ` is bar-even. -/
theorem quantum_dim_is_eigenvalue_gap (q : K) :
    q - (-q⁻¹) = q + q⁻¹ := by
  ring

/-- **`[2]_q` is bar-even:** `[2]_{q⁻¹} = [2]_q`, i.e. `q⁻¹ + (q⁻¹)⁻¹ = q + q⁻¹`.
(The eigenvalue gap is invariant under the Hecke bar-involution `q ↦ q⁻¹`; the linear
coefficient `q − q⁻¹` is not.) -/
theorem quantum_dim_bar_even (q : K) :
    q⁻¹ + (q⁻¹)⁻¹ = q + q⁻¹ := by
  rw [inv_inv, add_comm]

end QOU.Mass.HeckeStokes
