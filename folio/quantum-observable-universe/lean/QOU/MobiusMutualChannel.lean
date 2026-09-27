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
5. §9 `four_pi_abs_lk_le_energy` — the **link** analogue of BFHW's Theorem D,
   `4π|lk| ≤ E_mutual`, from the determinant bound `|det(a,b,c)| ≤ ‖a‖‖b‖‖c‖`
   (proved in §9a–§9b) and Gauss's integral formula (assumed, see below). It is
   **empty on a pairwise-unlinked pair**, which is the case this framework
   faces, and §9d proves no positive constant bounds the channel below at all.
   §9e guards it against vacuity: the hypotheses are jointly satisfiable with
   `lk ≠ 0`, and `4π` is the largest constant the bound admits. §9f settles
   that §9d's family performs a *separation at fixed length*, not a similarity,
   so the result is not an artefact of the model's pinned parameter interval.
   §9g turns the negative into a **localisation**: composing with the corpus's
   `b3_eq_zero_of_pairLocal`, any nonzero 3-body cumulant from this channel is
   entirely the assembly's effect on the pair's separations — so every number
   route (2) can supply is a derived geometry.

ASSUMED, and deliberately visible: `HasUniformSeparation` (a uniform gap),
measurability of `sep` in the integration variable, and — §9 only — **Gauss's
integral formula for the linking number**, carried as the explicit hypothesis
`hgauss` of `four_pi_abs_lk_le_energy` rather than as a class field.

For a genuine link — finitely many disjoint compact components — the uniform
gap is the distance between disjoint compacts and is automatic; it does **not**
follow from the pointwise positivity `LinkEmbedding.disjoint` supplies, which is
exactly what theorem 2 proves. None of the three is the conclusion in disguise,
and the one that most looks like it — the pointwise domination the link bound
runs on — is **proved** in §9b rather than assumed.

NOT DONE HERE, and not claimed: the **self/diagonal** channel. That still needs
O'Hara's theorem, it is `qou-bn8e`'s object rather than this bean's, and nothing
below weakens or sidesteps it.
-/
import QOU.MobiusEnergy
import QOU.Mass.CrossingModelPairLocality
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


/-! ## 8. The realisable-triples restriction — §7's open sub-item, CLOSED

§7 proved that Möbius invariance forces `f d = f 1 / d ^ 2`, and its docstring
flags one honest gap: `MobiusInvariantKernel` quantifies over **unconstrained**
positive triples `(d, da, db)`, while a geometrically realisable triple is three
distances among three points of `ℝ³` and must satisfy the triangle
inequalities. The witness §7 uses, `(1, 1/d, 1)`, needs `d ≥ 1/2`; the natural
alternative `da = db = 1/√d` covers only `d ≤ 4`. Neither family reaches all of
`(0, ∞)`, so §7 left open whether the characterisation survives the restriction.

**It does.** The mistake in §7's framing was looking for a *single* witness
family. The realisable hypothesis is a **two-parameter** family, and that is
enough room to bootstrap.

Take the isosceles configuration `da = db = t` with chord `c`. Of the three
triangle inequalities only `c ≤ 2t` binds — `t ≤ c + t` holds for free — and
invariance reads

    f (c / t²) = t⁴ · f c        whenever  0 < c,  0 < t,  c ≤ 2t.

That is `isoscelesStep`, and the rest is two applications of it:

* **`x ≤ 4`:** take `c = 1`, `t = 1/√x`. Realisable exactly when `√x ≤ 2`, i.e.
  `x ≤ 4`, which is the hypothesis; the argument lands on `c/t² = x`.
* **`x > 4`:** take `c = 1/x`, `t = 1/x`. Realisable because `1/x ≤ 2/x`, and
  again `c/t² = x`. Now `c = 1/x < 1/4`, so the first case applies to `f c`, and
  substituting gives the result.

So the restricted hypothesis is **not** weaker in its consequence, and §7's
result may now be cited without the caveat. Bean `qou-zfs6`.

**What this does not do.** It does not make the triples *geometric*: `Realisable`
is the triangle-inequality predicate on three reals, which is exactly the
condition for three points of `ℝ³` to realise them, but no points are
constructed here. And it says nothing about the FHW crossing bound or the mutual
channel's magnitude — it is purely about the kernel's functional form.
-/

/-- **Geometric realisability of a distance triple.** `(d, da, db)` are the
    pairwise distances of three points of `ℝ³` — the chord `d` between the two
    curve points, and their distances `da`, `db` to the inversion centre — iff
    they are positive and satisfy the three triangle inequalities. -/
def Realisable (d da db : ℝ) : Prop :=
  0 < d ∧ 0 < da ∧ 0 < db ∧ d ≤ da + db ∧ da ≤ d + db ∧ db ≤ d + da

/-- **Möbius invariance restricted to realisable triples** — the honest
    hypothesis §7 wished it had. Strictly weaker than `MobiusInvariantKernel`,
    which quantifies over all positive triples. -/
def MobiusInvariantOnRealisable (f : ℝ → ℝ) : Prop :=
  ∀ d da db : ℝ, Realisable d da db →
    f (d / (da * db)) * (1 / da ^ 2) * (1 / db ^ 2) = f d

/-- **The isosceles step.** With the inversion centre equidistant from both
    curve points (`da = db = t`), only `c ≤ 2t` binds, and invariance becomes a
    clean scaling law. This is the two-parameter freedom §7's single-witness
    search missed. -/
theorem isoscelesStep {f : ℝ → ℝ} (h : MobiusInvariantOnRealisable f)
    {c t : ℝ} (hc : 0 < c) (ht : 0 < t) (hle : c ≤ 2 * t) :
    f (c / t ^ 2) = t ^ 4 * f c := by
  have hr : Realisable c t t :=
    ⟨hc, ht, ht, by linarith, by linarith, by linarith⟩
  have key := h c t t hr
  rw [show t * t = t ^ 2 by ring] at key
  have ht2 : (t : ℝ) ^ 2 ≠ 0 := by positivity
  field_simp at key
  linarith [key]

/-- Step one: the characterisation on `(0, 4]`, from `c = 1` and `t = 1/√x`. -/
theorem realisable_inverse_square_of_le_four
    {f : ℝ → ℝ} (h : MobiusInvariantOnRealisable f)
    {x : ℝ} (hx : 0 < x) (hx4 : x ≤ 4) :
    f x = f 1 / x ^ 2 := by
  set s := Real.sqrt x with hs
  have hs0 : 0 < s := Real.sqrt_pos.mpr hx
  have hsx : s ^ 2 = x := Real.sq_sqrt hx.le
  have hs2 : s ≤ 2 := by
    have : Real.sqrt x ≤ Real.sqrt 4 := Real.sqrt_le_sqrt hx4
    rwa [show Real.sqrt 4 = 2 by
      rw [show (4:ℝ) = 2 ^ 2 by norm_num, Real.sqrt_sq (by norm_num : (0:ℝ) ≤ 2)]] at this
  have ht : (0:ℝ) < 1 / s := by positivity
  have hle : (1:ℝ) ≤ 2 * (1 / s) := by
    have hinv : s * (1 / s) = 1 := by field_simp
    nlinarith [hinv, hs2, ht, hs0]
  have hstep := isoscelesStep h (by norm_num : (0:ℝ) < 1) ht hle
  have harg : (1:ℝ) / (1 / s) ^ 2 = x := by
    field_simp; linarith [hsx]
  rw [harg] at hstep
  rw [hstep]
  have : (1 / s) ^ 4 = 1 / x ^ 2 := by
    have : s ^ 4 = x ^ 2 := by nlinarith [hsx]
    field_simp; linarith [this]
  rw [this]; ring

/-- **§7's open sub-item, closed: the restricted hypothesis still forces the
    inverse square, on all of `(0, ∞)`.**

    So `mobiusInvariant_forces_inverse_square` may be cited without its
    realisability caveat: no conclusion of §7 depended on triples the geometry
    cannot present. -/
theorem realisable_forces_inverse_square
    {f : ℝ → ℝ} (h : MobiusInvariantOnRealisable f)
    {x : ℝ} (hx : 0 < x) :
    f x = f 1 / x ^ 2 := by
  rcases le_or_gt x 4 with hx4 | hx4
  · exact realisable_inverse_square_of_le_four h hx hx4
  · -- `c = t = 1/x`: realisable since `1/x ≤ 2/x`, and `c / t ^ 2 = x`.
    have hxpos : (0:ℝ) < 1 / x := by positivity
    have hle : (1:ℝ) / x ≤ 2 * (1 / x) := by linarith [hxpos]
    have hstep := isoscelesStep h hxpos hxpos hle
    have harg : (1:ℝ) / x / (1 / x) ^ 2 = x := by field_simp
    rw [harg] at hstep
    -- `1/x < 1/4 ≤ 4`, so step one applies to `f (1/x)`
    have hsmall : (1:ℝ) / x ≤ 4 := by
      have hx0 : (0:ℝ) < x := by linarith
      have : (1:ℝ) / x ≤ 1 := by rw [div_le_one hx0]; linarith
      linarith
    have hinner := realisable_inverse_square_of_le_four h hxpos hsmall
    rw [hstep, hinner]
    field_simp

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

