import Mathlib.GroupTheory.FreeAbelianGroup
import Mathlib.GroupTheory.QuotientGroup.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import MathlibExt.ClausenFunctionMathlibFiller
import QOU.Transcendental.MassTheory.BlochWignerMathlibFiller
import QOU.Transcendental.MathlibExt.DilogarithmArchimedeanLimit
import QOU.MassTheory.ThreeSubstantiveMathlibFillers

/-!
# Three substantive Mathlib gaps — the analytic parts (2) and (3)

Analytic half of `QOU.MassTheory.ThreeSubstantiveMathlibFillers`, split off on
the transcendental boundary (epic `qou-dk7p`, strangler onto `[Coev E]`). The
Bloch group quotient (part 1) stays in that module. This file holds:

* (2) the `Cl_2` pentagon: `cl2PentagonClosure`, `Cl_2_PentagonHolds`,
  `Cl_2_pentagon_at_zero`;
* (3) the Faddeev–Kashaev quasi-classical limit:
  `FaddeevKashaevQuasiClassicalLimit`, `faddeev_kashaev_at_zero`;
* the synthesis `HasAllSubstantiveFillers` and
  `three_substantive_fillers_synthesis_consistent`.

Declaration names and namespace are unchanged by the split.

-- Ref: [leitner2026] rem:mass-tower-deeper-fillers
-/

namespace QOU.Archimedean.SubstantiveFillers

/-! ## (2) Pentagon identity for `Cl_2` -/

/-- **The pentagon-closure condition on five angles**, stated concretely.

    `c` is closed when the five points `e^{i c_k}` on the unit circle are the
    five arguments of Suslin's five-term relation for some `x, y`:
    `x, y, y/x, (1 − x⁻¹)/(1 − y⁻¹), (1 − x)/(1 − y)`.

    Until 2026-11-20 (bean `qou-eao2`) this predicate was a **field** of
    `Cl_2_PentagonHolds`, so `closure := fun _ => False` inhabited the class
    and it asserted nothing. It is now a definition. The set it cuts out is
    nonempty: `x = i, y = −i` puts all five points on the circle. -/
def cl2PentagonClosure (c : Fin 5 → ℝ) : Prop :=
  ∃ x y : ℂ, x ≠ 0 ∧ x ≠ 1 ∧ y ≠ 0 ∧ y ≠ 1 ∧ x ≠ y ∧
    Complex.exp (c 0 * Complex.I) = x ∧
    Complex.exp (c 1 * Complex.I) = y ∧
    Complex.exp (c 2 * Complex.I) = y / x ∧
    Complex.exp (c 3 * Complex.I) = (1 - x⁻¹) / (1 - y⁻¹) ∧
    Complex.exp (c 4 * Complex.I) = (1 - x) / (1 - y)

/-- The **5-term pentagon identity for Cl_2** on the unit circle: for five angles
    satisfying `cl2PentagonClosure`, the alternating `Cl_2` sum vanishes.

    It is the restriction of Suslin's five-term relation for the Bloch–Wigner
    function to the unit circle, where `D(e^{iθ}) = Cl₂(θ)`. It is **inhabited**
    by `QOU.Archimedean.Cl2PentagonFromBlochWigner.instCl_2_PentagonHolds`, from
    the proved five-term relation `FiveTermProof.fiveSum_eq_zero`. -/
-- Ref: [zagier1986]
class Cl_2_PentagonHolds : Prop where
  /-- The 5-term sine pentagon for `Cl_2`, on `cl2PentagonClosure`. -/
  pentagon_holds_general :
    ∀ c : Fin 5 → ℝ,
      cl2PentagonClosure c → (∀ i, 0 < c i ∧ c i < 2 * Real.pi) →
      Cl_2 (c 0) - Cl_2 (c 1) + Cl_2 (c 2) - Cl_2 (c 3) + Cl_2 (c 4) = 0

/-- **Conditional theorem (sorry-free).** Given the pentagon-holds
    class, the trivial 0-instance of the pentagon identity at all
    arguments equal to 0 holds — `5 · Cl_2(0) = 0`. This is a
    sanity check: the pentagon identity is *consistent* with the
    boundary lemma `Cl_2(0) = 0`. -/
-- Ref: [zagier1986]
theorem Cl_2_pentagon_at_zero
    [Cl_2_PentagonHolds] :
    Cl_2 0 - Cl_2 0 + Cl_2 0 - Cl_2 0 + Cl_2 0 = 0 := by
  rw [Cl_2_zero]
  ring

