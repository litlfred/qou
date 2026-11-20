import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import QOU.Photon
import QOU.BraidsAndKnots.NucleonWeightSpaceTraces

/-!
# No element of `H₃(q)` breaks u↔d on the nucleon weight spaces

Level-2 Jimbo braiding on `(C²)^{⊗3}`, basis `e₁ = u`, `e₂ = d`, `h = q - q⁻¹`, written here
with `qi` for `q⁻¹` and the single hypothesis `q * qi = 1` (generic `CommRing R`, §7c: no
field, no ordering, no `q² + 1 ≠ 0`).

On the proton-type weight space `W_p` (two `u`) the generators act by `A₁, A₂`; on the
neutron-type weight space `W_n` (one `u`) they act by `A₂, A₁` — the same two matrices with
`σ₀ ↔ σ₁` swapped (`NucleonWeightSpaceTraces.B₁ = A₂`, `B₂ = A₁`; see `B₁_eq`, `B₂_eq`).
The half-twist `Δ = σ₀σ₁σ₀` swaps the generators by conjugation (the braid relation), and
`Δ` is invertible with inverse `σ₀⁻¹σ₁⁻¹σ₀⁻¹`, `σᵢ⁻¹ = σᵢ - h` (the Hecke relation). Hence the
`W_n` representation of every element of the free algebra on `σ₀, σ₁` is the `Δ`-conjugate
of its `W_p` representation, and the two plain traces agree (`trace_ρn_eq_trace_ρp`).

Every element of `H₃(q)` — every braid word with inverses, the pair-production vertex
`V = σ₀σ₁⁻¹`, the four-term photon `γ(φ)` at any colour weights (`photon_symmetric`) — is
the image of a free-algebra element, so none of them separates `u` from `d` under the
plain weight-space trace. This extends `NucleonWeightSpaceTraces.trace_word_eq` (positive
words, over a field, with `q² + 1 ≠ 0`) to the whole algebra over any commutative ring.

The convention-D trace `Tr(K^{⊗3}·)/[2]³` weights `W_p` by `q` and `W_n` by `q⁻¹`, so its
flavour split is `(qi·tr_{W_n} − q·tr_{W_p}) = −h·tr_{W_p}` for every element
(`flavour_split`): any n/p difference it shows is the trace's own `K`-weighting times a
symmetric trace, not a property of the element. For the vertex, `tr_{W_p}(V) = −h²`
(`trace_vertex`).

Probe: `computations/probes/gg_twist_vertex_channel/gg_twist_vertex_channel_np_probe.py`
(ε-L1V, bean `qou-99qc`), which also checks the 32-dimensional ε-L1 multiplicity-trace
functional by a basis check; that functional is not formalised here.

-- Ref: [leitner2026] predicted-spectra, def:photon
-/

namespace QOU.BraidsAndKnots.HeckeWeightSpaceSymmetry

open Matrix

variable {R : Type*} [CommRing R]

variable {R : Type*} [CommRing R]

abbrev M3 (R : Type*) [CommRing R] := Matrix (Fin 3) (Fin 3) R

def A₁ (q qi : R) : M3 R := !![q, 0, 0; 0, 0, 1; 0, 1, q - qi]
def A₂ (q qi : R) : M3 R := !![0, 1, 0; 1, q - qi, 0; 0, 0, q]

theorem hecke₁ (q qi : R) (hq : q * qi = 1) :
    A₁ q qi * (A₁ q qi - (q - qi) • 1) = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A₁, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    linear_combination hq

theorem hecke₁' (q qi : R) (hq : q * qi = 1) :
    (A₁ q qi - (q - qi) • 1) * A₁ q qi = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A₁, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    linear_combination hq

theorem hecke₂ (q qi : R) (hq : q * qi = 1) :
    A₂ q qi * (A₂ q qi - (q - qi) • 1) = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A₂, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    linear_combination hq

theorem hecke₂' (q qi : R) (hq : q * qi = 1) :
    (A₂ q qi - (q - qi) • 1) * A₂ q qi = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A₂, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    linear_combination hq

theorem braid (q qi : R) (hq : q * qi = 1) :
    A₁ q qi * A₂ q qi * A₁ q qi = A₂ q qi * A₁ q qi * A₂ q qi := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A₁, A₂, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | ring1 | linear_combination (q - qi) * hq | linear_combination (qi - q) * hq

/-! ### Δ = A₁A₂A₁ swaps the generators by conjugation -/

theorem cancel_left {x y z : M3 R} (h : x * y = 1) : x * (y * z) = z := by
  rw [← mul_assoc, h, one_mul]

/-- `Δ = σ₀σ₁σ₀` on the weight space. -/
def Δ (q qi : R) : M3 R := A₁ q qi * A₂ q qi * A₁ q qi
/-- Its inverse `σ₀⁻¹σ₁⁻¹σ₀⁻¹`, with `σᵢ⁻¹ = σᵢ - h`. -/
def Δinv (q qi : R) : M3 R :=
  (A₁ q qi - (q - qi) • 1) * (A₂ q qi - (q - qi) • 1) * (A₁ q qi - (q - qi) • 1)