/-! ## §4  The structural gate: the mutual channel is ORIENTATION-BLIND

`qou-o6ml`'s constraint 2 prunes route (1)'s first ansatz. Two proved facts
compose: for the Borromean link every pairwise `lk_ij = 0`, so a nonzero `wᵢⱼ`
must be mediated by the triple invariant `μ̄₁₂₃`; and
`QOU.BraidsAndKnots.MilnorTripleLinkingMagnus.odd_symmetric_functional_vanishes`
(sorry-free) shows an exchange-symmetric functional that is ODD in `μ̄₁₂₃`
vanishes identically, because `μ̄₁₂₃` flips sign under that exchange
(`mubar_borromean_eq_one` / `mubar_swapped_eq_neg_one`). So an admissible `wᵢⱼ`
must be EVEN in `μ̄₁₂₃`, and the linear ansatz is dead
(`linear_coefficient_must_vanish`).

**The Möbius mutual channel clears that gate, and not narrowly.** Its integrand
is a function of the separation alone — no orientation, no sign, no ordering of
the strands enters it. So the exchange that flips `μ̄₁₂₃` leaves the energy
pointwise unchanged: the channel is not merely even in `μ̄₁₂₃`, it is *blind* to
it, which is strictly stronger than the constraint demands.

This section proves that blindness as an honest invariance theorem rather than
asserting it. `reverse` reparametrises every component backwards — the
operation under which an oriented invariant changes sign — and the energy comes
through unchanged. The proof is a genuine change of variables, not an unfolding.

