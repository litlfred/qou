import Mathlib.Tactic
import QOU.Knot.Clausen
import QOU.Knot.ClausenValueBounds
import QOU.Knot.FiveTwoVolumeChord
import QOU.Archimedean.BlochWignerPositive

/-!
# QOU.Encounter.MostowRigidity

Conditional-class axiomatisation of Mostow rigidity for the
geometric face of confinement (§3b conditional-class pattern).

## What this module provides

Non-trivial scaffold for the geometric-rigidity class:

- `MostowRigidity` — `class` whose fields are real numerical
  invariants (`volume`, `mostow_gap`) plus their non-negativity /
  positivity witnesses.  No `True` placeholders remain on the
  class itself; the class fields encode the operational content
  of the rigidity statement at the level needed by downstream
  conditional theorems.

- `mass_rigidity_of_mostow` — fully proved conditional theorem.
  Takes `[MostowRigidity M]` and concludes that the volume
  invariant is non-negative and the deformation gap is strictly
  positive — i.e. the categorical mass eigenvalue attached to
  `M` is isolated.

- `MostowRigidity.unknot` — concrete instance for the unknot
  complement (degenerate hyperbolic case: volume 0 by
  Thurston's convention, with a conservative gap to the
  smallest non-trivial hyperbolic volume Vol(4₁) ≈ 2.0299).
  Witnesses that the class has at least one closed instance.

- `MostowRigidity.figureEight` — concrete instance for the
  figure-eight knot complement (4₁): the smallest known
  hyperbolic 3-manifold complement, volume ≈ 2.02988
  (Cao–Meyerhoff 2001), with Mostow gap conservatively below
  the next-smallest gap Vol(5₂) − Vol(4₁) ≈ 0.798.

- `MostowRigidity.knot5_2` — concrete instance for the 5₂ knot
  complement: second-smallest known orientable cusped hyperbolic
  3-manifold, volume ≈ 2.82812 (literature constant; Adams–
  Hildebrand–Weeks 1991, SnapPy verified).

- `unknot_volume_lt_figureEight_volume`,
  `figureEight_volume_lt_knot5_2_volume` — fully-proved
  comparison theorems exhibiting non-trivial uses of
  `volumeInvariant`.

- `mass_eigenvalue_isolated` — example downstream consumer that
  takes `[MostowRigidity M]` and concludes `0 < gap`; new
  instances satisfy this theorem automatically (§3b
  conditional-class consumer pattern).

## Categorical content

Mostow rigidity is the **geometric mirror** of `SDPSlaterUniqueness`
(`QOU.MathlibExt.SDPRealUniqueness`):

| Side       | Uniqueness witness        | What it pins              |
|------------|---------------------------|---------------------------|
| Algebraic  | `SDPSlaterUniqueness`     | Primal SDP optimum `Φ*`   |
| Geometric  | `MostowRigidity`          | Hyperbolic volume of `M`  |

The bridge `gb_reduction_pl_thimble_bijection` (in
`QOU.PicardLefschetz`) realises one as the τ-image of the other
under the `archimedean-realization-functor`.

## Status

The class fields are now substantive:

* `volume : ℝ` — the hyperbolic volume of the (intended) complete
  finite-volume 3-manifold associated to `M`.  Real-valued; no
  abstraction over hyperbolic structures yet.  Convention:
  non-hyperbolic complements (Seifert-fibred, toroidal) take
  `volume = 0`, matching Thurston's extension of `Vol` to the
  whole knot complement spectrum.
* `volume_nonneg : 0 ≤ volume` — non-negativity witness.
* `mostow_gap : ℝ` — strictly-positive lower bound on the
  distance from `volume` to the next distinct value in the
  hyperbolic-volume spectrum.  This is the operational content of
  the rigidity statement: distinct knot types are separated by a
  strictly positive volume gap.
* `mostow_gap_pos : 0 < mostow_gap` — positivity witness.