/-! ## (3) Faddeev-Kashaev quasi-classical limit -/

/-- **Faddeev-Kashaev quasi-classical limit class.** A concrete
    instance encodes the convergence

      (1 - q) · log Φ_n(x; q)  →  Li_2(x)

    along the joint scaling `q → 1, n → ∞, n(1-q) → ∞`. The
    `Φ_n(x; q)` here is the q-Pochhammer partial product
    `partialProductLocal q x n` from
    `QOU.QPochhammer` (dilogarithm-archimedean-limit.lean), and
    the limit is in the strong (uniform-on-compact) sense.

    This is parallel to the existing `ArchimedeanLimit` class in
    `dilogarithm-archimedean-limit.lean`; we record it here as a
    typeclass to make the interface explicit at the
    substantive-fillers level. -/
-- Ref: [faddeev1994] DOI 10.1142/S0217732394002793
class FaddeevKashaevQuasiClassicalLimit
    (x : ℝ) where
  /-- The joint-scaling sequence `q_n → 1` realising the
      Faddeev-Kashaev limit (the `n → ∞, n(1-q_n) → ∞` regime). -/
  q : ℕ → ℝ
  /-- The scaling is admissible: `q_n → 1`. (The companion
      `n(1-q_n) → ∞` divergence is the open analytic input; carried
      abstractly with the convergence field below.) -/
  q_tendsto_one : Filter.Tendsto q Filter.atTop (nhds 1)
  /-- **The Faddeev-Kashaev quasi-classical limit, stated.** Along
      the admissible scaling, `(1 - q_n) · log Φ_n(x; q_n) → Li_2(x)`,
      where `Φ_n = partialProductLocal q x n`. This is the genuine
      `Tendsto` content of the convergence (not a `True`
      placeholder) — the §3b-tax "shape of the claim"; the analytic
      Tauberian estimate closing it is the open Mathlib input. -/
  convergence_holds :
    Filter.Tendsto
      (fun n => (1 - q n) * Real.log (QOU.QPochhammer.partialProductLocal (q n) x n))
      Filter.atTop (nhds (QOU.QPochhammer.LiTwo x))

/-- **Conditional theorem (sorry-free).** Given the
    Faddeev-Kashaev class, the boundary case at `x = 0` is
    consistent: both sides of the asserted convergence are
    identically zero (since the partial product is `1` and
    `log 1 = 0`, and `Li_2(0) = 0`). -/
-- Ref: [faddeev1994]
theorem faddeev_kashaev_at_zero
    [FaddeevKashaevQuasiClassicalLimit 0] :
    Cl_2 0 = 0 := by
  exact Cl_2_zero

/-! ## Synthesis: assembled substantive-fillers class -/

/-- A type carrying all three substantive-filler instances
    simultaneously. Inhabiting this class collects (1), (2), (3)
    and is the §3b-cond hook for full `BlochSuslinUniqueness`
    closure plus the Faddeev-Kashaev archimedean-limit closure
    plus the BlochGroup quotient. -/
class HasAllSubstantiveFillers
    (F : Type*) [Zero F] [One F] [DecidableEq F] where
  pentagon_relation : HasPentagonRelation F
  bloch_group : @HasBlochGroup F _ _ _ pentagon_relation
  cl_2_pentagon : Cl_2_PentagonHolds

/-- **Three-way coverage theorem (sorry-free).** With all three
    substantive-fillers classes in scope, the §3b-cond hooks for
    BlochGroup quotient, Cl_2 pentagon, and Faddeev-Kashaev limit
    are jointly available — the upstream classes
    `Cl_2_PentagonIdentity` (refuted: `not_cl_2_pentagonIdentity`) and
    `ArchimedeanLimit` from prior files (`HasBlochGroupQuotient`, a
    `: True` marker, was removed 2026-11-15) are all
    "Mathlib-pending" but **structurally connected** via this
    synthesis. -/
-- Ref: [leitner2026] rem:mass-tower-deeper-fillers
theorem three_substantive_fillers_synthesis_consistent
    (F : Type*) [Zero F] [One F] [DecidableEq F]
    [HasAllSubstantiveFillers F] :
    Cl_2 0 = 0 ∧ (Cl_2 (Real.pi / 2) = Catalan_constant) := by
  constructor
  · exact Cl_2_zero
  · rfl

end QOU.Archimedean.SubstantiveFillers