theorem Δ_mul_Δinv (q qi : R) (hq : q * qi = 1) : Δ q qi * Δinv q qi = 1 := by
  simp only [Δ, Δinv, mul_assoc, cancel_left (hecke₁ q qi hq), cancel_left (hecke₂ q qi hq),
    hecke₁ q qi hq]

theorem Δinv_mul_Δ (q qi : R) (hq : q * qi = 1) : Δinv q qi * Δ q qi = 1 := by
  simp only [Δ, Δinv, mul_assoc, cancel_left (hecke₁' q qi hq), cancel_left (hecke₂' q qi hq),
    hecke₁' q qi hq]

theorem Δ_conj₁ (q qi : R) (hq : q * qi = 1) :
    Δ q qi * A₁ q qi * Δinv q qi = A₂ q qi := by
  have h1 : Δ q qi * A₁ q qi = A₂ q qi * Δ q qi := by
    simp only [Δ]
    calc A₁ q qi * A₂ q qi * A₁ q qi * A₁ q qi = (A₁ q qi * A₂ q qi * A₁ q qi) * A₁ q qi := rfl
      _ = (A₂ q qi * A₁ q qi * A₂ q qi) * A₁ q qi := by rw [braid q qi hq]
      _ = A₂ q qi * (A₁ q qi * A₂ q qi * A₁ q qi) := by simp only [mul_assoc]
  rw [h1, mul_assoc, Δ_mul_Δinv q qi hq, mul_one]

theorem Δ_conj₂ (q qi : R) (hq : q * qi = 1) :
    Δ q qi * A₂ q qi * Δinv q qi = A₁ q qi := by
  have h1 : Δ q qi * A₂ q qi = A₁ q qi * Δ q qi := by
    simp only [Δ]
    calc A₁ q qi * A₂ q qi * A₁ q qi * A₂ q qi = A₁ q qi * (A₂ q qi * A₁ q qi * A₂ q qi) := by
            simp only [mul_assoc]
      _ = A₁ q qi * (A₁ q qi * A₂ q qi * A₁ q qi) := by rw [braid q qi hq]
  rw [h1, mul_assoc, Δ_mul_Δinv q qi hq, mul_one]

/-! ### Every element of the algebra generated by σ₀, σ₁ -/

/-- Generator assignment `0 ↦ X, 1 ↦ Y`. -/
def gens (X Y : M3 R) : Fin 2 → M3 R := ![X, Y]

/-- `σ₀ ↦ A₁, σ₁ ↦ A₂` (the `(2,1)` weight space). -/
noncomputable def ρp (q qi : R) : FreeAlgebra R (Fin 2) →ₐ[R] M3 R :=
  FreeAlgebra.lift R (gens (A₁ q qi) (A₂ q qi))
/-- `σ₀ ↦ A₂, σ₁ ↦ A₁` (the `(1,2)` weight space). -/
noncomputable def ρn (q qi : R) : FreeAlgebra R (Fin 2) →ₐ[R] M3 R :=
  FreeAlgebra.lift R (gens (A₂ q qi) (A₁ q qi))

theorem ρn_eq_conj (q qi : R) (hq : q * qi = 1) (x : FreeAlgebra R (Fin 2)) :
    ρn q qi x = Δ q qi * ρp q qi x * Δinv q qi := by
  induction x using FreeAlgebra.induction with
  | grade0 r =>
    rw [AlgHom.commutes, AlgHom.commutes, Algebra.algebraMap_eq_smul_one, mul_smul_comm,
      mul_one, smul_mul_assoc, Δ_mul_Δinv q qi hq]
  | grade1 i =>
    fin_cases i
    · simp [ρn, ρp, gens, Δ_conj₁ q qi hq]
    · simp [ρn, ρp, gens, Δ_conj₂ q qi hq]
  | mul a b ha hb =>
    rw [map_mul, ha, hb, map_mul]
    simp only [mul_assoc, cancel_left (Δinv_mul_Δ q qi hq)]
  | add a b ha hb =>
    rw [map_add, ha, hb, map_add, mul_add, add_mul]

/-- **u↔d symmetry of every Hecke element.** -/
theorem trace_ρn_eq_trace_ρp (q qi : R) (hq : q * qi = 1) (x : FreeAlgebra R (Fin 2)) :
    trace (ρn q qi x) = trace (ρp q qi x) := by
  rw [ρn_eq_conj q qi hq, Matrix.trace_mul_cycle, Δinv_mul_Δ q qi hq, one_mul]


/-! ### The photon -/

/-- `σ₁` on `W_p` as a unit (inverse `A₂ - h`). -/
def unitA₂ (q qi : R) (hq : q * qi = 1) : (M3 R)ˣ :=
  ⟨A₂ q qi, A₂ q qi - (q - qi) • 1, hecke₂ q qi hq, hecke₂' q qi hq⟩
/-- `σ₁` on `W_n` as a unit (inverse `A₁ - h`). -/
def unitA₁ (q qi : R) (hq : q * qi = 1) : (M3 R)ˣ :=
  ⟨A₁ q qi, A₁ q qi - (q - qi) • 1, hecke₁ q qi hq, hecke₁' q qi hq⟩

/-- The photon `γ(φ)` as a free-algebra element, with `σ₁⁻¹` written `σ₁ - h`. -/
noncomputable def freePhoton (q qi : R) (c : QOU.Photon.Colour R) : FreeAlgebra R (Fin 2) :=
  1 + c.phi0 • FreeAlgebra.ι R 0 + c.phi1 • FreeAlgebra.ι R 1 +
    c.phi01 • (FreeAlgebra.ι R 0 * (FreeAlgebra.ι R 1 - algebraMap R _ (q - qi)))

theorem ρp_freePhoton (q qi : R) (hq : q * qi = 1) (c : QOU.Photon.Colour R) :
    ρp q qi (freePhoton q qi c) = QOU.Photon.photon (A₁ q qi) (unitA₂ q qi hq) c := by
  simp [ρp, freePhoton, gens, QOU.Photon.photon, QOU.Photon.vertex, unitA₂,
    Algebra.algebraMap_eq_smul_one]

theorem ρn_freePhoton (q qi : R) (hq : q * qi = 1) (c : QOU.Photon.Colour R) :
    ρn q qi (freePhoton q qi c) = QOU.Photon.photon (A₂ q qi) (unitA₁ q qi hq) c := by
  simp [ρn, freePhoton, gens, QOU.Photon.photon, QOU.Photon.vertex, unitA₁,
    Algebra.algebraMap_eq_smul_one]

/-- **The photon does not break u↔d**: at every colour `(φ₀, φ₁, φ₀₁)` the photon has the
same plain trace on the proton-type and neutron-type weight spaces. -/
theorem photon_symmetric (q qi : R) (hq : q * qi = 1) (c : QOU.Photon.Colour R) :
    trace (QOU.Photon.photon (A₂ q qi) (unitA₁ q qi hq) c) =
      trace (QOU.Photon.photon (A₁ q qi) (unitA₂ q qi hq) c) := by
  rw [← ρn_freePhoton q qi hq, ← ρp_freePhoton q qi hq, trace_ρn_eq_trace_ρp q qi hq]

/-- **The vertex `V = σ₀σ₁⁻¹` does not break u↔d.** -/
theorem vertex_symmetric (q qi : R) (hq : q * qi = 1) :
    trace (QOU.Photon.vertex (A₂ q qi) (unitA₁ q qi hq)) =
      trace (QOU.Photon.vertex (A₁ q qi) (unitA₂ q qi hq)) := by
  have := photon_symmetric q qi hq ⟨0, 0, 1⟩
  simpa [QOU.Photon.photon] using this

/-- `tr_{W_p}(V) = −h²`. -/
theorem trace_vertex (q qi : R) (hq : q * qi = 1) :
    trace (QOU.Photon.vertex (A₁ q qi) (unitA₂ q qi hq)) = -(q - qi) ^ 2 := by
  rw [QOU.Photon.vertex, Matrix.trace_fin_three]
  simp [unitA₂, A₁, A₂, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply]
  ring

/-- **Flavour split of the convention-D weighting.** `K^{⊗3}` acts by `q` on `W_p` and by
`q⁻¹` on `W_n`; for every element the weighted difference is `−h` times the symmetric trace. -/
theorem flavour_split (q qi : R) (hq : q * qi = 1) (x : FreeAlgebra R (Fin 2)) :
    qi * trace (ρn q qi x) - q * trace (ρp q qi x) = -(q - qi) * trace (ρp q qi x) := by
  rw [trace_ρn_eq_trace_ρp q qi hq]; ring

/-! ### Agreement with `NucleonWeightSpaceTraces` -/

theorem B₁_eq {K : Type*} [Field K] (q : K) :
    NucleonWeightSpaceTraces.B₁ q = A₂ q q⁻¹ := rfl
theorem B₂_eq {K : Type*} [Field K] (q : K) :
    NucleonWeightSpaceTraces.B₂ q = A₁ q q⁻¹ := rfl
theorem A₁_eq {K : Type*} [Field K] (q : K) :
    NucleonWeightSpaceTraces.A₁ q = A₁ q q⁻¹ := rfl
theorem A₂_eq {K : Type*} [Field K] (q : K) :
    NucleonWeightSpaceTraces.A₂ q = A₂ q q⁻¹ := rfl

end QOU.BraidsAndKnots.HeckeWeightSpaceSymmetry