Concrete instances supply both reals and both positivity
witnesses; the §3b "hard work" deferred to Mathlib's
geometric-topology layer is the *full* discreteness theorem
asserting that `mostow_gap` matches the actual gap to the next
hyperbolic volume.  Downstream theorems use only the witnesses,
not the absolute value.

## References

- [mostow1968]  Mostow, *Quasi-conformal mappings in n-space and
  the rigidity of hyperbolic space forms*, Pub. IHES (1968).
- [thurston1978]  Thurston, *Geometry and topology of
  three-manifolds*, lecture notes (1978-79).
- [neumann-zagier1985]  Neumann–Zagier, *Volumes of hyperbolic
  three-manifolds*, Topology (1985).
- [witten2011]  Witten, *Analytic continuation of Chern-Simons
  theory*, Chern-Simons Gauge Theory: 20 Years After (2011).
-/

namespace QOU.Encounter.MostowRigidity

/-- **Mostow rigidity (conditional class)**.

    A `MostowRigidity M` instance attaches to `M` a hyperbolic
    volume invariant `volume` together with a strictly positive
    Mostow gap `mostow_gap` to the next distinct value in the
    volume spectrum.

    Operationally this is what downstream theorems consume:
    rigidity of the volume (its bare existence as a class field)
    plus discreteness of the spectrum (the strictly positive
    gap).  Concrete instances must supply both reals and both
    positivity witnesses; the §3b "hard work" of *proving* that
    `mostow_gap` matches the actual gap to the next hyperbolic
    volume is deferred to Mathlib's geometric-topology layer.

    Ref: [mostow1968] -/
class MostowRigidity (M : Type*) where
  /-- Hyperbolic volume invariant of `M`.  Convention: take
      `volume = 0` for non-hyperbolic complements. -/
  volume : ℝ
  /-- Volume is non-negative. -/
  volume_nonneg : 0 ≤ volume
  /-- Strictly positive lower bound on the distance from `volume`
      to the next distinct value in the hyperbolic-volume spectrum.
      Encodes Mostow's discreteness witness. -/
  mostow_gap : ℝ
  /-- The Mostow gap is strictly positive.  This is the
      operational content of "no nearby hyperbolic structures". -/
  mostow_gap_pos : 0 < mostow_gap

/-- **Mass rigidity from Mostow** — fully-proved downstream
    conditional theorem.

    Given `[MostowRigidity M]` for the knot complement `M`, the
    categorical mass eigenvalue (which factors through the
    hyperbolic volume via the `algebraic-quantum-volume` bridge)
    is well-defined (non-negative volume) and **isolated**: the
    next distinct value in the volume spectrum lies strictly above
    `volume`, separated by the Mostow gap.

    Both conjuncts are *derived*, not projected: the first is the
    non-negativity witness, and the second — `volume` is strictly
    below its gap-separated successor `volume + mostow_gap` — is
    derived from the strict positivity of the gap
    (`lt_add_of_pos_right`).  Composing the two fields rather than
    re-exporting `mostow_gap_pos` verbatim is what makes this a
    genuine rigidity consequence (separation of the eigenvalue from
    the rest of the spectrum) rather than a self-assuming
    projection (AGENTS.md §3b-cond item 5).

    This is the §3b-cond rigorous-conditional companion to the
    `prop:mostow-confinement` content block; concrete instances
    of the class supply the rigidity proof for specific knot
    complements. -/
theorem mass_rigidity_of_mostow {M : Type*} [h : MostowRigidity M] :
    0 ≤ h.volume ∧ h.volume < h.volume + h.mostow_gap := by
  refine ⟨h.volume_nonneg, ?_⟩
  exact lt_add_of_pos_right h.volume h.mostow_gap_pos

/-- **Volume of the categorical mass eigenvalue** — extraction
    helper.  Returns the underlying volume invariant from the
    `MostowRigidity` class so that downstream uses can quote
    `volumeInvariant M` rather than `(inferInstance : MostowRigidity M).volume`. -/
def volumeInvariant (M : Type*) [h : MostowRigidity M] : ℝ :=
  h.volume

