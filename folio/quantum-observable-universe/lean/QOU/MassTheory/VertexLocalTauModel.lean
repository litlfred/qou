/-
# Vertex-local τ model over ℂ — the degenerate H₂(i) Jordan module and its ρ-partner

Bean `qou-tq20` (B2 lift), second tranche: the vertex-local statement — *"τ
sends the H₂(i)-module to the vertex tangent module where `dU` acts by the
multiplier `i`, intertwining the fibre reality structure ρ with conjugation"*
— formalized at the MODULE level over genuine `ℂ` with Mathlib.

Why this upgrades the merged GInt shadow (#3960/#3982): the Gaussian-integer
shadow proved the assignment forced but could not *express* anti-linearity —
and B1 (#3955) showed the whole obstruction is one of ANALYTIC TYPE
(ℂ-linear channel-swap vs ℂ-anti-linear conjugation, nome-independent per
#3949). Over `ℂ` with `starRingEnd ℂ`, the statements below carry the actual
anti-linear structure.

Proved here, sorry-free:

* `hecke_relation_at_i` — the concrete 2×2 Jordan block `σ = !![i,1;0,i]`
  satisfies the Hecke relation `σ² = (q−q⁻¹)σ + 1` at `q = i`
  (`q − q⁻¹ = 2i`): this IS the H₂(i)-module of the degenerate locus.
* `jordan_nilpotent` / `not_semisimple` — `(σ − i·1)² = 0` with `σ ≠ i·1`:
  the module is non-semisimple (the degenerate confluence `q = −q⁻¹`), its
  semisimplification acting by the scalar `i` — exactly the vertex
  multiplier `dU|_V = i` of the geometric carrier (#3942).
* `rho_carries_module` — `ρ` (entrywise `starRingEnd ℂ`) carries the `q = i`
  Jordan module to the `q = −i` Jordan module: the GENUINELY ANTI-LINEAR
  statement the GInt shadow could only mirror combinatorially. Its Hecke
  relation `σ̄² = −2i·σ̄ + 1` (`hecke_relation_conj`) is the conjugated one.
* `shadow_unique_complex` — the forced-assignment theorem transported to
  `ℂ`: any `f : ℂ → Bool` with the normalization and the ρ-intertwining on
  the pair agrees with the forced assignment (`Complex.conj_I` carries the
  exchange).
* `multiplier_order_four` — the vertex multiplier is an honest order-4 unit
  (`i⁴ = 1`, `i² = −1`): the #3942 4-cycle data at scalar level over `ℂ`.

Open remainder (unchanged): the functorial statement itself — exhibiting the
`TauRhoHodgeLift` instance (see `TauRhoHodgeLiftInterface`) for the actual
α_EM loop weights from the categorical τ-functor. This module supplies the
ℂ-level model on BOTH sides of that lift; it does not construct the functor.
No axiom; no instance fabricated; nothing wired; `1/(8π)` stays phase-4.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Complex.Basic

namespace QOU.Archimedean.VertexLocalTauModel

open Complex Matrix

/-- The degenerate-locus Hecke generator at `q = i`: the 2×2 Jordan block
with eigenvalue `i`. -/
noncomputable def sigma : Matrix (Fin 2) (Fin 2) ℂ := !![I, 1; 0, I]

/-- Its ρ-partner: the Jordan block at `q = −i`. -/
noncomputable def sigmaBar : Matrix (Fin 2) (Fin 2) ℂ := !![-I, 1; 0, -I]

/-- `σ` satisfies the Hecke relation at `q = i` (`q − q⁻¹ = 2i`):
`σ² = 2i·σ + 1`. The Jordan block IS an H₂(i)-module. -/
theorem hecke_relation_at_i : sigma * sigma = (2 * I) • sigma + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigma, Matrix.mul_apply, Fin.sum_univ_two] <;>
    ring_nf <;> simp [Complex.I_sq] <;> ring

/-- The degenerate confluence: `(σ − i·1)² = 0` — at `q = i` the two Hecke
eigenvalues `q, −q⁻¹` coincide and the module is a nontrivial Jordan block. -/
theorem jordan_nilpotent : (sigma - I • 1) * (sigma - I • 1) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigma, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]

/-- Non-semisimplicity: `σ` is not the scalar `i·1` — the degenerate module
has genuine nilpotent content; only its SEMISIMPLIFICATION acts by `i`. -/
theorem not_semisimple : sigma ≠ I • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  intro h
  have h01 := congrFun (congrFun h 0) 1
  simp [sigma] at h01

/-- **ρ carries the `q = i` module to the `q = −i` module** — the genuinely
ANTI-LINEAR statement (entrywise `starRingEnd ℂ`) whose combinatorial mirror
was the GInt vertex-family swap (#3942). This is the analytic type B1
identified for the Hodge pairing. -/
theorem rho_carries_module : sigma.map (starRingEnd ℂ) = sigmaBar := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigma, sigmaBar, Matrix.map_apply]

/-- The ρ-partner satisfies the conjugated Hecke relation (`q = −i`,
`q − q⁻¹ = −2i`): `σ̄² = −2i·σ̄ + 1`. -/
theorem hecke_relation_conj : sigmaBar * sigmaBar = (-(2 * I)) • sigmaBar + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigmaBar, Matrix.mul_apply, Fin.sum_univ_two, Complex.ext_iff] <;>
    ring_nf

/-- **Forced assignment over ℂ.** Any `f : ℂ → Bool` satisfying the
normalization `f i = true` and the ρ-intertwining `f (conj i) = ¬ f i`
agrees with the forced Hodge-shadow assignment on the whole degenerate pair
— the #3960 uniqueness transported from the GInt shadow to genuine `ℂ`
conjugation. -/
theorem shadow_unique_complex (f : ℂ → Bool)
    (hnorm : f I = true)
    (hint : f ((starRingEnd ℂ) I) = !(f I)) :
    f I = true ∧ f (-I) = false := by
  refine ⟨hnorm, ?_⟩
  rw [← Complex.conj_I, hint, hnorm]
  rfl

/-- The vertex multiplier is an honest order-4 unit: `i⁴ = 1`, `i² = −1` —
the #3942 4-cycle eigendata at scalar level over `ℂ`. -/
theorem multiplier_order_four : (I : ℂ) ^ 4 = 1 ∧ (I : ℂ) ^ 2 = -1 := by
  constructor
  · calc (I : ℂ) ^ 4 = (I ^ 2) ^ 2 := by ring
    _ = (-1 : ℂ) ^ 2 := by rw [Complex.I_sq]
    _ = 1 := by ring
  · exact Complex.I_sq

end QOU.Archimedean.VertexLocalTauModel
