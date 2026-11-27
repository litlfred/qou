import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.ParticleInteractions.confinement_frobenius_reciprocity

**Conjecture** ([`conj:confinement-frobenius-reciprocity`](../../../quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md)):
*confinement Frobenius reciprocity.*

Let `T ∈ H_n(q)` be a confined bound-state operator selected by the
operator-selection LP with primal optimum `T = ∑ᵢ x*ᵢ bᵢ` and dual optimum
`(y₀*, y*)`, where `{b₁, …, b_d}` is the NF basis, `G_{ij} = tr_M(bᵢ bⱼ)`
is the Frobenius Gram matrix, and the LP-active set is
`A*(T) = {i : y*ᵢ > 0}`.  Then for every observable `O ∈ H_n(q)` the physical
expectation value is the **Gram-inverse dual pairing weighted by LP-active
shadow prices**:

    ⟨O⟩_T = O(T) = ∑_{i,j ∈ A*(T)} u*ᵢ (G⁻¹)_{ij} ⟨O, bⱼ⟩ .

## What is proved here (2026-11-21)

Until this date the context class carried the reciprocity formula and the
LP facts as fields and `confinement_frobenius_reciprocity` returned them
(`⟨ctx.reciprocity, …⟩`), the self-assuming projection of AGENTS.md
§3b-cond item 5, while this docstring claimed the class carried no
conclusion and the proof ended in `sorry`. Neither was true.

The block's own proof sketch has two inputs:

* **linearity** — `⟨O⟩_T = Σⱼ x*ⱼ ⟨O, bⱼ⟩`, since `T = Σⱼ x*ⱼ bⱼ`;
* **stationarity** — `x*ⱼ = Σ_{i ∈ A*} (G⁻¹)ⱼᵢ u*ᵢ` on the active set and
  `x*ⱼ = 0` off it.

`confinement_frobenius_reciprocity` now carries exactly those as
hypotheses (with `G⁻¹` symmetric, as the inverse of a symmetric Gram
matrix is) and **derives** the master formula, together with
"active ⇔ positive shadow price" (from the definition of `A*` as a filter)
and "active set nonempty" (from a nonzero optimum supported on `A*`).

**Stationarity is not a consequence of the LP.** The KKT conditions of a
linear program are feasibility and complementary slackness; they do not
give `x* = G⁻¹ u*`, which is the stationarity condition of a quadratic
program. So the master formula is proved *conditional on* stationarity,
and stationarity is the open input. Strong duality for this LP is proved
in `lp_dual_stability.lean`.
-/

namespace QOU.ParticleInteractions

open Finset

/-- The LP-active set `A*(T) = {i : u*ᵢ > 0}`. -/
noncomputable def activeSet {d : ℕ} (u : Fin d → ℝ) : Finset (Fin d) :=
  Finset.univ.filter fun i => 0 < u i

theorem mem_activeSet {d : ℕ} (u : Fin d → ℝ) (i : Fin d) :
    i ∈ activeSet u ↔ 0 < u i := by
  simp [activeSet]

/-- **Confinement Frobenius reciprocity, conditional on stationarity**
    ([`conj:confinement-frobenius-reciprocity`]).

    Given the primal optimum `x`, shadow prices `u`, a symmetric dual-basis
    matrix `Ginv`, linearity of the expectation in `x`, and stationarity
    `x = Ginv u` on the active set (with `x = 0` off it), every observable's
    expectation is the Gram-inverse pairing over the active set; membership in
    the active set is positivity of the shadow price; and a nonzero optimum
    makes the active set nonempty. Derived, sorry-free. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, complementary slackness)
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/confinement-frobenius-reciprocity.md
theorem confinement_frobenius_reciprocity {d : ℕ} {Obs : Type*}
    (Ginv : Fin d → Fin d → ℝ) (x u : Fin d → ℝ)
    (pairing : Obs → Fin d → ℝ) (physExp : Obs → ℝ)
    (hsymm : ∀ i j, Ginv i j = Ginv j i)
    (hlin : ∀ O, physExp O = ∑ j, x j * pairing O j)
    (hstat : ∀ j ∈ activeSet u, x j = ∑ i ∈ activeSet u, Ginv j i * u i)
    (hsupp : ∀ j, j ∉ activeSet u → x j = 0)
    (hnontriv : ∃ i, x i ≠ 0) :
    (∀ O, physExp O = ∑ i ∈ activeSet u, ∑ j ∈ activeSet u,
        u i * Ginv i j * pairing O j) ∧
    (∀ i, i ∈ activeSet u ↔ 0 < u i) ∧
    (activeSet u).Nonempty := by
  refine ⟨fun O => ?_, mem_activeSet u, ?_⟩
  · rw [hlin O, ← Finset.sum_subset (Finset.subset_univ (activeSet u))
      (fun j _ hj => by rw [hsupp j hj, zero_mul])]
    calc ∑ j ∈ activeSet u, x j * pairing O j
        = ∑ j ∈ activeSet u, ∑ i ∈ activeSet u, Ginv j i * u i * pairing O j := by
          refine Finset.sum_congr rfl fun j hj => ?_
          rw [hstat j hj, Finset.sum_mul]
      _ = ∑ i ∈ activeSet u, ∑ j ∈ activeSet u, u i * Ginv i j * pairing O j := by
          rw [Finset.sum_comm]
          refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
          rw [hsymm j i]; ring
  · obtain ⟨i, hi⟩ := hnontriv
    by_contra h
    rw [Finset.not_nonempty_iff_eq_empty] at h
    exact hi (hsupp i (by simp [h]))

end QOU.ParticleInteractions