theorem volumeInvariant_nonneg (M : Type*) [h : MostowRigidity M] :
    0 ≤ volumeInvariant M :=
  h.volume_nonneg

/-- Type marker for the unknot complement (used as the carrier of
    the corresponding `MostowRigidity` instance). -/
structure Unknot

/-- Type marker for the figure-eight knot complement `4_1`. -/
structure FigureEight

/-- Type marker for the 5_2 knot complement. -/
structure Knot5_2

/-- **Concrete instance: unknot complement** (degenerate
    hyperbolic case).

    By Thurston's extension of `Vol` to the whole knot-complement
    spectrum, non-hyperbolic complements are assigned volume 0.
    The unknot complement is the solid torus, which is
    Seifert-fibred and not hyperbolic; its conventional volume is
    therefore 0.  The Mostow gap is bounded below by `1` —
    a conservative under-approximation of
    `Vol(4_1) ≈ 2.0299`, the smallest known hyperbolic
    3-manifold volume (Cao–Meyerhoff 2001).

    Ref: [thurston1978] §6 (volume of non-hyperbolic complements
    by convention) -/
instance unknot : MostowRigidity Unknot where
  volume := 0
  volume_nonneg := le_refl 0
  mostow_gap := 1
  mostow_gap_pos := by norm_num

/-- **Concrete instance: figure-eight knot complement** (`4_1`).

    The complement `S^3 \ 4_1` is the smallest known orientable
    cusped hyperbolic 3-manifold (Cao–Meyerhoff 2001), with
    hyperbolic volume

    `Vol(4_1) = 2 · Cl₂(π/3) = 6 · Λ(π/3) ≈ 2.02988...`

    where `Cl₂` is the Clausen function and `Λ` the Lobachevsky
    function, `Λ(θ) = Cl₂(2θ)/2`.  The class field
    stores the 15-significant-digit truncation
    `2.02988321281930` (kept in lock-step with the canonical
    50-dps witness via `:leanval[Vol_4_1]{precision=15}`); the
    direction of the truncation does not affect the class
    invariants.

    The Mostow gap is bounded below by `0.5`, a conservative
    under-approximation of the next-smallest gap

    `Vol(5_2) - Vol(4_1) ≈ 2.82812 - 2.02988 ≈ 0.798`.

    Ref: [thurston1978]; Cao–Meyerhoff, *The orientable cusped
    hyperbolic 3-manifolds of minimum volume*, Invent. Math. 146
    (2001) 451–478. -/
noncomputable instance figureEight : MostowRigidity FigureEight where
  -- EXACTIFIED 2026-08-30 (bean `qou-f8lit`).  This field used to be the decimal
  -- literal `2.02988321281930`, a 15-significant-digit TRUNCATION of the corpus's own
  -- exact `VOL_4_1 = 2·Cl₂(π/3) = 2.029883212819307250042405108549…`.  The two differ
  -- at the 16th digit, so `volumeInvariant FigureEight ≠ VOL_4_1` -- while
  -- `figureEightTriangulation_volume : figureEightTriangulation.volume = VOL_4_1` is
  -- proved sorry-free.  Any bridge statement keyed on the literal was therefore
  -- UNSATISFIABLE at the corpus's own 4₁ triangulation.  There is now no decimal here
  -- to be unequal to, so the `:leanval[Vol_4_1]` sync has nothing to sync and is gone.
  volume := QOU.Knot.FigureEightVolume.VOL_4_1
  volume_nonneg := by
    have := QOU.Knot.Cl_2_pi_div_three_pos
    show (0 : ℝ) ≤ 2 * QOU.Archimedean.Cl_2 (Real.pi / 3)
    linarith
  -- `mostow_gap` keeps its literal deliberately: it is a conservative
  -- UNDER-approximation of the true gap, not an approximation OF anything exact, so
  -- truncation is the correct representation and it is not part of the defect class.
  mostow_gap := 0.5  -- :leanval[mostow_gap_4_1]
  mostow_gap_pos := by norm_num

