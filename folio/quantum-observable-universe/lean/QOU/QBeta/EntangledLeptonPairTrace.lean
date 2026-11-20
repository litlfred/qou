import QOU.Machinery.MarkovTraceOnHecke
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# The e⁻ν̄ pair as one braid word: what the Markov trace can see (bean `qou-99qc`, P2)

Identities behind `computations/qbeta/qbeta_entangled_lepton_pair_probe.py` and
`docs/audits/2026-11-20-beta-entangled-lepton-pair.md`, stated on the six-coordinate
normal-form model of `H₃(q)` in `QOU.Machinery.MarkovTraceOnHecke` (`H3.mulσ₀`,
`H3.mulσ₁`, `H3.trM`), over a generic commutative ring or field.

* `trefoil_trace`: the electron word `σ₀³` (`def:electron-knot`, the trefoil `T(2,3)`)
  has Markov trace `(h² + 1)·z + h`.
* `clasp_plus_trace`, `clasp_minus_trace`: a full twist `σ₁^{±2}` between a 2-strand
  element and a third strand multiplies the trace by a universal scalar
  `λ₊ = 1 + h·z` or `λ₋ = 1 + h² − h·z`, whatever the 2-strand element is. So linking
  the antineutrino strand to the electron by one clasp is invisible to the trace beyond
  that scalar: the trace does not know which particle the ν̄ is linked to.
* `lambdaPlus_conventionD`, `lambdaMinus_conventionD`, `trefoil_trace_conventionD`:
  the same at convention D, `z = q³/(q² + 1)`, `h = q − q⁻¹`.

Nothing here is fitted or evaluated at `q₀`.
-/

namespace QOU.QBeta.EntangledLeptonPair

open QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- The unit of `H₃` in normal-form coordinates. -/
def unitNF : Fin 6 → R := ![1, 0, 0, 0, 0, 0]

/-- The trefoil (electron) word `σ₀³`. -/
def trefoilNF (h : R) : Fin 6 → R := mulσ₀ h (mulσ₀ h (mulσ₀ h unitNF))

theorem trefoil_trace (z h : R) :
    trM z h (trefoilNF h) = (h ^ 2 + 1) * z + h := by
  simp [trefoilNF, unitNF, trM, TRM, mulσ₀, Fin.sum_univ_succ]
  ring

/-- Right multiplication by `σ₁⁻¹ = σ₁ − h`. -/
def mulσ₁inv (h : R) (v : Fin 6 → R) : Fin 6 → R := fun i => mulσ₁ h v i - h * v i

/-- An element of the 2-strand subalgebra `span{1, σ₀}`. -/
def twoStrand (a b : R) : Fin 6 → R := ![a, b, 0, 0, 0, 0]

theorem clasp_plus_trace (z h a b : R) :
    trM z h (mulσ₁ h (mulσ₁ h (twoStrand a b)))
      = (1 + h * z) * trM z h (twoStrand a b) := by
  simp [twoStrand, trM, TRM, mulσ₁, Fin.sum_univ_succ]
  ring

theorem clasp_minus_trace (z h a b : R) :
    trM z h (mulσ₁inv h (mulσ₁inv h (twoStrand a b)))
      = (1 + h ^ 2 - h * z) * trM z h (twoStrand a b) := by
  simp [twoStrand, mulσ₁inv, trM, TRM, mulσ₁, Fin.sum_univ_succ]
  ring

/-- The trefoil is a 2-strand element: `σ₀³ = h·1 + (h² + 1)·σ₀`. -/
theorem trefoilNF_eq (h : R) : trefoilNF h = twoStrand h (h ^ 2 + 1) := by
  funext i
  fin_cases i <;> simp [trefoilNF, unitNF, twoStrand, mulσ₀]
  ring

/-- The linked pair `σ₀³σ₁²`: trace `λ₊ · tr(e⁻)`. -/
theorem linked_pair_plus_trace (z h : R) :
    trM z h (mulσ₁ h (mulσ₁ h (trefoilNF h)))
      = (1 + h * z) * ((h ^ 2 + 1) * z + h) := by
  rw [trefoilNF_eq, clasp_plus_trace, ← trefoilNF_eq, trefoil_trace]

theorem linked_pair_minus_trace (z h : R) :
    trM z h (mulσ₁inv h (mulσ₁inv h (trefoilNF h)))
      = (1 + h ^ 2 - h * z) * ((h ^ 2 + 1) * z + h) := by
  rw [trefoilNF_eq, clasp_minus_trace, ← trefoilNF_eq, trefoil_trace]

section ConventionD

variable {K : Type*} [Field K]

theorem lambdaPlus_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    1 + (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) = (q ^ 4 + 1) / (q ^ 2 + 1) := by
  field_simp
  ring

theorem lambdaMinus_conventionD (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    1 + (q - q⁻¹) ^ 2 - (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1))
      = (q ^ 4 + 1) / (q ^ 2 * (q ^ 2 + 1)) := by
  field_simp
  ring

theorem trefoil_trace_conventionD (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    ((q - q⁻¹) ^ 2 + 1) * (q ^ 3 / (q ^ 2 + 1)) + (q - q⁻¹)
      = (q ^ 6 + q ^ 2 - 1) / (q * (q ^ 2 + 1)) := by
  field_simp
  ring

end ConventionD

end QOU.QBeta.EntangledLeptonPair
