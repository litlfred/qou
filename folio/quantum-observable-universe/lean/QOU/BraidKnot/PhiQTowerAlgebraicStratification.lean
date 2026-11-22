import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Powerset

/-!
# Algebraic stratification of the Φ_q tower

Narrative anchor for the Hecke-tower / GS-filtration reformulation of
the Φ_q tower. The JSJ identification is a separate τ-image conjecture
(see `phi-q-tower-jsj-bridge`); the algebraic stratification stands
unconditionally.

The mass formula sums over algebraic strata indexed by subsets
`S ⊆ {0, …, n-2}`, computed entirely within `H_n(R, q)`:

  𝔪(ϱ) = ‖tr_M(ρ(β_∅))‖_F
       + Σ_{|S|=1} Φ_q(‖V̂_S‖_F)
       + Σ_{|S|=2} z² Φ_q(‖V̂_S‖_F).

No 3-manifold language; everything is a Laurent polynomial in
`q^{±1/2}` (or, generically, an element of `R = ℚ(q^{1/2})`).  The
norm `‖·‖_F` is the **Frobenius norm** valued in `R` — *not* the
Archimedean absolute value.

This stub upgrades the previous `: True := trivial` placeholder to
a class-axiomatised statement, so the proposition has actual Lean
content (the four-point identification of the mass formula with a
sum over GS-filtration strata) rather than being vacuous.

## References

- [prop:phi-q-tower-algebraic-stratification]
- [def:phi-q-piece]
- [prop:mass-endomorphism-tower]
- [prop:graded-markov-trace-from-gs-filtration]
- [prop:gb-spectral-sequence]
-/

namespace QOU.BraidKnot

universe u

/-- **Algebraic stratification of the Φ_q tower.**

    A `(R, q)`-valued formal datum recording the four-piece
    decomposition of the mass formula by GS-filtration depth.  Caller
    supplies:

    * `R` — ground ring (typically `R ⊇ ℤ[q^{±1/2}]`),
    * `q v : R` with `v² = q`,
    * `frobeniusNorm : R → R` — the categorical Frobenius norm on
      the Hecke algebra,
    * the four sums (`level0`, `level1`, `level2_adj`, `level2_non_adj`)
      that appear on the right-hand side of the mass formula,
    * the equality `mass = level0 + level1 + level2_adj + level2_non_adj`,
    * the audit hypothesis `pentagon_ascension : level≥3 = 0` saying
      that no level-3 contribution survives at fixed jet level `n`.

    The class field `level_zero_descended` records that the level-0
    summand is `‖tr_M(ρ(β_∅))‖_F` (the descended carrier); the field
    `levels_in_R` records that every level lives in the ground ring
    (no Archimedean leakage).  These witness the algebraic-side
    discipline.

    This statement is **unconditional**: it does *not* depend on
    `[VolumeConjecture q]` or any τ_arch hypothesis.  Compare
    `QOU.PhiQJSJ.bridge` (the conjectural Archimedean bridge), which
    *does* depend on `[VolumeConjecture q]`. -/
class PhiQTowerAlgebraicStratification (R : Type u) [CommRing R] where
  q : R
  v : R
  v_sq : v * v = q
  frobeniusNorm : R → R
  /-- Categorical mass `𝔪(ϱ)` of the vortex. -/
  mass : R
  /-- Level-0 (descended) summand `‖tr_M(ρ(β_∅))‖_F`. -/
  level0 : R
  /-- Level-1 summand `Σ_{|S|=1} Φ_q(‖V̂_S‖_F)`. -/
  level1 : R
  /-- Level-2 adjacent-pair summand `z² · Σ_{adj} Φ_q(‖V̂_i V̂_j‖_F)`. -/
  level2_adj : R
  /-- Level-2 non-adjacent-pair summand. -/
  level2_non_adj : R
  /-- The mass formula sums over the four levels. -/
  mass_sum :
    mass = level0 + level1 + level2_adj + level2_non_adj
  /-- The cumulative level-≥3 GS-filtration contribution to the mass.
      Pentagon ascension says this vanishes at fixed jet level `n`. -/
  level3plus : R
  /-- Pentagon ascension: the level-≥3 contribution vanishes.  This is
      the categorical content of `prop:mass-endomorphism-tower`
      §"Pentagon ascension".  Cf. gemini-code-assist review on
      PR #535. -/
  pentagon_ascension : level3plus = 0