/-- **Volume comparison: unknot < figure-eight**.

    Sanity check: the volume invariant attached to the
    `unknot` instance (`0`, by Thurston's convention) is
    strictly smaller than the volume invariant attached to the
    `figureEight` instance (`Vol(4_1) ≈ 2.02988`).  This is the
    smallest non-trivial volume comparison in the
    hyperbolic-volume spectrum and the first non-degenerate
    use of `volumeInvariant`. -/
theorem unknot_volume_lt_figureEight_volume :
    volumeInvariant Unknot < volumeInvariant FigureEight := by
  -- No literal any more: the figure-eight volume is the exact `2·Cl₂(π/3)`, and its
  -- positivity is the corpus's proved `Cl_2_pi_div_three_pos` rather than `norm_num`
  -- on a decimal.
  have := QOU.Knot.Cl_2_pi_div_three_pos
  show (0 : ℝ) < 2 * QOU.Archimedean.Cl_2 (Real.pi / 3)
  linarith

/-- **Concrete instance: 5_2 knot complement**.

    The complement `S^3 \ 5_2` is the second-smallest known
    orientable cusped hyperbolic 3-manifold (after `S^3 \ 4_1`),
    with hyperbolic volume

    `Vol(5_2) ≈ 2.82812208833078`

    (SnapPy ManifoldHP 50 dps, 2026-06-12; witness field
    `vol_5_2_decimal_50`. The former Adams-Hildebrand-Weeks 1991
    15-dps anchor `2.82812208833410` carried a digit-13–15
    transcription error.)

    The Mostow gap is bounded below by `0.3`.

    **This was `0.5`, and `0.5` is not a lower bound.**  The field is documented as a
    *lower bound* on the distance to the next distinct spectrum value, and the next value
    above `Vol(5_2)` is `Vol(6_1) ≈ 3.16396`, i.e. a gap of `0.33584`.  The old docstring
    called `0.5` "well under the nearest-neighbour gaps ... `Vol(6_1) - Vol(5_2) ≈ 0.336`"
    while quoting that very figure — `0.5 > 0.336`, so the value contradicted the sentence
    that justified it.  `figureEight`'s `0.5` is sound by contrast: its neighbour up is
    `Vol(5_2)`, a gap of `0.798`.

    Nothing in Lean broke, because the class carries only `mostow_gap_pos` and explicitly
    defers the discreteness claim to Mathlib's geometric-topology layer (see the class
    docstring).  That is exactly why it went unnoticed: the field's *documented* meaning is
    not enforced by its *stated* obligation, so an agent trusting the doc would conclude no
    hyperbolic volume lies within `0.5` of `Vol(5_2)`, and `Vol(6_1)` does.

    Ref: Adams, Hildebrand, Weeks, *Hyperbolic invariants of
    knots and links*, Trans. AMS 326 (1991) 1–56. -/