WHAT IS AND IS NOT ESTABLISHED. This shows the functional *survives* the
constraint that killed the linear-in-`μ̄` ansatz. It does NOT show the
functional is correct, and it is not evidence for route (2) over any other
orientation-blind candidate. `κ(A)` cannot adjudicate that (PR #7080). -/

namespace KnotEmbedding

variable {M : Type*}

/-- Reverse a component's parametrisation, `s ↦ 1 - s`. Every distance field is
    precomposed; every law carries over because the substitution is an
    involution of the parameter interval. -/
def reverse (k : KnotEmbedding M) : KnotEmbedding M where
  curve := fun s => k.curve (1 - s)
  arcLengthDist := fun s t => k.arcLengthDist (1 - s) (1 - t)
  arcLength_symm := fun s t => k.arcLength_symm (1 - s) (1 - t)
  arcLength_nonneg := fun s t => k.arcLength_nonneg (1 - s) (1 - t)
  ambientDist := fun s t => k.ambientDist (1 - s) (1 - t)
  ambient_symm := fun s t => k.ambient_symm (1 - s) (1 - t)
  ambient_nonneg := fun s t => k.ambient_nonneg (1 - s) (1 - t)
  chord_le_arc := fun s t => k.chord_le_arc (1 - s) (1 - t)

end KnotEmbedding

namespace LinkEmbedding

variable {M : Type*} {n : ℕ}

/-- Reverse every component of a link simultaneously — the operation under
    which an oriented invariant such as `μ̄₁₂₃` changes sign. -/
def reverse (L : LinkEmbedding M n) : LinkEmbedding M n where
  component := fun i => (L.component i).reverse
  sep := fun i s j t => L.sep i (1 - s) j (1 - t)
  sep_symm := fun i s j t => L.sep_symm i (1 - s) j (1 - t)
  sep_nonneg := fun i s j t => L.sep_nonneg i (1 - s) j (1 - t)
  disjoint := fun i j hij s t => L.disjoint i j hij (1 - s) (1 - t)
  sep_self := fun i s t => L.sep_self i (1 - s) (1 - t)

@[simp] theorem reverse_sep (L : LinkEmbedding M n) (i j : Fin n) (s t : ℝ) :
    (L.reverse).sep i s j t = L.sep i (1 - s) j (1 - t) := rfl

@[simp] theorem mutualIntegrand_reverse (L : LinkEmbedding M n) (i j : Fin n)
    (s t : ℝ) :
    (L.reverse).mutualIntegrand i j s t = L.mutualIntegrand i j (1 - s) (1 - t) :=
  rfl

/-- **The pair energy is blind to orientation reversal.**

    A genuine change of variables `u = 1 - t` across the unit parameter
    interval, which the substitution preserves. This is the gate: the exchange
    that sends `μ̄₁₂₃ ↦ −μ̄₁₂₃` leaves this functional's value untouched, so it
    is even in `μ̄₁₂₃` — indeed independent of it — and is not the odd
    functional `odd_symmetric_functional_vanishes` annihilates. -/
theorem innerPairEnergy_reverse (L : LinkEmbedding M n) (i j : Fin n) (s : ℝ) :
    (L.reverse).innerPairEnergy i j s = L.innerPairEnergy i j (1 - s) := by
  unfold innerPairEnergy
  simp only [mutualIntegrand_reverse]
  rw [intervalIntegral.integral_comp_sub_left
    (fun u => L.mutualIntegrand i j (1 - s) u) 1]
  norm_num

/-! ### The lower bound — no cancellation is available

Constraint 2 kills a functional that can *vanish*. The bound below is the
positive half: with the components confined to a bounded region the pair energy
is bounded strictly AWAY from zero, so there is no configuration in which it
cancels. Both bounds are distances, so no signed quantity enters either. -/

/-- A link is **confined to diameter `D`** when no two points on distinct
    components are more than `D` apart — automatic for a link in a bounded
    region, and carried explicitly for the same reason the lower gap is. -/
def HasBoundedSeparation (L : LinkEmbedding M n) (D : ℝ) : Prop :=
  0 < D ∧ ∀ i j, i ≠ j → ∀ s t, L.sep i s j t ≤ D

/-- **The pair energy is bounded away from zero.**

    With `innerPairEnergy_le` this brackets the per-pair contribution into
    `[1/D², 1/δ²]`, both endpoints positive and both built from distances
    alone. A functional pinned inside a strictly positive interval cannot
    cancel, whatever the link's orientation data does. -/
theorem innerPairEnergy_ge (L : LinkEmbedding M n)
    {D : ℝ} (hD : HasBoundedSeparation L D) {i j : Fin n} (hij : i ≠ j)
    (s : ℝ) (hmeas : Measurable fun t => L.mutualIntegrand i j s t)
    {δ : ℝ} (hδ : HasUniformSeparation L δ) :
    1 / D ^ 2 ≤ L.innerPairEnergy i j s := by
  obtain ⟨hDpos, hub⟩ := hD
  unfold innerPairEnergy
  have hint := L.mutualIntegrand_intervalIntegrable hδ hij s 0 1 hmeas
  have hmono : (∫ _t in (0:ℝ)..1, 1 / D ^ 2)
      ≤ ∫ t in (0:ℝ)..1, L.mutualIntegrand i j s t := by
    apply intervalIntegral.integral_mono_on (by norm_num) intervalIntegrable_const
      hint
    intro t _
    have hpos : 0 < L.sep i s j t := L.disjoint i j hij s t
    have hsq : L.sep i s j t ^ 2 ≤ D ^ 2 := by
      have := hub i j hij s t; nlinarith
    unfold mutualIntegrand
    exact one_div_le_one_div_of_le (by positivity) hsq
  simpa using hmono

end LinkEmbedding

/-! ## §5  The O2 gate is NOT cleared by construction — a correction

I recorded on PR #7284 that this third gate "is the one the O'Hara subtraction
satisfies by construction". **That is wrong for this channel, and the `qou-o6ml`
ROAST it came from is wrong the same way.** Both reason from the *literature*
O'Hara integrand `1/|γ(s)−γ(t)|² − 1/D(s,t)²`, which is subtracted by
construction — but that subtraction lives in the **self** term, which by
`qou-o6ml`'s own split is `qou-bn8e`'s object, not this bean's.

The channel this bean needs is the **mutual** one, and `QOU.MobiusEnergy`'s own
`mutualIntegrand_eq_ohara_without_subtraction` states plainly that it is the
O'Hara integrand with the subtraction DROPPED (`1/D² = 0`). Worse for the
claim, §1 above proves `mutualIntegrand_pos_of_ne` — strictly positive,
unconditionally, no hypothesis at all.

**Strict positivity is exactly what made `coth` inadmissible under O2** (bean
`qou-17mq`, PR #7020/#7080): `∫_M Δu = 0` forces an admissible pair kernel to be
zero-mean, hence sign-changing, and a strictly positive kernel cannot be. So the
mutual channel stands in precisely `coth`'s position and inherits precisely
`coth`'s obligation.

THE FIX IS THE ONE #7080 ALREADY DERIVED, and that is the point worth keeping.
There the subtraction constant was not free: zero mean forced `c₀ = ⟨coth⟩_M`.
Here it forces the same shape — subtract the mean — and `innerPairEnergy` IS
that mean over the unit parameter interval. So the subtraction is determined by
the geometry rather than chosen, and §3's bracket already shows it is strictly
positive: the subtraction is not optional, and not zero.

What is proved below is the gate itself: the subtracted kernel satisfies O2, and
it is genuinely sign-changing rather than trivially so. -/

namespace LinkEmbedding

variable {M : Type*} {n : ℕ}

/-- The **zero-mean mutual kernel**: the mutual integrand with its own mean
    subtracted. The subtraction constant is `innerPairEnergy`, i.e. the mean
    itself — determined by the link, never chosen. -/
noncomputable def zeroMeanMutualKernel (L : LinkEmbedding M n) (i j : Fin n)
    (s t : ℝ) : ℝ :=
  L.mutualIntegrand i j s t - L.innerPairEnergy i j s

/-- **The subtracted kernel satisfies O2.** Its mean over the parameter
    interval is exactly zero — which is the condition `∫_M Δu = 0` imposes and
    the unsubtracted kernel provably cannot meet. -/
theorem zeroMeanMutualKernel_integral_zero (L : LinkEmbedding M n)
    {δ : ℝ} (hδ : HasUniformSeparation L δ) {i j : Fin n} (hij : i ≠ j)
    (s : ℝ) (hmeas : Measurable fun t => L.mutualIntegrand i j s t) :
    ∫ t in (0:ℝ)..1, L.zeroMeanMutualKernel i j s t = 0 := by
  have hint := L.mutualIntegrand_intervalIntegrable hδ hij s 0 1 hmeas
  unfold zeroMeanMutualKernel
  rw [intervalIntegral.integral_sub hint intervalIntegrable_const]
  unfold innerPairEnergy
  simp

/-- **And it genuinely changes sign** — it is not everywhere positive.

    This is what makes the O2 clearance real rather than formal: a kernel whose
    mean is zero cannot be strictly positive throughout, so the subtraction has
    actually moved the channel out of the class `coth` was excluded from. The
    contrast with `mutualIntegrand_pos_of_ne`, which holds with no hypothesis
    whatsoever, is the whole content. -/
theorem zeroMeanMutualKernel_not_pos (L : LinkEmbedding M n)
    {δ : ℝ} (hδ : HasUniformSeparation L δ) {i j : Fin n} (hij : i ≠ j)
    (s : ℝ) (hmeas : Measurable fun t => L.mutualIntegrand i j s t) :
    ¬ (∀ t ∈ Set.Ioo (0:ℝ) 1, 0 < L.zeroMeanMutualKernel i j s t) := by
  intro hpos
  have hint := L.mutualIntegrand_intervalIntegrable hδ hij s 0 1 hmeas
  have hintk : IntervalIntegrable
      (fun t => L.zeroMeanMutualKernel i j s t) volume 0 1 := by
    unfold zeroMeanMutualKernel
    exact hint.sub intervalIntegrable_const
  have hgt : 0 < ∫ t in (0:ℝ)..1, L.zeroMeanMutualKernel i j s t :=
    intervalIntegral.intervalIntegral_pos_of_pos_on hintk hpos (by norm_num)
  rw [L.zeroMeanMutualKernel_integral_zero hδ hij s hmeas] at hgt
  exact lt_irrefl 0 hgt

end LinkEmbedding

/-! ## §6  The measure was an unstated assumption — removed, not documented

§5's O2 theorem integrates against the **flat parameter measure** `ds`. The
literature O'Hara energy does not: its integrand carries the arclength weights
`|γ'(s)||γ'(t)|`, which is exactly what makes it reparametrisation-invariant.
The two coincide only for unit-speed parametrisation, and `LinkEmbedding` carries
no derivative data with which to say so — so §5 silently assumed constant speed.

"Zero mean" is a statement ABOUT A MEASURE, so that assumption is not cosmetic
here: the physically intended one is the charge/arclength density, not `ds`.

The fix is to state O2 against an ARBITRARY density `w` rather than to write the
constant-speed caveat into a docstring. Arclength is then one instance, `w = 1`
recovers §5 exactly, and nothing is assumed that is not named in the hypotheses.
`w` is a bare function, so its integrability and non-degeneracy are carried
explicitly — they cannot be derived from anything `LinkEmbedding` holds. -/

namespace LinkEmbedding

variable {M : Type*} {n : ℕ}

/-- The **`w`-weighted mean** of the mutual integrand over the second
    component's parameter. With `w = |γ'|` this is the arclength mean the
    O'Hara energy actually uses. -/
noncomputable def weightedPairMean (L : LinkEmbedding M n) (i j : Fin n)
    (s : ℝ) (w : ℝ → ℝ) : ℝ :=
  (∫ t in (0:ℝ)..1, L.mutualIntegrand i j s t * w t) / (∫ t in (0:ℝ)..1, w t)

/-- The mutual kernel with its own `w`-weighted mean subtracted. -/
noncomputable def zeroMeanMutualKernelW (L : LinkEmbedding M n) (i j : Fin n)
    (s : ℝ) (w : ℝ → ℝ) (t : ℝ) : ℝ :=
  L.mutualIntegrand i j s t - L.weightedPairMean i j s w

/-- **O2 against an arbitrary density.** The subtracted kernel has zero mean
    with respect to `w`, whatever `w` is — so the clearance no longer depends on
    which measure the fibre supplies, and in particular holds for arclength.

    The subtraction constant is still forced rather than chosen: it is the
    kernel's own `w`-mean, exactly as `c₀ = ⟨coth⟩_M` was forced in #7080. -/
theorem zeroMeanMutualKernelW_integral_zero (L : LinkEmbedding M n)
    (i j : Fin n) (s : ℝ) (w : ℝ → ℝ)
    (hw : IntervalIntegrable w volume 0 1)
    (hfw : IntervalIntegrable
      (fun t => L.mutualIntegrand i j s t * w t) volume 0 1)
    (hwne : (∫ t in (0:ℝ)..1, w t) ≠ 0) :
    ∫ t in (0:ℝ)..1, L.zeroMeanMutualKernelW i j s w t * w t = 0 := by
  have hsplit : ∀ t, L.zeroMeanMutualKernelW i j s w t * w t
      = L.mutualIntegrand i j s t * w t
        - L.weightedPairMean i j s w * w t := by
    intro t; unfold zeroMeanMutualKernelW; ring
  simp only [hsplit]
  rw [intervalIntegral.integral_sub hfw (hw.const_mul _),
    intervalIntegral.integral_const_mul]
  unfold weightedPairMean
  field_simp
  ring

/-- **`w = 1` recovers §5 exactly**, so the flat-measure statement is the
    constant-density instance of the general one rather than a separate claim. -/
theorem weightedPairMean_one (L : LinkEmbedding M n) (i j : Fin n) (s : ℝ) :
    L.weightedPairMean i j s (fun _ => 1) = L.innerPairEnergy i j s := by
  unfold weightedPairMean innerPairEnergy
  simp

end LinkEmbedding

/-! ## 7. The discriminator: Möbius invariance FORCES the inverse square

§§1-6 are **admissibility**: the mutual channel is integrable, blind to
orientation, bounded away from zero, and (after subtracting its own mean)
satisfies O2 against any density. Every one of those is a test that many
candidate kernels pass, so clearing them is not evidence for this channel over
another orientation-blind functional of separation. Bean `qou-o6ml` records the
resulting blocker: route (2) needs a *discriminating* observable, and `κ(A)`
cannot be it (#7020/#7080 proved that series constrains only the product
`s·p`).

This section supplies one, and it is the property that singles out the
Möbius/O'Hara energy among knot energies in the first place: **invariance under
Möbius transformations of the ambient space**.

**What makes it statable here.** A Möbius transformation is a map of `ℝ³ ∪ {∞}`,
and `LinkEmbedding` carries no ambient geometry — only `sep`, a real-valued
separation. But the classical transformation law under an inversion centred at
a point `a` is itself a statement about *distances*:

    |I(x) − I(y)| = |x − y| / (|x − a| · |y − a|)          (chord)
    |I(γ(s))′|    = 1 / |γ(s) − a|²                        (arclength element)

so the invariance condition can be written entirely in the language `sep`
already speaks. Those two laws are classical and are **assumed** here with a
citation, not derived; what is proved is what they force.

**What they force, and it is the whole point.** Not merely that `1/d²` happens
to be invariant — that the exponent is the ONLY one that can be. A functional
`f` of separation, carried against the arclength density, is Möbius invariant
**iff** `f(d) = f(1)/d²`. So the inverse square is not an ansatz and not a
choice: it is the unique orientation-blind kernel compatible with the symmetry.

**And it pins the density §6 deliberately left free.** §6 proved O2 against an
arbitrary `w`, with the honest note that `LinkEmbedding` supplies nothing that
would select one. Möbius invariance selects it: the Jacobian factors
`1/|γ − a|²` are exactly what cancel the chord factors, and §7c below shows the
flat parameter measure `ds dt` fails. So the two sections compose — §6 removed
an unnamed assumption, §7 derives the thing it left open, and neither
introduces a free parameter.

-- Ref: [ohara1991] https://doi.org/10.1016/0040-9383(91)90010-2
-- Ref: [freedman1994] https://doi.org/10.2307/2946626
-/

namespace MobiusMutualChannel

/-- **Möbius invariance of a separation kernel, carried against arclength.**

    `f` is the kernel as a function of separation; `d` is the chord between the
    two points; `da`, `db` are their distances to the inversion centre. The
    left-hand side is the transformed integrand: the kernel evaluated at the
    transformed chord, times the two arclength Jacobians. -/
def MobiusInvariantKernel (f : ℝ → ℝ) : Prop :=
  ∀ d da db : ℝ, 0 < d → 0 < da → 0 < db →
    f (d / (da * db)) * (1 / da ^ 2) * (1 / db ^ 2) = f d

/-- **THE DISCRIMINATOR.** Möbius invariance forces the inverse square.

    No ansatz, no fitted exponent, no appeal to the measured numbers: the
    hypothesis is the symmetry alone, and the conclusion is the kernel. Any
    orientation-blind functional of separation that is Möbius invariant against
    the arclength density *is* `f(1)/d²` — so the mutual channel's `1 / sep ^ 2`
    is the unique such kernel up to the overall constant.

    This is what §§1-6 could not supply. Those sections admit a whole class of
    candidates; this one cuts the class to a single ray.

    **🛑 SCOPE — the hypothesis is stronger than the geometry supplies, and the
    gap is at small chord.** `MobiusInvariantKernel` quantifies over
    *unconstrained* positive triples `(d, da, db)`. A geometrically realisable
    triple is three distances among three points of `ℝ³`, so it must satisfy the
    triangle inequalities; the witness this proof uses, `(1, 1/d, 1)`, needs
    `1/d ≤ 2`, i.e. **`d ≥ 1/2`**. For `d < 1/2` that triple is not realisable by
    any configuration, so the conclusion at small `d` rests on invariance over
    triples the geometry never presents.

    Taking `da = db = 1/√d` instead is realisable for `d ≤ 4` and fails past it,
    so neither single *witness family* covers `(0, ∞)`.

    **🟩 RESOLVED in §8 below — this caveat is retained as the record of the gap,
    not as a live one.** The restricted hypothesis gives the same conclusion:
    `realisable_forces_inverse_square` proves `f x = f 1 / x ^ 2` on all of
    `(0, ∞)` from `MobiusInvariantOnRealisable` alone. The gap was in the search,
    not in the mathematics — looking for ONE witness family missed that the
    realisable hypothesis is a two-parameter family, and the isosceles
    configuration `da = db = t` bootstraps from `(0, 4]` to everything.

    So this theorem MAY now be cited as forced by invariance over geometrically
    realisable triples; cite `realisable_forces_inverse_square` when that is the
    hypothesis you have. Bean `qou-zfs6`. -/
theorem mobiusInvariant_forces_inverse_square
    {f : ℝ → ℝ} (hf : MobiusInvariantKernel f) {d : ℝ} (hd : 0 < d) :
    f d = f 1 / d ^ 2 := by
  have hd' : d ≠ 0 := ne_of_gt hd
  -- Evaluate the invariance law at chord `1`, with the inversion centre placed
  -- so that `da * db = 1 / d`; the transformed chord is then exactly `d`.
  have h := hf 1 (1 / d) 1 one_pos (by positivity) one_pos
  have hrw : (1 : ℝ) / (1 / d * 1) = d := by field_simp
  rw [hrw] at h
  -- `h : f d * (1 / (1 / d) ^ 2) * (1 / 1 ^ 2) = f 1`, i.e. `f d * d ^ 2 = f 1`.
  field_simp at h
  field_simp
  linarith [h]

/-- The converse: the inverse-square kernel really is Möbius invariant, so the
    characterisation above is not vacuous. Together with it, `1/d²` is the
    unique Möbius-invariant separation kernel up to scale. -/
theorem inverse_square_mobiusInvariant :
    MobiusInvariantKernel (fun d => 1 / d ^ 2) := by
  intro d da db hd hda hdb
  have hd' : d ≠ 0 := ne_of_gt hd
  have hda' : da ≠ 0 := ne_of_gt hda
  have hdb' : db ≠ 0 := ne_of_gt hdb
  field_simp

/-- **§7c — the FLAT parameter measure is not Möbius invariant.**

    Dropping the arclength Jacobians leaves the bare kernel, and it does *not*
    survive an inversion. Witness: chord `1`, centre distances `2` and `1`, so
    the transformed chord is `1/2` and the kernel reads `4` against the original
    `1`.

    This is the exact assumption §6 removed rather than documented, now shown to
    be not merely unsupported but **false**: `ds dt` cannot be the measure the
    Möbius channel is carried against. -/
theorem flat_measure_not_mobiusInvariant :
    ¬ (∀ d da db : ℝ, 0 < d → 0 < da → 0 < db →
        (fun x : ℝ => 1 / x ^ 2) (d / (da * db))
          = (fun x : ℝ => 1 / x ^ 2) d) := by
  intro h
  have := h 1 2 1 one_pos (by norm_num) one_pos
  norm_num at this

/-! ## 9. The LINK version of Theorem D — it EXISTS, it is ELEMENTARY,
       and it is VACUOUS exactly where this framework needs it

`qou-dux3` records the gap this section closes and re-opens one level down:
BFHW's Theorem D, `2π c([γ]) + 4 ≤ E(γ)`, bounds the **self** energy of a knot
by its crossing number, and §7's triage recorded that it is not statable here
because `LinkEmbedding` carries no crossing data. The mutual channel needs a
**link** analogue, and the bean's verdict was that none was found.

**There is one, and it is elementary.** Write the Gauss linking integral

  lk(γ₁,γ₂) = (1/4π) ∬ det(γ̇₁(s), γ̇₂(t), γ₁(s) − γ₂(t)) / |γ₁(s) − γ₂(t)|³ ds dt

and bound the integrand by `|det(a,b,c)| ≤ ‖a‖‖b‖‖c‖`. The `‖c‖` cancels one
power of the denominator and what is left is **exactly** the Möbius mutual
integrand `‖γ̇₁‖‖γ̇₂‖ / |γ₁ − γ₂|²`. Hence

  4π |lk(γ₁,γ₂)| ≤ E_mutual(γ₁,γ₂).

No O'Hara theorem, no minimiser, no compactness — the mutual channel has no
diagonal (the whole point of this file), so the integral exists by §3 and the
bound is monotonicity applied to a pointwise inequality proved by `ring`.

Note what supplies the inverse square: the Gauss integrand carries `|c|³` in
the denominator and one power is spent on `|c|` from the determinant bound.
So the kernel §7/§8 force by Möbius invariance is **the same** kernel for which
this topological lower bound exists. That is a consistency check on §7, not a
new assumption.

### THE RESULT IS A NEGATIVE, AND THAT IS THE POINT

`qou-o6ml`'s gate for route (2) is that the mutual channel be **nonzero on a
pairwise-unlinked pair** — every pairwise `lk_ij` of the Borromean link is `0`
(`mirror_split_s3_em_functional_probe.py` A3). Against that gate this bound is
**empty**: `lk = 0` makes it read `0 ≤ E_mutual`, which §3's
`innerPairEnergy_nonneg` already gives unconditionally and with no hypotheses
at all. `lk_bound_iff_nonneg_of_lk_zero` states that degeneration as an `iff`
so the claim "it adds nothing" is itself proved rather than asserted.

And the failure is not an artefact of this particular bound. §9d shows that
**no positive constant lower-bounds the mutual pair energy at all**: the
`separatedLink` family realises every sufficiently small positive value, via
§3's own `innerPairEnergy_le`. So the mutual Möbius channel is a *geometric*
quantity, and any magnitude route (2) supplies must come from a **derived
configuration**, never from the pair's topology.

### AND IT IS NOT A TAUTOLOGY — §9e

§9e exhibits data satisfying all four hypotheses of
`four_pi_abs_lk_le_energy` with `lk ≠ 0`, so the theorem is true of something;
and `four_pi_is_the_largest_constant` shows `4π` is the largest constant that
can stand in front of `|lk|`, so the bound is sharp rather than merely valid.
Without the first of those, nothing here rules out the four hypotheses being
jointly contradictory — the dressed-up-tautology shape the 2026-08-30 roast
found four of in `QOU.MobiusEnergy`.

### WHAT IS ASSUMED, AND IT IS ONE THING

Gauss's integral formula for the linking number — classical, and carried as an
explicit hypothesis `hgauss` of `four_pi_abs_lk_le_energy` rather than as a
class field, so that a reader can see it is an input. Monotonicity and oddness
of the integral are the other two hypotheses; both are standard properties of
the Lebesgue integral and neither is the conclusion in disguise. The pointwise
domination is **not** assumed: §9b proves it.

### WHAT IS NOT CLAIMED

That `inf E_mutual = 0` over an **isotopy class**. `LinkEmbedding` carries no
isotopy data, so the statement below quantifies over the `separatedLink`
family, not over the configurations reachable from a fixed link. Upgrading it
would need the classical fact that a pairwise-unlinked pair is isotopic to a
split link; that is true and is *not* formalised here. The weaker statement is
already enough to kill a universal positive constant, which is what a
topological bound would have to be.
-/

variable {M : Type*}

/-! ### §9a  The determinant bound in ℝ³ — pure algebra -/

/-- The scalar triple product `(a × b) · c`, in coordinates. -/
def det3 (a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃ : ℝ) : ℝ :=
  (a₂ * b₃ - a₃ * b₂) * c₁ + (a₃ * b₁ - a₁ * b₃) * c₂ + (a₁ * b₂ - a₂ * b₁) * c₃

/-- The Euclidean norm on ℝ³, in coordinates. -/
noncomputable def nrm3 (x₁ x₂ x₃ : ℝ) : ℝ := Real.sqrt (x₁ ^ 2 + x₂ ^ 2 + x₃ ^ 2)

theorem nrm3_nonneg (x₁ x₂ x₃ : ℝ) : 0 ≤ nrm3 x₁ x₂ x₃ := Real.sqrt_nonneg _

theorem nrm3_sq (x₁ x₂ x₃ : ℝ) :
    nrm3 x₁ x₂ x₃ ^ 2 = x₁ ^ 2 + x₂ ^ 2 + x₃ ^ 2 :=
  Real.sq_sqrt (by positivity)

/-- **Lagrange's identity in ℝ³** — `‖a × b‖² = ‖a‖²‖b‖² − ⟪a,b⟫²`. A `ring`
    identity; it is what makes the cross-product bound free. -/
theorem lagrange3 (a₁ a₂ a₃ b₁ b₂ b₃ : ℝ) :
    (a₂ * b₃ - a₃ * b₂) ^ 2 + (a₃ * b₁ - a₁ * b₃) ^ 2 + (a₁ * b₂ - a₂ * b₁) ^ 2
      = (a₁ ^ 2 + a₂ ^ 2 + a₃ ^ 2) * (b₁ ^ 2 + b₂ ^ 2 + b₃ ^ 2)
        - (a₁ * b₁ + a₂ * b₂ + a₃ * b₃) ^ 2 := by
  ring

/-- **Cauchy–Schwarz in ℝ³**, in coordinates. -/
theorem cauchySchwarz3 (x₁ x₂ x₃ c₁ c₂ c₃ : ℝ) :
    (x₁ * c₁ + x₂ * c₂ + x₃ * c₃) ^ 2
      ≤ (x₁ ^ 2 + x₂ ^ 2 + x₃ ^ 2) * (c₁ ^ 2 + c₂ ^ 2 + c₃ ^ 2) := by
  nlinarith [sq_nonneg (x₁ * c₂ - x₂ * c₁), sq_nonneg (x₁ * c₃ - x₃ * c₁),
    sq_nonneg (x₂ * c₃ - x₃ * c₂)]

/-- **`det3² ≤ ‖a‖²‖b‖²‖c‖²`** — Cauchy–Schwarz against `a × b`, then Lagrange
    to drop the `⟪a,b⟫²` that only helps. -/
theorem det3_sq_le (a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃ : ℝ) :
    det3 a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃ ^ 2
      ≤ (a₁ ^ 2 + a₂ ^ 2 + a₃ ^ 2) * (b₁ ^ 2 + b₂ ^ 2 + b₃ ^ 2)
        * (c₁ ^ 2 + c₂ ^ 2 + c₃ ^ 2) := by
  have hcs := cauchySchwarz3 (a₂ * b₃ - a₃ * b₂) (a₃ * b₁ - a₁ * b₃)
    (a₁ * b₂ - a₂ * b₁) c₁ c₂ c₃
  have hlag : (a₂ * b₃ - a₃ * b₂) ^ 2 + (a₃ * b₁ - a₁ * b₃) ^ 2
      + (a₁ * b₂ - a₂ * b₁) ^ 2
      ≤ (a₁ ^ 2 + a₂ ^ 2 + a₃ ^ 2) * (b₁ ^ 2 + b₂ ^ 2 + b₃ ^ 2) := by
    nlinarith [lagrange3 a₁ a₂ a₃ b₁ b₂ b₃, sq_nonneg (a₁ * b₁ + a₂ * b₂ + a₃ * b₃)]
  have hc : (0 : ℝ) ≤ c₁ ^ 2 + c₂ ^ 2 + c₃ ^ 2 := by positivity
  have hstep := mul_le_mul_of_nonneg_right hlag hc
  have hdet : det3 a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃ ^ 2
      = ((a₂ * b₃ - a₃ * b₂) * c₁ + (a₃ * b₁ - a₁ * b₃) * c₂
          + (a₁ * b₂ - a₂ * b₁) * c₃) ^ 2 := by
    unfold det3; ring
  rw [hdet]
  linarith

/-- **`|det3| ≤ ‖a‖ ‖b‖ ‖c‖`.** -/
theorem abs_det3_le (a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃ : ℝ) :
    |det3 a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃|
      ≤ nrm3 a₁ a₂ a₃ * nrm3 b₁ b₂ b₃ * nrm3 c₁ c₂ c₃ := by
  have hprod : nrm3 a₁ a₂ a₃ * nrm3 b₁ b₂ b₃ * nrm3 c₁ c₂ c₃
      = Real.sqrt ((a₁ ^ 2 + a₂ ^ 2 + a₃ ^ 2) * (b₁ ^ 2 + b₂ ^ 2 + b₃ ^ 2)
          * (c₁ ^ 2 + c₂ ^ 2 + c₃ ^ 2)) := by
    unfold nrm3
    rw [← Real.sqrt_mul (by positivity), ← Real.sqrt_mul (by positivity)]
  rw [hprod, ← Real.sqrt_sq_eq_abs]
  exact Real.sqrt_le_sqrt (det3_sq_le a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃)

/-! ### §9b  The Gauss integrand is dominated by the Möbius mutual integrand -/

/-- **The pointwise domination.**

    `|det(a,b,c)| / ‖c‖³ ≤ ‖a‖‖b‖ / ‖c‖²`. This is the whole geometric content
    of the link bound: one power of `‖c‖` from the determinant estimate cancels
    against the cube in the Gauss kernel, leaving precisely the inverse-square
    Möbius kernel that §7 and §8 force by symmetry.

    It is **proved**, not assumed — `four_pi_abs_lk_le_energy` below takes the
    domination as a hypothesis because it is stated over an abstract parameter
    domain, and this is what discharges it in the concrete ℝ³ case. -/
theorem gaussIntegrand_le_mutualIntegrand
    (a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃ : ℝ) (hc : 0 < nrm3 c₁ c₂ c₃) :
    |det3 a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃| / nrm3 c₁ c₂ c₃ ^ 3
      ≤ nrm3 a₁ a₂ a₃ * nrm3 b₁ b₂ b₃ / nrm3 c₁ c₂ c₃ ^ 2 := by
  have hle := abs_det3_le a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃
  calc |det3 a₁ a₂ a₃ b₁ b₂ b₃ c₁ c₂ c₃| / nrm3 c₁ c₂ c₃ ^ 3
      ≤ (nrm3 a₁ a₂ a₃ * nrm3 b₁ b₂ b₃ * nrm3 c₁ c₂ c₃) / nrm3 c₁ c₂ c₃ ^ 3 := by
        gcongr
    _ = nrm3 a₁ a₂ a₃ * nrm3 b₁ b₂ b₃ / nrm3 c₁ c₂ c₃ ^ 2 := by
        field_simp

/-! ### §9c  The link version of Theorem D -/

/-- **`4π |lk| ≤ E_mutual`** — the link analogue of BFHW's Theorem D.

    Hypotheses, all visible and none of them the conclusion:

    * `hmono` / `hneg` — the integral is monotone and odd. Standard properties
      of the Lebesgue integral; abstracted so this statement does not depend on
      which integral is used.
    * `hgauss` — **Gauss's integral formula** `∫ gauss = 4π·lk`. Classical, and
      the one genuinely assumed input.
    * `hdom` — the pointwise domination, **proved** in §9b for the ℝ³
      integrands.

    The derivation is `|∫ g| ≤ ∫ |g| ≤ ∫ e`; the content is that `hdom` is
    available at all, and that is §9b's determinant estimate. -/
theorem four_pi_abs_lk_le_energy {Ω : Type*}
    (I : (Ω → ℝ) → ℝ) (gauss energy : Ω → ℝ) (lk : ℝ)
    (hmono : ∀ f g : Ω → ℝ, (∀ x, f x ≤ g x) → I f ≤ I g)
    (hneg : ∀ f : Ω → ℝ, I (fun x => -f x) = - I f)
    (hgauss : I gauss = 4 * Real.pi * lk)
    (hdom : ∀ x, |gauss x| ≤ energy x) :
    4 * Real.pi * |lk| ≤ I energy := by
  have hup : I gauss ≤ I energy :=
    hmono _ _ fun x => le_trans (le_abs_self _) (hdom x)
  have hdown : - I gauss ≤ I energy := by
    rw [← hneg]
    exact hmono _ _ fun x => le_trans (neg_le_abs _) (hdom x)
  have hpi : (0 : ℝ) < 4 * Real.pi := by positivity
  calc 4 * Real.pi * |lk| = |4 * Real.pi * lk| := by
        rw [abs_mul, abs_of_pos hpi]
    _ = |I gauss| := by rw [hgauss]
    _ ≤ I energy := abs_le.mpr ⟨by linarith, hup⟩

/-! ### §9d  The bound is empty on a pairwise-unlinked pair -/

/-- **At `lk = 0` the link bound IS non-negativity.**

    Stated as an `iff` so that "the bound adds nothing" is proved rather than
    asserted: its conclusion is *equivalent* to `0 ≤ E_mutual`, which §3's
    `LinkEmbedding.innerPairEnergy_nonneg` already supplies with no hypotheses.

    Every pairwise linking number of the Borromean link vanishes, so this is the
    case `qou-o6ml` route (2) actually faces. -/
theorem lk_bound_iff_nonneg_of_lk_zero {Ω : Type*}
    (I : (Ω → ℝ) → ℝ) (energy : Ω → ℝ) {lk : ℝ} (hlk : lk = 0) :
    (4 * Real.pi * |lk| ≤ I energy) ↔ 0 ≤ I energy := by
  subst hlk
  simp

/-- A two-component link whose components sit at **constant** separation
    `1 + |R|`. The `1 +` keeps it positive for every real `R`, so the family is
    indexed by all of `ℝ` with no side condition to carry. -/
noncomputable def separatedLink (m : M) (R : ℝ) : LinkEmbedding M 2 where
  component := fun _ => pointKnot m
  sep := fun i _ j _ => if i = j then 0 else 1 + |R|
  sep_symm := by
    intro i s j t
    by_cases h : i = j
    · subst h; simp
    · rw [if_neg h, if_neg (Ne.symm h)]
  sep_nonneg := by
    intro i s j t
    by_cases h : i = j
    · simp [h]
    · rw [if_neg h]; positivity
  disjoint := by
    intro i j hij s t
    rw [if_neg hij]; positivity
  sep_self := by intro i s t; simp [pointKnot]

theorem separatedLink_hasUniformSeparation (m : M) (R : ℝ) :
    LinkEmbedding.HasUniformSeparation (separatedLink m R) (1 + |R|) := by
  refine ⟨by positivity, ?_⟩
  intro i j hij s t
  show (1 + |R|) ≤ (if i = j then 0 else 1 + |R|)
  rw [if_neg hij]

/-- The pair energy of `separatedLink` is at most `1 / (1 + |R|)²` — §3's own
    `innerPairEnergy_le`, with the constant integrand discharging its
    measurability hypothesis. -/
theorem innerPairEnergy_separatedLink_le (m : M) (R s : ℝ) :
    (separatedLink m R).innerPairEnergy 0 1 s ≤ 1 / (1 + |R|) ^ 2 := by
  have hconst : (fun t => (separatedLink m R).mutualIntegrand 0 1 s t)
      = fun _ : ℝ => 1 / (1 + |R|) ^ 2 := by
    funext t
    show 1 / ((separatedLink m R).sep 0 s 1 t) ^ 2 = 1 / (1 + |R|) ^ 2
    rw [show (separatedLink m R).sep 0 s 1 t
        = (if (0 : Fin 2) = 1 then 0 else 1 + |R|) from rfl,
      if_neg (by decide : ¬ (0 : Fin 2) = 1)]
  exact LinkEmbedding.innerPairEnergy_le _ (separatedLink_hasUniformSeparation m R)
    (by decide) s (by rw [hconst]; exact measurable_const)

/-- **Every sufficiently small positive value is realised.** -/
theorem innerPairEnergy_separatedLink_small (m : M) {ε : ℝ} (hε : 0 < ε) (s : ℝ) :
    ∃ R : ℝ, (separatedLink m R).innerPairEnergy 0 1 s ≤ ε := by
  refine ⟨1 / ε, le_trans (innerPairEnergy_separatedLink_le m (1 / ε) s) ?_⟩
  rw [abs_of_pos (by positivity : (0:ℝ) < 1 / ε)]
  rw [div_le_iff₀ (by positivity)]
  have hexp : ε * (1 + 1 / ε) ^ 2 = ε + 2 + 1 / ε := by
    field_simp; ring
  rw [hexp]
  have : (0:ℝ) < 1 / ε := by positivity
  linarith

/-- **No positive constant lower-bounds a quantity that gets arbitrarily
    small.** The abstract step; `no_positive_uniform_mutual_lower_bound`
    instantiates it. -/
theorem uniformLowerBound_nonpos {ι : Type*} {F : ℝ} {E : ι → ℝ}
    (hlb : ∀ c, F ≤ E c) (hsmall : ∀ ε : ℝ, 0 < ε → ∃ c, E c ≤ ε) : F ≤ 0 := by
  by_contra hpos
  push_neg at hpos
  obtain ⟨c, hc⟩ := hsmall (F / 2) (by linarith)
  have := hlb c
  linarith

/-- **No positive constant lower-bounds the mutual pair energy.**

    So the Möbius mutual channel carries no universal positive floor, and in
    particular no topological invariant can bound it below by a positive
    amount on a pairwise-unlinked pair. Route (2)'s magnitude has to come from
    a *derived configuration* — a geometry — and not from the pair's link type.

    This is a scope-(b) structural exclusion in the sense of AGENTS.md: the
    invariant cited is `LinkEmbedding.innerPairEnergy_le`, the separation bound
    §1 proves, and the exclusion is of *topological* lower bounds only. It says
    nothing against a geometric magnitude, which is what the framework would
    have to derive. -/
theorem no_positive_uniform_mutual_lower_bound (m : M) (s : ℝ) {F : ℝ}
    (hlb : ∀ R : ℝ, F ≤ (separatedLink m R).innerPairEnergy 0 1 s) : F ≤ 0 :=
  uniformLowerBound_nonpos hlb fun _ hε => innerPairEnergy_separatedLink_small m hε s

/-! ### §9e  Non-vacuity — the four hypotheses are jointly satisfiable, with `lk ≠ 0`

`four_pi_abs_lk_le_energy` carries four hypotheses. Nothing above rules out
their being jointly contradictory, in which case the theorem would be true of
nothing and the whole section would be the dressed-up tautology that
`QOU.MobiusEnergy` produced four of before the 2026-08-30 roast. §7 guards
itself this way (`inverse_square_mobiusInvariant`); §9 did not, and this closes
that gap.

The witness is deliberately the sharp case: it satisfies all four with
`lk = 1 ≠ 0` AND attains equality, so the bound is not merely non-vacuous but
cannot be improved by any constant. -/

/-- **The hypotheses are satisfiable with a nonzero linking number.**

    A one-point parameter domain with `I = evaluation` is monotone and odd, and
    the constant integrands `gauss = energy = 4π` satisfy the domination. The
    resulting `lk` is `1`. -/
theorem four_pi_bound_hypotheses_satisfiable :
    ∃ (I : (Unit → ℝ) → ℝ) (gauss energy : Unit → ℝ) (lk : ℝ),
      lk ≠ 0 ∧
      (∀ f g : Unit → ℝ, (∀ x, f x ≤ g x) → I f ≤ I g) ∧
      (∀ f : Unit → ℝ, I (fun x => -f x) = - I f) ∧
      I gauss = 4 * Real.pi * lk ∧
      (∀ x, |gauss x| ≤ energy x) := by
  refine ⟨fun f => f (), fun _ => 4 * Real.pi, fun _ => 4 * Real.pi, 1,
    one_ne_zero, fun f g h => h (), fun _ => rfl, by ring, fun _ => ?_⟩
  rw [abs_of_pos (by positivity : (0:ℝ) < 4 * Real.pi)]

/-- **`4π` is the LARGEST constant that works** — the bound is sharp.

    The first draft of this stated equality on the witness above and left the
    sharpness claim to the docstring. That is the defect this whole subsection
    exists to catch, one level up: a narrated inference is not a proved one. So
    the claim is stated instead — any `c` for which `c·|lk| ≤ I energy` holds
    across all satisfying data satisfies `c ≤ 4π`, because the witness has
    `lk = 1` and `I energy = 4π`.

    Together with `four_pi_abs_lk_le_energy` this pins the constant exactly:
    `4π` works and nothing larger does. -/
theorem four_pi_is_the_largest_constant {c : ℝ}
    (h : ∀ (I : (Unit → ℝ) → ℝ) (gauss energy : Unit → ℝ) (lk : ℝ),
      (∀ f g : Unit → ℝ, (∀ x, f x ≤ g x) → I f ≤ I g) →
      (∀ f : Unit → ℝ, I (fun x => -f x) = - I f) →
      I gauss = 4 * Real.pi * lk →
      (∀ x, |gauss x| ≤ energy x) →
      c * |lk| ≤ I energy) :
    c ≤ 4 * Real.pi := by
  have hw := h (fun f => f ()) (fun _ => 4 * Real.pi) (fun _ => 4 * Real.pi) 1
    (fun _ _ hfg => hfg ()) (fun _ => rfl) (by ring)
    (fun _ => by rw [abs_of_pos (by positivity : (0:ℝ) < 4 * Real.pi)])
  simpa using hw

/-- **The `pointKnot` components of `separatedLink` do not weaken §9d** — a
    note a reader is entitled to demand, proved rather than asserted.

    `separatedLink` populates both components with `pointKnot`, a degenerate
    embedding. That is irrelevant to the conclusion because `mutualIntegrand`,
    and hence `innerPairEnergy`, reads **only** the `sep` field — this states
    exactly that, so the component data provably cannot enter. It is the same
    division of labour §2's `shrinkingLink` uses, where the content is in `sep`
    and the components merely populate the structure. -/
theorem mutualIntegrand_depends_only_on_sep {n : ℕ}
    (L L' : LinkEmbedding M n) (hsep : L.sep = L'.sep) (i j : Fin n) (s t : ℝ) :
    L.mutualIntegrand i j s t = L'.mutualIntegrand i j s t := by
  unfold LinkEmbedding.mutualIntegrand
  rw [hsep]

end MobiusMutualChannel

/-! ## §9f  Is §9d a RESCALING ARTEFACT?  No — and here is the proof

A reviewer's first objection to §9d should be this. The true mutual energy
`∬ ‖γ̇₁‖‖γ̇₂‖ / |γ₁ − γ₂|² ds dt` is **scale-invariant**: a similarity of ratio
`λ` multiplies the numerator's arclengths by `λ²` and the denominator by `λ²`.
So if §9d's `separatedLink` family were a family of *similarities*, driving the
energy to zero along it would be impossible in the true energy and the whole
subsection would be measuring the model rather than the mathematics.

`QOU.MobiusEnergy.mutualIntegrand_smul` names exactly this and stops there —
*"this is not scale-invariance of the energy; that also needs the `ds dt`
measure to scale by `c²`, which requires the integral this file does not
build."* §3 builds that integral, so the question is now answerable here.

**The answer: `innerPairEnergy` scales by `c⁻²`, and that is CORRECT rather
than a defect.** In the true energy the measures are *arclength*, so a
similarity rescales the parameter domain too — `[0, L]` becomes `[0, λL]` — and
the two effects cancel. `innerPairEnergy` integrates over `(0:ℝ)..1`,
**pinned**. So scaling `sep` while holding that interval fixed is not a
similarity at all: it is *"move the components apart and keep their arclength
budget"*, which is precisely the geometric move §9d needs and precisely the move
that makes a 2-component unlink's energy small.

Put the other way: the fixed unit interval **is** the fixed length. A genuine
similarity in this model would have to scale the domain as well, and nothing in
§9d does that.

**The similarity bookkeeping, NOT formalised, and stated so rather than
proved-by-docstring.** A genuine similarity rescales the parameter domain as
well, and at the level of the *full* energy the factors read
`c⁻² · c · c = c⁰` — one `c` from each of the two parameter integrations.
`innerPairEnergy` performs only the inner one, so under a domain-scaled
similarity it would carry `c⁻² · c = c⁻¹`, with the outer `s`-integration
supplying the missing `c`. That is arithmetic, not a theorem here: stating it
needs a reparametrisation `L.sep i s j (t/c)` which `LinkEmbedding` does not
supply from `hscale`, and the outer integration, which §3 does not build.

A first draft of this subsection carried a second theorem claiming to prove it.
Its statement was `c² · (c⁻² · E) = E` — a `field_simp` restatement of the
scaling law, with the domain-scaling claim living only in its docstring. That
is the narrated-inference defect §9e exists to catch, committed inside the
commit that added §9e. Deleted rather than reworded.

**Not claimed:** that `innerPairEnergy` is the true energy. It carries unit
weight rather than `‖γ̇‖`, which §6 showed is an unstated assumption and §7
showed must be the arclength Jacobian. This subsection settles which *move*
§9d's family performs; it does not settle the weight. -/

namespace LinkEmbedding

variable {M : Type*} {n : ℕ}

/-- **Scaling the separation by `c` scales the pair energy by `c⁻²`.**

    The half `QOU.MobiusEnergy.mutualIntegrand_smul` says it cannot supply,
    now that §3 has built the integral. Read it with the docstring above: the
    integration interval does **not** scale, so this is the law for
    separation-at-fixed-length, not for a similarity. -/
theorem innerPairEnergy_smul (L L' : LinkEmbedding M n) {c : ℝ} (hc : 0 < c)
    (i j : Fin n) (s : ℝ)
    (hscale : ∀ t, L'.sep i s j t = c * L.sep i s j t) :
    L'.innerPairEnergy i j s = c⁻¹ ^ 2 * L.innerPairEnergy i j s := by
  unfold innerPairEnergy
  rw [← intervalIntegral.integral_const_mul]
  refine intervalIntegral.integral_congr fun t _ => ?_
  exact mutualIntegrand_smul L L' c hc i j s t (hscale t)

end LinkEmbedding

/-! ## §9g  WHERE route (2)'s many-body content must live — and it is not topology

§9d says the Möbius mutual channel has no positive topological floor. That is a
negative. This subsection turns it into a *localisation*, by composing with the
corpus's own pair-locality theorem.

`QOU.Mass.CrossingModelPairLocality.PairLocal` is the hypothesis that a pair's
mutual energy is the same measured in isolation, inside a triple, and inside the
full assembly; `b3_eq_zero_of_pairLocal` shows it forces the connected 3-body
cumulant to vanish identically, and AME2020 measures `b₃ = +1.4262225` MeV
(`QOU.MassTheory.AmeBindingNotPairwise.ame_b3_eq`), so the physical binding is
**not** pair-local.

**The instinct to check first, because it is wrong.** "The Möbius mutual energy
is a two-body functional, therefore the channel is pair-local, therefore its
`b₃` is zero, therefore route (2) is dead." The first clause is right and the
second does **not** follow. `PairLocal` compares the pair's energy *across
assemblies*, and a two-body functional still moves when the assembly moves the
pair. Being two-body is a statement about the integrand; pair-locality is a
statement about the configurations.

**What is true instead.** `mobius_b3_eq_zero_of_sep_eq`: if the assemblies do
not move the pair — the separations agree pointwise — then the channel's `b₃`
vanishes identically. Contrapositive (`mobius_b3_ne_zero_forces_moved_sep`): any
nonzero `b₃` from this channel is **entirely** the assembly's effect on the
pair's separations.

So route (2)'s many-body content is exactly the configuration change, and
nothing else. Read with §9d — no topological floor — the two say the same thing
from opposite ends: **every number route (2) can supply is a derived geometry.**
That is not a refutation of the route; it is a specification of what it owes.

**Not claimed:** that the assemblies *do* move the separations in this
framework, nor by how much. That is a geometric measurement this file does not
make, and it is the open thing. Nor is this a claim about the true arclength-
weighted energy — see §9f on what `innerPairEnergy` does and does not model. -/

namespace MobiusMutualChannel

open QOU.Mass.CrossingModelPairLocality

variable {M : Type*}

/-- **The pair energy depends on the pair's separations and nothing else.**

    The per-`(i, j, s)` form of `mutualIntegrand_depends_only_on_sep`, which is
    what the pair-locality comparison actually needs: two *different* links
    agreeing on one pair's separations agree on that pair's energy. -/
theorem innerPairEnergy_congr_of_sep_eq {n : ℕ} (L L' : LinkEmbedding M n)
    (i j : Fin n) (s : ℝ) (h : ∀ t, L'.sep i s j t = L.sep i s j t) :
    L'.innerPairEnergy i j s = L.innerPairEnergy i j s := by
  unfold LinkEmbedding.innerPairEnergy
  refine intervalIntegral.integral_congr fun t _ => ?_
  unfold LinkEmbedding.mutualIntegrand
  rw [h t]

/-- The crossing model the Möbius mutual channel induces, given one link
    embedding per assembly: the isolated pair, the triple containing `k`, and
    the full four-component assembly. -/
noncomputable def mobiusCrossingModel (Lpair : LinkEmbedding M 4)
    (Ltriple : Fin 4 → LinkEmbedding M 4) (Lquad : LinkEmbedding M 4) (s : ℝ) :
    CrossingModel ℝ where
  w2 := fun i j => Lpair.innerPairEnergy i j s
  w3 := fun i j k => (Ltriple k).innerPairEnergy i j s
  w4 := fun i j => Lquad.innerPairEnergy i j s

/-- **If the assemblies do not move the pair, the channel is pair-local.** -/
theorem mobiusCrossingModel_pairLocal_of_sep_eq (Lpair : LinkEmbedding M 4)
    (Ltriple : Fin 4 → LinkEmbedding M 4) (Lquad : LinkEmbedding M 4) (s : ℝ)
    (h3 : ∀ k i j t, (Ltriple k).sep i s j t = Lpair.sep i s j t)
    (h4 : ∀ i j t, Lquad.sep i s j t = Lpair.sep i s j t) :
    (mobiusCrossingModel Lpair Ltriple Lquad s).PairLocal :=
  ⟨fun i j k => innerPairEnergy_congr_of_sep_eq Lpair (Ltriple k) i j s (h3 k i j),
   fun i j => innerPairEnergy_congr_of_sep_eq Lpair Lquad i j s (h4 i j)⟩

/-- **Hence the channel's 3-body cumulant vanishes identically** when the
    assemblies leave the separations alone. Composing the above with the
    corpus's `b3_eq_zero_of_pairLocal`. -/
theorem mobius_b3_eq_zero_of_sep_eq (Lpair : LinkEmbedding M 4)
    (Ltriple : Fin 4 → LinkEmbedding M 4) (Lquad : LinkEmbedding M 4) (s : ℝ)
    (h3 : ∀ k i j t, (Ltriple k).sep i s j t = Lpair.sep i s j t)
    (h4 : ∀ i j t, Lquad.sep i s j t = Lpair.sep i s j t) (i j k : Fin 4) :
    (mobiusCrossingModel Lpair Ltriple Lquad s).toBindingMap.b3 i j k = 0 :=
  b3_eq_zero_of_pairLocal
    (mobiusCrossingModel_pairLocal_of_sep_eq Lpair Ltriple Lquad s h3 h4) i j k

/-- **THE LOCALISATION.** A nonzero 3-body cumulant from this channel forces the
    assemblies to have moved the pair's separations.

    So route (2)'s entire many-body content is the configuration change — read
    with §9d, which rules out a topological floor, every number the channel can
    supply is a derived geometry. AME2020's `b₃ = +1.4262225` MeV is nonzero, so
    the hypothesis is not idle. -/
theorem mobius_b3_ne_zero_forces_moved_sep (Lpair : LinkEmbedding M 4)
    (Ltriple : Fin 4 → LinkEmbedding M 4) (Lquad : LinkEmbedding M 4) (s : ℝ)
    {i j k : Fin 4}
    (hb3 : (mobiusCrossingModel Lpair Ltriple Lquad s).toBindingMap.b3 i j k ≠ 0) :
    ¬ ((∀ k' i' j' t, (Ltriple k').sep i' s j' t = Lpair.sep i' s j' t) ∧
       (∀ i' j' t, Lquad.sep i' s j' t = Lpair.sep i' s j' t)) := by
  rintro ⟨h3, h4⟩
  exact hb3 (mobius_b3_eq_zero_of_sep_eq Lpair Ltriple Lquad s h3 h4 i j k)

/-! ### 9h. The charge-ANTISYMMETRIC content is the configuration difference too

§9g localises the channel's *many-body* content in the configuration change.
This localises its **charge-antisymmetric** content in the same place, and the
argument is one observation about the signature rather than anything new:

**`mobiusCrossingModel` takes no charge argument.** Its only inputs are link
embeddings and the arclength `s`; `CrossingModel` carries `w2`, `w3`, `w4` and
nothing else; `toBindingMap` is built from those three; and `BindingMap.b3` is
`triple i j k - (pair i j + pair i k + pair j k)`. So there is no point in the
chain at which a proton differs from a neutron. Two nuclei are two
*instantiations* of one functional.

Hence if two instantiations agree on the pair and triple separations, their `b₃`
agree — and the contrapositive is the statement this channel owes: **any nonzero
difference in `b₃` between two instantiations forces their separations to
differ.**

**Why this matters to the EM arc.** `qou-9v7t` splits the measured A = 3
cumulant by isospin and names the halves: `b3_sym = 1.4262225` MeV, *"the strong
channel's obligation"*, against `b3_asym = 0.3818775` MeV, *"the EM channel's"*.
The corpus's own summary of that split is that **the framework has no EM term in
any per-bond factor** (`f_pp = z`, `f_nn = z - h`, `f_pn = z - h(1/2 - δ/4)` —
charge-*labelled* but not charge-*coupled*). The result below says route (2)
does not need one: whatever charge-antisymmetric number this channel can supply
is a derived geometry, exactly as §9g found for the many-body number. One
obligation, not two.

**Two scope notes, both load-bearing.**

*Arity.* `CrossingModel` is `Fin 4`-indexed, so `b3 i j k` is a triple's cumulant
*inside* a four-component model, while the mirror pair ³H/³He is A = 3. The
theorem below is therefore stated for two arbitrary instantiations, which is what
is proved; reading them as ³H and ³He is an interpretation, and it carries that
spare fourth component with it.

*Not claimed.* That the mirror partners' separations **do** differ in this
framework, nor by how much — the same open item as §9g (`qou-a2w5`), now
reached from the charge side as well. In particular this is **not** a prediction
of `b3_asym`; it is a statement about where any such prediction would have to
come from. -/

/-- **The channel's `b₃` depends only on the pair and triple separations.**

    Note `Lquad` is unconstrained: `BindingMap.b3` is built from `pair` and
    `triple` alone, so the four-component assembly does not enter. -/
theorem mobius_b3_congr_of_sep_eq
    (Lpair Lpair' : LinkEmbedding M 4)
    (Ltriple Ltriple' : Fin 4 → LinkEmbedding M 4)
    (Lquad Lquad' : LinkEmbedding M 4) (s : ℝ) (i j k : Fin 4)
    (hp : ∀ i' j' t, Lpair'.sep i' s j' t = Lpair.sep i' s j' t)
    (ht : ∀ k' i' j' t, (Ltriple' k').sep i' s j' t = (Ltriple k').sep i' s j' t) :
    (mobiusCrossingModel Lpair' Ltriple' Lquad' s).toBindingMap.b3 i j k
      = (mobiusCrossingModel Lpair Ltriple Lquad s).toBindingMap.b3 i j k := by
  have e1 := innerPairEnergy_congr_of_sep_eq Lpair Lpair' i j s (hp i j)
  have e2 := innerPairEnergy_congr_of_sep_eq Lpair Lpair' i k s (hp i k)
  have e3 := innerPairEnergy_congr_of_sep_eq Lpair Lpair' j k s (hp j k)
  have t1 := innerPairEnergy_congr_of_sep_eq (Ltriple k) (Ltriple' k) i j s (ht k i j)
  have t2 := innerPairEnergy_congr_of_sep_eq (Ltriple j) (Ltriple' j) i k s (ht j i k)
  have t3 := innerPairEnergy_congr_of_sep_eq (Ltriple i) (Ltriple' i) j k s (ht i j k)
  simp only [QOU.Mass.PairwiseCumulantVanishing.BindingMap.b3,
    CrossingModel.toBindingMap, CrossingModel.tripleMutual, mobiusCrossingModel,
    e1, e2, e3, t1, t2, t3]

/-- **THE CHARGE-SIDE LOCALISATION.** Two instantiations whose `b₃` differ must
    differ in their pair or triple separations.

    Read with §9g: the many-body content and the charge-antisymmetric content of
    this channel are the same obligation — a derived geometry — not two. -/
theorem mobius_b3_differs_forces_sep_differ
    (Lpair Lpair' : LinkEmbedding M 4)
    (Ltriple Ltriple' : Fin 4 → LinkEmbedding M 4)
    (Lquad Lquad' : LinkEmbedding M 4) (s : ℝ) {i j k : Fin 4}
    (hne : (mobiusCrossingModel Lpair' Ltriple' Lquad' s).toBindingMap.b3 i j k
      ≠ (mobiusCrossingModel Lpair Ltriple Lquad s).toBindingMap.b3 i j k) :
    ¬ ((∀ i' j' t, Lpair'.sep i' s j' t = Lpair.sep i' s j' t) ∧
       (∀ k' i' j' t, (Ltriple' k').sep i' s j' t = (Ltriple k').sep i' s j' t)) := by
  rintro ⟨hp, ht⟩
  exact hne (mobius_b3_congr_of_sep_eq Lpair Lpair' Ltriple Ltriple' Lquad Lquad' s i j k hp ht)

end MobiusMutualChannel

end QOU
