/-
# Class B: dropping sign-definiteness of the bond energies

`QOU/Hecke/BondCutSymmetry.lean` (#7165, bean `qou-qve5`) excludes **positive**
pair-additive bond counts from supplying the SEMF symmetry energy. Its
enumeration of escapes (#7181, bean `qou-brng`) names four classes; **class B is
"a bond energy that is not sign-definite"** — `e_t < 0`, i.e. a bond factor
`b_t > 1`, a *repulsive* bond. It is called the smallest escape and the one the
physics wants, because a repulsive bond is what unbinds neutron matter, which is
precisely what `bondSum_nonneg` forbids.

This file asks what `BondCutSymmetry` still proves once that hypothesis is gone.
Nothing here is fitted: the three bond energies are treated as arbitrary
elements of a ring or an ordered field throughout, and every SEMF number stays
in the sibling probe as a *target*, never as a search direction.

## What survives, and it is almost everything

Exactly two of `BondCutSymmetry`'s theorems carry a sign hypothesis on an
*energy*: `bondSum_nonneg` and, through it, `bondSum_ne_semf_neutronMatter`.
Every other statement — the cut identity, the segregated and well-mixed
decompositions, `symmetryCoeff_pos_iff`, `cut_le_degree_bound` — quantifies over
the energies with no sign constraint at all, and so is a class-B theorem
already. The sibling `BondCutSymmetryLogBound.energySlope_convex_le` needs only
`0 < b_nn ≤ b_pp`; it never needs `b ≤ 1`. So **invariant (1), the `2 ln q` cap
on `δ`, was never a consequence of positivity**, and class B does not escape it.
That composition is made explicit in the archimedean sibling
`BondCutSymmetryNoSignDefiniteLogBound.lean`.

## The invariant this file adds

**A uniform energy shift moves the volume term and leaves `δ` exactly fixed**
(`energySlope_energyShift`, `symmetryCoeff_energyShift`). In bond-factor letters
a uniform shift is a common rescaling `b_t ↦ c·b_t`, which is the cheapest way
to reach class B — take `c` large enough and all three energies go negative at
once. On the well-mixed layout the total bond count is `kA/2` *independently of
the mixing density* `μ` (`bondSum_wellMixed_totalCount`), so the shift
contributes `s·kA/2`: a **pure volume term**
(`bondSum_wellMixed_energyShift`). It cannot produce, cancel, or rescale a
`(N-Z)²`.

So the sub-class of B reached by making the energies negative uniformly is
powerless on the symmetry term by a ring identity, not by a numerical estimate.

## The price of the escape, stated as an implication

Class B does genuinely escape invariant (2): at pure neutron matter the bond sum
is `e_nn·n_nn`, which may be negative. But the escape is not free, and
`enn_neg_of_semf_neutronMatter` prices it: **any bond count that reproduces the
SEMF at pure neutron matter must have `e_nn < 0`**, i.e. a *repulsive
neutron–neutron bond*, `b_nn > 1`. That is a falsifiable condition on a derived
quantity, not a modelling choice — and the sibling probe measures the corpus's
`b_nn` against it.

## The dichotomy

`energySlope_gt_convexCap_iff`: `δ` exceeds `(e_nn - e_pp)/2` **iff**
`e_pn > e_nn`, i.e. iff the interface bond is strictly weaker than *both*
like-species bonds. In bond-factor letters, iff `b_pn` lies strictly *below* the
convex hull of `b_pp` and `b_nn`. There is no sign hypothesis anywhere in it.
So beating the cap is equivalent to putting the interface outside the hull the
corpus derives it in (`SymmetrySignAmGm.weight_of_convention`) — at which point
`b_pn` is a chosen number, which is a fit with one free parameter and is
forbidden (AGENTS.md §NO FITTING).

Producer: `computations/qbeta/qbeta_class_b_nonsigndefinite_bond_probe.py`.
Builds on `QOU/Hecke/BondCutSymmetry.lean` (`qou-qve5`). Bean `qou-brng`.
-/

import QOU.Hecke.BondCutSymmetry

namespace QOU.Hecke.BondCutSymmetryNoSignDefinite

open QOU.Hecke.BondCutSymmetry

/-! ## A uniform energy shift is a total-bond-count term (generic ring) -/

section Ring

variable {R : Type*} [CommRing R]

/-- **A uniform shift of all three bond energies adds the shift times the total
bond count.** In bond-factor letters `e = -ln b`, a shift by `s` is the common
rescaling `b_t ↦ e^{-s}·b_t`; taking `s` negative enough drives every energy
below zero, which is exactly class B. What it buys is a term proportional to
`n_pp + n_pn + n_nn`, and nothing else. -/
theorem bondSum_energyShift (epp epn enn npp npn nnn s : R) :
    bondSum (epp + s) (epn + s) (enn + s) npp npn nnn
      = bondSum epp epn enn npp npn nnn + s * (npp + npn + nnn) := by
  unfold bondSum
  ring

end Ring

/-! ## `δ` is shift-invariant; the shift is a pure volume term (field) -/

section Field

variable {K : Type*} [Field K] [CharZero K]

/-- **The p–n slope is invariant under a uniform energy shift.** `δ` is a
second difference of the three energies, so a common additive constant cancels
identically. This is the whole of class B's uniform sub-case in one line: making
every bond repulsive at once changes `δ` by exactly zero. -/
theorem energySlope_energyShift (epp epn enn s : K) :
    energySlope (epp + s) (epn + s) (enn + s) = energySlope epp epn enn := by
  unfold energySlope
  ring

/-- The symmetry coefficient inherits the shift-invariance, for every mixing
density `μ`. -/
theorem symmetryCoeff_energyShift (epp epn enn μ s : K) :
    symmetryCoeff (epp + s) (epn + s) (enn + s) μ = symmetryCoeff epp epn enn μ := by
  unfold symmetryCoeff
  rw [energySlope_energyShift]

/-- **The well-mixed layout has total bond count `kA/2`, independently of the
mixing density.** The `μ·Z·N` bonds the mixing creates are taken from the
like-species counts one for one, so `μ` cancels. -/
theorem bondSum_wellMixed_totalCount (k μ Z N : K) :
    (k * Z - μ * Z * N) / 2 + μ * Z * N + (k * N - μ * Z * N) / 2 = k * (Z + N) / 2 := by
  ring

/-- **A uniform energy shift on the well-mixed layout is a pure volume term.**
It adds `s·k·A/2` — linear in `A = Z + N`, with no `(N-Z)²` and no dependence on
the mixing density `μ`. Combined with `symmetryCoeff_energyShift`, the shifted
law's symmetry coefficient is the unshifted one. -/
theorem bondSum_wellMixed_energyShift (epp epn enn k μ Z N s : K) :
    bondSum (epp + s) (epn + s) (enn + s)
        ((k * Z - μ * Z * N) / 2) (μ * Z * N) ((k * N - μ * Z * N) / 2)
      = bondSum epp epn enn
          ((k * Z - μ * Z * N) / 2) (μ * Z * N) ((k * N - μ * Z * N) / 2)
        + s * (k * (Z + N) / 2) := by
  rw [bondSum_energyShift, bondSum_wellMixed_totalCount]

end Field

/-! ## The price of the escape, and the dichotomy (ordered field) -/

section OrderedField

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- **The bond sum at pure neutron matter is `e_nn · n_nn`.** With `Z = 0` there
are no p–p and no p–n bonds; this is the composition at which `bondSum_nonneg`
did its work. -/
theorem bondSum_neutronMatter (epp epn enn nnn : K) :
    bondSum epp epn enn 0 0 nnn = enn * nnn := by
  unfold bondSum
  ring

/-- **Class B's escape has a price: a repulsive neutron–neutron bond.** If a
pair-additive bond count reproduces the SEMF at pure neutron matter — where the
SEMF with `a_A > a_V` is negative, i.e. unbound — then the n–n energy is
strictly negative. In bond-factor letters `e_nn = -ln b_nn < 0` means
`b_nn > 1`.

This is the honest statement of what dropping `bondSum_nonneg` costs: the escape
is real, and it converts a *structural* exclusion into a *falsifiable condition
on a derived quantity*. The hypothesis `a_V < a_A` is what AME2020 measures; it
enters here as a hypothesis, never as a fit. Conditional-lemma naming per
AGENTS.md §Conditional-proved ≠ premise-established. -/
theorem enn_neg_of_semf_neutronMatter {epp epn enn nnn E0 aV aA A : K}
    (hE0 : 0 < E0) (hnnn : 0 < nnn) (hA : 0 < A) (h : aV < aA)
    (heq : E0 * bondSum epp epn enn 0 0 nnn = aV * A - aA * (A * A / A)) :
    enn < 0 := by
  have hr : aV * A - aA * (A * A / A) < 0 := semf_neutronMatter_neg hA h
  rw [bondSum_neutronMatter] at heq
  by_contra hc
  push_neg at hc
  have : 0 ≤ E0 * (enn * nnn) := mul_nonneg hE0.le (mul_nonneg hc hnnn.le)
  linarith

/-- **Monotonicity of the symmetry coefficient in the slope.** Any bound on `δ`
transports to a bound on `a_A^eff` with no sign hypothesis on the energies; this
is the bridge the archimedean sibling uses to compose the `2 ln q` cap into a
MeV cap for class B. -/
theorem symmetryCoeff_le_of_energySlope_le {epp epn enn μ D : K} (hμ : 0 < μ)
    (h : energySlope epp epn enn ≤ D) :
    symmetryCoeff epp epn enn μ ≤ D * μ / 4 := by
  unfold symmetryCoeff
  have : energySlope epp epn enn * μ ≤ D * μ := mul_le_mul_of_nonneg_right h hμ.le
  linarith

/-- **The dichotomy: beating the convex cap is exactly leaving the convex hull.**
`δ > (e_nn - e_pp)/2` **iff** `e_pn > e_nn`, i.e. iff the p–n bond is *weaker
than both* like-species bonds. In bond-factor letters (`e = -ln b`, monotone
decreasing) that is `b_pn < b_nn ≤ b_pp`: strictly below the convex hull the
corpus derives the interface in.

No sign hypothesis appears, so class B changes nothing about it. The content is
that class B does not open a route to the magnitude: an interface outside the
hull is a *chosen* number, not a derived one, and choosing it to hit `a_A` is a
one-parameter fit (AGENTS.md §NO FITTING, "selection against the target"). -/
theorem energySlope_gt_convexCap_iff (epp epn enn : K) :
    (enn - epp) / 2 < energySlope epp epn enn ↔ enn < epn := by
  unfold energySlope
  constructor <;> intro h <;> linarith

/-- The same dichotomy at the boundary: `δ` attains the cap exactly when the
interface sits *at* the weaker like-species bond (`w = 0`, the pure `σ⁻¹`
interface of `BondCutSymmetryLogBound`). -/
theorem energySlope_eq_convexCap_iff (epp epn enn : K) :
    energySlope epp epn enn = (enn - epp) / 2 ↔ epn = enn := by
  unfold energySlope
  constructor <;> intro h <;> linarith

end OrderedField

end QOU.Hecke.BondCutSymmetryNoSignDefinite