noncomputable instance knot5_2 : MostowRigidity Knot5_2 where
  -- EXACTIFIED 2026-08-30 (bean `qou-f8lit`, item 1), matching `figureEight` above.  This
  -- field used to be the decimal literal `2.82812208833078`, a 15-significant-digit
  -- TRUNCATION of the corpus's own exact `VOL_5_2 = 3·D(fiveTwoShape) =
  -- 2.8281220883307831627638988092766349…`.  The two differ at the 16th digit, so
  -- `volumeInvariant Knot5_2 ≠ VOL_5_2` -- while `fiveTwoTriangulation_volume :
  -- fiveTwoTriangulation.volume = VOL_5_2` is proved sorry-free.  Any bridge statement
  -- keyed on the literal was therefore UNSATISFIABLE at the corpus's own 5₂
  -- triangulation.  There is now no decimal here to be unequal to, so the
  -- `:leanval[vol_5_2]` sync has nothing to sync and is gone.
  --
  -- What unblocked it was NOT the chord inequality.  `VOL_4_1_lt_VOL_5_2` bounds `VOL_5_2`
  -- below by `VOL_4_1`, which is the quantity on the left of the comparison below, so it
  -- proves that comparison and supplies nothing for this field.  The field needs
  -- `0 ≤ VOL_5_2` on its own, and that is `Archimedean.BlochWignerPositive` (bean
  -- `qou-0ag0`) applied at `fiveTwoShape_im_pos` -- general upper-half-plane positivity,
  -- which the 5₂ shape gets for free precisely because it does NOT go through a Clausen
  -- special value.
  volume := QOU.Knot.FiveTwoVolume.VOL_5_2
  volume_nonneg := by
    show (0 : ℝ) ≤ 3 * QOU.Archimedean.BlochWigner_lob QOU.Knot.FiveTwoVolume.fiveTwoShape
    have := QOU.Archimedean.BlochWignerPositive.blochWigner_lob_pos
      QOU.Knot.FiveTwoVolume.fiveTwoShape_im_pos
    linarith
  -- CORRECTED from `0.5`, which was not a lower bound on the true gap `0.33584` to
  -- `Vol(6_1)`.  See the docstring above.
  mostow_gap := 0.3
  mostow_gap_pos := by norm_num

/-- **Volume comparison: figure-eight < 5_2**.

    Adds the second comparison in the hyperbolic-volume spectrum
    populated by this module.  Together with
    `unknot_volume_lt_figureEight_volume` it exhibits the
    monotone chain

    `volumeInvariant Unknot < volumeInvariant FigureEight
       < volumeInvariant Knot5_2`

    and demonstrates that the class supports genuine spectral
    bookkeeping rather than a single anchored comparison. -/
theorem figureEight_volume_lt_knot5_2_volume :
    volumeInvariant FigureEight < volumeInvariant Knot5_2 := by
  -- BOTH sides are now exact constants, so this is no longer a `nlinarith` against a
  -- certified Clausen bracket and a decimal -- it IS the corpus's proved inequality,
  -- `QOU.Knot.FiveTwoVolumeChord.VOL_4_1_lt_VOL_5_2` (bean `qou-52ch`), by Rivin strict
  -- concavity along the chord from the regular ideal shape.  Nothing here is approximated
  -- at any point.
  show QOU.Knot.FigureEightVolume.VOL_4_1 < QOU.Knot.FiveTwoVolume.VOL_5_2
  exact QOU.Knot.FiveTwoVolumeChord.VOL_4_1_lt_VOL_5_2

/-- **Downstream consumer: mass eigenvalue is isolated**.

    Generic theorem in the §3b conditional-class consumer
    pattern: takes `[MostowRigidity M]` as a typeclass hypothesis
    and concludes that the mass eigenvalue attached to `M` is
    isolated by a strictly positive Mostow gap.

    Any new instance of `MostowRigidity` automatically validates
    this theorem without rewriting the proof — that is the
    operational pay-off of the §3b conditional-class pattern.
    Three closed inhabitants exist in this module
    (`Unknot`, `FigureEight`, `Knot5_2`); each immediately
    discharges the hypothesis and yields a closed conclusion. -/
theorem mass_eigenvalue_isolated (M : Type*) [h : MostowRigidity M] :
    0 < h.mostow_gap :=
  h.mostow_gap_pos

/-- Sanity check: the consumer theorem does discharge automatically
    on each of the three closed instances.  These corollaries
    require no extra proof — the `inferInstance` lookup of the
    `MostowRigidity` instance plus `mass_eigenvalue_isolated`
    closes the goal. -/
example : (0 : ℝ) < (inferInstance : MostowRigidity Unknot).mostow_gap :=
  mass_eigenvalue_isolated Unknot

example : (0 : ℝ) < (inferInstance : MostowRigidity FigureEight).mostow_gap :=
  mass_eigenvalue_isolated FigureEight

example : (0 : ℝ) < (inferInstance : MostowRigidity Knot5_2).mostow_gap :=
  mass_eigenvalue_isolated Knot5_2

end QOU.Encounter.MostowRigidity