/-! ### The stratification, proved

The class above *assumes* `mass = level0 + level1 + level2_adj + level2_non_adj`.
The content behind that field is a statement about sums over subsets: a mass
assembled as a sum over all strata `S ⊆ {0, …, n-2}` reduces to its `|S| ≤ 2`
strata exactly when every stratum with `|S| ≥ 3` contributes zero.  That
vanishing (pentagon ascension) is the hypothesis; the reduction is the theorem.
The per-stratum contribution `f S` is arbitrary, so the theorem covers the
block's choice `f ∅ = ‖tr_M(ρ(β_∅))‖_F`, `f S = Φ_q(‖V̂_S‖_F)` for `|S| = 1` and
`f S = z² Φ_q(‖V̂_S‖_F)` for `|S| = 2`.

Not proved here: that the `|S|`-grading coincides with the
`J^{|S|}/J^{|S|+1}` grading of the GS filtration, and pentagon ascension
itself.
-/

/-- **Algebraic stratification of the Φ_q tower, given pentagon ascension**
([`prop:phi-q-tower-algebraic-stratification`]).  For any finite index set `U`
(the generators `{0, …, n-2}`) and any per-stratum contribution `f`, if `f`
vanishes on every `S ⊆ U` with `|S| ≥ 3`, then

    Σ_{S ⊆ U} f S = f ∅ + Σ_{|S| = 1} f S + Σ_{|S| = 2} f S. -/
theorem phi_q_tower_algebraic_stratification_of_pentagon
    {R : Type u} [AddCommMonoid R] (U : Finset ℕ) (f : Finset ℕ → R)
    (hpent : ∀ S ⊆ U, 3 ≤ S.card → f S = 0) :
    ∑ S ∈ U.powerset, f S
      = f ∅ + ∑ S ∈ U.powersetCard 1, f S + ∑ S ∈ U.powersetCard 2, f S := by
  classical
  set g : ℕ → R := fun i => ∑ S ∈ U.powersetCard i, f S with hg
  have hbig : ∀ i, 3 ≤ i → g i = 0 := by
    intro i hi
    refine Finset.sum_eq_zero fun S hS => ?_
    obtain ⟨hsub, hcard⟩ := Finset.mem_powersetCard.mp hS
    exact hpent S hsub (hcard ▸ hi)
  have hout : ∀ i, U.card < i → g i = 0 := by
    intro i hi
    simp [hg, Finset.powersetCard_eq_empty.mpr hi]
  have hsplit : ∑ S ∈ U.powerset, f S = ∑ i ∈ Finset.range (U.card + 1), g i := by
    rw [Finset.powerset_card_disjiUnion, Finset.sum_disjiUnion]
  have h1 : ∑ i ∈ Finset.range (U.card + 1), g i = ∑ i ∈ Finset.range (U.card + 4), g i := by
    refine Finset.sum_subset (fun x hx => by simp only [Finset.mem_range] at hx ⊢; omega) fun i hi hni => ?_
    simp only [Finset.mem_range] at hi hni
    exact hout i (by omega)
  have h2 : ∑ i ∈ Finset.range 3, g i = ∑ i ∈ Finset.range (U.card + 4), g i := by
    refine Finset.sum_subset (fun x hx => by simp only [Finset.mem_range] at hx ⊢; omega) fun i hi hni => ?_
    simp only [Finset.mem_range] at hi hni
    exact hbig i (by omega)
  rw [hsplit, h1, ← h2, Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_one]
  simp [hg, Finset.powersetCard_zero]

/-! ### Removed 2026-08-30 — self-assuming projections

- `phi_q_tower_algebraic_stratification` — body was `s.mass_sum`: the conclusion was the projected field
  verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, which asserts the same proposition under the same hypotheses; only
the restatement goes. That is the vacuity ledger's recorded disposition for
this category — *"drop the pseudo-theorem and project the field at use sites"*
— and there were no use sites: each had **zero references anywhere in the
corpus**, including in this file. Bean `qou-z9ws`.
-/

end QOU.BraidKnot
