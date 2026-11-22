import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Powerset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Group.Subgroup.Lattice
import Mathlib.Tactic.Abel

/-!
# Algebraic stratification of the Φ_q tower

Narrative anchor for the Hecke-tower / GS-filtration reformulation of
the Φ_q tower. The JSJ identification is a separate τ-image conjecture
(see `phi-q-tower-jsj-bridge`). The algebraic stratification is
conditional on pentagon ascension only.

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

    The statement does not depend on `[VolumeConjecture q]` or on any
    τ_arch hypothesis. It does depend on pentagon ascension: the field
    `pentagon_ascension` carries the vanishing form, and
    `phi_q_tower_algebraic_stratification_of_regrouping` gives the
    regrouping form.  Compare
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

/-! ### What pentagon ascension would have to mean

`def:phi-q-piece` gives the stratum summand as `Φ_q(x_S)` with
`Φ_q(x) = ∏_{m ≥ 0} (1 − q^m x)`.  Every finite truncation of that product
vanishes only at a resonance, `q^m x = 1` for some `m`; in particular
`Φ_q(0) = 1`.  So if `f S` is that summand, "`f S = 0` for `|S| ≥ 3`" is not a
general fact: it holds only when every triple's argument is resonant.  The
narrative (proof step 3) says instead that a level-3 term is *rewritten* into
lower factors plus a residual at jet level `n + 1`; that is a statement about
regrouping the tower, and the vanishing hypothesis of
`phi_q_tower_algebraic_stratification_of_pentagon` is the bookkeeping form of
it, not a consequence of the summand's definition.
-/

/-- The truncated quantum dilogarithm `∏_{m < N} (1 − q^m x)`. -/
def phiQTrunc {R : Type u} [CommRing R] (q x : R) (N : ℕ) : R :=
  ∏ m ∈ Finset.range N, (1 - q ^ m * x)

/-- **A truncated `Φ_q` vanishes only at a resonance**: over a field (or any
domain), `∏_{m < N} (1 − q^m x) = 0` iff `q^m x = 1` for some `m < N`. -/
theorem phiQTrunc_eq_zero_iff {R : Type u} [CommRing R] [IsDomain R] (q x : R) (N : ℕ) :
    phiQTrunc q x N = 0 ↔ ∃ m < N, q ^ m * x = 1 := by
  unfold phiQTrunc
  rw [Finset.prod_eq_zero_iff]
  simp only [Finset.mem_range, sub_eq_zero]
  exact ⟨fun ⟨m, hm, h⟩ => ⟨m, hm, h.symm⟩, fun ⟨m, hm, h⟩ => ⟨m, hm, h.symm⟩⟩

/-- `Φ_q(0) = 1` at every truncation: a stratum whose argument is `0`
contributes `1`, not `0`. -/
theorem phiQTrunc_zero {R : Type u} [CommRing R] (q : R) (N : ℕ) :
    phiQTrunc q 0 N = 1 := by
  simp [phiQTrunc]

/-! ### Pentagon ascension as a regrouping

The narrative's ascension says that a level-3 term rewrites as factors at
lower strata plus a residual at the next jet level. A Lean statement needs three
pieces:

* a correction `δ S` added to each stratum with `|S| ≤ 2`;
* a submodule `J` of residuals that belong to jet level `n + 1`;
* the hypothesis that the level-≥3 sum, minus the total correction, lies in `J`.

Under that hypothesis the mass agrees, modulo `J`, with the corrected strata
with `|S| ≤ 2`. Taking `δ = 0` and `J = ⊥` gives back the vanishing form
`phi_q_tower_algebraic_stratification_of_pentagon`.

The hypothesis alone carries no content: every sum satisfies it with `δ = 0`
and `J = ⊤`. Its content is the choice of `δ` and `J`. Building `J` needs the
tower across jet levels, and `δ` needs the Faddeev–Kashaev pentagon. Neither
exists in the corpus, so the regrouping stays a hypothesis.
-/

/-- Strata with `|S| ≤ 2` sum as `g ∅ + Σ_{|S|=1} g + Σ_{|S|=2} g`. -/
theorem sum_low_strata {R : Type u} [AddCommMonoid R] (U : Finset ℕ)
    (g : Finset ℕ → R) :
    ∑ S ∈ U.powerset.filter (fun S => S.card ≤ 2), g S
      = g ∅ + ∑ S ∈ U.powersetCard 1, g S + ∑ S ∈ U.powersetCard 2, g S := by
  classical
  have h := phi_q_tower_algebraic_stratification_of_pentagon U
    (fun S => if S.card ≤ 2 then g S else 0)
    (fun S _ hS => by simp only [if_neg (by omega : ¬ S.card ≤ 2)])
  rw [← Finset.sum_filter] at h
  rw [h]
  have e : ∀ k ≤ 2, ∑ S ∈ U.powersetCard k, (if S.card ≤ 2 then g S else 0)
      = ∑ S ∈ U.powersetCard k, g S := fun k hk =>
    Finset.sum_congr rfl fun S hS => by
      rw [(Finset.mem_powersetCard.mp hS).2, if_pos hk]
  rw [e 1 (by decide), e 2 (by decide)]
  simp

/-- **Algebraic stratification, given pentagon ascension as a regrouping.**
If the level-≥3 strata sum, minus a correction `δ` on the strata with
`|S| ≤ 2`, lies in the next-jet-level residual submodule `J`, then the full
mass is congruent mod `J` to the corrected low strata:

    Σ_{S ⊆ U} f S − ((f+δ) ∅ + Σ_{|S|=1} (f+δ) + Σ_{|S|=2} (f+δ)) ∈ J. -/
theorem phi_q_tower_algebraic_stratification_of_regrouping
    {R : Type u} [AddCommGroup R] (U : Finset ℕ) (f δ : Finset ℕ → R)
    (J : AddSubgroup R)
    (hreg : ∑ S ∈ U.powerset.filter (fun S => ¬ S.card ≤ 2), f S
        - ∑ S ∈ U.powerset.filter (fun S => S.card ≤ 2), δ S ∈ J) :
    ∑ S ∈ U.powerset, f S
      - ((f ∅ + δ ∅) + ∑ S ∈ U.powersetCard 1, (f S + δ S)
          + ∑ S ∈ U.powersetCard 2, (f S + δ S)) ∈ J := by
  classical
  rw [← sum_low_strata U (fun S => f S + δ S), Finset.sum_add_distrib,
    ← Finset.sum_filter_add_sum_filter_not U.powerset (fun S => S.card ≤ 2) f]
  convert hreg using 1
  abel

/-- The vanishing form is the case `δ = 0`, `J = ⊥` of the regrouping form. -/
theorem stratification_vanishing_of_regrouping
    {R : Type u} [AddCommGroup R] (U : Finset ℕ) (f : Finset ℕ → R)
    (hpent : ∀ S ⊆ U, 3 ≤ S.card → f S = 0) :
    ∑ S ∈ U.powerset, f S
      - (f ∅ + ∑ S ∈ U.powersetCard 1, f S + ∑ S ∈ U.powersetCard 2, f S) ∈
        (⊥ : AddSubgroup R) := by
  classical
  have h := phi_q_tower_algebraic_stratification_of_regrouping U f 0 ⊥ (by
    rw [AddSubgroup.mem_bot]
    simp only [Pi.zero_apply, Finset.sum_const_zero, sub_zero]
    refine Finset.sum_eq_zero fun S hS => ?_
    obtain ⟨hsub, hc⟩ := Finset.mem_filter.mp hS
    exact hpent S (Finset.mem_powerset.mp hsub) (by omega))
  simpa using h

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
