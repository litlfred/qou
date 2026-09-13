/-
QOU.MobiusMutualChannel — the MUTUAL O'Hara channel is genuinely integrable,
and getting it does NOT require O'Hara's theorem.

Bean `qou-pc85`, under `qou-o6ml` route (2) (Möbius / knot-energy class).

WHY THIS FILE EXISTS
--------------------
`QOU.MobiusEnergy` builds the O'Hara integrand and proves its pointwise facts
— non-negativity derived from `chord_le_arc`, unconditional positivity of the
mutual term on distinct components — and then stops, saying three times in its
own docstrings that the integral "needs measure theory this file does not set
up".

The reason that looked expensive is the DIAGONAL. On one component, as `s → t`
the ambient distance goes to zero and `1/|γ(s) − γ(t)|²` blows up; that the
intrinsic subtraction still leaves something finite is **O'Hara's theorem**, a
genuine analysis result and not infrastructure.

FORMALIZE-FIRST PRUNE: THE CHANNEL WE NEED HAS NO DIAGONAL
-----------------------------------------------------------
Bean `qou-o6ml` owns only the **pairwise/linking** channel — the self term
belongs to `qou-bn8e` ("the self-energy question stays in `bn8e`; this bean
owns only the pairwise/linking channel"). And the mutual integrand carries no
diagonal at all: `LinkEmbedding.disjoint` says distinct components never meet.

So the singular behaviour that makes O'Hara hard **never arises in the channel
the bean needs**, and the mutual term is integrable by the ordinary route:
bounded + measurable on a finite-measure domain. That is the whole content of
this file, and it is why route (2) is cheaper than its reputation.

WHAT IS PROVED, AND WHAT IS ASSUMED
------------------------------------
1. `mutualIntegrand_le_of_uniformSeparation` — the bound `1/δ²`. Pure algebra.
2. `disjoint_not_imp_uniformSeparation` — **`disjoint` does NOT give the
   bound.** A concrete two-component link whose separation is positive
   everywhere and has infimum zero. This is why `HasUniformSeparation` is
   carried as a hypothesis rather than derived, and it is the guard against a
   later "simplification" that drops it.
3. `mutualIntegrand_intervalIntegrable` — the real Mathlib conclusion:
   `IntervalIntegrable` for the mutual integrand, from the bound plus
   measurability.
4. `innerPairEnergy` and `innerPairEnergy_le` — an actual `intervalIntegral`,
   with the bound carried through it.

ASSUMED, and deliberately visible: `HasUniformSeparation` (a uniform gap) and
measurability of `sep` in the integration variable. For a genuine link — finitely
many disjoint compact components — the uniform gap is the distance between
disjoint compacts and is automatic; it does **not** follow from the pointwise
positivity `LinkEmbedding.disjoint` supplies, which is exactly what theorem 2
proves. Neither hypothesis is the conclusion in disguise.

NOT DONE HERE, and not claimed: the **self/diagonal** channel. That still needs
O'Hara's theorem, it is `qou-bn8e`'s object rather than this bean's, and nothing
below weakens or sidesteps it.
-/
import QOU.MobiusEnergy
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

namespace QOU

open MeasureTheory

namespace LinkEmbedding

variable {M : Type*} {n : ℕ}

/-! ## §1  Uniform separation — the hypothesis the mutual channel actually needs -/

/-- A link has **uniform separation `δ`** when distinct components stay at least
    `δ` apart, uniformly in both parameters.

    For a genuine link — finitely many disjoint *compact* components — this is
    the distance between disjoint compacts and is automatic. It is carried here
    as an explicit hypothesis because `LinkEmbedding.disjoint` supplies only
    *pointwise* positivity, and `disjoint_not_imp_uniformSeparation` below
    proves that the two are genuinely different. -/
def HasUniformSeparation (L : LinkEmbedding M n) (δ : ℝ) : Prop :=
  0 < δ ∧ ∀ i j, i ≠ j → ∀ s t, δ ≤ L.sep i s j t

/-- **The mutual integrand is bounded on distinct components.**

    This is the whole prune: `1/sep²` is bounded because `sep` is bounded
    *below*, and `sep` is bounded below because the components are disjoint.
    No diagonal, no singularity, no O'Hara theorem. -/
theorem mutualIntegrand_le_of_uniformSeparation (L : LinkEmbedding M n)
    {δ : ℝ} (hδ : HasUniformSeparation L δ) {i j : Fin n} (hij : i ≠ j)
    (s t : ℝ) : L.mutualIntegrand i j s t ≤ 1 / δ ^ 2 := by
  obtain ⟨hδpos, hsep⟩ := hδ
  have hle : δ ≤ L.sep i s j t := hsep i j hij s t
  have hpos : 0 < L.sep i s j t := lt_of_lt_of_le hδpos hle
  have hsq : δ ^ 2 ≤ L.sep i s j t ^ 2 := by nlinarith
  unfold mutualIntegrand
  exact one_div_le_one_div_of_le (by positivity) hsq

/-- The mutual integrand is non-negative on distinct components — the lower
    half of the bound, recorded so `‖·‖` can be discharged below. -/
theorem mutualIntegrand_nonneg_of_ne (L : LinkEmbedding M n) {i j : Fin n}
    (hij : i ≠ j) (s t : ℝ) : 0 ≤ L.mutualIntegrand i j s t :=
  le_of_lt (L.mutualIntegrand_pos_of_ne hij s t)

end LinkEmbedding

/-! ## §2  `disjoint` does NOT give the bound

The hypothesis above is strictly stronger than what `LinkEmbedding` carries.
This section proves it, by exhibiting a link that is disjoint everywhere and
uniformly separated nowhere.

Without this, a later reader could "simplify" `HasUniformSeparation` away by
appealing to `disjoint`, and every bound below would silently become vacuous —
the precise failure mode that produced four vacuous declarations in
`QOU.MobiusEnergy` before 2026-08-30. -/

namespace MobiusMutualChannel

variable {M : Type*}

/-- A degenerate knot embedding: one point, all distances zero. Used only to
    populate the components of the counterexample link, whose content is in its
    `sep` field. -/
def pointKnot (m : M) : KnotEmbedding M where
  curve := fun _ => m
  arcLengthDist := fun _ _ => 0
  arcLength_symm := fun _ _ => rfl
  arcLength_nonneg := fun _ _ => le_refl 0
  ambientDist := fun _ _ => 0
  ambient_symm := fun _ _ => rfl
  ambient_nonneg := fun _ _ => le_refl 0
  chord_le_arc := fun _ _ => le_refl 0

/-- Separation that is **positive everywhere and has infimum zero**: it decays
    as either parameter runs off to infinity. Symmetric by construction. -/
noncomputable def decayingSep (s t : ℝ) : ℝ := 1 / (1 + |s| + |t|)

theorem decayingSep_pos (s t : ℝ) : 0 < decayingSep s t := by
  unfold decayingSep
  have : 0 < 1 + |s| + |t| := by positivity
  positivity

theorem decayingSep_symm (s t : ℝ) : decayingSep s t = decayingSep t s := by
  unfold decayingSep; ring_nf

/-- The counterexample link: two components, disjoint everywhere, separation
    decaying to zero. -/
noncomputable def shrinkingLink (m : M) : LinkEmbedding M 2 where
  component := fun _ => pointKnot m
  sep := fun i s j t => if i = j then 0 else decayingSep s t
  sep_symm := by
    intro i s j t
    by_cases h : i = j
    · subst h; simp
    · rw [if_neg h, if_neg (Ne.symm h), decayingSep_symm]
  sep_nonneg := by
    intro i s j t
    by_cases h : i = j
    · simp [h]
    · rw [if_neg h]; exact le_of_lt (decayingSep_pos s t)
  disjoint := by
    intro i j hij s t
    rw [if_neg hij]
    exact decayingSep_pos s t
  sep_self := by intro i s t; simp [pointKnot]

/-- **`disjoint` does not imply `HasUniformSeparation`.**

    The `shrinkingLink` satisfies every `LinkEmbedding` field — in particular
    `disjoint`, so its mutual integrand is positive everywhere — and admits no
    uniform gap whatsoever.

    Consequence: the bound in `mutualIntegrand_le_of_uniformSeparation` is a
    genuine additional hypothesis about the link, not repackaged `disjoint`.
    Concretely, this is where compactness of the components enters the mutual
    channel; drop it and the integrals below cease to exist. -/
theorem disjoint_not_imp_uniformSeparation (m : M) :
    ¬ ∃ δ : ℝ, LinkEmbedding.HasUniformSeparation (shrinkingLink m) δ := by
  rintro ⟨δ, hδpos, hsep⟩
  -- Evaluate the separation far out along the first parameter.
  have h01 : (0 : Fin 2) ≠ 1 := by decide
  have hbound := hsep 0 1 h01 (1 / δ) 0
  -- At `s = 1/δ`, `t = 0` the separation is `1 / (1 + 1/δ)`.
  have hval : (shrinkingLink m).sep 0 (1 / δ) 1 0 = 1 / (1 + 1 / δ) := by
    have hred : (shrinkingLink m).sep 0 (1 / δ) 1 0
        = (if (0 : Fin 2) = 1 then 0 else decayingSep (1 / δ) 0) := rfl
    rw [hred, if_neg h01]
    unfold decayingSep
    rw [abs_of_pos (by positivity : (0:ℝ) < 1 / δ), abs_zero, add_zero]
  rw [hval] at hbound
  have hden : (0:ℝ) < 1 + 1 / δ := by positivity
  rw [le_div_iff₀ hden] at hbound
  -- `δ * (1 + 1/δ) = δ + 1`, so the hypothesis forces `δ + 1 ≤ 1`, i.e. `δ ≤ 0`.
  have hexp : δ * (1 + 1 / δ) = δ + 1 := by field_simp
  rw [hexp] at hbound
  linarith

end MobiusMutualChannel

/-! ## §3  The integral — the Mathlib payoff

With the bound in hand the mutual channel is integrable by the ordinary route.
Measurability of `sep` in the integration variable is carried as a hypothesis:
`LinkEmbedding.sep` is a bare function with no regularity, so there is nothing
to derive it from. -/

namespace LinkEmbedding

variable {M : Type*} {n : ℕ}

/-- **The mutual integrand is interval-integrable.**

    Bounded (by `mutualIntegrand_le_of_uniformSeparation`) and measurable on a
    finite interval. This is the statement `QOU.MobiusEnergy` says it cannot
    make — and it costs no analysis beyond the uniform gap, because the mutual
    channel has no diagonal. -/
theorem mutualIntegrand_intervalIntegrable (L : LinkEmbedding M n)
    {δ : ℝ} (hδ : HasUniformSeparation L δ) {i j : Fin n} (hij : i ≠ j)
    (s a b : ℝ)
    (hmeas : Measurable fun t => L.mutualIntegrand i j s t) :
    IntervalIntegrable (fun t => L.mutualIntegrand i j s t) volume a b := by
  apply IntervalIntegrable.mono_fun (intervalIntegrable_const (c := 1 / δ ^ 2))
    hmeas.aestronglyMeasurable
  refine Filter.Eventually.of_forall fun t => ?_
  have hnn := L.mutualIntegrand_nonneg_of_ne hij s t
  simp only [Real.norm_eq_abs, abs_of_nonneg hnn,
    abs_of_nonneg (by positivity : (0:ℝ) ≤ 1 / δ ^ 2)]
  exact L.mutualIntegrand_le_of_uniformSeparation hδ hij s t

/-- The **inner pair energy** at fixed `s`: an honest `intervalIntegral` of the
    mutual integrand over the second component's parameter. -/
noncomputable def innerPairEnergy (L : LinkEmbedding M n) (i j : Fin n)
    (s : ℝ) : ℝ :=
  ∫ t in (0:ℝ)..1, L.mutualIntegrand i j s t

/-- **The inner pair energy is non-negative**, inherited from the integrand. -/
theorem innerPairEnergy_nonneg (L : LinkEmbedding M n) {i j : Fin n}
    (hij : i ≠ j) (s : ℝ) : 0 ≤ L.innerPairEnergy i j s := by
  unfold innerPairEnergy
  apply intervalIntegral.integral_nonneg (by norm_num)
  intro t _
  exact L.mutualIntegrand_nonneg_of_ne hij s t

/-- **The inner pair energy carries the bound through the integral.**

    Over a unit parameter interval the integral of something `≤ 1/δ²` is itself
    `≤ 1/δ²`. Together with `innerPairEnergy_nonneg` this pins the per-pair
    contribution into `[0, 1/δ²]` — a finite value derived from the link's
    geometry, with no fitted constant anywhere. -/
theorem innerPairEnergy_le (L : LinkEmbedding M n)
    {δ : ℝ} (hδ : HasUniformSeparation L δ) {i j : Fin n} (hij : i ≠ j)
    (s : ℝ) (hmeas : Measurable fun t => L.mutualIntegrand i j s t) :
    L.innerPairEnergy i j s ≤ 1 / δ ^ 2 := by
  unfold innerPairEnergy
  have hint := L.mutualIntegrand_intervalIntegrable hδ hij s 0 1 hmeas
  have hmono : (∫ t in (0:ℝ)..1, L.mutualIntegrand i j s t)
      ≤ ∫ _t in (0:ℝ)..1, 1 / δ ^ 2 := by
    apply intervalIntegral.integral_mono_on (by norm_num) hint
      intervalIntegrable_const
    intro t _
    exact L.mutualIntegrand_le_of_uniformSeparation hδ hij s t
  simpa using hmono

end LinkEmbedding

end QOU
