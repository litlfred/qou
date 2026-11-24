/-
# B2 lift — the interface form of the primary conjecture, with its consequences derived

Bean `qou-tq20` (milestone `qou-b5qg`): the single remaining open wall of the
α_EM per-loop measure is the **B2 functorial lift** — that the categorical
τ-functor carries the fibre reality structure `ρ: q ↦ q̄` to the Hodge
conjugation of `H¹(Bring)`, with one loop's mode space landing on the
conjugate pair `H^{1,0} ⊕ H^{0,1}`.

This file (Mathlib now reachable via the restored `lake-cache` oleans) states
the lift as a **content-bearing primary-conjecture class** in its *interface
form* — the exact data the merged bricks B4b (#3977) and B5 (#3982) consume —
and DERIVES its consequences as genuine conditional theorems:

* `TauRhoHodgeLift` — the conjecture carrier (§3b-cond / §3b-tax): parameters
  are the loop's spectral weight matrices on the two Hodge components; the
  fields assert (i) hermiticity of the `H^{1,0}` weight (reality of the
  underlying Laplacian data) and (ii) that the `H^{0,1}` weight is its
  entrywise conjugate (τ carries ρ to the Hodge conjugation). **No instance
  is declared** — the conjecture is OPEN; the class axiomatises the lift's
  *inputs*, and every theorem below derives its conclusion from them.
* `trace_map_star_eq_of_isHermitian` — the ρ-split engine in Mathlib
  generality: for hermitian `A`, `(A.map star).trace = A.trace` (upgrade of
  B4b's concrete 3×3 sympy check to a proved general theorem).
* `TauRhoHodgeLift.equal_split` / `.doubled_total` — the conditional
  theorems: GIVEN the lift, the loop weight splits equally across the
  conjugate pair, and the selected channel carries exactly half the doubled
  total (the ½ of the per-loop measure, derived — not assumed — from the
  class fields).
* `half_a0_eq_inv_8pi` / `gauss_bonnet_bring_eq_inv_8pi` — the archimedean
  identities with a genuine `Real.pi`: `½·(1/(4π)) = 1/(8π) = |χ|/(4·Area)`
  on Bring (`χ = −6`, `Area = 12π`) — the rational shadow of #3982 upgraded
  to π-carrying real-number theorems.

Honesty (STRICT, §"Axiomatization is NOT a Proof"): the class has **no
instance** anywhere; nothing here derives the lift; the conditional theorems
do not close the conjecture and nothing wires `1/(8π)` to production — the
identification stays phase-4. The class fields encode the conjecture's
*hypotheses* (hermiticity + conjugation intertwining), never its conclusion
(the trace equalities are proved from them), per §3b-cond rule 5.

The full categorical statement (the τ-functor itself between the braided
category and the geometric side) remains beyond this interface form; the
interface pins exactly what the measure derivation needs from it, so any
future categorical construction discharges the wall by exhibiting an
instance — legitimately, by *proving* these two fields for the actual loop
weights.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.Archimedean.TauRhoHodgeLiftInterface

open Matrix

/-- The ρ-split engine, Mathlib generality: an entrywise-conjugated hermitian
matrix has the same trace — reality forces the conjugate component's spectral
weight to equal the original's. (Upgrade of B4b's concrete check.) -/
theorem trace_map_star_eq_of_isHermitian {n : Type*} [Fintype n] [DecidableEq n]
    {A : Matrix n n ℂ} (hA : A.IsHermitian) :
    (A.map (starRingEnd ℂ)).trace = A.trace := by
  have hmap : (A.map (starRingEnd ℂ)).trace = star A.trace := by
    simp [Matrix.trace, Matrix.diag, Matrix.map_apply, star_sum]
  rw [hmap, ← Matrix.trace_conjTranspose, hA.eq]

/-- **Primary conjecture — the B2 functorial lift, interface form.**

Parameters: `g` = complex dimension of `H^{1,0}(Bring)` (= 4), `W` = the
loop's spectral weight on `H^{1,0}`, `Wbar` = the weight on `H^{0,1}`.

Fields (the lift's content — its *inputs*, not its conclusions):
* `hermitian`: the `H^{1,0}` weight is hermitian — the loop weight comes from
  a real (self-adjoint) Laplacian-type operator, the B3 inheritance;
* `conjugated`: the `H^{0,1}` weight is the entrywise conjugate of the
  `H^{1,0}` weight — τ carries the fibre reality structure ρ to the Hodge
  conjugation (the B1 dictionary implemented functorially; its degenerate-
  locus shadow is FORCED, PR #3960 `shadow_unique`).

OPEN: no instance exists in the corpus. Exhibiting one for the actual α_EM
loop weights (from the categorical τ-functor) IS the remaining wall of the
per-loop measure `½·a₀ = 1/(8π)`. -/
class TauRhoHodgeLift (g : ℕ) (W Wbar : Matrix (Fin g) (Fin g) ℂ) : Prop where
  hermitian : W.IsHermitian
  conjugated : Wbar = W.map (starRingEnd ℂ)

namespace TauRhoHodgeLift

variable {g : ℕ} {W Wbar : Matrix (Fin g) (Fin g) ℂ}

/-- **Conditional theorem (equal split).** Given the lift, the loop weight
splits equally across the conjugate pair — the ½ is ρ-forced, derived from
the class fields (B4b, now in Mathlib generality). -/
theorem equal_split [h : TauRhoHodgeLift g W Wbar] : Wbar.trace = W.trace := by
  rw [h.conjugated]
  exact trace_map_star_eq_of_isHermitian h.hermitian

/-- **Conditional theorem (doubled total).** The selected channel (`H^{1,0}`,
the FORCED shadow assignment) carries exactly half the pair total: the q→1
one-loop restores the doubled unit — bean B4's target statement. -/
theorem doubled_total [TauRhoHodgeLift g W Wbar] :
    W.trace + Wbar.trace = 2 * W.trace := by
  rw [equal_split (W := W) (Wbar := Wbar)]
  ring

end TauRhoHodgeLift

/-- The measure identity with a genuine π: `½ · a₀ = 1/(8π)`. -/
theorem half_a0_eq_inv_8pi :
    (1 / 2 : ℝ) * (1 / (4 * Real.pi)) = 1 / (8 * Real.pi) := by
  have h := Real.pi_ne_zero
  field_simp
  ring

/-- The Gauss–Bonnet placement on Bring (`χ = −6`, `Area = 12π`):
`|χ| / (4·Area) = 1/(8π)` — the merged GB identity's Bring instance, with the
π carried honestly. -/
theorem gauss_bonnet_bring_eq_inv_8pi :
    |(-6 : ℝ)| / (4 * (12 * Real.pi)) = 1 / (8 * Real.pi) := by
  have h := Real.pi_ne_zero
  rw [abs_of_nonpos (by norm_num : (-6 : ℝ) ≤ 0)]
  field_simp
  ring

end QOU.Archimedean.TauRhoHodgeLiftInterface
